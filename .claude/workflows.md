# Workflows

Runbooks for the things contributors do most. Each workflow lists the exact commands, the files you'll edit, expected output, and what to do when a step fails.

## Setup (first time on this repo)

1. **Clone and install the dev extras.**
   ```bash
   git clone https://github.com/OsamaMahmood/dd-cli.git
   cd dd-cli
   make install-dev          # pip install -e ".[dev,test]"
   ```
   Adds `ruff`, `mypy`, `pytest`, `pytest-httpx`, `syrupy`, `hypothesis`. `make install-all` adds `mkdocs-material` (for docs work) and `openapi-python-client` (for client regeneration).

2. **Verify it works.**
   ```bash
   dd --version              # prints "dd <X.Y.Z>"
   make lint && make typecheck && make test
   ```
   Expected: all green; `make test` reports `257 passed, 24 deselected, 12 snapshots passed` (counts may have grown — the deselected count is the integration tests).

3. **(Optional) Configure a real DefectDojo for `dd ping`.**
   ```bash
   dd configure
   # Profile name [default]: default
   # DefectDojo URL: https://your-dd.example.com
   # API key (hidden): …
   dd ping
   # {"ok": true, "user": "alice", "url": "..."}
   ```
   Writes `~/.config/dd-cli/config.toml`. Override the location with `DD_CLI_CONFIG_DIR`.

## Add a new resource

When DefectDojo ships an API resource that doesn't have a corresponding `dd <resource>` command. Allow ~30 minutes for the full pattern.

1. **Create the module.** Copy [src/dd_cli/cli/products.py](../src/dd_cli/cli/products.py) — it's the cleanest minimal example. Rename the file, the spec constant, the sub-app variable, and update the `path` and `columns`:
   ```bash
   cp src/dd_cli/cli/products.py src/dd_cli/cli/<resource>.py
   ```
   Edit:
   ```python
   <RESOURCE>_SPEC = ResourceSpec(
       name="<singular>", plural="<resource>",
       path="/api/v2/<resource>/",
       columns=("id", "name", ...),     # default table columns
       name_field="name",                # default; override if DD uses "title", "username", etc.
   )

   <resource>_app = typer.Typer(
       name="<resource>",
       help="List and get DefectDojo <resource>.",
       no_args_is_help=True,
       rich_markup_mode="rich",
       context_settings={"help_option_names": ["-h", "--help"]},
   )
   ```

2. **Add resource-specific filters to `list`.** Look at the OpenAPI spec section for `/api/v2/<resource>/` (in [dd-api.json](../dd-api.json), grep for the path) — those query params become CLI flags. The pattern from [findings.py:54-101](../src/dd_cli/cli/findings.py):
   ```python
   @<resource>_app.command("list")
   def <resource>_list(
       ctx: typer.Context,
       <flag>: Annotated[<type> | None, typer.Option("--<flag>", help="...")] = None,
       limit: Annotated[int, typer.Option("--limit", ...)] = DEFAULT_LIMIT,
       all_pages: Annotated[bool, typer.Option("--all", ...)] = False,
       output: Annotated[OutputFormat | None, typer.Option("--output", "-o", ...)] = None,
   ) -> None:
       list_resource(
           ctx, <RESOURCE>_SPEC,
           filters={"<flag>": <flag>, ...},   # passed through to the query string
           limit=limit, all_pages=all_pages, output=output,
       )
   ```

3. **Add the `get` command** — boilerplate, just call `get_dispatch`:
   ```python
   @<resource>_app.command("get")
   def <resource>_get(
       ctx: typer.Context,
       <r>_id: Annotated[int | None, typer.Argument(help="<R> ID (omit if using --name).")] = None,
       name: Annotated[str | None, typer.Option("--name", help="Resolve by exact name.")] = None,
       output: Annotated[OutputFormat | None, typer.Option("--output", "-o", ...)] = None,
   ) -> None:
       get_dispatch(ctx, <RESOURCE>_SPEC, resource_id=<r>_id, name=name, output=output)
   ```

4. **Wire generic CRUD.** One line at the bottom:
   ```python
   register_crud(<resource>_app, <RESOURCE>_SPEC)
   ```
   That gives you `create`, `update`, `delete`, `edit` for free.

