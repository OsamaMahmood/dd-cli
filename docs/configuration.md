# Configuration

dd-cli pulls settings from four sources, in this order (later wins):

1. Built-in defaults
2. The active profile in `~/.config/dd-cli/config.toml` (or `$DD_CLI_CONFIG_DIR/config.toml`)
3. **`DD_*`** environment variables (legacy contract — see [migration](migration.md))
4. **`DD_CLI_*`** environment variables (modern names, take precedence over `DD_*`)
5. Explicit CLI flags

API tokens are stored as `pydantic.SecretStr` and masked in `dd config show` output unless you pass `--show-secrets` to `dd config get api_key`.

## Profiles

A profile is a named bundle of credentials + connection settings. The TOML file looks like:

```toml
default_profile = "default"

[profiles.default]
url = "https://defectdojo.example.com"
api_key = "abc123…"
ssl_verify = true

[profiles.default.extra_headers]
"X-WAF-Token" = "…"

[profiles.staging]
url = "https://staging.defectdojo.example.com"
api_key = "xyz789…"
ssl_verify = false
```

Manage profiles:

```bash
dd configure --profile staging   # interactive setup; --no-input + flags for scripts
dd config show                   # resolved profile (env merged in, secrets masked)
dd config show --profile staging
dd config list                   # all profiles, with the default marked
dd config use staging            # change the default
dd config set ssl_verify false   # edit one field in the default profile
dd config delete staging --yes   # remove a profile
```

Pick a profile per-invocation without changing the default:

```bash
dd --profile staging products list
DD_PROFILE=staging dd findings list
```

## Environment variables

### Connection

| `DD_*` (legacy) | `DD_CLI_*` (modern) | Purpose |
|---|---|---|
| `DD_URL` | `DD_CLI_URL` | DefectDojo base URL |
| `DD_API_KEY` | `DD_CLI_API_KEY` | API token (DefectDojo `Token` auth scheme) |
| `DD_SSL_VERIFY` | `DD_CLI_SSL_VERIFY` | TLS verification (default: `true`) |
| `DD_EXTRA_HEADER_1` + `DD_EXTRA_HEADER_1_VALUE` | — | Optional WAF auth header |
| `DD_EXTRA_HEADER_2` + `DD_EXTRA_HEADER_2_VALUE` | — | Second optional WAF auth header |
| `DD_PROFILE` | `DD_CLI_PROFILE` | Profile name to use |
| `DD_OUTPUT` | `DD_CLI_OUTPUT` | Default output format (`table`, `json`, `yaml`) |

### Import workflow

These drive `dd-reimport-findings`, `dd-import-languages`, and `dd import findings`/`languages`:

| Variable | Purpose |
|---|---|
| `DD_PRODUCT_TYPE_NAME` | Product type (created if missing) |
| `DD_PRODUCT_NAME` | Product (created if missing) |
| `DD_ENGAGEMENT_NAME` | Engagement (required for traditional flow) |
| `DD_TEST_NAME` | Test title (required for traditional flow) |
| `DD_TEST_TYPE_NAME` | Scanner / parser name (e.g. `Trivy Scan`) |
| `DD_FILE_NAME` | Path to the scanner output |
| `DD_AUTO_CREATE_CONTEXT` | `true` to use the single-call auto-create flow |
| `DD_ACTIVE` / `DD_VERIFIED` | Default `true` / `true` |
| `DD_PUSH_TO_JIRA` | Push findings to Jira if configured |
| `DD_CLOSE_OLD_FINDINGS` / `DD_CLOSE_OLD_FINDINGS_PRODUCT_SCOPE` | Close-old-findings semantics |
| `DD_DO_NOT_REACTIVATE` | Don't reactivate previously-closed findings |
| `DD_DEDUPLICATION_ON_ENGAGEMENT` | Engagement-scoped dedup |
| `DD_MINIMUM_SEVERITY` | Drop findings below this (Info/Low/Medium/High/Critical) |
| `DD_GROUP_BY` | Group findings (file path, component, etc.) |
| `DD_ENGAGEMENT_TARGET_START` / `DD_ENGAGEMENT_TARGET_END` | Engagement dates (`YYYY-MM-DD`) |
| `DD_BUILD_ID` / `DD_COMMIT_HASH` / `DD_BRANCH_TAG` | Build context |
| `DD_VERSION` | Product version |
| `DD_SERVICE` | Service name |
| `DD_ENDPOINT_ID` / `DD_API_SCAN_CONFIGURATION_ID` / `DD_SOURCE_CODE_MANAGEMENT_URI` | Scoping helpers |
| `DD_PRODUCT_*` | Product metadata for new products (description, business_criticality, platform, lifecycle, origin, etc.) |
| `DD_ENGAGEMENT_*` | Engagement metadata (description, version, threat_model, api_test, pen_test, …) |
| `DD_TEST_*` | Test metadata (description, version, environment) |
| `DD_APPLY_TAGS_TO_FINDINGS` / `DD_APPLY_TAGS_TO_ENDPOINTS` / `DD_FINDING_TAGS` | Tag application |

For new pipelines we recommend the explicit CLI flags (`dd import findings --product …`); the env vars exist primarily for [migration](migration.md) compatibility.

## Config file location

In order of precedence:

1. `$DD_CLI_CONFIG_DIR/config.toml` (most useful for CI: per-job config dirs)
2. `$XDG_CONFIG_HOME/dd-cli/config.toml`
3. `~/.config/dd-cli/config.toml` (default on Linux/macOS)
4. `%APPDATA%\dd-cli\config.toml` (Windows)

## Output formats

Every read command supports `--output table|json|yaml` (default `table`):

```bash
dd findings list --severity High --output json | jq '.[] | {id, title, severity}'
dd products list --output yaml > products.yaml
```

The default is also configurable per-profile or via env:

```bash
dd config set output json
DD_CLI_OUTPUT=json dd ping
```

## Exit codes

dd-cli uses **typed exit codes** so CI scripts can branch on the failure category:

| Code | Meaning |
|---|---|
| 0 | success |
| 2 | usage error (missing/unknown flag) |
| 3 | authentication error (HTTP 401) |
| 4 | authorization error (HTTP 403) |
| 5 | resource not found (HTTP 404) |
| 6 | validation error (HTTP 400 or local input check) |
| 7 | API error (HTTP 5xx after retries) |
| 8 | network error |
| 9 | configuration error (missing url/api_key) |

The legacy `dd-reimport-findings` / `dd-import-languages` shims **flatten all errors to exit 1** to preserve backward compatibility — see [migration](migration.md).
