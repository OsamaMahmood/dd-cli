# Testing

`dd-cli` has four test suites with different cost/value trade-offs. The default `pytest` invocation runs three of them (~20 seconds, no network); the fourth needs a live DefectDojo.

## At a glance

| Suite | Where | Marker | Default `make test` | Needs |
|---|---|---|---|---|
| Unit | `tests/test_*.py` | (none) | yes | nothing |
| Snapshot | `tests/test_*.py` (intermixed; uses `syrupy`) | (none) | yes | nothing |
| Compat | `tests/compat/` | `@pytest.mark.compat` | yes | nothing |
| Integration | `tests/integration/` | `@pytest.mark.integration` | **no** | `DD_URL` + `DD_API_KEY` env vars + a reachable DefectDojo |

`pyproject.toml` excludes integration by default:

```toml
[tool.pytest.ini_options]
addopts = ["-ra", "--strict-markers", "--strict-config", "-m", "not integration", "--cov=dd_cli", ...]
markers = [
    "integration: tests that require a live DefectDojo instance",
    "compat: backward-compatibility tests for the dd-import contract",
]
```

`--strict-markers` means a typo in `@pytest.mark.foo` is a hard error (not a warning). `--strict-config` rejects unknown config keys.

Run:

```bash
make test            # unit + snapshot + compat (~257 + 12 + 9, ~20s)
make test-cov        # same, with HTML coverage at htmlcov/index.html
pytest -m compat     # compat only
pytest -m integration  # integration only (still needs DD_URL + DD_API_KEY)
make smoke           # `pytest -m integration --no-cov -v`, gated on env vars
```

## Top-level fixtures

[tests/conftest.py](../tests/conftest.py) is intentionally tiny:

```python
import pytest
from typer.testing import CliRunner

@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()
```

That's it. Every other fixture is per-file. The reason is hermetic isolation — see "Per-file isolation" below.

## Unit + snapshot tests (`tests/test_*.py`)

These cover the CLI commands, config layer, output renderers, error mapping, and workflows in isolation. **No real network**: HTTP is mocked via `pytest-httpx`.

### Per-file isolation pattern

Every test file that exercises CLI commands declares an autouse fixture that:
1. Points `DD_CLI_CONFIG_DIR` at `tmp_path` so the user's real config isn't touched.
2. Clears every `DD_*` and `DD_CLI_*` env var that might be set in the dev's shell.
3. Re-sets `DD_URL` and `DD_API_KEY` to known fake values so commands have a complete profile.

The canonical version (from [tests/test_cli_resources.py:20-34](../tests/test_cli_resources.py)):

```python
@pytest.fixture(autouse=True)
def isolated_env(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Per-test config dir + a complete profile via env vars, no DD_*/DD_CLI_* leakage."""
    monkeypatch.setenv("DD_CLI_CONFIG_DIR", str(tmp_path))
    for var in (
        "DD_URL",
        "DD_API_KEY",
        "DD_CLI_URL",
        "DD_CLI_API_KEY",
        "DD_CLI_PROFILE",
        "DD_PROFILE",
    ):
        monkeypatch.delenv(var, raising=False)
    monkeypatch.setenv("DD_URL", "https://dd.example")
    monkeypatch.setenv("DD_API_KEY", "the-token")
```

The compat suite has a stronger version (clears **every** `DD_*`/`DD_CLI_*` var, not just a fixed list) — see "Compat tests".

**Why this matters**: without the autouse fixture, a developer who has `DD_API_KEY` exported in their shell will run a different test than CI does. The fixture guarantees the test environment matches CI.

### HTTP mocking with `pytest-httpx`

The `httpx_mock` fixture is provided by `pytest-httpx`. **Any unmocked HTTP request fails the test** — that's how `--dry-run` is verified to send zero HTTP.

Pattern:

```python
def test_products_list_renders_table(runner, httpx_mock, snapshot):
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/",
        json={"next": None, "results": [{"id": 1, "name": "alpha", ...}, ...]},
    )

    result = runner.invoke(app, ["products", "list"])
    assert result.exit_code == 0, result.output
    assert result.stdout == snapshot
```

To match a URL with query params explicitly:

