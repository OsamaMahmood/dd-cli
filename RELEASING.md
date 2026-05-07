# Releasing dd-cli

dd-cli releases are **tag-driven**. Pushing any tag matching `v*` to GitHub
triggers [`.github/workflows/release.yml`](.github/workflows/release.yml),
which builds sdist + wheel, verifies the version, generates `SHA256SUMS`,
and creates a GitHub Release with auto-generated notes from merged PRs
since the previous tag.

## Versioning

Versions come from the latest git tag via [`hatch-vcs`](https://github.com/ofek/hatch-vcs).

| Git state | Resolved version |
|---|---|
| At tag `v0.3.0` | `0.3.0` |
| 3 commits past `v0.3.0` | `0.3.1.dev3+g<sha>` |
| Dirty working tree past `v0.3.0` | `0.3.1.dev3+g<sha>.d<date>` |

Untagged builds are explicitly **dev versions** — never publish them.

## Cutting a release

1. **Make sure `main` is what you want to ship.** All intended PRs are merged,
   CI is green.

   ```bash
   git checkout main
   git pull --ff-only
   ```

2. **Pick the next version number** following [SemVer](https://semver.org/).
   Examples: `v0.3.0`, `v0.3.1`, `v1.0.0`. Prereleases use a hyphen:
   `v0.3.0-rc.1`, `v1.0.0-beta.2` (the workflow auto-detects these via
   the `-` and marks the GitHub Release as a prerelease).

3. **Tag and push:**

   ```bash
   git tag -a v0.3.0 -m "v0.3.0"
   git push origin v0.3.0
   ```

4. **Watch the workflow** at [Actions → Release](https://github.com/OsamaMahmood/dd-cli/actions/workflows/release.yml).
   It will:
   - build sdist + wheel via `python -m build`
   - install the wheel into a fresh venv and assert `dd --version` matches the tag
   - generate `SHA256SUMS`
   - create the GitHub Release with auto-generated notes and attached artifacts

5. **Verify the release page** at [Releases](https://github.com/OsamaMahmood/dd-cli/releases).
   Edit the auto-generated notes if they need polishing.

## Manual trigger / fixing a bad release

If a release fails partway, you can re-run the workflow from the Actions
tab. If a tag was published but no Release page exists, run locally:

```bash
gh release create v0.3.0 \
  --title v0.3.0 \
  --generate-notes \
  dist/*.whl dist/*.tar.gz dist/SHA256SUMS
```

To **delete** a bad release (rare), use the GitHub UI or:

```bash
gh release delete v0.3.0 --cleanup-tag --yes
```

`--cleanup-tag` also removes the tag, freeing the version number for reuse.

## PyPI publish

Tag pushes also publish the wheel + sdist to PyPI as
[`dd-cli`](https://pypi.org/project/dd-cli/) via the
[`publish-pypi`](.github/workflows/release.yml) job. No long-lived API
token is stored in the repo — the job uses GitHub's OIDC trusted-publisher
mechanism: PyPI is configured to trust this specific
`OsamaMahmood/dd-cli` workflow + `pypi` GitHub Actions environment.

### One-time setup

These are already done for the `dd-cli` project; documented here so the
process is reproducible if the trust relationship needs to be rebuilt.

1. Create the `pypi` environment in this repo:
   **Settings → Environments → New environment** → name `pypi`. Optional
   but recommended: under "Deployment branches", restrict to "Selected
   branches and tags" → add a tag rule `v*`.
2. On PyPI, sign in and visit
   **[Account settings → Publishing](https://pypi.org/manage/account/publishing/)** →
   "Add a new pending publisher" with:
   - PyPI project name: `dd-cli`
   - Owner: `OsamaMahmood`
   - Repository name: `dd-cli`
   - Workflow name: `release.yml`
   - Environment name: `pypi`
3. The first successful tag-driven workflow run creates the `dd-cli`
   project on PyPI (the publisher transitions from "pending" to active).

## Docker publish

Tag pushes also build and push a multi-arch (linux/amd64 + linux/arm64)
container image to two registries via the
[`publish-docker`](.github/workflows/release.yml) job:

- `ghcr.io/osamamahmood/dd-cli` (GitHub Container Registry)
- `m4rkm3n/dd-cli` (Docker Hub — namespace differs from GitHub handle)

Tag aliases follow standard semver convention:

| Tag pushed | Image tags produced |
|---|---|
| `v1.2.3` (stable) | `1.2.3`, `1.2`, `1`, `latest` |
| `v2.0.0-rc.1` (prerelease) | `2.0.0-rc.1` only |

### One-time setup

Already done for this repo; documented for reproducibility.

1. **Docker Hub credentials.** On Docker Hub, create an access token at
   [Account Settings → Security](https://hub.docker.com/settings/security).
   In this repo, add two secrets at **Settings → Secrets and variables →
   Actions**:
   - `DOCKERHUB_USERNAME` — Docker Hub username
   - `DOCKERHUB_TOKEN` — the access token (NOT the account password)

2. **`docker` GitHub Actions environment.** Same as `pypi`: create at
   **Settings → Environments → New environment** named `docker`, with
   the same `v*` tag deployment-branch rule.

3. **GHCR.** No setup needed — the workflow uses the built-in
   `GITHUB_TOKEN` with `packages: write` permission. The first
   successful push creates the package under your GitHub user/org.

### Allowlist additions required

The Docker publish step uses these third-party actions (all official
PyPA / Docker / GitHub-published). Add to your Actions allowlist at
[**Settings → Actions → General**](https://github.com/settings/actions):

```
docker/setup-qemu-action@*
docker/setup-buildx-action@*
docker/build-push-action@*
```

(`docker/login-action@*` is already allowlisted.)

## What the workflow does NOT do yet

- **Homebrew formula bump** PR to `OsamaMahmood/homebrew-tap` —
  deferred post-v2.0; most users will reach for `pip` or `pipx`
  rather than `brew install`, and per-release resource-list
  generation is a real maintenance cost
- **cosign** signing of the published artifacts

## Backfilling a release for an existing tag

`v0.1.0` and `v0.2.0` were tagged before this workflow existed. To create a
GitHub Release page for either of them after the fact, run the workflow
manually after the next push, or use:

```bash
gh release create v0.2.0 --title v0.2.0 --generate-notes
```

(no artifacts — those tags predate the build pipeline).
