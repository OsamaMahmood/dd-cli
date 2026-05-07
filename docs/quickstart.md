# Quickstart

A complete first session — install, set up, browse, manage, import.

## 1. Install

```bash
pip install dd-cli
```

## 2. Configure a profile

```bash
dd configure
# Profile name [default]: default
# DefectDojo URL: https://defectdojo.example.com
# API key (hidden): …
# Verify TLS certificates? [Y/n]: Y
# Add extra HTTP headers (e.g. for WAF auth)? [y/N]: n
#
# ✓ Saved profile default to /Users/.../config/dd-cli/config.toml
```

`dd configure` is interactive. For scripts, use flags + `--no-input`:

```bash
dd configure \
  --profile prod \
  --url https://defectdojo.example.com \
  --api-key "$DD_API_KEY" \
  --no-input
```

## 3. Verify

```bash
dd ping
# {
#   "ok": true,
#   "profile": "default",
#   "url": "https://defectdojo.example.com",
#   "user": "alice"
# }
```

## 4. Browse

```bash
dd products list                                # default table format
dd products list --output json | jq             # pipe-friendly
dd findings list --severity Critical --active --output json | jq

dd products get 5
dd products get --name "Payments"               # resolve by name
dd findings list --product 5 --severity High
```

## 5. Manage

Action verbs — close a finding, mark it as a false positive:

```bash
dd findings close 42 --note "Fixed in v2.1.0" --yes
dd findings close 51 --false-positive --note "Reviewed by appsec" --yes
dd findings reopen 42 --yes
dd findings risk-accept 51 \
  --until 2026-12-31 \
  --reason "Compensating WAF rule" \
  --yes
dd engagements close 12 --yes
dd engagements reopen 12 --yes
dd users deactivate alice --yes
```

Generic CRUD — `--field` overlays on top of `--from-file`, both optional:

```bash
dd products create \
  --field name=NewProduct \
  --field prod_type=2 \
  --field business_criticality=high
dd products update 5 --field business_criticality=very_high
dd products edit 5                              # opens YAML in $EDITOR; PATCH on save
dd products delete 5 --dry-run                  # preview, no HTTP
dd products delete 5 --yes
```

Bulk via JSON/YAML payload:

```bash
cat > engagement.yaml <<EOF
name: Q1 Pen Test
product: 5
target_start: 2026-01-15
target_end: 2026-04-15
engagement_type: Interactive
EOF
dd engagements create --from-file engagement.yaml
```

## 6. Import a scanner report

```bash
trivy fs --format json -o trivy.json .

dd import findings \
  --file trivy.json \
  --scanner "Trivy Scan" \
  --product-type "Web Apps" \
  --product "Payments" \
  --engagement "Q4 Release" \
  --test-name "Trivy" \
  --auto-create \
  --yes
# Imported 'Trivy Scan' findings into test 18 (new=2, closed=0, reactivated=0).
```

See [Importing findings](importing-findings.md) for both flow modes and scanner-specific tips, and [CI recipes](recipes/github-actions.md) for ready-to-paste pipeline blocks.

## What's next

- [Configuration](configuration.md) — profiles, env vars, exit codes
- [Migration from dd-import](migration.md) — drop-in replacement, `DD_*` env-var contract
- [CLI reference](cli-reference.md) — every command, every flag
