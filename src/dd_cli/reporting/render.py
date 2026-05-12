"""Jinja2 renderers for the report context.

Templates ship inside the package at ``reporting/templates/``. PDF is
intentionally not implemented — users render the Markdown or HTML to PDF
with their tool of choice (`pandoc`, browser-print to PDF, etc.). See
``docs/reporting.md``.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import markdown as md_lib
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup

TEMPLATE_DIR = Path(__file__).parent / "templates"

# Module-level Markdown converter — Jinja templates call this via the
# `| md` filter to render description / mitigation fields. `.reset()` is
# called per invocation so converter state doesn't leak across findings.
_MD = md_lib.Markdown(
    extensions=["extra", "sane_lists", "nl2br"],
    output_format="html",
)


def _md_filter(text: str | None) -> Markup:
    if not text:
        return Markup("")
    _MD.reset()
    return Markup(_MD.convert(str(text)))


def _fmt_date(value: str | None) -> str:
    """Strip the time portion off an ISO datetime; render `—` for empty."""
    if not value:
        return "—"
    return str(value).split("T")[0]


def _env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["fmt_date"] = _fmt_date
    env.filters["md"] = _md_filter
    return env


def render_markdown(context: dict[str, Any]) -> str:
    """Render the report context as Markdown."""
    return _env().get_template("report.md.j2").render(**context)


def render_html(context: dict[str, Any]) -> str:
    """Render the report context as a self-contained HTML document.

    The template inlines its own CSS so the file is portable — open it
    in any browser, ⌘P → Save as PDF for a polished PDF without any
    extra tooling.
    """
    return _env().get_template("report.html.j2").render(**context)
