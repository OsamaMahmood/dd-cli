# Domain knowledge

DefectDojo-specific concepts, terminology, and quirks that don't live in the code. Read this if you've never used DefectDojo, or if you're about to add a CLI command for an unfamiliar resource.

## What DefectDojo is

[DefectDojo](https://www.defectdojo.org/) is an open-source vulnerability-management platform. AppSec teams use it as a single source of truth for findings from many scanners: Trivy, SAST tools, container scanners, DAST tools, etc. Output from each scanner is parsed and stored as **findings** attached to a **test** inside an **engagement** inside a **product**.

`dd-cli` is a CLI client; DefectDojo runs server-side. The CLI talks to DefectDojo's REST API (`/api/v2/...`).

## Resource hierarchy

```
Product type    (organisational bucket — "Web Apps", "Mobile Apps", "Internal Tools")
└── Product     (the actual application — "Payments", "Login Service")
    └── Engagement (a unit of work — "Q4 2026 Pentest", "main branch CI", "Release 2.1")
        └── Test  (one scan run — "Trivy 2026-05-08 build #1234")
            └── Findings  (the vulnerabilities — one row per CVE/issue)
```

Most CI/CD imports target the chain `(product_type_name, product_name, engagement_name, test_name)`. DefectDojo finds-or-creates each level via the auto-create mode, or you find-or-create each one explicitly via the traditional mode.

**Other top-level resources** that dd-cli covers (less commonly imported but managed via `dd <resource>`):

| dd command | DefectDojo API path | What |
|---|---|---|
| `dd products` | `/api/v2/products/` | The application being scanned |
| `dd product-types` | `/api/v2/product_types/` | Organisational buckets |
| `dd engagements` | `/api/v2/engagements/` | A unit of testing work |
| `dd tests` | `/api/v2/tests/` | One scan run (note: `dd-cli` module is `tests_cmd.py`) |
| `dd findings` | `/api/v2/findings/` | Individual vulnerabilities |
| `dd users` | `/api/v2/users/` | DefectDojo user accounts |
| `dd dojo-groups` | `/api/v2/dojo_groups/` | Authorization groups |
| `dd jira-instances` | `/api/v2/jira_instances/` | JIRA integration configurations |
| `dd risk-acceptances` | `/api/v2/risk_acceptance/` | Risk-accepted finding records |
| `dd metadata` | `/api/v2/metadata/` | Key-value tags attached to products/engagements/tests/findings |
| `dd endpoints` | `/api/v2/endpoints/` | URL endpoints associated with findings (DAST-style) |
| `dd finding-templates` | `/api/v2/finding_templates/` | Reusable finding shapes |

The full OpenAPI spec is in [dd-api.json](../dd-api.json) — 226 path templates, ~450 operations.

## Authentication

`Authorization: Token <api_key>` header. DefectDojo issues per-user tokens via:

- The UI: User profile → API Key (web) or "API v2 Key" link.
- The API: `POST /api/v2/api-token-auth/` with `{"username": "...", "password": "..."}` returns `{"token": "..."}`.

The nightly-smoke workflow uses the second method to mint a token from the admin password it parses from the initializer container's logs.

There's no OAuth, no API-key-with-scopes, no per-token expiry. Tokens are long-lived and equivalent to the user's full session permissions.

## Two import strategies

When `dd import findings` or `dd-reimport-findings` runs, it picks one of two paths based on `auto_create_context` (CLI: `--auto-create` / env: `DD_AUTO_CREATE_CONTEXT`):

### Auto-create (recommended for new pipelines)

Single POST to `/api/v2/reimport-scan/` with `auto_create_context: true`. DefectDojo handles the find-or-create chain server-side: if the product type / product / engagement / test don't exist, they're created from the names + metadata in the payload. **One API call**, simpler error handling.

```
[client] POST /api/v2/reimport-scan/  (multipart with file + form fields)
[DD]     creates product type, product, engagement, test as needed
[DD]     parses the scan file and stores findings
[DD]     returns the test record
```

### Traditional (when you need fine control)

Find-or-create each resource explicitly, then upload. **Five API calls** in the simplest case:

```
[client] GET  /api/v2/product_types/?name=Web        → POST if missing
[client] GET  /api/v2/products/?name=Payments&prod_type=N → POST if missing
[client] GET  /api/v2/engagements/?name=Q4&product=N → POST if missing
[client] GET  /api/v2/tests/?title=Trivy&engagement=N → POST if missing (with test_type resolve)
[client] POST /api/v2/reimport-scan/ (with the file)
[client] PATCH /api/v2/engagements/N/ (optional, for build_id/commit_hash/branch_tag)
```

Used when:
- You want to control engagement metadata (target start/end, type, build details) that the auto-create endpoint doesn't accept verbatim.
- You're integrating into a workflow that already created some of the chain elsewhere.

Both modes are implemented in [src/dd_cli/workflows/import_findings.py](../src/dd_cli/workflows/import_findings.py). Pick by setting `auto_create_context=True` (or `DD_AUTO_CREATE_CONTEXT=true`).

## Scanner names

The `--scanner` value (legacy: `DD_TEST_TYPE_NAME`) must match a name DefectDojo's parser registry knows about. The full list lives in DefectDojo's [parser docs](https://defectdojo.github.io/django-DefectDojo/integrations/parsers/) and in the `/api/v2/test_types/` endpoint at runtime.

Common ones:

| Scanner name | Typical input |
|---|---|
| `Trivy Scan` | `trivy fs/image --format json` output |
| `Generic Findings Import` | DefectDojo's stable, schema-documented JSON format |
| `Bandit Scan` | `bandit -f json` |
| `SonarQube API Import` | SonarQube REST data |
| `OWASP ZAP Scan` | ZAP `-J` output |
| `Semgrep JSON Report` | `semgrep --json` |
| `GitHub Vulnerability Scan` | GitHub Dependabot/Code Scanning export |
| `Anchore Engine Scan` | Anchore CLI JSON |
| `npm Audit` | `npm audit --json` |
| `pip-audit` | `pip-audit --format=json` |

To list every scanner the live DD instance knows:

```bash
curl -sS https://your-dd/api/v2/test_types/?limit=200 \
  -H "Authorization: Token $DD_API_KEY" \
  | jq -r '.results[].name' | sort
```

## Quirks and gotchas

### `found_by` is undocumented-required on POST `/api/v2/findings/`

When creating a finding directly (not via the import workflows — those bypass this), DefectDojo's API requires a `found_by: [<test_type_id>, ...]` field. The OpenAPI spec marks it as optional; the server rejects requests without it with a 400 that doesn't clearly say *what* is wrong.

dd-cli's wrapper renders a useful error message for this case. The pinning test:

```python
# tests/integration/test_real_defectdojo.py
def test_findings_create_without_found_by_renders_useful_error(...): ...
```

If you're working on findings-create code and the integration suite trips this test, **don't** "fix" by removing the requirement — DefectDojo's server-side validation still enforces it. The right fix is to make the error message even more helpful.

### DefectDojo Pro upsell noise in error responses

Some error responses from DefectDojo include `pro` and `message` keys that are upsells for the commercial "DefectDojo Pro" product. These otherwise drown the real error. The error-message extractor in [client.py](../src/dd_cli/client.py) filters them:

```python
cleaned = {k: v for k, v in body.items() if k not in {"pro", "message"}}
```

Don't unfilter them. If you find another upsell key polluting error output, add it to the set.

### Findings severity is case-sensitive in DefectDojo

DefectDojo stores severities as `Critical`/`High`/`Medium`/`Low`/`Info` (capitalised). Lower-case input on the API or query string returns an empty filter result silently. [src/dd_cli/cli/findings.py:_canonicalise_severity](../src/dd_cli/cli/findings.py) normalises input case-insensitively to the canonical capitalisation and raises `ValidationError` for unknown values:

```python
canonical_severity = _canonicalise_severity(severity)  # "critical" → "Critical"; "bogus" → raises
```

If you add a new severity-related command, route through this helper.

### Severity-related fields on findings vary by parser

Some scanners populate `severity` only; others populate `severity` + `severity_justification` + `numerical_severity` (a string like `"S0"`). dd-cli's default columns (`id`, `title`, `severity`, `active`, `verified`, `found_by`) cover the common case; if you need parser-specific output, pass `--columns col1,col2,...` to the list command.

### Filter param naming inconsistencies

DefectDojo's API filter naming isn't always intuitive. Examples found in `cli/findings.py`:

- `--product` maps to *both* `product=N` and `test__engagement__product=N` (different code paths in DD's filter resolution).
- `--engagement` maps to `test__engagement=N`.
- `--test` maps to `test=N`.

When adding a filter to a new resource, check both:
1. What `/api/v2/<resource>/?filter=value` accepts (URL-level).
2. What `/api/v2/<resource>/` filters return when applied (semantic).

Run the integration suite or test against a real DD to verify.

### Pagination uses `next` URLs, not `?page=N`

DefectDojo's list endpoints return `{"next": "<url>", "previous": "<url>", "results": [...]}` where `next` is a full URL with all query params re-embedded. `client.paginate` follows these:

```python
# src/dd_cli/client.py:paginate (abridged)
while True:
    response = self._raw.get_httpx_client().get(next_url, params=query if query else None)
    body = response.json()
    for item in body["results"]:
        yield item
    next_link = body.get("next")
    if not isinstance(next_link, str):
        break
    next_url = next_link
    query = {}  # next URL has params embedded
```

**Note**: after the first request, our explicit `query` is cleared because `next` already embeds them. Constructing `next + your params` would duplicate them.

### The `Authorization: Token` prefix (not `Bearer`)

DefectDojo uses `Authorization: Token <key>`, not `Bearer`. The generated client is configured for this in [client.py](../src/dd_cli/client.py):

```python
self._raw = AuthenticatedClient(
    base_url=profile.url,
    token=profile.api_key.get_secret_value(),
    prefix="Token",
    auth_header_name="Authorization",
    ...
)
```

If you ever see a 401 with the right token, double-check the prefix.

### `/reimport-scan/` accepts multipart even with no file

When re-importing without a new scan file (just updating metadata), DefectDojo accepts a multipart body with an empty file slot — it reuses the previous scan. The wrapper does this for us:

```python
# src/dd_cli/client.py:upload
files = (
    {file_field: (file[0], file[1], "application/json")} if file is not None
    else {file_field: ("", b"", "application/octet-stream")}  # empty placeholder
)
```

httpx also requires this placeholder — without it, the request defaults to form-encoding, not multipart, and DefectDojo rejects it. This matches the legacy `dd-import` behavior.

### Risk acceptance is its own resource

`dd findings risk-accept <id>` POSTs to `/api/v2/findings/{id}/risk-accept/` (the action verb). But there's also `dd risk-acceptances list/get/create/...` which manages the underlying `/api/v2/risk_acceptance/` records directly (note the singular `risk_acceptance` in the URL — DefectDojo's quirk; we plural-form the command).

The two are linked: the action verb creates an underlying risk_acceptance record. The CRUD on risk-acceptances lets you list/delete them after the fact, change their expiry, etc.

## Exit codes

`dd-cli` exits with typed codes via the `DDCliError` hierarchy (errors.py).

| Code | Meaning | Class | When |
|---|---|---|---|
| 0 | Success | — | Happy path |
| 1 | Generic error | `DDCliError` base | Anything not categorised; legacy console scripts always use this |
| 2 | Usage error | (Typer-internal) | Bad CLI flag, missing required argument |
| 3 | Auth failure | `AuthError` | DefectDojo returned 401 (invalid token) |
| 4 | Authorization failure | `AuthorizationError` | DefectDojo returned 403 (valid token, insufficient permissions) |
| 5 | Not found | `NotFoundError` | DefectDojo returned 404 (resource doesn't exist) |
| 6 | Validation error | `ValidationError` | DefectDojo returned 400, or local input validation failed |
| 7 | API error | `APIError` | DefectDojo returned 5xx after retries, or unexpected status |
| 8 | Network error | `NetworkError` | Connection refused, timeout, DNS failure, etc., after retries |
| 9 | Config error | `ConfigError` | Missing/invalid dd-cli configuration (no profile, no URL, no API key) |

CI can branch on these for the new `dd import findings` command:

```bash
dd import findings --file scan.json --scanner "Trivy Scan" --product-type "Web" --product "Payments" --auto-create --yes
rc=$?
case $rc in
  0) echo "ok";;
  3) echo "auth failed — rotate DD_API_KEY"; exit 1;;
  8) echo "network blip — retry later"; exit $rc;;
  9) echo "configuration missing"; exit 1;;
  *) echo "upload failed: $rc"; exit $rc;;
esac
```

The **legacy** `dd-reimport-findings` / `dd-import-languages` console scripts always exit 1 on any failure — see [compatibility.md](compatibility.md#exit-code-contract--legacy-vs-new).

## Working with a local DefectDojo

For testing changes locally, run DefectDojo via their docker compose:

```bash
git clone https://github.com/DefectDojo/django-DefectDojo /tmp/dd && cd /tmp/dd
docker/setEnv.sh release
docker compose up -d
```

Wait 5–15 minutes for the initializer container to finish DB migrations and fixtures. Watch for the line:

```
initializer-1 | Admin password: <generated>
```

in `docker compose logs initializer`. That's the admin password. The username is `admin`.

Mint a token:

```bash
ADMIN_PASS=$(docker compose logs initializer | grep "Admin password:" | sed -E 's/.*Admin password:[[:space:]]*//' | tr -d '[:space:]')
TOKEN=$(curl -sf -X POST http://localhost:8080/api/v2/api-token-auth/ \
  -H 'Content-Type: application/json' \
  -d "{\"username\":\"admin\",\"password\":\"$ADMIN_PASS\"}" \
  | python3 -c "import json,sys; print(json.load(sys.stdin)['token'])")

DD_URL=http://localhost:8080 DD_API_KEY=$TOKEN dd ping
```

DefectDojo's local DB lives in named volumes (`dd_defectdojo_postgres`, `dd_defectdojo_media`, `dd_defectdojo_redis`). `docker compose down -v` removes them — handy when you want a clean start. Bring-up after a `down -v` runs the full DB initialiser again, so it takes another 5–15 minutes.

The nightly-smoke workflow does this same flow in CI — see [.github/workflows/nightly-smoke.yml](../.github/workflows/nightly-smoke.yml).
