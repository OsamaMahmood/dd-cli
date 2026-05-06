"""`dd engagements` — list, get, CRUD, plus close / reopen verbs."""

from __future__ import annotations

from typing import Annotated

import typer

from dd_cli.cli._resource import (
    DEFAULT_LIMIT,
    ResourceSpec,
    confirm_or_abort,
    get_active_profile,
    get_dispatch,
    list_resource,
    print_dry_run,
    register_crud,
    render_response,
)
from dd_cli.client import DefectDojoClient
from dd_cli.output import OutputFormat

ENGAGEMENTS_SPEC = ResourceSpec(
    name="engagement",
    plural="engagements",
    path="/api/v2/engagements/",
    columns=("id", "name", "product", "target_start", "target_end", "status"),
)


engagements_app = typer.Typer(
    name="engagements",
    help="List and get DefectDojo engagements.",
    no_args_is_help=True,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@engagements_app.command("list")
def engagements_list(
    ctx: typer.Context,
    name: Annotated[str | None, typer.Option("--name", help="Filter by exact name.")] = None,
    product: Annotated[int | None, typer.Option("--product", help="Filter by product ID.")] = None,
    status: Annotated[
        str | None,
        typer.Option(
            "--status",
            help="Filter by status (e.g. 'In Progress', 'Completed', 'Not Started').",
        ),
    ] = None,
    target_start: Annotated[
        str | None,
        typer.Option("--target-start", help="Filter by target_start (YYYY-MM-DD)."),
    ] = None,
    target_end: Annotated[
        str | None,
        typer.Option("--target-end", help="Filter by target_end (YYYY-MM-DD)."),
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
    """List engagements with optional filters."""
    list_resource(
        ctx,
        ENGAGEMENTS_SPEC,
        filters={
            "name": name,
            "product": product,
            "status": status,
            "target_start": target_start,
            "target_end": target_end,
            "tag": tag,
        },
        limit=limit,
        all_pages=all_pages,
        output=output,
    )


@engagements_app.command("get")
def engagements_get(
    ctx: typer.Context,
    engagement_id: Annotated[
        int | None,
        typer.Argument(help="Engagement ID (omit if using --name)."),
    ] = None,
    name: Annotated[
        str | None,
        typer.Option("--name", help="Resolve by exact engagement name."),
    ] = None,
    output: Annotated[
        OutputFormat | None,
        typer.Option("--output", "-o", help="Output format."),
    ] = None,
) -> None:
    """Get a single engagement by ID or name."""
    get_dispatch(ctx, ENGAGEMENTS_SPEC, resource_id=engagement_id, name=name, output=output)


register_crud(engagements_app, ENGAGEMENTS_SPEC)


# ---------------------------- action verbs ------------------------------ #


@engagements_app.command("close")
def engagements_close(
    ctx: typer.Context,
    engagement_id: Annotated[int, typer.Argument(help="Engagement ID.")],
    yes: Annotated[bool, typer.Option("--yes", "-y", help="Skip confirmation.")] = False,
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Print intent only.")] = False,
    output: Annotated[
        OutputFormat | None, typer.Option("--output", "-o", help="Output format.")
    ] = None,
) -> None:
    """Close an engagement via DefectDojo's dedicated /close/ endpoint."""
    target = f"/api/v2/engagements/{engagement_id}/close/"
    if dry_run:
        print_dry_run("POST", target, {}, ctx, output)
        return
    confirm_or_abort(f"Close engagement {engagement_id}?", yes=yes)
    profile = get_active_profile(ctx)
    with DefectDojoClient(profile) as client:
        body = client.post(target, json={})
    typer.echo(f"Closed engagement {engagement_id}.")
    render_response(body, ctx, output)


@engagements_app.command("reopen")
def engagements_reopen(
    ctx: typer.Context,
    engagement_id: Annotated[int, typer.Argument(help="Engagement ID.")],
    yes: Annotated[bool, typer.Option("--yes", "-y", help="Skip confirmation.")] = False,
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Print intent only.")] = False,
    output: Annotated[
        OutputFormat | None, typer.Option("--output", "-o", help="Output format.")
    ] = None,
) -> None:
    """Reopen a closed engagement via DefectDojo's dedicated /reopen/ endpoint."""
    target = f"/api/v2/engagements/{engagement_id}/reopen/"
    if dry_run:
        print_dry_run("POST", target, {}, ctx, output)
        return
    confirm_or_abort(f"Reopen engagement {engagement_id}?", yes=yes)
    profile = get_active_profile(ctx)
    with DefectDojoClient(profile) as client:
        body = client.post(target, json={})
    typer.echo(f"Reopened engagement {engagement_id}.")
    render_response(body, ctx, output)
