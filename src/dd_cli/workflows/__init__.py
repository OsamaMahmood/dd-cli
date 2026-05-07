"""Composable workflows for dd-cli.

Workflows orchestrate multi-step DefectDojo operations on top of the
generic CRUD primitives in `dd_cli.client`. They live in this package
so they can be exercised either via the CLI (`dd import findings`) or
via the legacy console-script shims (`dd-reimport-findings`) that pass
the same `DD_*` env vars the original `dd-import` tool uses.

Two workflows ship today:
- `import_findings` — re-imports scanner output into DefectDojo, in
  either traditional (find-or-create per resource, then upload) or
  auto-create (single API call, DefectDojo creates resources) modes.
- `import_languages` — uploads `cloc` JSON output for a product.
"""

from dd_cli.workflows.import_findings import (
    ImportFindingsOptions,
    ImportFindingsWorkflow,
)
from dd_cli.workflows.import_languages import (
    ImportLanguagesOptions,
    ImportLanguagesWorkflow,
)

__all__ = [
    "ImportFindingsOptions",
    "ImportFindingsWorkflow",
    "ImportLanguagesOptions",
    "ImportLanguagesWorkflow",
]
