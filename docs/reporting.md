# Reporting

`dd report generate` produces a security report for a single DefectDojo product, walking active engagements → tests → findings, enriching the data with SLA / KEV / EPSS / risk-acceptance metadata, and rendering bundled Jinja templates as Markdown and/or HTML.

Two outputs by default. Open the HTML in any browser and print to PDF for a polished hand-off; pipe the Markdown into your wiki, your release notes, or `pandoc` for anything else.

```bash
dd report generate --product 42
# → ./reports/42-payments.md
# → ./reports/42-payments.html
```

## Why a built-in reporter

DefectDojo's open-source reporting has known limitations: the PDF builder hangs on large engagements, the Report Builder only takes predefined widgets (no custom fields, no full templating), SLA-compliance dashboards live behind DefectDojo Pro, and there's no native scan-over-scan diff. `dd report` is a self-contained tool that hits the v2 API directly and renders polished output from a single command — no daemon, no scheduled jobs, no hidden state.

## The basic flow

```bash
dd report generate --product 42 --output-dir ./out/
```

What the command does, in order:

1. `GET /api/v2/products/{id}/`
2. `paginate /api/v2/engagements/?product={id}&active=true`
3. For each engagement: `paginate /api/v2/tests/?engagement={N}` → for each test: `paginate /api/v2/findings/?test={M}&active=true`
4. Resolve any `test_type` IDs not inlined in the test record: `GET /api/v2/test_types/{id}/`
5. `paginate /api/v2/sla_configurations/` (best-effort — missing or 403 is fine)
6. `paginate /api/v2/risk_acceptance/?engagement__product={id}` (best-effort)
7. Render context → write `{id}-{slug}.md` and `{id}-{slug}.html`

For a product with ~5 engagements / ~20 tests / a few hundred findings, the full pipeline finishes in a couple of seconds.

## What's in the report

