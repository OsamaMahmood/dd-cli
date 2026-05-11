# Decisions

The durable project lore. Why `dd-cli` is the way it is, with the specific incident, constraint, or trade-off behind each non-obvious choice. Read this before proposing a change that contradicts an existing pattern — the answer to "why didn't we just do X?" usually lives here.

If you find yourself confused by a design choice, check here first; if it's not documented, ask before changing.

## Locked-in design decisions (D1–D17)

The table below was the pre-implementation contract for `dd-cli` — every choice was flagged before scaffolding so the team could push back. None of them have been overturned. Anchored here in case you're tempted to revisit one without realising it was decided deliberately.

| # | Decision | Choice | Rationale |
|---|---|---|---|
| D1 | Minimum Python | **3.11** | Better typing (`Self`, exception groups), ~25% faster startup than 3.10, universally available on CI. |
| D2 | CLI framework | **Typer 0.12+** | Type-hint driven, Click-based, automatic shell completion, industry standard. |
| D3 | API client | **Generated** via `openapi-python-client`, **vendored** in `src/dd_cli/_client/` | 450 endpoints typed for free; regen via `make generate-client`. Vendoring keeps installs offline-friendly and PRs greppable. |
| D4 | Config | **pydantic-settings** with TOML profiles at `~/.config/dd-cli/config.toml` | Layered: CLI flag > env var > profile > defaults. `DD_*` env vars wired in as aliases. |
| D5 | Terminal output | **Rich** for humans; orjson/PyYAML for `--output json\|yaml` | Pretty by default, scriptable on demand. |
| D6 | Packaging | **`pyproject.toml` only**, build via **hatchling + hatch-vcs** | Drop `setup.cfg` and `requirements.txt`. Version comes from the git tag, not a hand-bumped field. |
| D7 | Lint/format | **ruff** | Replaces flake8 + black + isort. One tool. |
| D8 | Type check | **mypy --strict** | Cheaper than pyright in CI; catches the same bugs for our code. |
| D9 | Test framework | **pytest** + `pytest-httpx` + `syrupy` (snapshots) + `coverage` | Migrate off `unittest`. |
| D10 | PyPI name | **`dd-cli`** (binary command: `dd`) | Originally locked in as `defectdojo-cli` but that name turned out to be taken on PyPI by an unrelated project. `dd-cli` was available, matches the binary, and matches the GitHub repo name. See "PyPI name pivot" below. |
| D11 | Repo layout | **src layout** | Standard, prevents shadowing during dev. |
| D12 | Docs | **mkdocs-material**, command reference auto-generated from Typer via `mkdocs-click` | Single source of truth, deploys to GitHub Pages. |
| D13 | Versioning | **SemVer**. v0.x during scaffolding, v1.0 = legacy parity, v2.0 = full mgmt CLI | Predictable for downstream pipelines. |
| D14 | License | **3-Clause BSD** (unchanged from upstream) | Honors original license terms. |
| D15 | Docker base | **`python:3.12-slim`** | No musl quirks; ~30 MB larger than alpine but compatible with every scanner JSON parser we've seen. |
| D16 | Homebrew tap | **`OsamaMahmood/homebrew-tap`** (new repo) | Originally planned for M5; deferred post-v2.0 — see "Why no Homebrew tap (yet)" below. |
| D17 | Generated client regen cadence | **On-demand**, when a new endpoint is needed | Avoids churn; minor DD releases don't force a regen. |

## Project goals and non-goals

**Goals** (what dd-cli is for):
1. Full management CLI for the 12 DefectDojo resources users actually manage day-to-day.
2. 100% backward compatibility with the existing `DD_*` env-var contract and the `dd-reimport-findings` / `dd-import-languages` console scripts.
3. Production-grade UX: Rich output, `--output json|yaml|table`, shell completion, profiles, helpful error messages, `--dry-run`, confirmation prompts.
4. Production-grade quality: typed throughout (`mypy --strict`), ≥85% test coverage target, automated PyPI + Docker releases.
5. Sustainable for a solo maintainer: API client regenerable from `dd-api.json` in seconds; automation everywhere.

