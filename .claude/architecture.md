# Architecture

`dd-cli` is a Python CLI that wraps DefectDojo's REST API (~226 path templates, ~450 operations across ~80 resources). The codebase is layered so that the dominant concern at each level is independent of the others.

```
┌────────────────────────────────────────────────────────────────┐
│  CLI layer  (Typer)                                            │
│  src/dd_cli/cli/app.py — root app + 14 sub-apps + ping/configure
│  One module per resource: products.py, findings.py, ...        │
│  Generic CRUD via cli/_resource.py                             │
└──────────┬─────────────────────────────┬───────────────────────┘
           │                             │
           ▼                             ▼
  ┌────────────────────┐         ┌──────────────────────────────┐
  │ Workflows          │         │ Legacy shims                 │
  │ workflows/         │         │ cli/legacy.py                │
  │ import_findings.py │         │ entry points for             │
  │ import_languages.py│         │ dd-reimport-findings,        │
  │                    │         │ dd-import-languages          │
  └─────────┬──────────┘         └─────────┬────────────────────┘
            │                              │
            └──────────┬───────────────────┘
                       ▼
         ┌──────────────────────────────────────┐
         │  DefectDojoClient  (client.py)       │
         │  retry · paginate · error map ·      │
         │  multipart upload                    │
         └──────────────┬───────────────────────┘
                        ▼
            ┌────────────────────────────┐
            │ Generated client (_client/)│
            │ openapi-python-client out  │
            │ vendored, attrs-based      │
            │ excluded from ruff/mypy    │
            └──────────────┬─────────────┘
                           ▼  Authorization: Token <key>
                   ┌──────────────────┐
                   │  DefectDojo API  │
                   └──────────────────┘

  ┌──────────────────────────┐    ┌──────────────────────────┐
  │ Config (config/)         │    │ Output (output/)         │
  │ pydantic-settings layers │    │ table · json · yaml      │
  │ TOML profile + DD_*/     │    │ via Renderer Protocol    │
  │ DD_CLI_* env             │    │                          │
  │ XDG paths                │    └──────────────────────────┘
  └──────────────────────────┘

  ┌──────────────────────────┐
  │ Errors (errors.py)       │
  │ DDCliError → exit codes  │
  │ HTTP status → typed exc. │
  └──────────────────────────┘
```

## Layer 1 — CLI (Typer)

### Root app

[src/dd_cli/cli/app.py](../src/dd_cli/cli/app.py) builds one Typer app with global options (`--profile`, `--output`, `--verbose`, `--version`) and registers every sub-app:

```python
# src/dd_cli/cli/app.py:34-57 (abridged)
app = typer.Typer(name="dd", help="Production-grade CLI for managing DefectDojo.", ...)
app.add_typer(config_app)
app.add_typer(products_app)
app.add_typer(product_types_app)
app.add_typer(engagements_app)
# ... 14 sub-apps total ...
app.add_typer(import_app)
app.command("configure", ...)(configure)
app.command("ping", ...)(ping)
click_app = typer.main.get_command(app)
```

`click_app` is a Click `Command` exported for `mkdocs-click` (the docs CLI reference auto-generator) — `mkdocs-click` requires a `click.Command`, not a Typer app.

The shell entry point is `dd_cli.cli.app:main` (mapped via `[project.scripts]` in `pyproject.toml`). It catches `DDCliError` and exits with the typed exit code; everything else propagates as exit 1. Don't `sys.exit()` from inside command bodies — raise a typed error instead.

### Resource modules — the dominant pattern

Fourteen resources under [src/dd_cli/cli/](../src/dd_cli/cli/) follow an identical shape. The minimum viable resource module is ~95 lines:

