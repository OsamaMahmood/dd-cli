# Importing findings

dd-cli supports the same two flows as the original `dd-import`:

- **`--auto-create`** — single API call, DefectDojo creates the product / engagement / test as needed
- **`--traditional`** — find-or-create each resource explicitly, then upload

For new pipelines we recommend `--auto-create` (one HTTP call vs five, simpler error handling). Use `--traditional` when you need fine-grained control over engagement / test metadata that the auto-create endpoint doesn't accept.

## Auto-create flow

```bash
dd import findings \
  --file trivy.json \
  --scanner "Trivy Scan" \
  --product-type "Web Apps" \
  --product "Payments" \
  --auto-create \
  --yes
```

You can optionally pass `--engagement` and `--test-name` — DefectDojo will reuse them if they exist, create them if not. Without them, DefectDojo invents reasonable defaults.

## Traditional flow

```bash
dd import findings \
  --file trivy.json \
  --scanner "Trivy Scan" \
  --product-type "Web Apps" \
  --product "Payments" \
  --engagement "Q4 Release" \
  --test-name "Trivy" \
  --traditional \
  --yes
```

`--engagement` and `--test-name` are required for traditional. The workflow does:

1. GET `/product_types/?name=…`; POST if missing
2. GET `/products/?name=…&prod_type=N`; POST if missing
3. GET `/engagements/?name=…&product=N`; POST if missing
4. GET `/tests/?title=…&engagement=N`; resolve test_type, POST if test missing
5. POST `/reimport-scan/` with the file
6. PATCH `/engagements/N/` with `build_id` / `commit_hash` / `branch_tag` if any are set

## Choosing a `--scanner` value

The `--scanner` value must match one of DefectDojo's parser names. Browse them:

```bash
dd --help    # find the right command:
# (use raw API for now)
curl -sS https://your-dd/api/v2/test_types/?limit=200 \
  -H "Authorization: Token $DD_API_KEY" \
  | jq -r '.results[].name' | sort
```

Common scanner names:

- `Trivy Scan` — `trivy fs` / `trivy image` JSON output
- `Generic Findings Import` — DefectDojo's stable, schema-documented format
- `Bandit Scan`
- `SonarQube API Import`
- `OWASP ZAP Scan`
- `Semgrep JSON Report`
- `GitHub Vulnerability Scan`
- `Anchore Engine Scan`
- `npm Audit`
- `pip-audit`
- … see DefectDojo's [parser list](https://defectdojo.github.io/django-DefectDojo/integrations/parsers/) for the full set.

## Common knobs

```bash
dd import findings \
  --file trivy.json --scanner "Trivy Scan" \
  --product-type "Web Apps" --product "Payments" \
  --auto-create \
  --minimum-severity Medium     `# drop Info+Low` \
  --push-to-jira                `# create Jira tickets if configured` \
  --close-old-findings          `# close findings missing from this scan (default: on)` \
  --yes
```

## Build context

For correlating findings to commits / builds:

```bash
DD_BUILD_ID=$CI_BUILD_ID \
DD_COMMIT_HASH=$CI_COMMIT_SHA \
DD_BRANCH_TAG=$CI_COMMIT_REF_NAME \
DD_VERSION=v2.1.0 \
  dd import findings \
    --file trivy.json --scanner "Trivy Scan" \
    --product-type "Web Apps" --product "Payments" \
    --auto-create --yes
```

(All four also have CLI flags and `DD_CLI_*` env-var aliases — see [Configuration](configuration.md).)

## Dry-run

Preview the request without sending HTTP:

```bash
dd import findings \
  --file trivy.json --scanner "Trivy Scan" \
  --product-type "Web Apps" --product "Payments" \
  --auto-create --dry-run
# DRY RUN: would POST /api/v2/reimport-scan/ with payload:
# scanner             Trivy Scan
# product_type_name   Web Apps
# product_name        Payments
# auto_create_context true
# file                /Users/.../trivy.json
```

`--dry-run` is verified to send **zero HTTP** in CI — pytest-httpx fails the test if any unmocked request slips out.

## Importing language statistics

[`cloc`](https://github.com/AlDanial/cloc) JSON output uploaded for a product:

```bash
cloc src --json --out cloc.json
dd import languages \
  --file cloc.json \
  --product-type "Web Apps" \
  --product "Payments"
```

Auto-creates the product type and product if they're missing.

## Legacy console scripts

For pipelines migrating from `dd-import`:

```bash
DD_URL=… DD_API_KEY=… DD_PRODUCT_TYPE_NAME=Web DD_PRODUCT_NAME=Payments \
DD_TEST_TYPE_NAME="Trivy Scan" DD_FILE_NAME=trivy.json \
DD_AUTO_CREATE_CONTEXT=true \
  dd-reimport-findings
```

These remain fully supported. The only behavior difference is the exit-code mapping — see [migration](migration.md#exit-code-contract).

## Validating that findings actually landed

After an import, list findings under the new product to confirm:

```bash
PRODUCT_ID=$(dd products list --name Payments --output json | jq -r '.[0].id')
dd findings list --product "$PRODUCT_ID" --output json | jq '. | length'
```

The integration test suite does this in CI for every release using a real `trivy fs` report — see [tests/integration/test_import_against_real_dd.py](https://github.com/OsamaMahmood/dd-cli/blob/main/tests/integration/test_import_against_real_dd.py).