**Non-goals** (what dd-cli is *not*, by design — if you're proposing one of these, expect pushback):
- **Not a TUI.** Plain CLI only. Interactive Textual-based UI is post-v2 scope.
- **Not a daemon, webhook server, or long-running process.** Each invocation is a one-shot.
- **Not a marketed Python SDK.** The generated client at `src/dd_cli/_client/` is an internal dependency, not a public API. Don't import from it outside `dd_cli.client`.
- **Not a scanner.** We import scanner output; we don't run scanners.
- **Not a DefectDojo replacement or fork.** We talk to DefectDojo over its REST API.

## Milestone history (v0.x → v2.0)

`dd-cli` shipped in six milestones over ~6.5 weeks. Anchoring the timeline here so the current state makes sense; the per-PR git log has the full detail.

| Milestone | What shipped | Tag |
|---|---|---|
| **M0** | Scaffold — `pyproject.toml`, src layout, Makefile, generated client wiring, Typer skeleton, ci.yml | `v0.1.0` |
| **M1** | Config layer (pydantic-settings, TOML profiles, `DD_*` aliases), `DefectDojoClient` (retry + pagination + error mapping), output renderers, `dd ping`, `dd configure`, `dd config get/set/list/use` | `v0.2.0` |
| **M2** | Read commands — `list` + `get` for 12 resources; snapshot tests; the `_resource.py` shared helpers pattern | `v0.3.0` |
| **M3** | Write commands — `create`/`update`/`delete`/`edit` + action verbs (`findings close`, `engagements close`, `users deactivate`, etc.); `--dry-run` and `--yes` enforcement | `v1.0.0` |
| **M4** | Import workflows (`workflows/import_findings.py`, `workflows/import_languages.py`), legacy console-script shims (`cli/legacy.py`), Dockerfile rewrite (multi-stage, non-root), `dd-import/` deletion | (M4-a/b inside the v1.x line) |
| **M5** | Polish & v2.0 — PyPI OIDC publishing, multi-arch Docker (GHCR + Docker Hub), mkdocs-material site at GitHub Pages, mkdocs-click auto-generated CLI reference, migration guide, CI recipes, nightly-smoke workflow | `v2.0.0` (2026-05-07) |

What v2.0 explicitly did *not* ship: a Homebrew tap (deferred — see below), a separate `dd-import` PyPI shim package (superseded by in-repo console scripts — see below), telemetry (out of scope), CHANGELOG.md (use GitHub Releases auto-notes instead).

## Risks the project actively manages

These were called out before v1.0 and the mitigations live in code/CI today. Re-listed here so contributors don't accidentally weaken the mitigation:

| Risk | Likelihood | Impact | Mitigation (where it lives) |
|---|---|---|---|
| Generated client breaks on DD spec change | Medium | High | Pin `dd-api.json`; regenerate intentionally via `make generate-client`; nightly-smoke catches regressions against DD master. |
| DefectDojo introduces breaking API changes | Medium | High | Nightly-smoke against latest `master` opens a deduped issue on failure — `.github/workflows/nightly-smoke.yml`. |
| Backward-compat regression silently breaks user CI | Low | **Critical** | `tests/compat/` suite gates every PR; snapshots the request payloads of legacy flows; assert exact stdout strings (including the legacy emojis). See [compatibility.md](compatibility.md). |
| `dd-cli` PyPI name unavailable | (Realised) | Low | Already happened with `defectdojo-cli`; pivoted to `dd-cli` in M5a. Future package names: check PyPI first. |
| Solo-maintainer burnout | **High** | **Critical** | Phased delivery; automate everything; dependabot; trusted publisher; no manual release steps. **Don't add manual steps to the release flow without strong justification.** |
| Generated client is huge / slow imports | Low | Medium | Lazy-import per command; `dd --version` startup benchmarked. |

## Package layout

### Why a typed, vendored, generated API client

**Choice**: client at `src/dd_cli/_client/` generated by `openapi-python-client` against [dd-api.json](../dd-api.json), committed to the repo, excluded from lint/typecheck/coverage.

**Why**:
- DefectDojo's OpenAPI spec describes ~450 operations across ~80 resources. Hand-wrapping is unviable; the surface is too large and DefectDojo cuts a release every few weeks.
- Generation gives us free typed models. mypy `--strict` catches typos at every call site even though we mostly bypass the per-endpoint functions.
- **Vendoring** (committing the generated tree rather than treating it as a build artifact) means:
  - Offline installs work — no openapi-python-client at install time.
  - PRs are greppable for endpoint shapes (you can search `_client/` to see how DD models a field).
  - We control regen cadence; minor DD releases don't force a regen.

**Trade-off**: large diffs whenever we regenerate. The hardcoded `make generate-client` command wipes and rewrites the tree, so review the diff carefully (PR template asks for it).

### Why we mostly bypass the generated per-endpoint functions

`client.py` calls `self._raw.get_httpx_client().get(path, params=...)` directly rather than `self._raw.products.products_list(...)` or similar.

**Why**:
- Generated per-endpoint functions are typed but verbose; each takes 5–10 lines to invoke vs. a one-line path string.
- We get retry, pagination, and error mapping for free in the wrapper. Going through generated functions would duplicate that logic.
- The wrapper still exposes `client.raw` for cases where the typed endpoint genuinely helps (e.g. complex query-param structs).

**When you should use a generated endpoint**: if the request shape is unusually complex (nested objects, polymorphic params) and writing it as a dict would be error-prone, reach for `client.raw.api.<group>.<endpoint>(...)`. Most resource commands don't need this.

### Why `src/` layout

**Choice**: package source at `src/dd_cli/`, not at the repo root.

**Why**: prevents accidental `import dd_cli` from the working directory shadowing the installed version. `pip install -e .` is the only way to make imports work in dev — this catches packaging mistakes early. Standard Python community recommendation; nothing dd-cli-specific.

### Why the `_cmd` suffix on `tests_cmd.py` and `config_cmd.py`

**Choice**: the CLI module for `dd tests` is `tests_cmd.py`, not `tests.py`. Similar for `config_cmd.py`.

**Why**:
- `tests.py` would collide with pytest's `tests_*.py` discovery pattern. ruff's `PT` (pytest-style) rules would also fire on the filename. A per-file ignore exists (`pyproject.toml` has `"**/tests_cmd.py" = ["PT"]`), but renaming the file to `tests.py` would re-trip the false-positive flood and confuse pytest.
- `config.py` would shadow the `dd_cli/config/` package (`from dd_cli.config import ...` would resolve to the file, not the package).

**Don't rename these files.** The naming is load-bearing.

## Naming and external identity

### PyPI name: `dd-cli` (not `defectdojo-cli`)

**Original choice**: `defectdojo-cli`.

**Reality**: the PyPI name `defectdojo-cli` is taken by an unrelated project ([fopina/defectdojo-api-generated](https://pypi.org/project/defectdojo-cli/)). Locked in as decision **D10** without checking PyPI availability.

**Pivot**: `dd-cli`. Matches the binary name (`dd`), matches the GitHub repo (`OsamaMahmood/dd-cli`), available on PyPI, short enough for CI scripts.

The pyproject.toml `name` was changed during M5a (PR #12) when PyPI publishing was being wired up. Tests, docs, README, and the install instructions were updated in the same PR.

**Lesson for future package names**: check PyPI availability before committing to one in design docs.

### Docker Hub namespace: `m4rkm3n/dd-cli`

**Choice**: Docker Hub publishes to `m4rkm3n/dd-cli`. GHCR publishes to `ghcr.io/osamamahmood/dd-cli`. The two namespaces differ.

**Why**: the maintainer's Docker Hub username (`m4rkm3n`) doesn't match the GitHub handle (`osamamahmood`). The two accounts were never linked. This was caught by PR #16 after an initial release pushed to `osamamahmood/dd-cli` on Docker Hub, which doesn't exist (or did exist as someone else's namespace).

**Don't try to "fix" the mismatch.** No `osamamahmood/dd-cli` repo exists on Docker Hub; creating one would split user pulls across two namespaces and confuse the docs/examples.

The mismatch is documented in:
- [.github/workflows/release.yml](../.github/workflows/release.yml) (comment on the tag-computation step).
- [README.md](../README.md) install section.
- [docs/install.md](../docs/install.md).
- [.claude/release.md](release.md).

## Versioning + release

### Why hatch-vcs (version from git tag)

**Choice**: package version comes from the latest git tag via hatch-vcs. No `version = "x.y.z"` field in pyproject.toml.

**Why**:
- Single source of truth: the git tag is the version. No `pyproject.toml` field to forget to bump, no `_version.py` to commit and then forget to bump.
- Untagged builds get explicit dev versions (`2.0.1.dev3+g<sha>`) — you can't accidentally publish a dev build as a stable release.

**Trade-off**: builds need `.git/` to resolve the version. Wheels embed the resolved version at build time via the `hatch-vcs` build hook (`version-file = "src/dd_cli/_version.py"`), so installed wheels work without git. The Dockerfile preserves `.git/` in the builder stage for this reason.

### Why the PEP 440 normalisation check in release.yml

**Choice**: the wheel-version-verify step uses `packaging.version.Version()` to canonicalise both sides before comparing the tag against the built wheel's version.

**Why** (specific past failure):
- v2.0.0-rc.1 was tagged as `v2.0.0-rc.1`.
- hatch-vcs normalised the version to `2.0.0rc1` per PEP 440 § Public version identifiers (strip the `v`, collapse `-rc.` to `rc`, drop the dot before the digit).
- The original verify step did a literal string compare: `"$BUILT_VERSION" != "${GITHUB_REF_NAME#v}"` → `"2.0.0rc1" != "2.0.0-rc.1"` → workflow failed even though the wheel was correct.

The fix (PR #15): `NORMALIZED_TAG=$(python -c "from packaging.version import Version; print(Version('$TAG_VERSION'))")` then compare against `NORMALIZED_TAG`. This canonicalises both sides identically.

**Implication for tagging**: prereleases must use `-rc.N` (note the dot). `v2.0.0-rc1` normalises differently and breaks the check.

### Why the tag-on-main guard

**Choice**: `release.yml` checks `git merge-base --is-ancestor "$TAG_SHA" origin/main` before doing anything.

**Why** (specific past failure):
- v0.4.0 was once tagged on the tip of a feature branch instead of the merge commit on main.
- `gh release create --generate-notes` looks for PRs between the previous tag and the new tag. With the tag on a feature branch, the merge commit (and therefore the PR association) wasn't reachable, so the auto-generated notes came up empty.
- Result: v0.4.0 shipped with an empty changelog.

The guard catches this before publishing anything. If you see `Tag ... is not an ancestor of origin/main`, delete the tag locally + remote, `git pull --ff-only origin main`, re-tag on the current `HEAD`.

### Why `--latest=true` is explicit (not "newest tag" heuristic)

**Choice**: stable tags pass `--latest=true` to `gh release create`; prerelease tags pass `--latest=false`.

**Why** (specific past failure):
- v0.1.0 and v0.2.0 were backfilled (created as GitHub Releases after v0.3.0 already existed).
- GitHub's default "Latest" heuristic uses the `publishedAt` timestamp, not the version number.
- Result: v0.2.0 was marked "Latest" even though v0.3.0 was actually newer.

Passing `--latest=true` explicitly bypasses the heuristic and pins the flag to whatever the workflow decides based on the tag shape (stable = latest, prerelease = not latest).

## Backward compatibility

### Why the legacy console scripts always exit 1

**Choice**: `dd-reimport-findings` and `dd-import-languages` collapse every `DDCliError` (and every unexpected exception) to `sys.exit(1)`. They don't use the typed exit codes (3 for auth, 5 for not-found, etc.) that `dd import findings` uses.

**Why**: existing CI/CD pipelines grep `$?` and assume "non-zero = bad". Many `if [ $? -ne 0 ]; then …; fi` constructs in production don't care about *why* the import failed, only *that* it failed. Switching to typed codes would silently change the behavior of pipelines that bail on any non-zero — they'd now also bail on `9` (config error), which is correct, but the semantic would be different from what the legacy tool did.

The new typed codes are opt-in: pipelines that want them migrate to `dd import findings`. See [compatibility.md](compatibility.md#exit-code-contract--legacy-vs-new).

### Why emojis in `cli/legacy.py`

**Choice**: `cli/legacy.py` prints `❌ Error during import:`, `✅ Import completed successfully!`, `🚀 Using AUTO-CREATE workflow`, `📋 Using TRADITIONAL workflow`. Every other source file is emoji-free.

**Why**: the upstream `dd-import` tool printed those exact strings. Real CI logs grep for them (`grep "Import completed" build.log`), and pipelines parse them in custom dashboards. Removing or changing them would silently break alerting setups in production.

Compat tests (`tests/compat/test_legacy_entry_points.py`) assert the strings explicitly. If you change them, the test fails — that's the forcing function.

**Lesson**: "we should drop the emojis to match our code style" is a wrong fix. The contract trumps style for the legacy surface.

### Why we dropped the `dd-import` shim package

**Original plan** (M5): publish a final `dd-import==X.Y.Z` to PyPI as a meta-package that depends on `dd-cli`, so `pip install dd-import` keeps working.

**Why dropped**: the legacy console scripts (`dd-reimport-findings`, `dd-import-languages`) ship inside `dd-cli` itself via `pyproject.toml [project.scripts]`. A user migrating from `dd-import` just does `pip install dd-cli` instead — same binaries on PATH, same `DD_*` env vars honored. The shim package was unnecessary indirection.

If someone files an issue asking for the shim, the answer is "you already have it — `pip install dd-cli`".

## Deferred features

### Why no Homebrew tap (yet)

**Choice**: a `homebrew-tap` repo with a `dd-cli` formula was originally planned for M5 (see D16) but deferred post-v2.0.

**Why**:
- Most likely install path is `pip install dd-cli` or `pipx install dd-cli` — they're zero-friction for the Python and CI/CD audience.
- A Homebrew formula needs per-release resource-list generation (every Python dep becomes a `resource "..."` block in the formula). That's maintenance cost in exchange for `brew install` ergonomics, and the maintainer's bandwidth is more useful on actual features.
- If demand materialises, it can be added later without breaking anything.

The `RELEASING.md "What the workflow does NOT do yet"` section calls this out.

### Why no CHANGELOG.md

**Choice**: rely on GitHub Releases' auto-generated notes (`gh release create --generate-notes`).

**Why**:
- The notes are generated from PR titles and bodies between consecutive tags, and they ship on the release page. A separate `CHANGELOG.md` would just duplicate this.
- Maintaining `CHANGELOG.md` by hand is error-prone (forgotten entries, merge conflicts on every release PR).
- Tools that need a changelog (e.g. dependabot, package indexers) can read the GitHub Releases API.

**Known gap**: `pyproject.toml [project.urls].Changelog` and `[tool.hatch.build.targets.sdist].include` still reference `CHANGELOG.md`. This is a small cleanup task — drop both — that hasn't been done yet.

### Why no coverage gate

**Choice**: `pytest --cov=dd_cli` runs by default and writes `coverage.xml`, but no threshold is enforced.

**Why**:
- The original project target was ≥85% (aspirational).
- The repo is at ~88% as of v2.0.
- A hard gate would block PRs on regression noise (e.g. a one-line bug fix that doesn't touch a hot path). codecov's patch check would help with this but adds another third-party dependency.

**If you want to enforce locally**: add `--cov-fail-under=85` to your invocation. If you want it in CI, either add it to `addopts` (project-wide) or wire `codecov.yml` (per-PR patch check).

## Operational

### Why nightly-smoke probes `/login`, not `/api/v2/users/`

**Choice**: the readiness probe in [.github/workflows/nightly-smoke.yml](../.github/workflows/nightly-smoke.yml) hits `http://localhost:8080/login` and accepts any 2xx.

**Why** (specific past failure, captured in PR #20 → PR #21):
- The initial probe hit `/api/v2/users/`. DefectDojo returns 403 Forbidden on that path for unauthenticated requests. `curl -sf` treats 403 as failure, so the wait loop never broke and the workflow timed out after 15 minutes.
- The second attempt hit `/login/` (with trailing slash). DefectDojo returned 404 for that path (Django route is `/login`, no trailing slash). Same timeout.
- The third (current) attempt hits `/login`. Returns 200 with the DefectDojo login page once uwsgi is serving.

**The general lesson**: don't pin readiness probes to specific upstream paths without checking that they return a useful status code on the version you're testing against. Generic "any HTTP response from uwsgi means it's alive" logic survives upstream route changes; specific path probes don't.

### Why nightly-smoke does bring-up + auth in one workflow step

**Choice**: the `Bring DefectDojo up and prepare credentials` step in `nightly-smoke.yml` does `docker compose up`, the readiness wait, the admin-password parse, and the API token mint in **one** shell block — not four separate workflow steps.

**Why**:
- Same shell context, so `ADMIN_PASS` stays as a local variable rather than round-tripping through `GITHUB_OUTPUT` (which would mask the value across steps).
- Fewer surface areas for state to drift between steps.
- The whole bring-up + auth flow lives in one readable block; the per-stage `::group::` markers keep the run UI collapsible.

**Trade-off**: a single failure in the block doesn't pinpoint which substep broke. The `::group::` markers + a per-step `echo` ("DefectDojo is live...", "Admin password parsed", "Token minted") mitigate this.

### Why `docker compose up -d` directly (not `dc-up.sh release`)

**Choice**: the nightly-smoke workflow runs `docker/setEnv.sh release && docker compose up -d`, not `./dc-up.sh release`.

**Why** (specific past failure, captured in PR #19):
- The initial workflow used DefectDojo's `dc-up.sh` helper script.
- DefectDojo upstream removed `dc-up.sh` / `dc-down.sh` from master.
- Workflow failed at the bring-up step with `./dc-up.sh: No such file or directory`.

The current command matches what DefectDojo's own `readme-docs/DOCKER.md` documents. If they break that too, the failure will be at the same step and the fix will be a quick find-and-replace.

## Documentation tooling

### Why `mkdocs-click` lives under `markdown_extensions:`, not `plugins:`

**Choice**: in `mkdocs.yml`, `- mkdocs-click` appears in the `markdown_extensions:` list, not under `plugins:`.

**Why** (specific past failure):
- An early version of `mkdocs.yml` had `plugins: [search, mkdocs-click]`.
- `mkdocs build --strict` failed with `ERROR - Config value 'plugins': The "mkdocs-click" plugin is not installed`.
- `mkdocs-click` is a markdown extension, not a plugin — the package ships a markdown preprocessor (`::: mkdocs-click ...`), not a mkdocs plugin entry point.

The fix is the position in the config file. Don't move it back.

### Why `click_app = typer.main.get_command(app)` is exported

**Choice**: `src/dd_cli/cli/app.py` ends with `click_app = typer.main.get_command(app)`.

**Why**:
- `mkdocs-click` requires a `click.Command`-like object to render the CLI reference.
- Typer's `app` is a `typer.Typer` instance, not a Click `Command`.
- `typer.main.get_command(app)` converts it. We export the result as a module attribute so `docs/cli-reference.md` can reference it via `:command: click_app`.

`click_app` is not used at runtime — only by `mkdocs-click` at docs-build time. Don't delete it.

## Lessons that apply broadly

A few patterns that come up often enough they're worth naming:

- **Check upstream availability before locking names.** The `defectdojo-cli` → `dd-cli` pivot was avoidable.
- **Probe specific upstream behavior, not specific paths.** The `/api/v2/users/` → `/login/` → `/login` parade was three iterations of the same anti-pattern.
- **Write down the legacy contract as tests, not docs.** The compat suite has caught regressions that doc-only enforcement would have missed.
- **Single source of truth for versions.** hatch-vcs over a manual `version = "..."` field has been net-positive — no forgotten bumps.
- **Tag from main, with a guard.** The v0.4.0 empty-changelog incident is the canonical example of how stale-branch tags fail silently.
- **Don't add a step to the release process without strong justification.** The maintainer is solo; release automation is the burnout-mitigation explicitly tracked in the risk register above.

## When you find a new gotcha

Add it here, with: the choice, the specific failure or constraint that motivated it, and (if available) the PR/commit that landed the fix. Keep entries terse — one paragraph plus a code or config snippet is usually enough. Future-you will thank you.
