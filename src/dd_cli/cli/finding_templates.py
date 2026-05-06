"""`dd finding-templates` — list and get DefectDojo finding templates."""

from __future__ import annotations

from typing import Annotated

import typer

from dd_cli.cli._resource import (
    DEFAULT_LIMIT,
    ResourceSpec,
    get_dispatch,
    list_resource,
    register_crud,
)
from dd_cli.errors import ValidationError
from dd_cli.output import OutputFormat

FINDING_TEMPLATES_SPEC = ResourceSpec(
    name="finding template",
    plural="finding templates",
    path="/api/v2/finding_templates/",
    columns=("id", "title", "severity", "cwe", "tags"),
    name_field="title",
)


VALID_SEVERITIES = {"Critical", "High", "Medium", "Low", "Info"}


finding_templates_app = typer.Typer(
    name="finding-templates",
    help="List and get DefectDojo finding templates.",
    no_args_is_help=True,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@finding_templates_app.command("list")
def finding_templates_list(
    ctx: typer.Context,
    title: Annotated[str | None, typer.Option("--title", help="Filter by exact title.")] = None,
    severity: Annotated[
        str | None,
        typer.Option(
            "--severity",
            help=f"Filter by severity. One of: {', '.join(sorted(VALID_SEVERITIES))}.",
        ),
    ] = None,
    cwe: Annotated[int | None, typer.Option("--cwe", help="Filter by CWE number.")] = None,
    tag: Annotated[str | None, typer.Option("--tag", help="Filter by tag (exact match).")] = None,
    limit: Annotated[
        int, typer.Option("--limit", help=f"Maximum rows. Default: {DEFAULT_LIMIT}.")
    ] = DEFAULT_LIMIT,
    all_pages: Annotated[bool, typer.Option("--all", help="Stream every page.")] = False,
    output: Annotated[
        OutputFormat | None,
        typer.Option("--output", "-o", help="Output format."),
    ] = None,
) -> None:
    """List finding templates with optional filters."""
    canonical_severity = _canonicalise_severity(severity)
    list_resource(
        ctx,
        FINDING_TEMPLATES_SPEC,
        filters={
            "title": title,
            "severity": canonical_severity,
            "cwe": cwe,
            "tag": tag,
        },
        limit=limit,
        all_pages=all_pages,
        output=output,
    )


@finding_templates_app.command("get")
def finding_templates_get(
    ctx: typer.Context,
    template_id: Annotated[
        int | None,
        typer.Argument(help="Template ID (omit if using --name)."),
    ] = None,
    name: Annotated[
        str | None,
        typer.Option("--name", help="Resolve by exact template title."),
    ] = None,
    output: Annotated[
        OutputFormat | None,
        typer.Option("--output", "-o", help="Output format."),
    ] = None,
) -> None:
    """Get a single finding template by ID or title."""
    get_dispatch(
        ctx,
        FINDING_TEMPLATES_SPEC,
        resource_id=template_id,
        name=name,
        output=output,
    )


def _canonicalise_severity(value: str | None) -> str | None:
    if value is None:
        return None
    by_lower = {s.lower(): s for s in VALID_SEVERITIES}
    canonical = by_lower.get(value.lower())
    if canonical is None:
        raise ValidationError(
            f"Unknown severity {value!r}. Expected one of {sorted(VALID_SEVERITIES)}.",
        )
    return canonical


register_crud(finding_templates_app, FINDING_TEMPLATES_SPEC)
