"""Output rendering for `dd` commands.

`render(data, fmt)` is the only entry point most callers need. It dispatches
to the right renderer based on the `OutputFormat` global option set on the
Typer context.
"""

from dd_cli.output.base import OutputFormat, Renderer, render

__all__ = ["OutputFormat", "Renderer", "render"]
