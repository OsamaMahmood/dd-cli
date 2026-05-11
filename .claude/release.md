# Release

How `dd-cli` releases are cut and what to do when something goes wrong. Source of truth for the runbook is [RELEASING.md](../RELEASING.md); this doc adds the why behind the non-obvious parts and the failure-recovery procedures the runbook doesn't cover in depth.

## Mental model

**Releases are tag-driven.** Pushing any tag matching `v*` to GitHub triggers [`.github/workflows/release.yml`](../.github/workflows/release.yml), which does everything: builds artifacts, verifies the wheel, publishes to PyPI via OIDC, builds and pushes multi-arch Docker images to two registries, and creates the GitHub Release. No manual upload, no `twine` invocation, no Docker `push` from a maintainer's laptop.

Maintainer responsibilities:
1. Get `main` to the state you want to ship.
2. Pick a version per SemVer.
3. `git tag -a vX.Y.Z -m "vX.Y.Z" && git push origin vX.Y.Z`.
4. Watch the workflow run.

That's it.

## Versioning

Versions come from the latest git tag via [hatch-vcs](https://github.com/ofek/hatch-vcs). The build hook writes the resolved version to `src/dd_cli/_version.py` (gitignored, regenerated each build) and `dd_cli/__init__.py` re-exports it via `importlib.metadata`.

| Git state | Resolved version |
|---|---|
| At tag `v2.0.0` | `2.0.0` |
| 3 commits past `v2.0.0` | `2.0.1.dev3+g<sha>` |
| Dirty working tree past `v2.0.0` | `2.0.1.dev3+g<sha>.d<date>` |
| At tag `v2.0.0-rc.1` | `2.0.0rc1` (PEP 440 normalised) |

**Untagged builds are explicitly dev versions — never publish them.** The release workflow only fires on `v*` tag pushes; you can't publish a dev version even if you wanted to (no `pypi` environment trigger).

## The five things `release.yml` does

```
push tag v* → build-and-release ─┬─ publish-pypi
                                 └─ publish-docker
```

### 1. Tag-on-main guard

```yaml
- name: Verify tag points at a commit reachable from main
  run: |
    TAG_SHA=$(git rev-parse "$GITHUB_REF")
    if ! git merge-base --is-ancestor "$TAG_SHA" origin/main; then
      echo "::error::Tag $GITHUB_REF_NAME points at $TAG_SHA, which is not"
      echo "::error::an ancestor of origin/main. Re-tag from a fully-pulled"
      echo "::error::main checkout — see RELEASING.md."
      exit 1
    fi
```

**Why this exists**: v0.4.0 was once tagged on the tip of a feature branch instead of the merge commit on main. `gh release create --generate-notes` then couldn't find the PR (because the tag wasn't on the merge commit), so the release shipped with an empty changelog. The guard prevents the repeat.

If you see `Tag ... is not an ancestor of origin/main`: you tagged the wrong commit. Delete the tag locally and remotely, `git pull --ff-only origin main`, re-tag on `HEAD`, repush.

### 2. Wheel-version verify (PEP 440 normalised)

```yaml
- name: Verify wheel installs and `dd --version` matches the tag
  run: |
    /tmp/verify/bin/pip install dist/*.whl
    BUILT_VERSION=$(/tmp/verify/bin/dd --version | awk '{print $2}')
    TAG_VERSION="${GITHUB_REF_NAME#v}"
    NORMALIZED_TAG=$(/tmp/verify/bin/python -c "from packaging.version import Version; print(Version('$TAG_VERSION'))")
    if [ "$BUILT_VERSION" != "$NORMALIZED_TAG" ]; then
      echo "::error::Version mismatch — built wheel reports $BUILT_VERSION but tag normalizes to $NORMALIZED_TAG"
      exit 1
    fi
```

**Why this exists**: a prior release shipped wheels whose embedded version was `2.0.0rc1` but the tag was `v2.0.0-rc.1`. A literal string compare failed. PEP 440 canonicalises `v2.0.0-rc.1` → `2.0.0rc1` (hatch-vcs strips the `v` prefix and normalises the prerelease segment per PEP 440 § Public version identifiers). The fix uses `packaging.version.Version()` to canonicalise both sides before comparing.

**Implication for tagging**: prereleases must use `vX.Y.Z-rc.N` (note the `-rc.` infix). `vX.Y.Z-rcN` or `vX.Y.Z.rc1` will normalise differently and fail the check.

### 3. Prerelease / latest flag selection

```yaml
- name: Pick prerelease + latest flags from tag shape
  id: release_flags
  run: |
    if [[ "${GITHUB_REF_NAME}" == *-* ]]; then
      echo "flags=--prerelease --latest=false" >> "$GITHUB_OUTPUT"
    else
      echo "flags=--latest=true" >> "$GITHUB_OUTPUT"
    fi
```

Stable tags get `--latest=true` explicitly so GitHub doesn't fall back to the publishedAt-time heuristic. That heuristic once left v0.2.0 incorrectly tagged as "Latest" after a backfill of v0.1.0/v0.2.0 — they were published *after* v0.3.0 in wall-clock time, so the heuristic ranked them higher.