5. **Register the sub-app in [src/dd_cli/cli/app.py](../src/dd_cli/cli/app.py).** Add an import at the top and an `app.add_typer(...)` call (alphabetical order is preferred but not enforced):
   ```python
   from dd_cli.cli.<resource> import <resource>_app
   ...
   app.add_typer(<resource>_app)
   ```

6. **Add tests.** Open [tests/test_cli_resources.py](../tests/test_cli_resources.py) and follow the pattern of an existing block (e.g. `test_products_list_renders_table` and the four follow-up tests). At minimum:
   - Snapshot test for the table output (uses syrupy).
   - JSON output round-trip test.
   - Filter-passes-through-as-query-param test.
   - `get` by ID and `get --name` tests.

7. **Run the local checks.**
   ```bash
   make format && make lint && make typecheck && make test
   ```
   If snapshots fail because they're new: `pytest --snapshot-update tests/test_cli_resources.py` and inspect the diff.

8. **(Optional) Add an action verb** if the resource has a non-CRUD operation (close, deactivate, etc.). See "Add an action verb" below.

**Failure recovery**:
- If `make test` says `pytest_collection_modifyitems` failed → you forgot the `runner` fixture import or you accidentally set the file as `tests_<name>.py`. Rename to `test_cli_<resource>.py`.
- If ruff complains about `PT` rules in your new file → you put the CLI module in `tests/` by mistake. Move it back to `src/dd_cli/cli/`.

## Add an action verb to an existing resource

DefectDojo has dedicated `/close/`, `/reopen/`, `/risk-accept/`, etc. endpoints on some resources. These don't fit CRUD, so they live as named commands.

1. **Pick the canonical example.** [findings.py:close](../src/dd_cli/cli/findings.py) and [engagements.py:close](../src/dd_cli/cli/engagements.py) cover the two common shapes (with a payload, with no payload).

2. **Add the import** for the helpers if not already present:
   ```python
   from dd_cli.cli._resource import (
       confirm_or_abort, get_active_profile,
       print_dry_run, render_response,
   )
   ```

3. **Add the command** below `register_crud(...)`. Pattern (with payload):
   ```python
   @<resource>_app.command("<verb>")
   def <resource>_<verb>(
       ctx: typer.Context,
       <r>_id: Annotated[int, typer.Argument(help="<R> ID.")],
       # ... verb-specific flags ...
       yes: Annotated[bool, typer.Option("--yes", "-y", help="Skip confirmation.")] = False,
       dry_run: Annotated[bool, typer.Option("--dry-run", help="Print intent only.")] = False,
       output: Annotated[OutputFormat | None, typer.Option("--output", "-o", help="Output format.")] = None,
   ) -> None:
       """One-line summary used as the --help text."""
       payload: dict[str, Any] = {...}
       target = f"/api/v2/<resource>/{<r>_id}/<verb>/"

       if dry_run:
           print_dry_run("POST", target, payload, ctx, output)
           return
       confirm_or_abort(f"<Verb> <r> {<r>_id}?", yes=yes)

       profile = get_active_profile(ctx)
       with DefectDojoClient(profile) as client:
           body = client.post(target, json=payload)

       typer.echo(f"<Verbed> <r> {<r>_id}.")
       render_response(body, ctx, output)
   ```

