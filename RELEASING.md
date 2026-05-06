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

## What the workflow does NOT do (yet)

These land in M5 per [`PLAN.md`](PLAN.md) §8:

- **PyPI publish** via OIDC trusted publisher
- **Docker images** to `ghcr.io` and Docker Hub
- **Homebrew formula bump** PR to `OsamaMahmood/homebrew-tap`
- **SBOM** generation, **cosign** signing

The current workflow is structured so adding these is additive — new jobs
that depend on `build-and-release`, not a rewrite.

## Backfilling a release for an existing tag

`v0.1.0` and `v0.2.0` were tagged before this workflow existed. To create a
GitHub Release page for either of them after the fact, run the workflow
manually after the next push, or use:

```bash
gh release create v0.2.0 --title v0.2.0 --generate-notes
```

(no artifacts — those tags predate the build pipeline).
