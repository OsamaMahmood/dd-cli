# dd-cli

[![PyPI](https://img.shields.io/pypi/v/dd-cli.svg)](https://pypi.org/project/dd-cli/)
[![Python](https://img.shields.io/pypi/pyversions/dd-cli.svg)](https://pypi.org/project/dd-cli/)
[![CI](https://github.com/OsamaMahmood/dd-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/OsamaMahmood/dd-cli/actions/workflows/ci.yml)
[![Docs](https://github.com/OsamaMahmood/dd-cli/actions/workflows/docs.yml/badge.svg)](https://osamamahmood.github.io/dd-cli/)
[![License](https://img.shields.io/badge/license-BSD--3--Clause-blue.svg)](LICENSE.txt)

A production-grade CLI for managing [DefectDojo](https://www.defectdojo.org/) — list / create / update / delete every resource the API exposes, plus a fully backward-compatible import path for users coming from the original [`dd-import`](https://github.com/MaibornWolff/dd-import) tool (now archived).

```bash
pip install dd-cli
```

```text
$ dd --help

 Usage: dd [OPTIONS] COMMAND [ARGS]...

 Production-grade CLI for managing DefectDojo.

 Commands:
   configure          Interactively create or update a profile.
   ping               Verify connectivity and authentication against DefectDojo.
   config             Manage dd-cli profiles and on-disk configuration.
   products           List and get DefectDojo products.
   product-types      List and get DefectDojo product types.
   engagements        List and get DefectDojo engagements.
   tests              List and get DefectDojo tests.
   findings           List and get DefectDojo findings.
   users              List and get DefectDojo users.
   dojo-groups        List and get DefectDojo authorization groups.
   jira-instances     List and get DefectDojo Jira instance configurations.
   risk-acceptances   List and get DefectDojo risk acceptances.
   metadata           List and get DefectDojo metadata entries.
   endpoints          List and get DefectDojo endpoints.
   finding-templates  List and get DefectDojo finding templates.
   import             Import scanner findings or language data into DefectDojo.
```

## Why dd-cli

- **Complete API coverage.** Every read and write across 12 DefectDojo resource types — products, product-types, engagements, tests, findings, users, dojo-groups, jira-instances, risk-acceptances, metadata, endpoints, finding-templates — driven from a typed client generated from DefectDojo's OpenAPI spec.
- **Drop-in replacement for `dd-import`.** Existing CI pipelines that invoke `dd-reimport-findings` or `dd-import-languages` with `DD_*` env vars keep working unchanged. The legacy console scripts are wired as thin shims over the new workflow code.
- **Pleasant interactive use.** Rich tables, JSON / YAML output for piping, profiles for switching between DefectDojo instances, `dd configure` interactive setup, `dd <resource> edit <id>` opens the resource as YAML in `$EDITOR`, action verbs like `dd findings close`, `risk-accept`, `dd engagements close/reopen`.
- **Safe writes.** `--dry-run` previews every mutation without sending HTTP. `--yes`/`-y` skips the destructive-op confirmation prompt for scripts. Typed exit codes (auth=3, not-found=5, etc.) so CI can branch on what went wrong.
- **Validated against real DefectDojo.** 24 integration tests run against a live instance per release, including a full Trivy-report import round-trip.

## Install

### From PyPI (recommended)

```bash
pip install dd-cli
# or, for an isolated install of the CLI:
pipx install dd-cli
```

`dd`, `dd-reimport-findings`, and `dd-import-languages` go on `PATH`.

### From source

```bash
git clone https://github.com/OsamaMahmood/dd-cli.git
cd dd-cli
pip install -e ".[dev,test]"
```

### Docker

```bash
podman run --rm \
  -e DD_URL=https://defectdojo.example.com \
  -e DD_API_KEY=… \
  ghcr.io/osamamahmood/dd-cli:latest \
  ping     # or any other dd subcommand
```

> Docker images are published to `ghcr.io/osamamahmood/dd-cli` (GitHub Container Registry) and `m4rkm3n/dd-cli` (Docker Hub) on each tag.

## Quickstart

```bash
# 1. Set up a profile (writes ~/.config/dd-cli/config.toml)
dd configure
# Profile name [default]: default
# DefectDojo URL: https://defectdojo.example.com
# API key (hidden): …
# Verify TLS certificates? [Y/n]: Y

# 2. Confirm it works
dd ping
# {"ok": true, "user": "alice", "url": "https://defectdojo.example.com"}

# 3. Browse
dd products list --output json | jq
dd findings list --severity Critical --active --output json | jq

# 4. Manage
dd findings close 42 --note "Fixed in v2.1.0" --yes
dd findings risk-accept 51 --until 2026-12-31 --reason "Compensating WAF rule"
dd engagements close 12 --yes
dd users deactivate alice --yes

# 5. Import a scanner report
dd import findings \
  --file trivy.json \
  --scanner "Trivy Scan" \
  --product-type "Web Apps" \
  --product "Payments" \
  --auto-create
```

## Configuration

dd-cli resolves settings in this order (later wins):

1. Built-in defaults
2. The active profile in `~/.config/dd-cli/config.toml` (or `$DD_CLI_CONFIG_DIR/config.toml`)
3. `DD_*` environment variables (legacy contract, see [migration](#migrating-from-dd-import))
4. `DD_CLI_*` environment variables (modern names, take precedence over `DD_*`)
5. Explicit CLI flags

API tokens are stored as `pydantic.SecretStr` and masked in `dd config show` output unless you pass `--show-secrets` to `dd config get api_key`.

### Profiles

Switch between multiple DefectDojo instances with named profiles:

```bash
dd configure --profile prod
dd configure --profile staging
dd config use prod          # default profile when --profile isn't given
dd --profile staging products list
```

### Output formats

Every read command supports `--output table|json|yaml` (default: `table`). YAML and JSON are stable and pipe-friendly:

```bash
dd findings list --severity High --output json | jq '.[] | {id, title, severity}'
```

## Importing scanner findings

The new ergonomic form:

```bash
dd import findings \
  --file trivy.json \
  --scanner "Trivy Scan" \
  --product-type "Web Apps" \
  --product "Payments" \
  --engagement "Q4 Release" \
  --test-name "Trivy" \
  [--auto-create | --traditional] \
  [--minimum-severity Medium] \
  [--push-to-jira] [--close-old-findings] \
  [--dry-run] [--yes] [--output table|json|yaml]
```

Two modes:

- **`--auto-create`** (recommended) — single API call. DefectDojo creates the product, engagement, and test as needed.
- **`--traditional`** — find-or-create each resource explicitly, then upload. Useful when DefectDojo's auto-create logic disagrees with what you want.

Either mode reads the same `DD_*` env vars the legacy tool used; CLI flags override env vars.

### From CI/CD

```yaml
# GitHub Actions
- name: Trivy
  run: trivy fs --format json -o trivy.json .

- name: Upload to DefectDojo
  env:
    DD_URL: ${{ secrets.DD_URL }}
    DD_API_KEY: ${{ secrets.DD_API_KEY }}
  run: |
    pip install dd-cli
    dd import findings \
      --file trivy.json \
      --scanner "Trivy Scan" \
      --product-type "Web Apps" \
      --product "${{ github.repository }}" \
      --engagement "${{ github.ref_name }}" \
      --test-name "Trivy" \
      --auto-create \
      --yes
```

```yaml
# GitLab CI
upload_findings:
  image: dd-cli:latest
  variables:
    DD_PRODUCT_TYPE_NAME: "Web Apps"
    DD_PRODUCT_NAME: "$CI_PROJECT_NAME"
    DD_ENGAGEMENT_NAME: "$CI_COMMIT_REF_SLUG"
    DD_TEST_NAME: "Trivy"
    DD_TEST_TYPE_NAME: "Trivy Scan"
    DD_FILE_NAME: "trivy.json"
    DD_AUTO_CREATE_CONTEXT: "true"
  script:
    - dd-reimport-findings    # legacy console script — still works
```

### Importing language statistics

[`cloc`](https://github.com/AlDanial/cloc) JSON output for a product:

```bash
cloc src --json --out cloc.json
dd import languages --file cloc.json --product-type "Web Apps" --product "Payments"
```

## Migrating from `dd-import`

`dd-cli` is a drop-in replacement. **Existing pipelines work unchanged** — install `dd-cli`, the legacy console scripts and all `DD_*` env vars stay valid:

| Legacy | Replacement | Status |
|---|---|---|
| `dd-reimport-findings` | `dd-reimport-findings` (shim) **or** `dd import findings` (new) | both work; `DD_*` env vars unchanged |
| `dd-import-languages` | `dd-import-languages` (shim) **or** `dd import languages` (new) | both work; `DD_*` env vars unchanged |
| `pip install dd-import` | `pip install dd-cli` | new package name |
| `osamamahmood/dd-import:latest` (Docker) | `ghcr.io/osamamahmood/dd-cli:latest` | swap image, no other changes |

Recommended migration path:

1. **Today:** swap the install command (`pip install dd-cli`) or the Docker image. Pipelines keep working.
2. **When convenient:** migrate to the new ergonomic commands (`dd import findings --file …`) for `--dry-run`, typed exit codes, profile support.

The new and legacy entry points have one deliberate difference:

- `dd-reimport-findings` exits **`1` on any failure** (legacy contract — pipelines that grep `$?` keep working)
- `dd import findings` exits with **typed codes**: 3 (auth), 5 (not found), 6 (validation), 7 (API), 8 (network), 9 (config). Useful for branching CI logic.

A full DD_* env-var reference lives in the [Configuration guide](https://osamamahmood.github.io/dd-cli/configuration/) and is pinned by a 9-test `@pytest.mark.compat` suite in [`tests/compat/`](tests/compat/).

## Documentation

- **[Documentation site](https://osamamahmood.github.io/dd-cli/)** — install, quickstart, configuration, CLI reference, CI recipes, migration guide
- [`RELEASING.md`](RELEASING.md) — how releases are cut and published
- [`CLAUDE.md`](CLAUDE.md) + [`.claude/`](.claude/) — contributor + agent ramp-up docs (architecture, conventions, workflows, decisions)

## Development

```bash
git clone https://github.com/OsamaMahmood/dd-cli.git
cd dd-cli
pip install -e ".[dev,test]"
make test           # 257 unit tests + 12 snapshots
make lint           # ruff
make typecheck      # mypy --strict
make smoke          # 24 integration tests against a live DD (env vars required)
```

The typed API client in `src/dd_cli/_client/` is generated from [`dd-api.json`](dd-api.json) (DefectDojo's OpenAPI spec). Regenerate after a DefectDojo upgrade:

```bash
make install-all    # adds openapi-python-client
make generate-client
# review the diff before committing
```

## License

[3-Clause BSD](LICENSE.txt) — same as the upstream `dd-import` project.

## Acknowledgments

dd-cli builds on [`dd-import`](https://github.com/MaibornWolff/dd-import) by **Stefan Fleckenstein** at **MaibornWolff GmbH**, now archived. The original tool's `DD_*` env-var contract is preserved exactly so existing CI pipelines migrate without changes.
