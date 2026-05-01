# dd-cli v2 — Implementation Plan

> Source of truth for the rewrite of `dd-import` into `dd-cli`, a complete CLI for managing DefectDojo.
> Last updated: 2026-05-01

---

## 1. Background

`dd-import` was created by Stefan Fleckenstein at MaibornWolff GmbH as a small utility to push scanner findings and `cloc` language data into DefectDojo from CI/CD pipelines. The upstream project is now **archived** with no active development.

This fork (`dd-cli`, [github.com/OsamaMahmood/dd-import-v2](https://github.com/OsamaMahmood/dd-import-v2)) takes over and **expands the scope**: from "an importer driven by `DD_*` environment variables" to "a full DefectDojo management CLI" — covering products, engagements, tests, findings, users, JIRA configuration, risk acceptances, and the rest of the API surface — while keeping every existing CI integration working unchanged.

DefectDojo's REST API (v2.54.3) is documented in [`dd-api.json`](./dd-api.json) at the repo root: **226 path templates, ~450 operations across ~80 resources**. Hand-wrapping that surface is not viable; the new architecture generates a typed client from the spec.

## 2. Goals

1. **Full management CLI.** First-class subcommands for the resources DefectDojo users actually manage day to day: products, product types, engagements, tests, findings, users, JIRA configs, metadata, risk acceptances, endpoints, dojo groups.
2. **100% backward compatibility** with the existing `DD_*` env-var contract and the `dd-reimport-findings` / `dd-import-languages` entry points. Existing CI pipelines must not need a single line changed.
3. **Production-grade UX.** Rich terminal output, `--output json|yaml|table`, shell completion, profiles, helpful error messages, `--dry-run`, confirmation prompts on destructive ops.
4. **Production-grade quality.** Typed throughout (`mypy --strict`), ≥85% test coverage, lockfile-based reproducible installs, semantic versioning, automated PyPI + Docker + Homebrew releases.
5. **Sustainable maintenance.** API client regenerated from `dd-api.json` in seconds when DefectDojo cuts a new version. Solo-maintainer-friendly automation everywhere.

## 3. Non-goals

- Not a TUI (terminal UI). Plain CLI only.
- Not a daemon, webhook server, or long-running process.
- Not a marketed Python SDK. The generated client is an internal dependency, not a public API.
- Not a scanner. We import scanner output; we don't run scanners.
- Not a DefectDojo replacement or fork. We talk to DefectDojo over its REST API.

## 4. Decisions

These are locked-in defaults — flag any you want changed before scaffolding starts.

| # | Decision | Choice | Rationale |
|---|---|---|---|
| D1 | Minimum Python | **3.11** | Better typing (`Self`, exception groups), ~25% faster startup than 3.10, universally available on CI. |
| D2 | CLI framework | **Typer 0.12+** | Type-hint driven, Click-based, automatic shell completion, industry standard. |
| D3 | API client | **Generated** via `openapi-python-client`, **vendored** in `src/dd_cli/_client/` | 450 endpoints typed for free; regen via `make generate-client`. Vendoring keeps installs offline-friendly and PRs greppable. |
| D4 | Config | **pydantic-settings** with TOML profiles at `~/.config/dd-cli/config.toml` | Layered: CLI flag > env var > profile > defaults. `DD_*` env vars wired in as aliases. |
| D5 | Terminal output | **Rich** for humans; orjson/PyYAML for `--output json\|yaml` | Pretty by default, scriptable on demand. |
| D6 | Packaging | **`pyproject.toml` only**, managed by **uv** | Drop `setup.cfg` and `requirements.txt`. Lockfile via `uv.lock`. |
| D7 | Lint/format | **ruff** | Replaces flake8 + black + isort. One tool. |
| D8 | Type check | **mypy --strict** | Cheaper than pyright in CI; catches the same bugs for our code. |
| D9 | Test framework | **pytest** + `pytest-httpx` + `syrupy` (snapshots) + `coverage` | Migrate off `unittest`. |
| D10 | PyPI name | **`defectdojo-cli`** (binary command: `dd`) | `dd-cli` is taken on PyPI. `defectdojo-cli` is descriptive and discoverable. We continue publishing `dd-import` as a meta-package that depends on `defectdojo-cli` for one release cycle, then deprecate. |
| D11 | Repo layout | **src layout** | Standard, prevents shadowing during dev. |
| D12 | Docs | **mkdocs-material**, command reference auto-generated from Typer via `mkdocs-click` | Single source of truth, deploys to GitHub Pages. |
| D13 | Versioning | **SemVer**. v0.x during scaffolding, v1.0 = legacy parity, v2.0 = full mgmt CLI | Predictable for downstream pipelines. |
| D14 | License | **3-Clause BSD** (unchanged from upstream) | Honors original license terms. |

## 5. Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  dd CLI (Typer)                                             │
│  cli/app.py · cli/products.py · cli/findings.py · ...       │
├─────────────────────────────────────────────────────────────┤
│  Workflows / Services                                       │
│  workflows/import_findings.py · workflows/import_languages  │
│  services/bulk.py · services/risk_acceptance.py             │
├─────────────────────────────────────────────────────────────┤
│  DefectDojoClient (thin wrapper)                            │
│  retry · pagination iterator · error mapping · auth         │
├─────────────────────────────────────────────────────────────┤
│  Generated API client (openapi-python-client, vendored)     │
│  src/dd_cli/_client/                                        │
└─────────────────────────────────────────────────────────────┘
        ▲                                          ▲
        │                                          │
   ┌────┴───────────────┐                  ┌───────┴────────┐
   │ pydantic-settings  │                  │ Rich / orjson  │
   │ (config + DD_*)    │                  │ (output)       │
   └────────────────────┘                  └────────────────┘
```

### Cross-cutting concerns

| Concern | Where it lives | Notes |
|---|---|---|
| Config | `dd_cli/config/settings.py` | Layered. Profiles in TOML. `DD_*` aliases for compat. |
| Output | `dd_cli/output/` | `TableRenderer`, `JsonRenderer`, `YamlRenderer`. Selected by global `--output`. |
| Errors | `dd_cli/errors.py` | Typed: `AuthError`, `NotFoundError`, `ValidationError`, `APIError`. Each maps to a stable exit code. |
| Logging | `dd_cli/logging.py` | `structlog`. `-v`/`-vv` raise verbosity. JSON logs in CI. |
| Retry | `dd_cli/_client/retry.py` | Exponential backoff on 429/5xx. Idempotent verbs only. |
| Auth | `dd_cli/auth.py` | Bearer token from config/env. Optional keychain (later). |

### Exit codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 1 | Generic error |
| 2 | Usage error (bad flag, missing arg) — Typer default |
| 3 | Authentication failure |
| 4 | Authorization failure (403) |
| 5 | Resource not found (404) |
| 6 | Validation error (400) |
| 7 | API error (5xx after retries) |
| 8 | Network error |
| 9 | Configuration error |

## 6. Target repo layout

```
dd-cli/
├── pyproject.toml                # single source for build, deps, tools
├── uv.lock
├── README.md
├── PLAN.md                       # this document
├── CHANGELOG.md
├── LICENSE.txt                   # BSD 3-clause (unchanged)
├── Dockerfile                    # multi-stage; non-root; thin runtime
├── Makefile                      # generate-client, lint, test, docs, release
├── dd-api.json                   # DefectDojo OpenAPI 3.0.3 spec, source of truth
├── .github/
│   ├── workflows/
│   │   ├── ci.yml                # lint + type + test on PR/main
│   │   ├── release.yml           # tag → PyPI + Docker + Homebrew bump
│   │   ├── docs.yml              # main → gh-pages
│   │   └── nightly-smoke.yml     # docker-compose DefectDojo + integration tests
│   └── dependabot.yml
├── src/
│   └── dd_cli/
│       ├── __init__.py
│       ├── __main__.py           # python -m dd_cli
│       ├── cli/
│       │   ├── app.py            # root Typer app, global options
│       │   ├── configure.py      # `dd configure` interactive setup
│       │   ├── config_cmd.py     # `dd config get/set/list`
│       │   ├── products.py
│       │   ├── product_types.py
│       │   ├── engagements.py
│       │   ├── tests.py
│       │   ├── findings.py
│       │   ├── users.py
│       │   ├── jira.py
│       │   ├── risk_acceptance.py
│       │   ├── metadata.py
│       │   ├── endpoints.py
│       │   ├── import_cmd.py     # `dd import findings|languages`
│       │   └── legacy.py         # `dd-reimport-findings`, `dd-import-languages` shims
│       ├── _client/              # GENERATED — do not edit by hand
│       │   ├── __init__.py
│       │   ├── client.py
│       │   ├── api/
│       │   └── models/
│       ├── client.py             # DefectDojoClient (hand-written wrapper)
│       ├── config/
│       │   ├── __init__.py
│       │   ├── settings.py       # pydantic-settings models
│       │   ├── profiles.py
│       │   └── legacy_env.py     # DD_* compat layer
│       ├── output/
│       │   ├── __init__.py
│       │   ├── base.py
│       │   ├── table.py
│       │   ├── json_out.py
│       │   └── yaml_out.py
│       ├── workflows/
│       │   ├── import_findings.py
│       │   └── import_languages.py
│       ├── services/
│       │   ├── pagination.py
│       │   └── bulk.py
│       ├── auth.py
│       ├── errors.py
│       ├── logging.py
│       └── version.py
├── tests/
│   ├── conftest.py
│   ├── unit/
│   │   ├── cli/
│   │   ├── config/
│   │   ├── workflows/
│   │   └── client/
│   ├── integration/              # opt-in, requires docker-compose DD
│   ├── snapshots/                # syrupy
│   └── fixtures/
└── docs/
    ├── index.md
    ├── install.md
    ├── quickstart.md
    ├── configuration.md
    ├── reference/                # auto-generated from Typer
    ├── migration-from-dd-import.md
    ├── ci-recipes/
    │   ├── github-actions.md
    │   └── gitlab-ci.md
    └── contributing.md
```

The legacy `dd_import/`, `bin/`, `unittests/`, `setup.cfg`, `requirements.txt`, `.flake8`, `.coveragerc` are **deleted in M4** once shims and tests are ported. They stay on disk through M0–M3 to keep the legacy package installable from a checkout during the transition.

## 7. Backward compatibility strategy

Three guarantees, in priority order:

1. **`DD_*` env-var contract is sacred.** Every variable currently read by `dd_import/environment.py` keeps the same name and semantics. Pydantic-settings declares each as an alias on the new config model. Behavior on a clean checkout matches byte-for-byte for the supported scanners.
2. **Console scripts `dd-reimport-findings` and `dd-import-languages` keep working.** They become thin shims that load `DD_*` env vars and call the new workflow code. Same stdout, same exit codes, same Docker image entry points (`bin/dd-reimport-findings.sh`, `bin/dd-import-languages.sh`).
3. **The `dd-import` PyPI package keeps publishing for one minor release after v1.0**, as a meta-package that pins `defectdojo-cli==X.Y.*`. Existing `pip install dd-import` works. Release notes point to the new name.

### Compat tests

A dedicated test suite (`tests/compat/`) drives the legacy entry points end to end with mocked HTTP and asserts:
- Identical exit codes
- Identical stdout up to whitespace
- Identical request payloads to DefectDojo (snapshot tests on captured `httpx` calls)

These tests gate every PR until the legacy package is deleted in M4.

## 8. Milestones

Each milestone ends with a tagged release (`v0.M.0`). PRs are scoped per milestone and don't cross boundaries except for compat fixes.

### M0 — Scaffold (target: 1 week)

Deliverables:
- `pyproject.toml` with deps, optional-deps groups (`dev`, `docs`, `test`), tool configs (ruff, mypy, pytest, coverage).
- `src/dd_cli/` skeleton: `__init__.py` (version), `__main__.py`, `cli/app.py` (Typer root with `--version`, `--help`, `--profile`, `--output`, `-v`).
- `Makefile`: `make generate-client`, `make lint`, `make test`, `make docs`, `make build`.
- `make generate-client` runs `openapi-python-client` against `dd-api.json` into `src/dd_cli/_client/`.
- `.github/workflows/ci.yml`: ruff + mypy + pytest matrix on Python 3.11/3.12/3.13.
- `dd --version` works after `pip install -e .`.

Acceptance:
- `make lint && make test` passes locally and in CI.
- `dd --help` renders Typer's auto-help.
- Generated client compiles (`mypy` clean).

### M1 — Config & client wrapper (target: 1 week)

Deliverables:
- `dd_cli/config/settings.py`: pydantic-settings models for `Auth`, `Output`, `Logging`, `Profile`. Loads from CLI > env > TOML > defaults.
- `dd_cli/config/legacy_env.py`: `DD_*` aliases. Tested against every var in current `environment.py`.
- `~/.config/dd-cli/config.toml` profile loader. `dd configure` interactive setup writes one.
- `dd config get/set/list/use` subcommands.
- `dd_cli/client.py` `DefectDojoClient`: wraps generated client, adds:
  - `retry` decorator (429/5xx, exponential backoff, capped attempts).
  - `paginate(endpoint, **filters)` async iterator.
  - Error mapping → typed exceptions in `errors.py`.
  - Auth header injection (incl. `DD_EXTRA_HEADER_*` compat).
- `dd_cli/output/` renderers + `--output table|json|yaml` global flag.

Acceptance:
- `dd config set api_key …` round-trips through TOML.
- `DD_API_KEY=… dd config show` reads legacy env.
- `dd ping` (debug command) hits `/api/v2/users/me/` and prints in the chosen format.
- Compat tests for `DD_*` parsing match legacy behavior.

### M2 — Read commands (target: 1 week)

Deliverables — `list` and `get` for:
- products, product-types, engagements, tests, findings, users, dojo-groups, jira-instances, risk-acceptances, metadata, endpoints, finding-templates.

Each `list`:
- Accepts `--limit`, `--all`, `--filter key=value` (repeatable), resource-specific flags (e.g. `dd findings list --severity high --product "X"`).
- Streams results via `paginate()`.
- Renders via output formatter.

Each `get`:
- Takes ID or `--name` (resolves to ID).
- Renders single resource.

Acceptance:
- `dd findings list --severity critical --output json | jq` works.
- Snapshot tests cover table output for each resource.
- mypy --strict passes.

### M3 — Write commands (target: 1.5 weeks)

Deliverables:
- `create`, `update`, `delete` for the resources above where DefectDojo supports them.
- Action verbs: `dd findings close`, `dd findings reopen`, `dd findings risk-accept`, `dd engagements close`, `dd users deactivate`.
- Bulk operations: `--from-file findings.json` for create/update.
- Confirmation prompts on destructive ops; `--yes` to skip; `--dry-run` shows what would happen.
- Editor-driven update: `dd findings edit ID` opens `$EDITOR` with YAML.

Acceptance:
- Round-trip: `dd products create … && dd products update … && dd products delete …` with mocked HTTP.
- `--dry-run` produces no HTTP traffic.
- Compat tests still green.

### M4 — Import parity & legacy migration (target: 1 week)

Deliverables:
- `dd_cli/workflows/import_findings.py`: refactor of current `Api.reimport_scan` + `reimport_scan_with_auto_create` into a single workflow with strategy selection.
- `dd_cli/workflows/import_languages.py`: refactor of current `Api.import_languages`.
- New ergonomic commands: `dd import findings --file trivy.json --scanner "Trivy Scan" --product "X" …`. All `DD_*` env vars accepted as fallback.
- `dd_cli/cli/legacy.py`: `dd_reimport_findings_main()` and `dd_import_languages_main()` shims wired to `[project.scripts]` entry points `dd-reimport-findings` and `dd-import-languages`.
- All current `unittests/` ported to `tests/` under pytest.
- Legacy `dd_import/`, `bin/*.sh` (still installed via Docker), `setup.cfg`, `requirements.txt`, `.flake8`, `.coveragerc` deleted.
- Dockerfile rewritten as multi-stage on `python:3.12-slim`, runtime layer ~50 MB, non-root user, both legacy shell wrappers preserved.

Acceptance:
- Compat test suite green.
- Existing GitLab CI / GitHub Actions example workflows in upstream README run unchanged against new image.
- Docker image size measurably smaller than current alpine build.

### M5 — Polish & v2.0 release (target: 1 week)

Deliverables:
- `dd completion install bash|zsh|fish` (Typer's built-in).
- mkdocs-material site at `docs/` deployed to `gh-pages` on main.
- Auto-generated command reference (`mkdocs-click`).
- Migration guide from `dd-import`.
- CI recipes (GitHub Actions, GitLab CI, Jenkins).
- `release.yml`: tag `v*` → PyPI publish (trusted publisher), Docker push (ghcr.io + docker.io), Homebrew formula bump (PR to tap repo).
- `homebrew-tap` repo created with `defectdojo-cli` formula.
- `dd-import` shim package published one last time (depends on `defectdojo-cli`).
- v2.0.0 release.

Acceptance:
- `pip install defectdojo-cli` and `brew install osamamahmood/tap/defectdojo-cli` both produce a working `dd`.
- Docs site live with command reference.

### Total: ~6.5 weeks of focused effort.

## 9. Testing strategy

| Layer | Tooling | Coverage target |
|---|---|---|
| Unit (CLI parsing, config, formatters, error mapping) | pytest | ≥90% |
| Workflow (import flows, bulk ops) | pytest + pytest-httpx | ≥85% |
| Client wrapper (retry, pagination, auth) | pytest + pytest-httpx | ≥90% |
| Snapshot (table/JSON output) | syrupy | per-command |
| Compat (legacy DD_* + entry points) | pytest + pytest-httpx | every legacy code path |
| Integration (real DefectDojo) | pytest + docker-compose | smoke only, nightly |

**Coverage gate**: PRs fail under 85% line coverage on changed files (codecov patch check). Total coverage gate at 80% on main.

**Generated client is excluded** from coverage and mypy strict (it's vendored third-party code).

## 10. CI/CD

### `ci.yml` (every PR + push to main)
- Matrix: Python 3.11, 3.12, 3.13 × ubuntu-latest
- Steps: `uv sync --frozen` → `make lint` → `make typecheck` → `make test`
- Coverage upload to codecov
- Cache: uv, ruff, mypy

### `release.yml` (tag `v*`)
- Build sdist + wheel via `uv build`
- Publish to PyPI via OIDC trusted publisher (no API token in repo)
- Build & push Docker images: `ghcr.io/osamamahmood/dd-cli:vX.Y.Z`, `:vX.Y`, `:latest`
- Open PR to `homebrew-tap` repo bumping the formula
- Generate GitHub Release notes from CHANGELOG section

### `docs.yml` (push to main)
- `mkdocs build` → deploy to `gh-pages`

### `nightly-smoke.yml` (cron)
- docker-compose up DefectDojo
- Run integration suite against it
- Open issue on failure

### `dependabot.yml`
- Weekly: pip deps, GitHub Actions
- Auto-merge for patch updates that pass CI

## 11. Distribution

| Channel | Artifact | Audience |
|---|---|---|
| PyPI | `defectdojo-cli` | Python users, CI runners |
| PyPI | `dd-import` (shim, one release) | Existing users — soft migration |
| Docker (ghcr.io) | `ghcr.io/osamamahmood/dd-cli:tag` | CI pipelines |
| Docker Hub | `osamamahmood/dd-cli:tag` | Existing CI pipelines (legacy image name preserved) |
| Homebrew | `osamamahmood/tap/defectdojo-cli` | macOS/Linux developers |
| GitHub Releases | sdist + wheel + checksums + SBOM | Air-gapped installs |

`pipx install defectdojo-cli` is the recommended developer-machine install.

## 12. Documentation

`docs/` is mkdocs-material. Pages:

1. **Home** — what dd-cli is, why it exists.
2. **Install** — pipx, pip, brew, docker.
3. **Quickstart** — `dd configure`, list a product, import findings.
4. **Configuration & profiles** — TOML schema, env vars, precedence.
5. **Command reference** (auto-generated from Typer).
6. **Importing findings** — both `dd import findings` and the legacy entry points.
7. **Migration from dd-import** — for users of the upstream tool.
8. **CI recipes** — GitHub Actions, GitLab CI, Jenkins examples.
9. **Contributing** — repo layout, generate-client, release process.
10. **Architecture** — short version of this PLAN, kept current.

`README.md` shrinks to: install, one quickstart example, link to docs site.

## 13. Risks & mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Generated client breaks on DD spec change | Medium | High | Pin `dd-api.json` version; regenerate intentionally; integration smoke tests catch regressions. |
| DefectDojo introduces breaking API changes | Medium | High | Version-pin client; declare supported DD versions in README; nightly smoke against latest stable DD. |
| Backward-compat regression silently breaks user CI | Low | Critical | Compat test suite gates every PR; snapshot HTTP payloads of legacy flows. |
| `defectdojo-cli` PyPI name unavailable | Low | Low | Fall back to `ddcli` or `osmc-defectdojo`; verify in M0 before naming. |
| Solo-maintainer burnout | High | Critical | Phased delivery; automate everything; dependabot; trusted publisher; no manual release steps. |
| Generated client is huge / slow imports | Low | Medium | Lazy-import per command; benchmark `dd --version` startup in CI. |

## 14. Out of scope (post-v2)

Tracked as `future/*.md` once we get there:

- Interactive TUI (Textual) — separate package.
- Watch mode (`dd findings watch --severity critical`).
- Webhook receiver / event-driven imports.
- Plugin system for custom scanners and output formats.
- SBOM upload helpers (CycloneDX, SPDX scanner integrations).
- Bulk migration tools (DD instance → DD instance).
- Local DefectDojo lifecycle commands (`dd dev up/down`).

## 15. Success criteria

v2.0.0 ships when **all** are true:

- [ ] `pip install defectdojo-cli` produces a working `dd` on Python 3.11/3.12/3.13.
- [ ] All existing `DD_*`-driven CI pipelines pass with the new Docker image, no config change.
- [ ] `dd` covers list/get/create/update/delete for the 12 resources in §8 M2/M3.
- [ ] Coverage ≥85%, mypy --strict clean, ruff clean.
- [ ] Docs site live; command reference up to date.
- [ ] PyPI + Docker (both registries) + Homebrew tap all publish on tag automatically.
- [ ] Compat test suite green.

---

## Appendix A — First scaffolding PR (concrete file list)

When M0 starts, the first PR contains exactly these new files and **no deletions**:

```
pyproject.toml
uv.lock
Makefile
PLAN.md                                  # this doc, already merged
.github/workflows/ci.yml
.github/dependabot.yml
src/dd_cli/__init__.py                   # __version__ = "0.0.1"
src/dd_cli/__main__.py                   # from .cli.app import app; app()
src/dd_cli/version.py
src/dd_cli/cli/__init__.py
src/dd_cli/cli/app.py                    # Typer app with --version, --help
src/dd_cli/_client/.gitkeep              # populated by `make generate-client`
tests/__init__.py
tests/test_smoke.py                      # asserts `dd --version` prints expected
docs/.gitkeep
.gitignore                               # add uv, ruff, mypy, pytest, dist/, build/
```

After this PR is merged: `pip install -e .` then `dd --help` works.

## Appendix B — `pyproject.toml` skeleton (target shape)

```toml
[project]
name = "defectdojo-cli"
version = "0.0.1"
description = "Production-grade CLI for DefectDojo"
readme = "README.md"
requires-python = ">=3.11"
license = { file = "LICENSE.txt" }
authors = [{ name = "Osama Mahmood", email = "osama.mahmood40@gmail.com" }]
dependencies = [
  "typer>=0.12",
  "rich>=13",
  "pydantic>=2.6",
  "pydantic-settings>=2.2",
  "httpx>=0.27",
  "structlog>=24",
  "tomli-w>=1",          # writing config TOML
  "PyYAML>=6",
  "orjson>=3.10",
]

[project.optional-dependencies]
dev = ["ruff", "mypy", "pre-commit"]
test = ["pytest", "pytest-httpx", "pytest-cov", "syrupy", "hypothesis"]
docs = ["mkdocs-material", "mkdocs-click", "mkdocstrings[python]"]

[project.scripts]
dd                    = "dd_cli.cli.app:app"
dd-reimport-findings  = "dd_cli.cli.legacy:dd_reimport_findings_main"
dd-import-languages   = "dd_cli.cli.legacy:dd_import_languages_main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/dd_cli"]

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "B", "UP", "N", "SIM", "RUF"]

[tool.mypy]
python_version = "3.11"
strict = true
exclude = ["src/dd_cli/_client/"]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-ra --strict-markers --cov=dd_cli --cov-report=term-missing"

[tool.coverage.run]
source = ["dd_cli"]
omit = ["src/dd_cli/_client/*"]
```

## Appendix C — Open questions

1. **Docker base image**: stay on `python:3.12-alpine` (small but musl quirks with some scanner JSON parsers) or move to `python:3.12-slim` (~30 MB larger, but no musl issues)? Recommend **slim**.
2. **Homebrew tap location**: new repo `OsamaMahmood/homebrew-tap` or repurpose existing one? Need to check.
3. **Telemetry**: opt-in anonymous usage (helps prioritize commands)? Default off, well documented. Decide before v2.0.
4. **Generated client regeneration cadence**: on every DefectDojo minor release, or only when we need a new endpoint? Recommend **on-demand** to avoid churn.

---

*Plan owner: @OsamaMahmood. Updates to this document go through PR review like any other code change.*
