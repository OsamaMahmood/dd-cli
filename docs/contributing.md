# Contributing

dd-cli is maintained by [Osama Mahmood](https://github.com/OsamaMahmood) and welcomes contributions of any size — bug reports, doc fixes, new commands, scanner integrations.

## Setup

```bash
git clone https://github.com/OsamaMahmood/dd-cli.git
cd dd-cli
pip install -e ".[dev,test,docs]"
```

The `[dev,test]` extras give you ruff, mypy, pytest. The `[docs]` extra adds mkdocs-material so you can preview the docs site locally.

## Make targets

| | What |
|---|---|
| `make install-dev` | `pip install -e ".[dev,test]"` |
| `make install-all` | adds `[docs,client-gen]` |
| `make lint` | `ruff check` + `ruff format --check` |
| `make format` | `ruff check --fix` + `ruff format` |
| `make typecheck` | `mypy --strict` |
| `make test` | `pytest` (excludes `@pytest.mark.integration`) |
| `make test-cov` | with HTML coverage report |
| `make smoke` | runs `pytest -m integration` against a live DD instance (requires `DD_URL` + `DD_API_KEY` env vars) |
| `make docs` | `mkdocs build --strict` |
| `make docs-serve` | `mkdocs serve` on `:8000` |
| `make generate-client` | regenerates `src/dd_cli/_client/` from `dd-api.json` |
| `make build` | `python -m build` (sdist + wheel) |
| `make clean` | wipe caches and build artifacts |

## Test categories

| Suite | Marker | Runs by default | Needs |
|---|---|---|---|
| Unit | (none) | yes | nothing |
| Snapshot | (none, syrupy) | yes | nothing |
| Compat (`tests/compat/`) | `@pytest.mark.compat` | yes | nothing |
| Integration (`tests/integration/`) | `@pytest.mark.integration` | **no** — opt in via `make smoke` | `DD_URL`, `DD_API_KEY` env vars + a reachable DefectDojo instance |

The default `pytest` invocation runs unit + snapshot + compat (257 tests at the time of this writing). Integration tests are excluded via `addopts = ["-m", "not integration", ...]` in `pyproject.toml`.

## Code style

- **`ruff`** for lint + format. Config in `pyproject.toml`. Run `make format` before committing.
- **`mypy --strict`** for type-checks. Generated `src/dd_cli/_client/` is excluded; everything else is strict.
- **No emojis in code or docstrings** unless explicitly meaningful (the legacy `❌ Error during import:` prefix is a deliberate exception for the migration shim).
- **One short comment per non-obvious WHY.** Code that explains itself doesn't need a comment.

## Regenerating the API client

When DefectDojo cuts a new version with new endpoints we need:

```bash
# 1. Update dd-api.json (download from your DefectDojo instance)
curl -sS http://your-dd/api/v2/oa3/schema/?format=json -o dd-api.json

# 2. Regenerate the typed client
make generate-client

# 3. Verify everything still builds and passes
pip install -e ".[dev,test]"
make lint && make typecheck && make test
```

The generated tree is vendored — committed to the repo. `make generate-client` overwrites it.

## Adding a new resource

To add CLI surface for a new DefectDojo resource (when DD ships one in a future version):

1. Create `src/dd_cli/cli/<resource>.py` following the pattern of one of the existing 12 (`products.py` is the cleanest reference).
2. Add a `ResourceSpec` with the resource's API path, default columns, and `name_field`.
3. Wire `register_crud(<sub_app>, <SPEC>)` at the bottom — gives you `create`, `update`, `delete`, `edit` for free.
4. Implement `list` and `get` Typer commands using `list_resource()` and `get_dispatch()` from `cli/_resource.py`.
5. Add the sub-app to `cli/app.py`.
6. Add tests in `tests/test_cli_resources.py` (or `_m2b.py`).
7. Add a snapshot test for the table output.

Look at any existing M2 commit (PR #4 or PR #5) for the full pattern.

## Releasing

See [`RELEASING.md`](https://github.com/OsamaMahmood/dd-cli/blob/main/RELEASING.md) for the tag-driven release process.

In short: push a tag, the workflow handles GitHub Release + PyPI + Docker. Both registries get multi-arch images. Use SemVer. Prereleases use `-rc.N` suffix.

## PR conventions

- Conventional Commits style for messages (`feat(cli):`, `fix(client):`, `docs:`, `chore:`, `test:`, `refactor:`).
- One logical change per PR. The repo's history has lots of focused PRs as a reference.
- CI must be green before merge.
- The "Test plan" section of a PR description is a checkbox list for the reviewer to walk through. Include realistic local-validation steps.
- Don't add a `Co-Authored-By: Claude` trailer.

## Reporting bugs

Open an issue at [github.com/OsamaMahmood/dd-cli/issues](https://github.com/OsamaMahmood/dd-cli/issues). Helpful info to include:

- `dd --version`
- The DefectDojo version you're running against (`/api/v2/oa3/schema/`)
- The full command + the output (redact secrets)
- For import bugs: the full `DD_*` env-var set you used (redacted)

## License

dd-cli is BSD 3-Clause licensed — same as the upstream `dd-import` it succeeds.