### 4. PyPI publish via OIDC trusted publisher

```yaml
publish-pypi:
  environment:
    name: pypi
    url: https://pypi.org/project/dd-cli/
  permissions:
    id-token: write   # required for OIDC token minting
  steps:
    - name: Publish to PyPI
      uses: pypa/gh-action-pypi-publish@release/v1
      with:
        packages-dir: dist/
        skip-existing: false
```

**No PyPI API token in the repo.** The `pypi` GitHub Actions environment is linked to the `dd-cli` PyPI project as a trusted publisher. PyPI is told to trust `OsamaMahmood/dd-cli` workflow + `pypi` environment specifically; the workflow mints a short-lived OIDC token at publish time.

`skip-existing: false` is deliberate — fail loudly if the version is already published, rather than silently skipping.

**One-time setup** (already done; documented in case it needs rebuilding):
1. In repo Settings → Environments → New environment → name `pypi`. Optional: restrict deployment branches to tags matching `v*`.
2. On PyPI: Account settings → Publishing → "Add a new pending publisher" with project name `dd-cli`, owner `OsamaMahmood`, repository `dd-cli`, workflow `release.yml`, environment `pypi`.
3. First successful tag-driven publish creates the project on PyPI; the pending publisher transitions to active.

### 5. Multi-arch Docker publish (GHCR + Docker Hub)

```yaml
publish-docker:
  environment:
    name: docker
    url: https://github.com/OsamaMahmood/dd-cli/pkgs/container/dd-cli
  permissions:
    packages: write
```

Builds `linux/amd64 + linux/arm64` via QEMU + Buildx, pushes to **both** registries:

- `ghcr.io/osamamahmood/dd-cli` (GitHub Container Registry; namespace mirrors GitHub handle)
- **`m4rkm3n/dd-cli`** (Docker Hub; namespace **differs** from the GitHub handle — see "Docker Hub namespace mismatch" below)

Tag aliases:

| Tag pushed | Image tags produced |
|---|---|
| `v2.0.0` (stable) | `2.0.0`, `2.0`, `2`, `latest` (in **both** registries) |
| `v2.0.0-rc.1` (prerelease) | `2.0.0-rc.1` only |

Note the asymmetry: stable tags get full SemVer aliases (`2`, `2.0`, `2.0.0`) so users can pin loosely (`ghcr.io/osamamahmood/dd-cli:2` floats with patches and minors). Prereleases get the exact tag only — a `:2` alias should always point at a stable release.

The build uses `cache-from`/`cache-to: type=gha` so arm64 builds stay reasonable across runs, and ships `provenance: true` + `sbom: true` for downstream vulnerability scanners.

**One-time setup**:
1. Repo secrets `DOCKERHUB_USERNAME` + `DOCKERHUB_TOKEN` (Docker Hub access token, **not** the account password).
2. Repo Settings → Environments → New environment `docker`, same tag-rule pattern as `pypi`.
3. GHCR needs no setup — the workflow uses the built-in `GITHUB_TOKEN` with `packages: write`.

## Docker Hub namespace mismatch

**`m4rkm3n/dd-cli` (Docker Hub) ≠ `osamamahmood/dd-cli` (GHCR).**

The maintainer's Docker Hub username is `m4rkm3n`; the GitHub handle is `osamamahmood`. The two were never linked. PR #16 fixed an early mistake where the workflow hardcoded `osamamahmood/dd-cli` on Docker Hub. **Don't try to "fix" the mismatch** — there is no `osamamahmood/dd-cli` repo on Docker Hub, and creating one would split user pulls across two namespaces.

This is documented in:
- The image-tag computation in `release.yml:170-195`.
- The README install section.
- [docs/install.md](../docs/install.md).
- [docs/recipes/github-actions.md](../docs/recipes/github-actions.md) + [docs/recipes/gitlab-ci.md](../docs/recipes/gitlab-ci.md).

## GitHub Actions allowlist

If the org/repo has an Actions allowlist (Settings → Actions → General), these third-party actions must be allowed:

```
pypa/gh-action-pypi-publish@*    # required for PyPI publish
docker/setup-qemu-action@*       # multi-arch builds
docker/setup-buildx-action@*     # multi-arch builds
docker/build-push-action@*       # multi-arch push
docker/login-action@*            # GHCR + Docker Hub login
```

`actions/upload-pages-artifact@*` and `actions/deploy-pages@*` are also needed by the docs workflow.

Early releases failed because `pypa/gh-action-pypi-publish` wasn't allowlisted; the docker actions failed similarly in the same era. If a new run fails with `Resource not accessible by integration` or similar, check the allowlist first.

## Cutting a release — full procedure

1. **Verify main is ready.**
   ```bash
   git checkout main && git pull --ff-only origin main
   gh run list --branch main --limit 5    # confirm CI green on the latest commits
   ```

