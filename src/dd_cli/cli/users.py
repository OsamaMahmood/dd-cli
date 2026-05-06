"""`dd users` — list, get, CRUD, plus deactivate / activate verbs."""

from __future__ import annotations

from itertools import islice
from typing import Annotated, Any

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
from dd_cli.errors import APIError, NotFoundError, ValidationError
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


# ---------------------------- action verbs ------------------------------ #


@users_app.command("deactivate")
def users_deactivate(
    ctx: typer.Context,
    user: Annotated[str, typer.Argument(help="User ID or username.")],
    yes: Annotated[bool, typer.Option("--yes", "-y", help="Skip confirmation.")] = False,
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Print intent only.")] = False,
    output: Annotated[
        OutputFormat | None, typer.Option("--output", "-o", help="Output format.")
    ] = None,
) -> None:
    """Deactivate a user (PATCH is_active=false). Accepts ID or username."""
    _toggle_user_active(ctx, user, active=False, yes=yes, dry_run=dry_run, output=output)


@users_app.command("activate")
def users_activate(
    ctx: typer.Context,
    user: Annotated[str, typer.Argument(help="User ID or username.")],
    yes: Annotated[bool, typer.Option("--yes", "-y", help="Skip confirmation.")] = False,
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Print intent only.")] = False,
    output: Annotated[
        OutputFormat | None, typer.Option("--output", "-o", help="Output format.")
    ] = None,
) -> None:
    """Reactivate a user (PATCH is_active=true). Accepts ID or username."""
    _toggle_user_active(ctx, user, active=True, yes=yes, dry_run=dry_run, output=output)


def _toggle_user_active(
    ctx: typer.Context,
    user: str,
    *,
    active: bool,
    yes: bool,
    dry_run: bool,
    output: OutputFormat | None,
) -> None:
    payload: dict[str, Any] = {"is_active": active}
    verb = "Activate" if active else "Deactivate"
    past = "Activated" if active else "Deactivated"

    profile = get_active_profile(ctx)

    with DefectDojoClient(profile) as client:
        user_id = _resolve_user(client, user)
        target = f"/api/v2/users/{user_id}/"

        if dry_run:
            print_dry_run("PATCH", target, payload, ctx, output)
            return

        confirm_or_abort(f"{verb} user {user_id}?", yes=yes)
        body = client.patch(target, json=payload)

    typer.echo(f"{past} user {user_id}.")
    render_response(body, ctx, output)


def _resolve_user(client: DefectDojoClient, user: str) -> int:
    """Resolve a user reference (numeric ID or username) to an integer ID."""
    if user.isdigit():
        return int(user)
    if not user:
        raise ValidationError("Empty user reference.")
    matches = list(islice(client.paginate("/api/v2/users/", params={"username": user}), 100))
    exact = [m for m in matches if m.get("username") == user]
    if not exact:
        raise NotFoundError(f"User `{user}` not found")
    if len(exact) > 1:
        raise APIError(
            f"Multiple users match `{user}`",
            hint="Pass the numeric ID instead.",
        )
    user_id = exact[0].get("id")
    if not isinstance(user_id, int):
        raise APIError(f"Resolved user `{user}` has no integer `id` field")
    return user_id
