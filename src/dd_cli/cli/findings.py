"""`dd findings` — list and get DefectDojo findings."""

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

FINDINGS_SPEC = ResourceSpec(
    name="finding",
    plural="findings",
    path="/api/v2/findings/",
    columns=("id", "title", "severity", "active", "verified", "found_by"),
    name_field="title",
)


VALID_SEVERITIES = {"Critical", "High", "Medium", "Low", "Info"}


findings_app = typer.Typer(
    name="findings",
    help="List and get DefectDojo findings.",
    no_args_is_help=True,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@findings_app.command("list")
def findings_list(
    ctx: typer.Context,
    title: Annotated[
        str | None,
        typer.Option("--title", help="Filter by exact finding title."),
    ] = None,
    product: Annotated[
        int | None,
        typer.Option("--product", help="Filter by product ID."),
    ] = None,
    engagement: Annotated[
        int | None,
        typer.Option("--engagement", help="Filter by engagement ID."),
    ] = None,
    test: Annotated[int | None, typer.Option("--test", help="Filter by test ID.")] = None,
    severity: Annotated[
        str | None,
        typer.Option(
            "--severity",
            help=f"Filter by severity. One of: {', '.join(sorted(VALID_SEVERITIES))}.",
        ),
    ] = None,
    active: Annotated[
        bool | None,
        typer.Option(
            "--active/--inactive",
            help="Filter by active flag.",
        ),
    ] = None,
    verified: Annotated[
        bool | None,
        typer.Option(
            "--verified/--unverified",
            help="Filter by verified flag.",
        ),
    ] = None,
    duplicate: Annotated[
        bool | None,
        typer.Option(
            "--duplicate/--non-duplicate",
            help="Filter by duplicate flag.",
        ),
    ] = None,
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
    """List findings with optional filters.

    Severity is case-insensitive on input but normalised to DefectDojo's
    canonical capitalisation (`Critical`, `High`, …) before the API call.
    """
    canonical_severity = _canonicalise_severity(severity)

    list_resource(
        ctx,
        FINDINGS_SPEC,
        filters={
            "title": title,
            "product": product,
            "test__engagement__product": product,
            "test__engagement": engagement,
            "test": test,
            "severity": canonical_severity,
            "active": active,
            "verified": verified,
            "duplicate": duplicate,
            "tag": tag,
        },
        limit=limit,
        all_pages=all_pages,
        output=output,
    )


@findings_app.command("get")
def findings_get(
    ctx: typer.Context,
    finding_id: Annotated[
        int | None,
        typer.Argument(help="Finding ID (omit if using --name)."),
    ] = None,
    name: Annotated[
        str | None,
        typer.Option("--name", help="Resolve by exact finding title."),
    ] = None,
    output: Annotated[
        OutputFormat | None,
        typer.Option("--output", "-o", help="Output format."),
    ] = None,
) -> None:
    """Get a single finding by ID or title."""
    get_dispatch(ctx, FINDINGS_SPEC, resource_id=finding_id, name=name, output=output)


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


register_crud(findings_app, FINDINGS_SPEC)
