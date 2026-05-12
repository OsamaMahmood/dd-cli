# Compatibility

`dd-cli` is a drop-in replacement for the archived [`dd-import`](https://github.com/MaibornWolff/dd-import) tool. Existing CI/CD pipelines must keep working unchanged when a user does nothing more than swap `pip install dd-import` for `pip install dd-cli`.

This is the most load-bearing constraint in the codebase. Read this before touching anything in `cli/legacy.py`, the workflows, or the env-var aliases.

## The three guarantees

These are the contract. The compat test suite (`tests/compat/`, marked `@pytest.mark.compat`) pins them.

### 1. The `DD_*` env-var contract is sacred

Every environment variable the original `dd-import` tool read keeps its name and its semantics. Adding a new `DD_*` var is fine; renaming or removing one is not.

A field gets a legacy alias via pydantic's `AliasChoices`:

```python
# src/dd_cli/workflows/import_findings.py
product_type_name: str | None = Field(
    default=None,
    validation_alias=AliasChoices("DD_CLI_PRODUCT_TYPE", "DD_PRODUCT_TYPE_NAME"),
)
```

`AliasChoices(new, old)` — first listed wins. The new `DD_CLI_*` name takes precedence over the legacy `DD_*` name; if both are set, `DD_CLI_*` is honored. This is documented in [conventions.md](conventions.md#pydantic-conventions).

If you're adding a new import knob:
- If DefectDojo's `/reimport-scan/` endpoint already has a flag for it that `dd-import` exposed → reuse the legacy `DD_*` name in `AliasChoices`.
- If it's brand-new → use only `DD_CLI_*`. Don't invent a `DD_*` name that the legacy tool never read.

### 2. The console scripts keep working byte-for-byte

`pyproject.toml [project.scripts]` maps:

```toml
dd-reimport-findings = "dd_cli.cli.legacy:dd_reimport_findings_main"
dd-import-languages  = "dd_cli.cli.legacy:dd_import_languages_main"
```

After `pip install dd-cli`, these binaries are on `PATH`. Their contract:

- All configuration via `DD_*` env vars only. No CLI flags.
- Print human progress to stdout, errors to stderr.
- Exit 0 on success, **1 on any failure** — irrespective of the typed exit codes the new `dd import findings` command uses.
- Specific strings are preserved (compat tests assert):
  - `🚀 Using AUTO-CREATE workflow (single API call)` (stdout, auto-create mode)
  - `📋 Using TRADITIONAL workflow (multiple API calls)` (stdout, traditional mode)
  - `✅ Import completed successfully!` (stdout, success)
  - `❌ Error during import: <message>` (stderr, failure)
  - `✅ Languages imported` (stdout, languages success)

The strings include emojis. **This is the only place in the codebase where emojis are allowed.** See [conventions.md](conventions.md#emojis).

### 3. The Docker image works for existing CI pipelines

The shipped image (`ghcr.io/osamamahmood/dd-cli` and `m4rkm3n/dd-cli`) keeps the legacy shell wrappers on `PATH`:

```dockerfile
# Dockerfile:53-58
RUN install -d -o ${user} -g ${group} /usr/local/dd-cli/bin
COPY --chown=${user}:${group} bin/dd-reimport-findings.sh /usr/local/dd-cli/bin/dd-reimport-findings.sh
COPY --chown=${user}:${group} bin/dd-import-languages.sh  /usr/local/dd-cli/bin/dd-import-languages.sh
RUN chmod +x /usr/local/dd-cli/bin/*.sh
ENV PATH="/usr/local/dd-cli/bin:$PATH"
```

The `.sh` wrappers `exec` the installed console scripts directly, but exist for CI pipelines that called the wrappers by path. Don't delete them.

## Exit-code contract — legacy vs new

This is the single deliberate behavioral difference between the legacy and new commands. It's documented as a feature, not a bug.

| Command | Exit codes |
|---|---|
| `dd-reimport-findings` / `dd-import-languages` (legacy console scripts) | 0 on success, **1 on any failure** |
| `dd import findings` / `dd import languages` (new command) | 0, 2 (usage), 3 (auth), 4 (authz), 5 (not found), 6 (validation), 7 (API 5xx), 8 (network), 9 (config) |

Why the asymmetry: existing CI pipelines grep `$?` and assume "non-zero = bad". Switching them to typed codes silently would change the behavior of `if [ $? -ne 0 ]; then …; fi` constructs that don't care about the specific failure mode. The new typed codes are opt-in: a pipeline that wants them migrates to `dd import findings`.

Implementation, [src/dd_cli/cli/legacy.py:62-68](../src/dd_cli/cli/legacy.py):

```python
except DDCliError as exc:
    _print_legacy_error(exc.message, hint=exc.hint)
    sys.exit(1)
except Exception as exc:
    _print_legacy_error(str(exc))
    sys.exit(1)
```

The `except DDCliError` branch deliberately collapses the typed exit code to 1. Don't change this without a compat test failure as forcing function.

## `DD_*` environment variable reference

These are read by the import workflows. Every variable here is honored by the legacy console scripts via `validation_alias=AliasChoices("DD_CLI_*", "DD_*")` on the workflow options model — see [workflows/import_findings.py](../src/dd_cli/workflows/import_findings.py) and [workflows/import_languages.py](../src/dd_cli/workflows/import_languages.py).

### Connection

| Legacy | New | What |
|---|---|---|
| `DD_URL` | `DD_CLI_URL` | DefectDojo base URL |
| `DD_API_KEY` / `DD_API_TOKEN` | `DD_CLI_API_KEY` | API token (sent as `Authorization: Token <key>`). `DD_API_TOKEN` is the name used by [`dd-reporting`](https://github.com/OsamaMahmood/dd-reporting) and is honored as of v2.1 so users migrating to `dd report` don't have to rename their `.env`. `DD_CLI_API_KEY` still takes precedence. |
| `DD_SSL_VERIFY` | `DD_CLI_SSL_VERIFY` | `true`/`false` |
| `DD_EXTRA_HEADER_1` + `DD_EXTRA_HEADER_1_VALUE` | — | Header *name* + *value* pair (slot 1) |
| `DD_EXTRA_HEADER_2` + `DD_EXTRA_HEADER_2_VALUE` | — | Header *name* + *value* pair (slot 2) |

Connection vars are handled in [config/settings.py](../src/dd_cli/config/settings.py); extra-header pairing is in [config/legacy_env.py](../src/dd_cli/config/legacy_env.py) because pydantic-settings can't natively model paired vars.

### Scoping (which product/engagement/test)

| Legacy | New CLI flag / DD_CLI_* | Default |
|---|---|---|
| `DD_PRODUCT_TYPE_NAME` | `--product-type` / `DD_CLI_PRODUCT_TYPE` | — |
| `DD_PRODUCT_NAME` | `--product` / `DD_CLI_PRODUCT` | — |
| `DD_ENGAGEMENT_NAME` | `--engagement` / `DD_CLI_ENGAGEMENT` | — |
| `DD_TEST_NAME` | `--test-name` / `DD_CLI_TEST_NAME` | — |
| `DD_TEST_TYPE_NAME` | `--scanner` / `DD_CLI_SCANNER` | — (e.g. `"Trivy Scan"`) |
| `DD_FILE_NAME` | `--file` / `DD_CLI_FILE` | — |
| `DD_AUTO_CREATE_CONTEXT` | `--auto-create` / `DD_CLI_AUTO_CREATE_CONTEXT` | `false` |

### Engagement targeting (traditional flow)

| Legacy | Default |
|---|---|
| `DD_ENGAGEMENT_TARGET_START` | today (ISO date) |
| `DD_ENGAGEMENT_TARGET_END` | `2999-12-31` |

### Scan flags

| Legacy | Default |
|---|---|
| `DD_ACTIVE` | `true` |
| `DD_VERIFIED` | `true` |
| `DD_MINIMUM_SEVERITY` | — (no filter; one of `Critical`/`High`/`Medium`/`Low`/`Info`) |
| `DD_PUSH_TO_JIRA` | `false` |
| `DD_CLOSE_OLD_FINDINGS` | `true` |
| `DD_CLOSE_OLD_FINDINGS_PRODUCT_SCOPE` | `false` |
| `DD_DO_NOT_REACTIVATE` | `false` |
| `DD_DEDUPLICATION_ON_ENGAGEMENT` | `false` |

### Build context (PATCHed onto the engagement after import)

| Legacy | Default |
|---|---|
| `DD_VERSION` | — |
| `DD_BUILD_ID` | — |
| `DD_COMMIT_HASH` | — |
| `DD_BRANCH_TAG` | — |

### Scoping helpers

| Legacy | Default |
|---|---|
| `DD_ENDPOINT_ID` | — (limit scan to a specific endpoint) |
| `DD_SERVICE` | — (free-form service tag) |
| `DD_API_SCAN_CONFIGURATION_ID` | — |
| `DD_SOURCE_CODE_MANAGEMENT_URI` | — |
| `DD_GROUP_BY` | — |

### Product metadata (used during auto-create / traditional product-creation)

| Legacy | Default |
|---|---|
| `DD_PRODUCT_DESCRIPTION` | — |
| `DD_PRODUCT_BUSINESS_CRITICALITY` | — (one of `very high`, `high`, `medium`, `low`, `very low`, `none`) |
| `DD_PRODUCT_PLATFORM` | — (one of `web service`, `desktop`, `iot`, `mobile`, `web`) |
| `DD_PRODUCT_LIFECYCLE` | — (one of `construction`, `production`, `retirement`) |
| `DD_PRODUCT_ORIGIN` | — |
| `DD_PRODUCT_USER_RECORDS` | — (int) |
| `DD_PRODUCT_REVENUE` | — |
| `DD_PRODUCT_EXTERNAL_AUDIENCE` | `false` |
| `DD_PRODUCT_INTERNET_ACCESSIBLE` | `false` |
| `DD_PRODUCT_ENABLE_SIMPLE_RISK_ACCEPTANCE` | `true` |

### CLI scope

| Legacy | New | What |
|---|---|---|
| `DD_PROFILE` | `DD_CLI_PROFILE` / `--profile` | Named profile to use |
| `DD_OUTPUT` | `DD_CLI_OUTPUT` / `--output` | Output format |
| — | `DD_CLI_CONFIG_DIR` | Override the config-file directory (used heavily in tests) |

If you find a `DD_*` variable in `dd-import`'s `environment.py` that's missing here, it's a gap — add it via `validation_alias` and a compat test.

## Adding a new `DD_*`-aliased option

Procedure:

1. **Add the field** to `ImportFindingsOptions` or `ImportLanguagesOptions` in `workflows/`:
   ```python
   new_flag: bool = Field(
       default=False,
       validation_alias=AliasChoices("DD_CLI_NEW_FLAG", "DD_NEW_FLAG"),
   )
   ```

2. **Use it in the workflow body**. Add the field to the `data=` dict passed to `client.upload(...)`.

3. **Expose a CLI flag** in `cli/import_cmd.py`:
   ```python
   new_flag: Annotated[bool, typer.Option("--new-flag", help="...")] = False
   ```
   Pass via `make_findings_options(new_flag=new_flag, ...)`.

4. **Add a compat test** in `tests/compat/test_legacy_entry_points.py`:
   ```python
   monkeypatch.setenv("DD_NEW_FLAG", "true")
   # ... rest of the test ...
   ```
   Assert the request httpx-mock captured includes `new_flag=true` in the multipart body.

5. **Document the variable** in [docs/configuration.md](../docs/configuration.md) and update the table in this file.

## Things that don't need a `DD_*` alias

These never existed in the legacy tool, so they're `DD_CLI_*`-only:

- `DD_CLI_CONFIG_DIR` — override the config directory.
- Anything related to profiles (`DD_CLI_PROFILE`, the TOML file itself).
- New management commands (`dd findings close`, etc.) — never read env vars at all; they take CLI flags.

## What changes when you break compat

The compat suite catches most regressions, but it can't catch silent semantic changes. Things that have failed in the past:

- Removing the `❌` prefix on error lines (CI logs grepping for `❌ Error during import:` lost their match).
- Changing the JSON structure of `dd ping --output json` (alerts that grep'd specific keys silently went green forever).
- Adding a CLI flag without a `DD_*` alias for legacy users (the new flag was unreachable from the legacy console scripts).

**If you intend to break compat**: name it explicitly in the PR description, document it as a breaking change in the GitHub Release notes, and bump the SemVer major version. v2 is full-mgmt-CLI; v3 would be the next opportunity for breaking changes.

## How to verify compat locally

```bash
pytest -m compat -v                              # runs the compat suite, ~1s
pytest tests/compat/test_legacy_entry_points.py  # same
```

The full unit + snapshot + compat suite is `make test` (~20s).

For a smoke test against the actual installed console scripts:

```bash
pip install -e . && which dd-reimport-findings && which dd-import-languages
# both should resolve into your venv's bin/ directory
```
