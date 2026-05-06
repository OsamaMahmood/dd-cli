"""`dd risk-acceptances` — list and get DefectDojo risk acceptances."""

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

RISK_ACCEPTANCES_SPEC = ResourceSpec(
    name="risk acceptance",
    plural="risk acceptances",
    # Note: API path is singular `risk_acceptance` per OpenAPI spec.
    path="/api/v2/risk_acceptance/",
    columns=("id", "name", "owner", "decision", "expiration_date", "reactivate_expired"),
)


risk_acceptances_app = typer.Typer(
    name="risk-acceptances",
    help="List and get DefectDojo risk acceptances.",
    no_args_is_help=True,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@risk_acceptances_app.command("list")
def risk_acceptances_list(
    ctx: typer.Context,
    name: Annotated[str | None, typer.Option("--name", help="Filter by exact name.")] = None,
    owner: Annotated[int | None, typer.Option("--owner", help="Filter by owner user ID.")] = None,
    decision: Annotated[
        str | None,
        typer.Option(
            "--decision",
            help="Filter by decision (e.g. 'Accept', 'Transfer', 'Avoid', 'Mitigate').",
        ),
    ] = None,
    expiration_date: Annotated[
        str | None,
        typer.Option("--expiration-date", help="Filter by expiration date (YYYY-MM-DD)."),
    ] = None,
    reactivate_expired: Annotated[
        bool | None,
        typer.Option(
            "--reactivate-expired/--keep-expired",
            help="Filter by the reactivate-on-expiration flag.",
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
    """List risk acceptances with optional filters."""
    list_resource(
        ctx,
        RISK_ACCEPTANCES_SPEC,
        filters={
            "name": name,
            "owner": owner,
            "decision": decision,
            "expiration_date": expiration_date,
            "reactivate_expired": reactivate_expired,
        },
        limit=limit,
        all_pages=all_pages,
        output=output,
    )


@risk_acceptances_app.command("get")
def risk_acceptances_get(
    ctx: typer.Context,
    acceptance_id: Annotated[
        int | None,
        typer.Argument(help="Risk-acceptance ID (omit if using --name)."),
    ] = None,
    name: Annotated[
        str | None,
        typer.Option("--name", help="Resolve by exact risk-acceptance name."),
    ] = None,
    output: Annotated[
        OutputFormat | None,
        typer.Option("--output", "-o", help="Output format."),
    ] = None,
) -> None:
    """Get a single risk acceptance by ID or name."""
    get_dispatch(
        ctx,
        RISK_ACCEPTANCES_SPEC,
        resource_id=acceptance_id,
        name=name,
        output=output,
    )


register_crud(risk_acceptances_app, RISK_ACCEPTANCES_SPEC)