```python
httpx_mock.add_response(
    url="https://dd.example/api/v2/products/?name=alpha&prod_type=3",
    json={"next": None, "results": []},
)
result = runner.invoke(app, ["products", "list", "--name", "alpha", "--prod-type", "3"])
```

To assert pagination is followed:

```python
httpx_mock.add_response(
    url="https://dd.example/api/v2/products/",
    json={"next": "https://dd.example/api/v2/products/?page=2", "results": [...]},
)
httpx_mock.add_response(
    url="https://dd.example/api/v2/products/?page=2",
    json={"next": None, "results": [...]},
)
```

To assert error mapping:

```python
httpx_mock.add_response(
    url="...",
    status_code=401,
    json={"detail": "Invalid token."},
)
result = runner.invoke(app, [...])
assert result.exit_code == 3                # AuthError → ExitCode.AUTH_ERROR
assert "Invalid token" in result.output     # message rendered to stderr
```

### Snapshot tests with `syrupy`

Used to pin table output (which is whitespace-sensitive and error-prone to assert by hand). The `snapshot` fixture comes from syrupy:

```python
def test_products_list_renders_table(runner, httpx_mock, snapshot):
    httpx_mock.add_response(...)
    result = runner.invoke(app, ["products", "list"])
    assert result.exit_code == 0
    assert result.stdout == snapshot
```

Snapshots live next to the test file in `__snapshots__/<test_file>.ambr`. Update with `pytest --snapshot-update <file>` and **inspect the diff** before committing — a wrong snapshot is silently locked in.

The repo has 12 snapshots as of v2.0; they cover table rendering for the 14 resources.

### Output-format round-trips

For each resource, there's a JSON output test that asserts the parsed JSON equals the expected dict — this catches column-projection bugs that snapshot tests can miss:

```python
def test_products_list_json_output(runner, httpx_mock):
    httpx_mock.add_response(...)
    result = runner.invoke(app, ["products", "list", "--output", "json"])
    assert result.exit_code == 0
    data = json.loads(result.stdout)
    assert data == [{"id": 1, "name": "x", "prod_type": 2, "business_criticality": "high", "lifecycle": None}]
```

### Action-verb tests

[tests/test_cli_action_verbs.py](../tests/test_cli_action_verbs.py) covers every action verb (`findings close/reopen/risk-accept`, `engagements close/reopen`, `users deactivate/activate`). Three tests per verb:

1. Happy path — mock the POST, assert exit 0 and the right URL.
2. `--dry-run` — **don't** mock anything, assert exit 0. If the dry-run accidentally calls HTTP, `pytest-httpx` fails the test.
3. `--yes` skips the confirmation prompt; declining the prompt exits 0 silently.

### Tests for `_resource.py` helpers

These are exercised through the resource modules — there's no direct test file for `_resource.py` itself. Adding a new helper means adding tests via a resource that uses it.

## Compat tests (`tests/compat/`)

**These are the most important tests in the suite.** They pin the legacy `dd-import` contract — every existing CI pipeline relies on this contract being unchanged.

[tests/compat/test_legacy_entry_points.py](../tests/compat/test_legacy_entry_points.py) marks the whole module:

```python
pytestmark = pytest.mark.compat
```

The autouse fixture is stricter than the unit tests:

```python
@pytest.fixture(autouse=True)
def _hermetic_env(tmp_path, monkeypatch):
    """Clear all DD_* / DD_CLI_* env vars and isolate config dir."""
    monkeypatch.setenv("DD_CLI_CONFIG_DIR", str(tmp_path))
    for var in list(os.environ.keys()):
        if var.startswith(("DD_", "DD_CLI_")):
            monkeypatch.delenv(var, raising=False)
```

Each test sets only the env vars the legacy CI pipeline would set (e.g. `DD_URL`, `DD_API_KEY`, `DD_PRODUCT_TYPE_NAME`, `DD_TEST_TYPE_NAME`, `DD_FILE_NAME`) and invokes the entry-point function directly:

```python
def test_reimport_findings_auto_create_happy_path(capsys, httpx_mock, monkeypatch, tmp_path):
    scan = tmp_path / "trivy.json"
    scan.write_text("{}")
    monkeypatch.setenv("DD_URL", "https://dd.example")
    monkeypatch.setenv("DD_API_KEY", "the-token")
    monkeypatch.setenv("DD_PRODUCT_TYPE_NAME", "Web")
    monkeypatch.setenv("DD_PRODUCT_NAME", "Payments")
    monkeypatch.setenv("DD_TEST_TYPE_NAME", "Trivy Scan")
    monkeypatch.setenv("DD_FILE_NAME", str(scan))
    monkeypatch.setenv("DD_AUTO_CREATE_CONTEXT", "true")

    httpx_mock.add_response(
        url="https://dd.example/api/v2/reimport-scan/",
        method="POST",
        json={"test": 1, "scan_type": "Trivy Scan"},
    )

    with pytest.raises(SystemExit) as excinfo:
        legacy.dd_reimport_findings_main()
    assert excinfo.value.code == 0

    captured = capsys.readouterr()
    assert "AUTO-CREATE" in captured.out
    assert "Import completed successfully" in captured.out
```

The tests **invoke the entry-point function directly** (rather than spawning a subprocess) — same code path as the installed console scripts (`pyproject.toml [project.scripts]` maps `dd-reimport-findings` → `dd_cli.cli.legacy:dd_reimport_findings_main`), but ~50× faster.

**What the compat suite asserts**:
- Identical exit codes (always 0 on success, **always 1 on any failure**).
- Identical stdout/stderr strings — including the `❌ Error during import:` and `✅ Import completed successfully!` lines that real CI logs grep for.
- Identical request payloads to DefectDojo (snapshot of the captured `httpx` calls).

**The strings are load-bearing.** When changing `cli/legacy.py` for any reason, run `pytest -m compat` first and confirm everything passes before doing anything else. If a compat test fails, **assume the production users would notice the change** and find another way to make your fix.

See [.claude/compatibility.md](compatibility.md) for the full list of guarantees.

## Integration tests (`tests/integration/`)

These hit a real DefectDojo. They catch things mocked tests can't:
- Real API response shapes survive `client.paginate` and `_parse_response`.
- The `Authorization: Token <key>` header is what DefectDojo actually expects.
- Quirks like the `found_by` requirement on findings-create (see [.claude/domain.md](domain.md)).
- Round-trip CRUD + every action verb actually flips the right state.

[tests/integration/conftest.py](../tests/integration/conftest.py) skips every integration test automatically when `DD_URL` or `DD_API_KEY` is missing:

```python
def pytest_collection_modifyitems(config, items):
    if os.environ.get("DD_URL") and os.environ.get("DD_API_KEY"):
        return
    skip_marker = pytest.mark.skip(reason="Integration tests require DD_URL and DD_API_KEY env vars.")
    for item in items:
        if "integration" in item.keywords:
            item.add_marker(skip_marker)
```

It also provides:

```python
@pytest.fixture
def isolated_config(tmp_path, monkeypatch):
    monkeypatch.setenv("DD_CLI_CONFIG_DIR", str(tmp_path))

@pytest.fixture
def cleanup_stack():
    """Records (resource, id) pairs to delete via dd-cli at teardown."""
    stack: list[tuple[str, int]] = []
    yield stack
    teardown = CliRunner()
    for resource, resource_id in reversed(stack):
        teardown.invoke(app, [resource, "delete", str(resource_id), "--yes"])
```

**Tests must clean up** — append `(resource, id)` to `cleanup_stack` for every resource they create. The teardown deletes them in reverse so the live DD ends each test in its starting state. Skipping cleanup means the next run inherits dirty state and probably fails non-deterministically.

The 24-test suite covers:
- `dd ping` against real DD (auth + connectivity).
- `dd <resource> list` for all 14 resources.
- Product round-trip (create → update → delete).
- Engagement close/reopen.
- Finding close/reopen/risk-accept.
- The `found_by` error-rendering test (see [domain.md](domain.md)).
- A real Trivy-report import end-to-end.
- User dry-run (no actual side effect — just asserts the dry-run output shape).

### Running locally