- **Cover & executive summary** — product metadata, SLA thresholds, severity totals, active findings, KEV count, SLA-breached count.
- **Top-10 riskiest findings** — composite sort: severity → KEV exposure → EPSS desc → age desc → DefectDojo's `S0`–`S4` numerical severity.
- **Finding age distribution** — counts per severity bucket (0–30 / 30–90 / 90–180 / 180+ days).
- **Risk acceptance** — formal accepted-findings records, with decision, accepted-by, expiration, and the list of accepted findings (excluded from the active counts above so they're easy to miss otherwise).
- **Per engagement / per test / per finding** — title + severity chip, KEV / Fix-available badges, full metadata grid (severity, SLA status, CWE, CVE, CVSS, EPSS score + percentile, scanner confidence, file:line, component@version, endpoints affected, type), then markdown-rendered description / severity justification / impact / steps to reproduce / mitigation / references, plus DAST evidence (URL / parameter / payload) or SAST evidence (source file:line / source object / sink object) where present.
- **Empty tests** — still rendered with "No active findings were identified for this test." so stakeholders can confirm the coverage exists.

## CLI options

| Flag | Default | What |
|---|---|---|
| `--product N` | required | DefectDojo product ID. Omit only with `--sample`. |
| `--format md\|html\|both` | `both` | Pick one or both output formats. |
| `--output-dir PATH` | `./reports` | Where to write. Created if missing. |
| `--test NAME` (repeatable) | — | Substring filter on the test's title, `test_type_name`, or `scan_type` (case-insensitive). Narrows the report to a subset of tests; engagements with no matches are dropped entirely. |
| `--detailed` | off | Adds per-finding notes, Jira mappings, and endpoint status. 3 extra reads per finding, parallelised. |
| `--with-history` | off | Adds the scan-delta block per test (created / closed / reactivated / untouched since the last import). 1 extra read per test, parallelised. |
| `--sample` | off | Render from bundled mock data; no API call, no profile required. Useful for previewing the layout. |

## Output filenames

Default pattern: `{product_id}-{slug-of-name}.{ext}`. With `--test` filters: appended `-{slug-of-filter}`. With `--sample`: `sample-report.{ext}`.

```text
./reports/42-payments.md
./reports/42-payments.html
./reports/42-payments-sast.md          # --test "SAST"
./reports/sample-report.html           # --sample
```

## `--detailed` — what it adds

```bash
dd report generate --product 42 --detailed
```

For every finding in the product, fetches:

- `/api/v2/findings/{id}/notes/` — analyst comments / triage notes.
- `/api/v2/jira_finding_mappings/?finding={id}` — linked Jira tickets with last-sync timestamps.
- `/api/v2/endpoint_status/?finding={id}` — per-endpoint mitigation state for DAST findings.

These fan out concurrently (10-way thread pool by default) so wall time stays bounded. Empty buckets render nothing; if your DefectDojo doesn't have Jira configured, the section is silently omitted.

## `--with-history` — scan deltas per test

```bash
dd report generate --product 42 --with-history
```

For each test, fetches `/api/v2/test_imports/?test={id}` and produces a "Scan delta" block in the report:

```text
| New | Reactivated | Closed | Untouched |
|---:|---:|---:|---:|
|  3  |  0          |  12    |  74       |
```

Useful in release-train workflows — shows what changed since the last upload, plus the latest import's branch / commit / build ID.

## `--sample` — preview without a DefectDojo

```bash
dd report generate --sample
dd report generate --sample --detailed --with-history --format html
```

Bundled mock data exercises every branch in the template — all five severities, a KEV finding, a fix-available finding, both DAST and SAST evidence blocks, a zero-finding test, a formal risk-acceptance record. Useful when you want to:

- See what the report looks like before configuring DefectDojo.
- Iterate on layout/style locally (when we ship a `--template-dir` override in a later release).
- Show the format to a stakeholder without exposing real findings.

No `DD_URL`, no `DD_API_KEY`, no profile required.

## Configuration

`dd report generate` uses the same profile / `DD_*` env-var precedence as every other `dd` command. See [configuration](configuration.md) for the full table.

### `DD_API_TOKEN` works too

`dd-cli` reads `DD_API_KEY` and `DD_CLI_API_KEY` natively. As of v2.1 it also accepts `DD_API_TOKEN` — the name used by the standalone [`dd-reporting`](https://github.com/OsamaMahmood/dd-reporting) tool — so users migrating from `dd-reporting` to `dd report` don't have to rename anything in their `.env`. `DD_CLI_API_KEY` still wins if more than one is set.

## Want PDF?

`dd report` writes Markdown and HTML. PDF is intentionally not a built-in format — it would mean shipping native dependencies (WeasyPrint needs `pango` / `cairo` / `gdk-pixbuf` on the host) for an output the browser already produces. See [Recipes → Reporting to PDF](recipes/reporting-pdf.md) for the supported paths: browser print, `pandoc`, and similar.

## CI usage

`dd report` runs cleanly in CI; pair it with whichever scheduler you use.

```yaml
# GitHub Actions — generate + upload report as an artifact every Monday
name: Weekly DefectDojo report
on:
  schedule:
    - cron: "0 6 * * 1"
  workflow_dispatch:

jobs:
  report:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install dd-cli
      - env:
          DD_URL: ${{ secrets.DD_URL }}
          DD_API_KEY: ${{ secrets.DD_API_KEY }}
        run: |
          dd report generate \
            --product 42 \
            --detailed \
            --with-history \
            --output-dir ./report-out
      - uses: actions/upload-artifact@v4
        with:
          name: weekly-report
          path: ./report-out/
          retention-days: 90
```

## Exit codes

Same typed codes as the rest of `dd`:

- **3** — auth (`DD_API_KEY` invalid).
- **5** — product not found.
- **6** — validation (missing `--product`, no tests matched `--test` filter, etc.).
- **8** — network failure after retries.
- **9** — missing config (no `DD_URL` / no profile).

See [migration](migration.md#exit-code-contract) for the full table.
