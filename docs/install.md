# Install

## From PyPI (recommended)

=== "pip"

    ```bash
    pip install dd-cli
    ```

=== "pipx (isolated)"

    ```bash
    pipx install dd-cli
    ```

=== "uv"

    ```bash
    uv tool install dd-cli
    ```

After install, three commands go on `PATH`:

| Command | Purpose |
|---|---|
| `dd` | Modern CLI — every DefectDojo resource, action verbs, `--dry-run`, profiles |
| `dd-reimport-findings` | Legacy console-script shim for `dd-import` users — env-var driven |
| `dd-import-languages` | Same, for `cloc` JSON uploads |

Verify:

```bash
dd --version
# dd 2.0.0
```

## Docker

=== "GitHub Container Registry"

    ```bash
    podman pull ghcr.io/osamamahmood/dd-cli:latest
    podman pull ghcr.io/osamamahmood/dd-cli:2.0.0
    ```

=== "Docker Hub"

    ```bash
    podman pull m4rkm3n/dd-cli:latest
    podman pull m4rkm3n/dd-cli:2.0.0
    ```

The image is multi-arch (`linux/amd64` + `linux/arm64`) and runs as a non-root user. Tag aliases follow standard semver:

| Tag pushed | Image tags produced |
|---|---|
| `v1.2.3` (stable) | `1.2.3`, `1.2`, `1`, `latest` |
| `v2.0.0-rc.1` (prerelease) | `2.0.0-rc.1` only |

Quick run:

```bash
podman run --rm \
  -e DD_URL=https://defectdojo.example.com \
  -e DD_API_KEY=… \
  ghcr.io/osamamahmood/dd-cli:latest \
  ping
```

Mount a directory for scanner output uploads:

```bash
podman run --rm \
  -v $(pwd)/reports:/work \
  -e DD_URL=… -e DD_API_KEY=… \
  ghcr.io/osamamahmood/dd-cli:latest \
  import findings \
    --file /work/trivy.json \
    --scanner "Trivy Scan" \
    --product-type "Web Apps" \
    --product "Payments" \
    --auto-create --yes
```

## From source

```bash
git clone https://github.com/OsamaMahmood/dd-cli.git
cd dd-cli
pip install -e ".[dev,test]"
```

For [contributing](contributing.md), this is the path that gives you `make test`, `make lint`, `make typecheck`, `make smoke`, and `make generate-client`.

## Shell completion

Typer ships completion for bash / zsh / fish. Install once:

```bash
dd --install-completion
```

Or print the script to inspect:

```bash
dd --show-completion
```

## Supported Python versions

| Python | Status |
|---|---|
| 3.11 | ✅ tested in CI |
| 3.12 | ✅ tested in CI |
| 3.13 | ✅ tested in CI |
| ≤ 3.10 | not supported (uses `StrEnum`, `Self`, modern union syntax) |
