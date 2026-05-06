"""`dd dojo-groups` — list and get DefectDojo authorization groups."""

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
from dd_cli.output import OutputFormat

DOJO_GROUPS_SPEC = ResourceSpec(
    name="dojo group",
    plural="dojo groups",
    path="/api/v2/dojo_groups/",
    columns=("id", "name", "description", "social_provider"),
)


dojo_groups_app = typer.Typer(
    name="dojo-groups",
    help="List and get DefectDojo authorization groups.",
    no_args_is_help=True,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@dojo_groups_app.command("list")
def dojo_groups_list(
    ctx: typer.Context,
    name: Annotated[str | None, typer.Option("--name", help="Filter by exact name.")] = None,
    social_provider: Annotated[
        str | None,
        typer.Option(
            "--social-provider",
            help="Filter by social-auth provider (e.g. 'AzureAD', 'Google').",
        ),
    ] = None,
    limit: Annotated[
        int, typer.Option("--limit", help=f"Maximum rows. Default: {DEFAULT_LIMIT}.")
    ] = DEFAULT_LIMIT,
    all_pages: Annotated[bool, typer.Option("--all", help="Stream every page.")] = False,
    output: Annotated[
        OutputFormat | None,
        typer.Option("--output", "-o", help="Output format."),
    ] = None,
) -> None:
    """List dojo groups."""
    list_resource(
        ctx,
        DOJO_GROUPS_SPEC,
        filters={"name": name, "social_provider": social_provider},
        limit=limit,
        all_pages=all_pages,
        output=output,
    )


@dojo_groups_app.command("get")
def dojo_groups_get(
    ctx: typer.Context,
    group_id: Annotated[
        int | None,
        typer.Argument(help="Group ID (omit if using --name)."),
    ] = None,
    name: Annotated[
        str | None,
        typer.Option("--name", help="Resolve by exact group name."),
    ] = None,
    output: Annotated[
        OutputFormat | None,
        typer.Option("--output", "-o", help="Output format."),
    ] = None,
) -> None:
    """Get a single dojo group by ID or name."""
    get_dispatch(ctx, DOJO_GROUPS_SPEC, resource_id=group_id, name=name, output=output)


register_crud(dojo_groups_app, DOJO_GROUPS_SPEC)
