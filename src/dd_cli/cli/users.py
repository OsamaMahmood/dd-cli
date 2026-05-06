"""`dd users` — list and get DefectDojo users."""

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

USERS_SPEC = ResourceSpec(
    name="user",
    plural="users",
    path="/api/v2/users/",
    columns=("id", "username", "first_name", "last_name", "email", "is_active"),
    name_field="username",
)


users_app = typer.Typer(
    name="users",
    help="List and get DefectDojo users.",
    no_args_is_help=True,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@users_app.command("list")
def users_list(
    ctx: typer.Context,
    username: Annotated[
        str | None,
        typer.Option("--username", help="Filter by exact username."),
    ] = None,
    first_name: Annotated[
        str | None, typer.Option("--first-name", help="Filter by first name.")
    ] = None,
    last_name: Annotated[
        str | None, typer.Option("--last-name", help="Filter by last name.")
    ] = None,
    is_active: Annotated[
        bool | None,
        typer.Option(
            "--active/--inactive",
            help="Filter by active flag.",
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
    """List users with optional filters."""
    list_resource(
        ctx,
        USERS_SPEC,
        filters={
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "is_active": is_active,
        },
        limit=limit,
        all_pages=all_pages,
        output=output,
    )


@users_app.command("get")
def users_get(
    ctx: typer.Context,
    user_id: Annotated[
        int | None,
        typer.Argument(help="User ID (omit if using --name)."),
    ] = None,
    name: Annotated[
        str | None,
        typer.Option("--name", help="Resolve by exact username."),
    ] = None,
    output: Annotated[
        OutputFormat | None,
        typer.Option("--output", "-o", help="Output format."),
    ] = None,
) -> None:
    """Get a single user by ID or username."""
    get_dispatch(ctx, USERS_SPEC, resource_id=user_id, name=name, output=output)


register_crud(users_app, USERS_SPEC)
