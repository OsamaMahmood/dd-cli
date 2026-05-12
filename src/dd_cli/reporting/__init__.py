"""Report generation for DefectDojo products.

Public surface:

- :func:`build_context` — fetch results → renderer-ready context dict
- :func:`render_markdown` — context dict → Markdown string

The package is pure Python (Jinja2 + the `markdown` lib). No native deps.
PDF output is deliberately out of scope; users render the Markdown via
their tool of choice (browser print, `pandoc`, etc.).
"""

from dd_cli.reporting.context import build_context
from dd_cli.reporting.render import render_markdown

__all__ = ["build_context", "render_markdown"]
