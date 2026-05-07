"""Console-script shims for backwards compatibility with the original ``dd-import``.

`dd-reimport-findings` and `dd-import-languages` entry points are wired
to these functions in ``pyproject.toml [project.scripts]``. Their
contract matches the legacy tool exactly:

- All configuration comes from ``DD_*`` environment variables (the
  ``ImportFindingsOptions`` / ``ImportLanguagesOptions`` validation
  aliases shipped in M4a wire these through cleanly).
- Print human progress lines to stdout, errors to stderr.
- Exit 0 on success, 1 on **any** failure — irrespective of the typed
  exit codes the new ``dd import findings`` command uses. CI pipelines
  already in production rely on the exit-1 contract; preserve it.

For new users we recommend ``dd import findings`` / ``dd import
languages`` (typed exit codes, dry-run, profile support). These shims
exist to keep existing pipelines working unchanged through the
``dd-import`` → ``defectdojo-cli`` migration.
"""

from __future__ import annotations

import sys
from typing import NoReturn

from dd_cli.client import DefectDojoClient
from dd_cli.config import load_profile
from dd_cli.errors import ConfigError, DDCliError
from dd_cli.workflows.import_findings import (
    ImportFindingsOptions,
    ImportFindingsWorkflow,
)
from dd_cli.workflows.import_languages import (
    ImportLanguagesOptions,
    ImportLanguagesWorkflow,
)


def dd_reimport_findings_main() -> NoReturn:
    """Entry point for the legacy ``dd-reimport-findings`` console script."""
    try:
        opts = ImportFindingsOptions()
        profile = load_profile()
        if not profile.is_complete():
            raise ConfigError(
                "Profile is missing url and/or api_key.",
                hint="Set DD_URL and DD_API_KEY environment variables.",
            )

        if opts.auto_create_context:
            print("🚀 Using AUTO-CREATE workflow (single API call)")
            print("   DefectDojo will create all resources automatically...")
        else:
            print("📋 Using TRADITIONAL workflow (multiple API calls)")
            print("   Creating/finding resources step by step...")

        with DefectDojoClient(profile) as client:
            ImportFindingsWorkflow(client, opts).run()

        print("✅ Import completed successfully!")
        sys.exit(0)

    except DDCliError as exc:
        _print_legacy_error(exc.message, hint=exc.hint)
        sys.exit(1)
    except Exception as exc:
        _print_legacy_error(str(exc))
        sys.exit(1)


def dd_import_languages_main() -> NoReturn:
    """Entry point for the legacy ``dd-import-languages`` console script."""
    try:
        opts = ImportLanguagesOptions()
        profile = load_profile()
        if not profile.is_complete():
            raise ConfigError(
                "Profile is missing url and/or api_key.",
                hint="Set DD_URL and DD_API_KEY environment variables.",
            )
        with DefectDojoClient(profile) as client:
            ImportLanguagesWorkflow(client, opts).run()
        print("✅ Languages imported")
        sys.exit(0)

    except DDCliError as exc:
        _print_legacy_error(exc.message, hint=exc.hint)
        sys.exit(1)
    except Exception as exc:
        _print_legacy_error(str(exc))
        sys.exit(1)


def _print_legacy_error(message: str, *, hint: str | None = None) -> None:
    """Emit a legacy-style error line to stderr."""
    print(f"❌ Error during import: {message}", file=sys.stderr)
    if hint:
        print(f"   Hint: {hint}", file=sys.stderr)