```bash
# Bring up DefectDojo via their docker compose
git clone https://github.com/DefectDojo/django-DefectDojo /tmp/dd && cd /tmp/dd
docker/setEnv.sh release
docker compose up -d
# wait ~5–10 min for /login to respond
ADMIN_PASS=$(docker compose logs initializer | grep "Admin password:" | sed -E 's/.*Admin password:[[:space:]]*//' | tr -d '[:space:]')
TOKEN=$(curl -sf -X POST http://localhost:8080/api/v2/api-token-auth/ \
  -H 'Content-Type: application/json' \
  -d "{\"username\":\"admin\",\"password\":\"$ADMIN_PASS\"}" | python3 -c "import json,sys; print(json.load(sys.stdin)['token'])")

cd <dd-cli-checkout>
DD_URL=http://localhost:8080 DD_API_KEY=$TOKEN make smoke
```

This is the same flow `.github/workflows/nightly-smoke.yml` runs in CI.

## Naming gotcha — `tests_cmd.py` is **not** a test file

`src/dd_cli/cli/tests_cmd.py` is the CLI module for `dd tests` (DefectDojo "tests" — the per-engagement scan results, not pytest tests). Naming collision with pytest's `tests_*.py` discovery pattern:

- ruff's `PT` (pytest-style) rule fires on the filename.
- `pyproject.toml` has a per-file ignore: `"**/tests_cmd.py" = ["PT"]`.
- The `_cmd` suffix is the workaround. **Don't rename the file.**

Other workarounds for similar collisions:
- Tests for the `dd tests` CLI go in [tests/test_cli_resources_m2b.py](../tests/test_cli_resources_m2b.py) — explicitly avoiding `test_tests*` which would be ambiguous.
- The `dd config` CLI module is [config_cmd.py](../src/dd_cli/cli/config_cmd.py) — same `_cmd` pattern, here to avoid shadowing the `dd_cli/config/` package.

## Coverage

`pytest --cov=dd_cli` runs by default (in `addopts`). Coverage configuration:

```toml
[tool.coverage.run]
source = ["dd_cli"]
branch = true
omit = ["*/dd_cli/_client/*", "*/tests/*"]
```

`coverage.xml` is written to the repo root after every test run (gitignored). CI uploads it as a workflow artifact (`coverage-xml`) on the Python 3.12 matrix slot only. **No coverage gate is currently enforced** — there's no `codecov.yml`, no `--cov-fail-under` in `addopts`. The project target is ≥85% (see [.claude/decisions.md](decisions.md#why-no-coverage-gate)) but it's advisory today.

If you want to gate locally:

```bash
pytest --cov-fail-under=85
# or for a specific suite:
pytest --cov-fail-under=85 tests/test_client.py
```

The repo currently runs at ~88% line coverage; the generated client and the legacy `dd_import/` directory (deleted in M4) are excluded.

## Writing a new test — checklist

Before pushing:

- [ ] **Right marker?** No marker for unit/snapshot. `@pytest.mark.compat` for compat (or `pytestmark = pytest.mark.compat` at module level). `@pytest.mark.integration` for integration.
- [ ] **Right directory?** Unit/snapshot in `tests/test_*.py`. Compat in `tests/compat/`. Integration in `tests/integration/`.
- [ ] **`isolated_env` fixture** (or equivalent) clears `DD_*`/`DD_CLI_*` and points `DD_CLI_CONFIG_DIR` at `tmp_path`?
- [ ] **No real HTTP?** All requests `httpx_mock.add_response(...)`-mocked. Unmocked = test fails.
- [ ] **Snapshot diff inspected** before committing if you ran `--snapshot-update`?
- [ ] **For integration tests**: every resource you create is appended to `cleanup_stack`?
- [ ] **For compat tests**: changes to stdout/stderr strings are intentional and the user knows about them?

## Debugging a flaky / failing test

1. **Run it alone**: `pytest tests/test_cli_resources.py::test_products_list_renders_table -xvs`.
2. **Show the captured stdout/stderr**: pass `-s` (don't capture) or check `result.output` in the assertion message. The repo's tests use `assert result.exit_code == 0, result.output` — output is included on failure.
3. **Inspect the snapshot**: open `tests/__snapshots__/<test_file>.ambr`.
4. **For integration**: tail the DefectDojo container logs (`docker compose logs uwsgi -f` from the `/tmp/dd` clone) to see the actual API request that failed.
