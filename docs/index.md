# dd-cli

A production-grade CLI for managing [DefectDojo](https://www.defectdojo.org/) — list / create / update / delete every resource the API exposes, plus a fully backward-compatible import path for users coming from the original [`dd-import`](https://github.com/MaibornWolff/dd-import) tool (now archived).

```bash
pip install dd-cli
```

## Why dd-cli

- **Complete API coverage.** Every read and write across 12 DefectDojo resource types — products, product-types, engagements, tests, findings, users, dojo-groups, jira-instances, risk-acceptances, metadata, endpoints, finding-templates — driven from a typed client generated from DefectDojo's OpenAPI spec.
- **Drop-in replacement for `dd-import`.** Existing CI pipelines that invoke `dd-reimport-findings` or `dd-import-languages` with `DD_*` env vars keep working unchanged. The legacy console scripts are wired as thin shims over the new workflow code.
- **Pleasant interactive use.** Rich tables, JSON / YAML output for piping, profiles for switching between DefectDojo instances, `dd configure` interactive setup, `dd <resource> edit <id>` opens the resource as YAML in `$EDITOR`, action verbs like `dd findings close`, `risk-accept`, `dd engagements close/reopen`, `dd users deactivate`.
- **Safe writes.** `--dry-run` previews every mutation without sending HTTP. `--yes`/`-y` skips the destructive-op confirmation prompt for scripts. Typed exit codes (auth=3, not-found=5, etc.) so CI can branch on what went wrong.
- **Validated against real DefectDojo.** 24 integration tests run against a live DefectDojo instance per release, including a full Trivy-report import round-trip with finding-count assertions.

## Where to next

- [Install](install.md) — PyPI, Docker, source
- [Quickstart](quickstart.md) — first session: `configure`, `ping`, list, manage, import
- [Configuration](configuration.md) — TOML profiles, env-var precedence, exit codes
- [Importing findings](importing-findings.md) — both modes, scanner-specific tips
- [Migration from dd-import](migration.md) — drop-in replacement details
- [CLI reference](cli-reference.md) — every command, every flag
- [CI recipes](recipes/github-actions.md) — copy-paste pipelines

## Status

dd-cli is **v2.0** — feature-complete, shipped 2026-05-07. Maintained by [Osama Mahmood](https://github.com/OsamaMahmood) under the BSD 3-Clause license, the same as the upstream `dd-import` project it succeeds.