2. **Pick the version.**
   - Stable: `v2.1.0`, `v2.1.1`.
   - Prerelease: `v2.1.0-rc.1`, `v2.1.0-rc.2`, `v2.1.0-beta.1`.
   - **Note the `-rc.N` infix** — `v2.1.0-rc1` (no dot) PEP-440-normalises differently and will fail the wheel-version check.

3. **Tag and push.**
   ```bash
   git tag -a v2.1.0 -m "v2.1.0"
   git push origin v2.1.0
   ```
   Annotated tag (`-a`) is required; the workflow's `git rev-parse "$GITHUB_REF"` resolves it to the right commit, but using `-a` also gives you the option to write release notes in the tag body.

4. **Watch the run.**
   ```bash
   gh run watch
   ```
   Or [Actions → Release](https://github.com/OsamaMahmood/dd-cli/actions/workflows/release.yml).

5. **Verify outputs.**
   - https://pypi.org/project/dd-cli/  → new version listed.
   - https://github.com/OsamaMahmood/dd-cli/releases → new release page with auto-generated notes + `SHA256SUMS` asset.
   - `docker pull ghcr.io/osamamahmood/dd-cli:2.1.0` → succeeds.
   - `docker pull m4rkm3n/dd-cli:2.1.0` → succeeds.
   - `pip install --upgrade dd-cli && dd --version` → reports the new version.

## Failure recovery

### Workflow failed midway

The job is idempotent up to the point of the side effect:
- `build-and-release` is fully re-runnable.
- `publish-pypi` is **not** re-runnable for the same version (PyPI rejects duplicate uploads); see "Bad version published" below.
- `publish-docker` is re-runnable (Docker registry tag push overwrites).

**Re-run the failed jobs only** from the Actions UI ("Re-run failed jobs"). If the failure was in `build-and-release` and the GitHub Release wasn't created, the re-run will create it.

### GitHub Release missing for an existing tag

```bash
# Build locally
python -m build --outdir dist/
shasum -a 256 dist/*.whl dist/*.tar.gz > dist/SHA256SUMS

gh release create v2.1.0 \
  --title v2.1.0 \
  --generate-notes \
  --latest=true \
  dist/*.whl dist/*.tar.gz dist/SHA256SUMS
```

For a prerelease, swap `--latest=true` with `--prerelease --latest=false`.

### Bad version published (need to undo)

PyPI does not allow re-uploading the same version. You can yank a release (marks it as "do not use", but it stays installable for users who pinned it):

```bash
# via the PyPI UI: project → manage → release → options → yank
```

Then publish `v2.1.1` with the fix. **Don't rewrite history or force-push tags** — pip caches and proxies will still serve the original wheel from caches.

For a bad GitHub Release (typo in notes, etc.):

```bash
gh release edit v2.1.0 --title "..." --notes "..."
```

To delete a bad release entirely (rare; for prereleases that should never have shipped):

```bash
gh release delete v2.1.0 --cleanup-tag --yes
```

`--cleanup-tag` also removes the tag, freeing the version for reuse. **Don't do this on a published-to-PyPI version** — the wheel is still on PyPI and you can't republish.

### Docker push failed mid-arch

Buildx pushes both arches before tagging; a partial failure usually means QEMU emulation timed out on arm64. Re-run the `publish-docker` job. If it fails twice in a row on the same arch, raise the timeout in `release.yml` or temporarily drop arm64 to ship the release, then fix the workflow in a follow-up.

### PyPI OIDC publish failed with "Resource not accessible by integration"

The `pypi` environment isn't wired correctly. Check:
- Repo Settings → Environments → `pypi` exists.
- PyPI project's trusted-publisher list includes `OsamaMahmood/dd-cli` / `release.yml` / `pypi`.
- `permissions: id-token: write` is set on the `publish-pypi` job.

### "skip-existing: false" failed because version already exists

Someone (probably a prior run) already published this version. **Don't reset `skip-existing` to true** — that hides real conflicts. Bump the patch version (`v2.1.1`) and re-tag.

## What the release workflow does NOT do

- **Homebrew formula bump** — deferred post-v2.0. pip/pipx is the recommended developer install. Adding a Homebrew tap would mean per-release resource-list generation and a separate repo to maintain; the trade-off was judged not worth it for the install volume (PLAN.md §14).
- **cosign signing** of the published artifacts — deferred.
- **`dd-import` shim package** publish — deferred. The legacy console scripts ship inside `dd-cli` itself, so existing `dd-import` users `pip install dd-cli` instead of `pip install dd-import==<shim-version>`.
- **CHANGELOG.md update** — there is no `CHANGELOG.md` file. The GitHub Release's auto-generated notes (`--generate-notes`) replace it. The `pyproject.toml [project.urls].Changelog` URL still points at a missing file in the repo; this is a known cleanup-task gap.

## When you need to do something this runbook doesn't cover

Cross-reference [RELEASING.md](../RELEASING.md) (the maintainer-facing runbook) and `release.yml` itself. Both are short. If you find yourself doing something not documented in either, add it here.