4. **Add tests** in [tests/test_cli_action_verbs.py](../tests/test_cli_action_verbs.py). At minimum:
   - Happy path: mock the POST, assert exit 0 and the right URL was called.
   - `--dry-run` test: assert **no HTTP** is sent (pytest-httpx fails on unmocked requests, so just don't add a mock and assert exit 0).
   - `--yes` skips the confirmation prompt.
   - Confirmation declined exits 0 silently.

5. **Run locally**: `make format && make lint && make typecheck && make test`.

## Add a new import knob (`DD_NEW_FLAG` / `--new-flag`)

When DefectDojo's `/reimport-scan/` endpoint accepts a new field that the CLI should expose.

1. **Add a field to `ImportFindingsOptions`** in [src/dd_cli/workflows/import_findings.py](../src/dd_cli/workflows/import_findings.py). Pattern:
   ```python
   new_flag: bool = Field(
       default=False,
       validation_alias=AliasChoices("DD_CLI_NEW_FLAG", "DD_NEW_FLAG"),
   )
   ```
   Order in `AliasChoices` is **(new, old)** — the first one wins. If the field is brand-new (no legacy `dd-import` equivalent), drop the `DD_*` alias and keep just `DD_CLI_NEW_FLAG`.

2. **Wire the field into the workflow body** — `workflows/import_findings.py:ImportFindingsWorkflow.run()` builds the multipart payload. Add the new field to the `data=` dict in the right branch (auto-create or traditional or both).

3. **Add a CLI flag** in [src/dd_cli/cli/import_cmd.py](../src/dd_cli/cli/import_cmd.py) using `Annotated[..., typer.Option(...)]` and pass it via `make_findings_options(new_flag=new_flag, ...)`.

4. **Add a compat test** in [tests/compat/test_legacy_entry_points.py](../tests/compat/test_legacy_entry_points.py) **only if the field has a legacy `DD_*` alias.** The test should set the env var and assert the request payload contains the right value.

5. **Update the docs** — [docs/configuration.md](../docs/configuration.md) DD_* env-var table.

6. **Local checks**:
   ```bash
   make format && make lint && make typecheck && make test
   ```
   Compat tests (`pytest -m compat`) are part of `make test`.

## Regenerate the API client

When DefectDojo upgrades and ships new endpoints, or when an existing endpoint's shape changed.

1. **Update [`dd-api.json`](../dd-api.json).** Either pull from a live DefectDojo:
   ```bash
   curl -sS https://your-dd/api/v2/oa3/schema/?format=json -o dd-api.json
   ```
   or download from a known release of DefectDojo. The file is committed.

2. **Install the generator** (once):
   ```bash
   make install-all     # adds openapi-python-client
   ```

3. **Regenerate.**
   ```bash
   make generate-client
   ```
   Wipes `src/dd_cli/_client/` and writes a fresh tree. Output ends with `Client regenerated. Review the diff before committing.`

4. **Review the diff.** `git diff src/dd_cli/_client/` — expect new endpoint files for new paths, possibly small attrs-class changes for existing ones. Reject the diff if the changes are mostly cosmetic noise; rerun the generator if needed.

5. **Verify nothing broke.**
   ```bash
   pip install -e ".[dev,test]"   # picks up any new generated runtime deps
   make lint                      # generated files are excluded; this only re-lints our code
   make typecheck                 # ensures call sites still type-check
   make test
   ```

6. **Commit `dd-api.json` + `_client/` together.** Message: `chore(client): regenerate from DefectDojo <X.Y.Z> spec`.

**Failure recovery**:
- If `make typecheck` errors with `dd_cli._client.api.<thing> is missing` → an endpoint we use was renamed. Update the call site in `client.py` or wherever it's referenced.
- If `make generate-client` errors with `openapi-python-client: command not found` → run `make install-all`.
- If pip refuses to install with new attrs/dateutil pins → bump the deps in `pyproject.toml`.

## Run tests

```bash
make test            # unit + snapshot + compat (~257 + 12 + 9, ~20s)
make test-cov        # same, with HTML coverage report at htmlcov/index.html
make smoke           # integration suite (24 tests) against a live DD — requires DD_URL + DD_API_KEY
```

`make smoke` checks the env vars first and refuses to run if either is missing. Stand up a local DD via DefectDojo's docker compose:

```bash
git clone https://github.com/DefectDojo/django-DefectDojo /tmp/dd && cd /tmp/dd
docker/setEnv.sh release
docker compose up -d
# wait ~5–10 min until /login responds
ADMIN_PASS=$(docker compose logs initializer | grep "Admin password:" | sed -E 's/.*Admin password:[[:space:]]*//' | tr -d '[:space:]')
TOKEN=$(curl -sf -X POST http://localhost:8080/api/v2/api-token-auth/ \
  -H 'Content-Type: application/json' \
  -d "{\"username\":\"admin\",\"password\":\"$ADMIN_PASS\"}" | python3 -c "import json,sys; print(json.load(sys.stdin)['token'])")
DD_URL=http://localhost:8080 DD_API_KEY=$TOKEN make smoke
```

(Same flow as `.github/workflows/nightly-smoke.yml` runs in CI.)

See [.claude/testing.md](testing.md) for what each suite covers and how to write tests in each.

## Cut a release

Tag-driven. Pushing a tag matching `v*` to GitHub triggers `.github/workflows/release.yml`.

1. **Make sure `main` is what you want shipped.**
   ```bash
   git checkout main && git pull --ff-only origin main
   ```

2. **Pick the version** following [SemVer](https://semver.org/). Stable: `v2.1.0`. Prerelease: `v2.1.0-rc.1` (the workflow detects the `-` and marks it prerelease, no `:latest` Docker alias).

3. **Tag and push.**
   ```bash
   git tag -a v2.1.0 -m "v2.1.0"
   git push origin v2.1.0
   ```

4. **Watch [Actions → Release](https://github.com/OsamaMahmood/dd-cli/actions/workflows/release.yml).** It will:
   - Verify the tag points at a commit reachable from `origin/main` (guard added after v0.4.0 footgun — see [decisions.md](decisions.md)).
   - Build sdist + wheel via `python -m build`.
   - Verify `dd --version` from the wheel matches the **PEP 440-normalized** tag. `v2.0.0-rc.1` → `2.0.0rc1`; the workflow uses `packaging.version.Version()` to canonicalise both sides before comparing.
   - Generate `SHA256SUMS`.
   - Create the GitHub Release (auto-generated notes from PRs since the previous tag).
   - Publish to PyPI via OIDC (no token in repo — uses the `pypi` GHA environment).
   - Build & push multi-arch (linux/amd64 + linux/arm64) Docker image to `ghcr.io/osamamahmood/dd-cli` and **`m4rkm3n/dd-cli`** (Docker Hub namespace differs from the GitHub handle — see [release.md](release.md)).

5. **Verify**: visit https://pypi.org/project/dd-cli/, the [GitHub Release page](https://github.com/OsamaMahmood/dd-cli/releases), and `docker pull ghcr.io/osamamahmood/dd-cli:<tag>`.

**Failure recovery**: see [.claude/release.md](release.md) — covers re-running the workflow, manually creating a missing release with `gh release create`, and undoing a bad tag with `gh release delete --cleanup-tag`.

## Build / serve docs locally

The site at https://osamamahmood.github.io/dd-cli/ is built by `mkdocs-material` from [docs/](../docs/) and deployed by `.github/workflows/docs.yml` on every push to `main` that touches `docs/**`, `mkdocs.yml`, or `src/dd_cli/cli/**`.

```bash
make install-all      # adds mkdocs-material, mkdocs-click, mkdocstrings
make docs-serve       # http://localhost:8000 — live reload on file changes
make docs             # mkdocs build --strict (what CI runs; fails on broken links / missing pages)
```

The CLI reference page ([docs/cli-reference.md](../docs/cli-reference.md)) auto-generates from the Typer app via `mkdocs-click`:

```markdown
::: mkdocs-click
    :module: dd_cli.cli.app
    :command: click_app
    :prog_name: dd
    :depth: 1
    :style: table
    :list_subcommands: true
```

`click_app = typer.main.get_command(app)` is exported in [cli/app.py](../src/dd_cli/cli/app.py) for this — `mkdocs-click` requires a Click `Command`, not a Typer app.

**`mkdocs-click` is a markdown extension, not a plugin.** In `mkdocs.yml` it must be listed under `markdown_extensions:`, not `plugins:`. Putting it under `plugins:` fails with `The "mkdocs-click" plugin is not installed`.

## Verify a change against a live DefectDojo

Quick sanity check against your own instance:

```bash
dd configure                              # one-time: writes ~/.config/dd-cli/config.toml
dd ping                                   # confirms URL + API key
dd products list --limit 5
dd products get --name "<known-product>"  # name resolution
dd findings list --severity Critical --output json | jq '. | length'
```

Or, against the dockerized DD from "Run tests":

```bash
DD_URL=http://localhost:8080 DD_API_KEY=$TOKEN dd ping
```

## Common one-offs

| Task | Command |
|---|---|
| See every Typer subcommand | `dd --help` |
| Reset config | `rm -rf ~/.config/dd-cli/` then `dd configure` |
| Use a different config dir for one command | `DD_CLI_CONFIG_DIR=/tmp/test dd ping` |
| Mask the API key in `dd config show` | (default) — pass `--show-secrets` to reveal |
| Find every DD_* env var the CLI reads | `grep -nE 'AliasChoices.*"DD_' src/dd_cli/` |
| Check coverage | `make test-cov` then `open htmlcov/index.html` |
| List every endpoint dd-cli touches | `grep -nE '/api/v2/[a-z_/-]+' src/dd_cli/ -r` |
