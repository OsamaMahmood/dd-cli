# Migrating from `dd-import`

dd-cli is a **drop-in replacement** for the original [`dd-import`](https://github.com/MaibornWolff/dd-import) by Stefan Fleckenstein at MaibornWolff (now archived). Existing pipelines work unchanged — install dd-cli and the legacy console scripts + `DD_*` env-var contract continue to work.

## Mapping

| Legacy | Replacement | Status |
|---|---|---|
| `dd-reimport-findings` | `dd-reimport-findings` (shim) **or** `dd import findings` (new) | both work; `DD_*` env vars unchanged |
| `dd-import-languages` | `dd-import-languages` (shim) **or** `dd import languages` (new) | both work; `DD_*` env vars unchanged |
| `pip install dd-import` | `pip install dd-cli` | new package name |
| `osamamahmood/dd-import:latest` (Docker) | `ghcr.io/osamamahmood/dd-cli:latest` **or** `m4rkm3n/dd-cli:latest` | swap image, no other changes |
| `python -m dd_import.dd_reimport_findings` | `python -m dd_cli.cli.legacy` is **not** the public path — use the `dd-reimport-findings` console script instead | the legacy `dd_import` Python package is gone |

## Recommended path

1. **Today:** swap install command (`pip install dd-cli`) or the Docker image. Pipelines keep working.
2. **When convenient:** migrate to the new ergonomic commands (`dd import findings --file …`) for `--dry-run`, typed exit codes, profile support.

Both styles can coexist in the same image / install — a CI job using the legacy shim and another job using the new commands work side by side.

## Exit code contract

The shims and the new commands have **one deliberate difference**:

| | `dd-reimport-findings` (legacy) | `dd import findings` (new) |
|---|---|---|
| success | 0 | 0 |
| auth error (401) | 1 | 3 |
| not found (404) | 1 | 5 |
| validation (400) | 1 | 6 |
| API 5xx after retries | 1 | 7 |
| network error | 1 | 8 |
| missing config | 1 | 9 |

The shims **flatten everything to exit 1** to preserve backward compatibility — pipelines that grep `$?` keep working. Use the new commands if you want to branch CI logic on the failure category.

The full legacy contract is pinned by 9 tests under `@pytest.mark.compat` in [`tests/compat/`](https://github.com/OsamaMahmood/dd-cli/tree/main/tests/compat).

## `DD_*` env vars — every legacy variable still works

Every `DD_*` variable the legacy `Environment` class read is honored as a `pydantic-settings` validation alias on the workflow's options model. Plus you can use the modern `DD_CLI_*` form for new pipelines (takes precedence over `DD_*`).

A full reference lives in [Configuration → Environment variables](configuration.md#environment-variables).

Common ones for findings imports:

```bash
export DD_URL="https://defectdojo.example.com"
export DD_API_KEY="…"
export DD_PRODUCT_TYPE_NAME="Web Apps"
export DD_PRODUCT_NAME="Payments"
export DD_ENGAGEMENT_NAME="Q4 Release"
export DD_TEST_NAME="Trivy"
export DD_TEST_TYPE_NAME="Trivy Scan"
export DD_FILE_NAME="trivy.json"
export DD_AUTO_CREATE_CONTEXT="true"

dd-reimport-findings              # legacy shim — still works
# OR
dd import findings --yes          # new ergonomic form, all flags read from env
```

## Things that look different (but aren't)

- **Auto-create vs traditional flow.** Both are still here. `DD_AUTO_CREATE_CONTEXT=true` selects auto-create; otherwise traditional. The new commands also accept `--auto-create` / `--traditional` flags as a more explicit way to choose.
- **Build context (`DD_BUILD_ID`, `DD_COMMIT_HASH`, `DD_BRANCH_TAG`).** Still patched onto the engagement after a traditional re-import. In auto-create mode they go onto the `reimport-scan` payload directly.
- **Extra headers (`DD_EXTRA_HEADER_1` + `DD_EXTRA_HEADER_1_VALUE`).** Still combined into request headers. Useful for WAF auth.

## Things that genuinely changed

- **The Python module path.** `from dd_import.dd_api import Api` is gone. The new entry points are:
  - `dd_cli.cli.legacy.dd_reimport_findings_main` (console-script entry)
  - `dd_cli.cli.legacy.dd_import_languages_main` (console-script entry)
  - `dd_cli.workflows.import_findings.ImportFindingsWorkflow` (library use)
  - `dd_cli.workflows.import_languages.ImportLanguagesWorkflow` (library use)

  If you had Python code that imported `dd_import` directly, you'll need to update it. CI pipelines that called `dd-reimport-findings` as a binary are unaffected.

- **The Docker image name.** `osamamahmood/dd-import:latest` → `ghcr.io/osamamahmood/dd-cli:latest` or `m4rkm3n/dd-cli:latest`. Inside the image, the working directory has changed, but you don't usually depend on that — CI pipelines just call the console scripts.

- **Distribution.** The package on PyPI is `dd-cli` (was `dd-import`). The original `dd-import` package on PyPI is unchanged and still present at the upstream's archived state — but doesn't get new releases.

## Reporting issues

If a pipeline that worked under `dd-import` doesn't work under `dd-cli`, open an issue at [github.com/OsamaMahmood/dd-cli/issues](https://github.com/OsamaMahmood/dd-cli/issues) with:

1. The exact `DD_*` env vars you set (redact secrets)
2. The command you ran (`dd-reimport-findings` or `dd import findings`)
3. The output (especially the error line) — `dd-cli`'s error rendering preserves the legacy `❌ Error during import:` prefix to make grep-friendly comparisons easy.

The compat-test suite is intended to catch the well-trodden paths, but the original tool's surface is broad — there might be edge cases.