```python
# src/dd_cli/cli/products.py — the canonical example
from dd_cli.cli._resource import (
    DEFAULT_LIMIT, ResourceSpec,
    get_dispatch, list_resource, register_crud,
)

PRODUCTS_SPEC = ResourceSpec(
    name="product", plural="products",
    path="/api/v2/products/",
    columns=("id", "name", "prod_type", "business_criticality", "lifecycle"),
)

products_app = typer.Typer(
    name="products",
    help="List and get DefectDojo products.",
    no_args_is_help=True,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
)

@products_app.command("list")
def products_list(ctx, name=None, prod_type=None, tag=None, limit=DEFAULT_LIMIT, all_pages=False, output=None):
    list_resource(ctx, PRODUCTS_SPEC,
                  filters={"name": name, "prod_type": prod_type, "tag": tag},
                  limit=limit, all_pages=all_pages, output=output)

@products_app.command("get")
def products_get(ctx, product_id=None, name=None, output=None):
    get_dispatch(ctx, PRODUCTS_SPEC, resource_id=product_id, name=name, output=output)

register_crud(products_app, PRODUCTS_SPEC)
```

`register_crud` attaches `create`, `update`, `delete`, and `edit` commands using the shared payload-building flags (`--from-file`, `--field key=value`, `--dry-run`, `--yes` on delete). Per-resource modules add their own ergonomic command flags on top — e.g. `dd findings list --severity High --product 12 --active`.

**Action verbs** (`dd findings close`, `dd users deactivate`, `dd engagements close/reopen`) are added in the same module on top of the generic CRUD. They use the public helpers exported by `_resource.py`:

| Helper | Purpose |
|---|---|
| `get_active_profile(ctx)` | Resolve profile from CLI ctx + env + TOML, raise `ConfigError` if incomplete |
| `get_output_format(ctx, override)` | Resolve `OutputFormat` from CLI ctx with optional override |
| `confirm_or_abort(msg, yes=...)` | Prompt unless `yes=True`; exit 0 on decline |
| `print_dry_run(method, path, payload, ctx, output)` | Echo intended request without sending HTTP |
| `render_response(body, ctx, output)` | Render via the active formatter; skip empty bodies |

The pattern for an action verb (from [src/dd_cli/cli/findings.py:173-217](../src/dd_cli/cli/findings.py)):

```python
@findings_app.command("close")
def findings_close(ctx, finding_id, note=None, false_positive=False, ..., yes=False, dry_run=False, output=None):
    payload = {"is_mitigated": True}
    if note: payload["note"] = note
    if false_positive: payload["false_p"] = True
    target = f"/api/v2/findings/{finding_id}/close/"

    if dry_run:
        print_dry_run("POST", target, payload, ctx, output)
        return
    confirm_or_abort(f"Close finding {finding_id}?", yes=yes)

    profile = get_active_profile(ctx)
    with DefectDojoClient(profile) as client:
        body = client.post(target, json=payload)

    typer.echo(f"Closed finding {finding_id}.")
    render_response(body, ctx, output)
```

### Why this design

The OpenAPI spec describes 226 path templates. Hand-writing 14 list/get/create/update/delete commands × ~10 lines each would be ~700 lines of boilerplate. The `_resource.py` indirection means each new resource module costs you ~95 lines and any improvement to CRUD ergonomics flows to all 14 at once. That's the deal.

## Layer 2 — Workflows

[src/dd_cli/workflows/](../src/dd_cli/workflows/) holds multi-step business logic that's distinct from "call one endpoint and render the result":

- **[import_findings.py](../src/dd_cli/workflows/import_findings.py)** — uploads a scan report. Two strategies, picked by `auto_create_context`:
  - **Auto-create**: single POST to `/api/v2/reimport-scan/` with `auto_create_context: true`; DefectDojo creates the product type → product → engagement → test chain. One API call.
  - **Traditional**: GET-or-POST chain — `/product_types/?name=…` → `/products/?name=…&prod_type=N` → `/engagements/?name=…&product=N` → `/tests/?title=…&engagement=N` → POST `/reimport-scan/` → optional PATCH `/engagements/N/` for build context. ~5 API calls.
