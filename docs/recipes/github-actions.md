# GitHub Actions

Two ready-to-paste blocks: a minimal "scan and upload to DefectDojo" job, and a fuller multi-scanner version.

## Minimal: Trivy + dd-cli

```yaml
name: Security scan
on: [push, pull_request]

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run Trivy
        run: |
          curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh \
            | sh -s -- -b /usr/local/bin
          trivy fs --format json -o trivy.json .

      - name: Set up Python + install dd-cli
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install dd-cli

      - name: Upload to DefectDojo
        env:
          DD_URL: ${{ secrets.DD_URL }}
          DD_API_KEY: ${{ secrets.DD_API_KEY }}
        run: |
          dd import findings \
            --file trivy.json \
            --scanner "Trivy Scan" \
            --product-type "GitHub Repos" \
            --product "${{ github.repository }}" \
            --engagement "${{ github.ref_name }}" \
            --test-name "Trivy" \
            --auto-create \
            --yes
```

## With Docker (no Python install in the runner)

```yaml
- name: Upload to DefectDojo
  env:
    DD_URL: ${{ secrets.DD_URL }}
    DD_API_KEY: ${{ secrets.DD_API_KEY }}
  run: |
    docker run --rm \
      -v "$PWD:/work" -w /work \
      -e DD_URL -e DD_API_KEY \
      ghcr.io/osamamahmood/dd-cli:2 \
      import findings \
        --file trivy.json --scanner "Trivy Scan" \
        --product-type "GitHub Repos" \
        --product "${{ github.repository }}" \
        --engagement "${{ github.ref_name }}" \
        --test-name "Trivy" \
        --auto-create --yes
```

> Pin to a major version (`:2`) so dependabot picks up patch / minor updates but not breaking ones.

## Multi-scanner: Trivy + Bandit + Semgrep

```yaml
name: Security scans
on:
  push:
    branches: [main]
  schedule:
    - cron: "0 6 * * *"   # daily at 6am UTC

env:
  DD_URL: ${{ secrets.DD_URL }}
  DD_API_KEY: ${{ secrets.DD_API_KEY }}
  DD_PRODUCT_TYPE_NAME: GitHub Repos
  DD_PRODUCT_NAME: ${{ github.repository }}
  DD_ENGAGEMENT_NAME: ${{ github.ref_name }}
  DD_AUTO_CREATE_CONTEXT: "true"

jobs:
  trivy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: |
          curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin
          trivy fs --format json -o trivy.json .
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: pip install dd-cli
      - run: dd-reimport-findings   # legacy shim — DD_* env vars do everything
        env:
          DD_TEST_NAME: Trivy
          DD_TEST_TYPE_NAME: Trivy Scan
          DD_FILE_NAME: trivy.json

  bandit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: pip install bandit dd-cli
      - run: bandit -r src/ -f json -o bandit.json || true
      - run: dd-reimport-findings
        env:
          DD_TEST_NAME: Bandit
          DD_TEST_TYPE_NAME: Bandit Scan
          DD_FILE_NAME: bandit.json

  semgrep:
    runs-on: ubuntu-latest
    container: returntocorp/semgrep
    steps:
      - uses: actions/checkout@v4
      - run: semgrep --config auto --json --output semgrep.json
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: pip install dd-cli
      - run: dd-reimport-findings
        env:
          DD_TEST_NAME: Semgrep
          DD_TEST_TYPE_NAME: Semgrep JSON Report
          DD_FILE_NAME: semgrep.json
```

The pattern: shared `env:` block at the workflow level for everything every job needs (auth + product / engagement scoping), per-job `env:` for the scanner-specific bits.

## Branching on the new typed exit codes

`dd import findings` (the new command) exits with typed codes — useful for CI logic:

```yaml
- name: Upload + branch on result
  env:
    DD_URL: ${{ secrets.DD_URL }}
    DD_API_KEY: ${{ secrets.DD_API_KEY }}
  run: |
    set +e
    dd import findings \
      --file trivy.json --scanner "Trivy Scan" \
      --product-type "Web" --product "Payments" \
      --auto-create --yes
    rc=$?
    set -e

    case $rc in
      0) echo "Upload successful";;
      3) echo "::error::DefectDojo authentication failed — rotate DD_API_KEY"; exit 1;;
      8) echo "::warning::Network blip — retrying"; sleep 30; dd import findings ...;;
      9) echo "::error::Configuration missing"; exit 1;;
      *) echo "::error::Upload failed with code $rc"; exit 1;;
    esac
```

The legacy `dd-reimport-findings` shim **flattens all errors to exit 1** for backward compatibility — see [migration](../migration.md#exit-code-contract).