- **[import_languages.py](../src/dd_cli/workflows/import_languages.py)** — uploads `cloc` JSON to `/api/v2/import-languages/` with the same auto-create logic, scoped to the product.

Each workflow's options are a `pydantic_settings.BaseSettings` model. **Every CLI flag has a matching `validation_alias=AliasChoices("DD_CLI_*", "DD_*")`** so users coming from `dd-import` can keep their `DD_*` env vars unchanged. The legacy shims ([cli/legacy.py](../src/dd_cli/cli/legacy.py)) call these workflows with no overrides; the new ergonomic command [cli/import_cmd.py](../src/dd_cli/cli/import_cmd.py) passes explicit values from CLI flags.

Example option field ([workflows/import_findings.py:78-81](../src/dd_cli/workflows/import_findings.py)):

```python
product_type_name: str | None = Field(
    default=None,
    validation_alias=AliasChoices("DD_CLI_PRODUCT_TYPE", "DD_PRODUCT_TYPE_NAME"),
)
```

The list of `validation_alias` entries is also the contract pinned by `tests/compat/test_legacy_entry_points.py` — see [.claude/compatibility.md](compatibility.md).

## Layer 3 — DefectDojoClient (HTTP wrapper)

[src/dd_cli/client.py](../src/dd_cli/client.py) is a hand-written wrapper around the generated `AuthenticatedClient`. It adds five things the generated client deliberately doesn't:

### 1. Retry with exponential backoff

```python
RETRYABLE_STATUS_CODES = frozenset({429, 500, 502, 503, 504})
DEFAULT_MAX_RETRIES = 3
DEFAULT_BACKOFF_FACTOR = 0.5  # delay(attempt) = 0.5 * 2^attempt
```

Retries on transport errors (`httpx.TimeoutException`, `httpx.RequestError`) and on the listed status codes. Exhausting retries on a transport error raises `NetworkError` (exit 8); exhausting on a status code returns the last response and lets `_parse_response` map it to a typed exception.

### 2. Pagination iterator

`client.paginate(path, params=...)` yields one item at a time from a list endpoint, walking the `next` URL each response returns. Subsequent pages embed all params in `next`, so the caller's `params` are only sent on the first request.

```python
for item in client.paginate("/api/v2/products/", params={"name": "Payments"}):
    ...
```

This is what `list_resource` calls; callers rarely use it directly.

### 3. Error mapping

`_parse_response` reads `response.json()` and raises:

| HTTP | Exception | Exit code |
|---|---|---|
| 2xx | (returns body) | — |
| 400 | `ValidationError` | 6 |
| 401 | `AuthError` | 3 |
| 403 | `AuthorizationError` | 4 |
| 404 | `NotFoundError` | 5 |
| 5xx after retries | `APIError` | 7 |

Error message extraction handles three response shapes DefectDojo actually returns:
- `{"detail": "..."}` → `"HTTP 401: <detail>"`
- `{"<field>": ["msg", ...], ...}` (DRF field-level validation) → `"HTTP 400: field=msg1; field2=msg2"`
- anything else → `"HTTP <code>: <json-formatted body>"`

DefectDojo Pro upsell keys (`pro` and `message`) are stripped. They appear in some error responses and otherwise drown the real problem.

### 4. Multipart upload

`client.upload(path, data=..., file=(filename, content))` is used by the import workflows for `/api/v2/reimport-scan/` and `/api/v2/import-languages/`. Two non-obvious details:

- **httpx requires a non-empty `files` dict to switch to multipart**, so when we have form fields but no actual file, we send a placeholder (`("", b"", "application/octet-stream")`). DefectDojo reuses the previous scan file in that case — matching legacy `dd-import` behavior.
- **Form fields are coerced** by `_flatten_for_multipart`: `bool` → `"true"`/`"false"`, `None` dropped (so it doesn't appear as the literal string `"None"`), lists → repeated keys, ints/floats kept as-is.

### 5. Auth header injection

The generated client takes `token`, `prefix="Token"`, `auth_header_name="Authorization"` and emits `Authorization: Token <key>`. The wrapper also forwards `extra_headers` from the profile (covers `DD_EXTRA_HEADER_<N>` legacy compat — see [compatibility.md](compatibility.md)).

The wrapper is a context manager — wrap with `with DefectDojoClient(profile) as client:` so the underlying httpx connection pool is closed.

## Layer 4 — Generated client (`_client/`)

[src/dd_cli/_client/](../src/dd_cli/_client/) is the output of [`openapi-python-client`](https://github.com/openapi-generators/openapi-python-client) run against [dd-api.json](../dd-api.json). It's **vendored** (committed to the repo) so installs work offline and PRs are greppable for endpoint shapes.

**Hard rules**:
- Never edit by hand. Regenerate via `make generate-client`.
- It's excluded from ruff (`extend-exclude` in pyproject.toml), mypy (`exclude` + module-level `ignore_errors`), and coverage (`omit`). Don't try to "fix" the warnings inside it.
- It uses **attrs**, not pydantic. Both `attrs>=23.2` and `python-dateutil>=2.9` are runtime deps because of this.
- The wrapper in `client.py` mostly bypasses the generated endpoints and uses `client.raw.get_httpx_client()` directly — the generated per-endpoint functions are typed but verbose, and we're already paying the runtime cost of the typed models for free.

## Layer 5 — Config (`config/`)

[src/dd_cli/config/](../src/dd_cli/config/) is three small modules:

- **[paths.py](../src/dd_cli/config/paths.py)** — XDG-compliant config dir resolution. Honors `DD_CLI_CONFIG_DIR` (used heavily in tests), then `XDG_CONFIG_HOME`, then `~/.config/dd-cli/` on Unix; `%APPDATA%\dd-cli\` on Windows.
- **[settings.py](../src/dd_cli/config/settings.py)** — pydantic models:
  - `Profile` (per-target: `name`, `url`, `api_key: SecretStr`, `ssl_verify: bool`, `extra_headers: dict[str, str]`)
  - `Config` (top-level: `default_profile: str`, `profiles: dict[str, Profile]`)
  - `_EnvOverrides` — env-var view, reads `DD_CLI_URL` / `DD_URL`, `DD_CLI_API_KEY` / `DD_API_KEY`, `DD_CLI_SSL_VERIFY` / `DD_SSL_VERIFY` via `AliasChoices`. **`DD_CLI_*` is listed first** in `AliasChoices(...)` → it takes precedence.
  - `load_config(path)` / `save_config(config, path)` — TOML I/O via `tomllib`/`tomli-w`.
  - `load_profile(name=None, *, apply_env=True)` — the function callers actually use; merges defaults → TOML profile → env overrides.
- **[legacy_env.py](../src/dd_cli/config/legacy_env.py)** — handles `DD_EXTRA_HEADER_<N>` / `DD_EXTRA_HEADER_<N>_VALUE` paired vars (slots 1 and 2). pydantic-settings can't model the pairing directly, so this module does it imperatively and returns a `{name: value}` dict that `load_profile` merges into `Profile.extra_headers`.

Profile models use `extra="forbid"` (catches typos in `config.toml`); `_EnvOverrides` uses `extra="ignore"` (ignore unrelated env vars in the user's shell).

## Layer 6 — Output (`output/`)

[src/dd_cli/output/](../src/dd_cli/output/) is a tiny dispatcher:

```python
class OutputFormat(StrEnum):
    table = "table"
    json = "json"
    yaml = "yaml"

def render(data, fmt=OutputFormat.table, *, columns=None) -> str:
    renderers = {
        OutputFormat.table: TableRenderer(),
        OutputFormat.json: JsonRenderer(),
        OutputFormat.yaml: YamlRenderer(),
    }
    return renderers[fmt].render(data, columns=columns)
```

`Renderer` is a `Protocol` — table uses Rich, JSON uses `orjson`, YAML uses PyYAML. `columns` is a hint for table rendering only; JSON/YAML preserve the input structure verbatim.

The active format propagates via `ctx.obj["output"]` set by the root callback in `cli/app.py`. `_resource.py` resolves it via `get_output_format(ctx, override)`.

## Layer 7 — Errors (`errors.py`)

[src/dd_cli/errors.py](../src/dd_cli/errors.py) is the typed exception hierarchy:

```python
class DDCliError(Exception):
    exit_code: int = ExitCode.GENERIC_ERROR     # 1
    def __init__(self, message: str, *, hint: str | None = None): ...

class AuthError(DDCliError):          exit_code = ExitCode.AUTH_ERROR        # 3
class AuthorizationError(DDCliError): exit_code = ExitCode.AUTHZ_ERROR       # 4
class NotFoundError(DDCliError):      exit_code = ExitCode.NOT_FOUND          # 5
class ValidationError(DDCliError):    exit_code = ExitCode.VALIDATION_ERROR   # 6
class APIError(DDCliError):           exit_code = ExitCode.API_ERROR          # 7
class NetworkError(DDCliError):       exit_code = ExitCode.NETWORK_ERROR      # 8
class ConfigError(DDCliError):        exit_code = ExitCode.CONFIG_ERROR       # 9
```

`from_status_code(status, message, hint=None)` maps an HTTP status to the right typed exception (`client.py:_parse_response` uses it).

The `cli/app.py:main()` wrapper is the only place that handles these:

```python
def main() -> None:
    try:
        app()
    except DDCliError as exc:
        err_console.print(f"[red bold]Error:[/red bold] {exc.message}")
        if exc.hint:
            err_console.print(f"[yellow]Hint:[/yellow] {exc.hint}")
        raise SystemExit(exc.exit_code) from None
```

**The legacy shims [cli/legacy.py](../src/dd_cli/cli/legacy.py) bypass this** — they catch `DDCliError` and unconditionally `sys.exit(1)` to match the upstream `dd-import` exit-1-on-any-failure contract. See [compatibility.md](compatibility.md).

## End-to-end data flow

### Read flow: `dd products list --name Payments --output json`

1. Typer parses args → `products_list(ctx, name="Payments", ..., output=OutputFormat.json)`.
2. `list_resource(ctx, PRODUCTS_SPEC, filters={"name": "Payments", ...}, ...)`.
3. `_resolved_profile_name(ctx)` reads `ctx.obj["profile"]` (set by the root callback).
4. `load_profile(profile_name)` → defaults → TOML at `~/.config/dd-cli/config.toml` → env (`DD_CLI_URL`/`DD_URL` etc.).
5. `_require_complete(...)` raises `ConfigError(exit 9)` if `url` or `api_key` is missing.
6. `with DefectDojoClient(profile) as client:` opens an authenticated httpx session.
7. `client.paginate("/api/v2/products/", params={"name": "Payments"})` yields items, walking `next` URLs.
8. `islice(iterator, 50)` caps at `--limit` (default 50) unless `--all`.
9. Column projection: `[{col: item.get(col) for col in cols} for item in items]`.
10. `render(records, OutputFormat.json)` → `JsonRenderer` → orjson dump → `typer.echo(...)`.

A 401 anywhere in step 7 raises `AuthError`, propagates to `main()`, prints the error + hint, exits 3.

### Write flow: `dd products create --field name=Foo --field prod_type=2`

1. `register_crud`'s `_create` Typer command runs.
2. `create_resource(ctx, PRODUCTS_SPEC, from_file=None, fields=["name=Foo", "prod_type=2"], dry_run=False, output=None)`.
3. `build_payload(...)` parses each field with `json.loads()` first (so `prod_type=2` → int 2), falls back to string. Result: `{"name": "Foo", "prod_type": 2}`.
4. If `--dry-run`: `_print_dry_run("POST", path, payload, ctx, output)` and return; no HTTP.
5. `load_profile(...)` → `DefectDojoClient(profile).post(spec.path, json=payload)`.
6. `_with_retry` calls httpx; retries on `RETRYABLE_STATUS_CODES`.
7. `_parse_response`: 201 → return body; 400 → `ValidationError` (DRF field-level errors formatted); 401 → `AuthError`; etc.
8. `render(body, fmt)` → stdout.

### Import flow: `dd-reimport-findings` (legacy console script)

1. `pyproject.toml` console script entry point: `dd-reimport-findings = "dd_cli.cli.legacy:dd_reimport_findings_main"`.
2. `dd_reimport_findings_main()` instantiates `ImportFindingsOptions()` with no overrides → pydantic-settings reads `DD_*`/`DD_CLI_*` env vars via `validation_alias`.
3. `load_profile()` resolves URL/API key from env (no CLI flag override path).
4. Prints `🚀 Using AUTO-CREATE workflow` or `📋 Using TRADITIONAL workflow` to stdout (intentional emojis — match upstream).
5. `with DefectDojoClient(profile) as client: ImportFindingsWorkflow(client, opts).run()`.
6. On success: `print("✅ Import completed successfully!")`, `sys.exit(0)`.
7. On any `DDCliError` or unexpected exception: `print("❌ Error during import: <msg>", file=sys.stderr)`, **`sys.exit(1)`** — typed exit codes are deliberately collapsed.

## What changes vs what stays

| Change | Recommended approach |
|---|---|
| Add a new resource (DefectDojo ships a new endpoint) | New module in `cli/` following [products.py](../src/dd_cli/cli/products.py); `add_typer` in [app.py](../src/dd_cli/cli/app.py); see [workflows.md](workflows.md). |
| Add an action verb on an existing resource | New `@<resource>_app.command(...)` using `_resource.py` helpers; see [workflows.md](workflows.md). |
| Add a new HTTP method or retry policy | Edit `client.py`. Cross-cuts every command, so add tests in `tests/test_client.py`. |
| Add a new output format (TOML, CSV, etc.) | New `Renderer` in `output/`, register in `render()`. Update `OutputFormat` enum. |
| Add a new error type | New `DDCliError` subclass in `errors.py` with a fresh exit code. Update `from_status_code` if HTTP-derived. Update PLAN.md §5 exit-code table. |
| Add a new import knob (DD ships a flag on `/reimport-scan/`) | Field on `ImportFindingsOptions` with `validation_alias=AliasChoices("DD_CLI_*", "DD_*")`. CLI flag in `cli/import_cmd.py`. Compat test if it's a legacy var. |
| Add a config layer (e.g., a system-wide config in `/etc`) | Edit `config/paths.py` + `load_config`. Maintain the precedence order documented in [conventions.md](conventions.md). |

## Files you'll grep most

- [src/dd_cli/cli/_resource.py](../src/dd_cli/cli/_resource.py) — every CRUD pattern
- [src/dd_cli/client.py](../src/dd_cli/client.py) — HTTP, retry, pagination, errors
- [src/dd_cli/errors.py](../src/dd_cli/errors.py) — exception hierarchy + exit codes
- [src/dd_cli/config/settings.py](../src/dd_cli/config/settings.py) — Profile model + `load_profile`
- [src/dd_cli/cli/products.py](../src/dd_cli/cli/products.py) — minimal canonical resource
- [src/dd_cli/cli/findings.py](../src/dd_cli/cli/findings.py) — full-featured resource (action verbs + custom flags)
- [src/dd_cli/workflows/import_findings.py](../src/dd_cli/workflows/import_findings.py) — biggest non-CLI module; auto-create + traditional logic
