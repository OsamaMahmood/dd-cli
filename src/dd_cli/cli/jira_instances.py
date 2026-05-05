"""`dd jira-instances` — list and get DefectDojo Jira instance configurations."""

from __future__ import annotations

from typing import Annotated

import typer

from dd_cli.cli._resource import (
    DEFAULT_LIMIT,
    ResourceSpec,
    get_dispatch,
    list_resource,
)
from dd_cli.output import OutputFormat

JIRA_INSTANCES_SPEC = ResourceSpec(
    name="JIRA instance",
    plural="JIRA instances",
    path="/api/v2/jira_instances/",
    columns=("id", "configuration_name", "url", "username", "default_issue_type"),
    name_field="configuration_name",
)


jira_instances_app = typer.Typer(
    name="jira-instances",
    help="List and get DefectDojo Jira instance configurations.",
    no_args_is_help=True,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@jira_instances_app.command("list")
def jira_instances_list(
    ctx: typer.Context,
    url: Annotated[
        str | None,
        typer.Option("--url", help="Filter by Jira base URL."),
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
    """List Jira instance configurations."""
    list_resource(
        ctx,
        JIRA_INSTANCES_SPEC,
        filters={"url": url},
        limit=limit,
        all_pages=all_pages,
        output=output,
    )


@jira_instances_app.command("get")
def jira_instances_get(
    ctx: typer.Context,
    instance_id: Annotated[
        int | None,
        typer.Argument(help="Instance ID (omit if using --name)."),
    ] = None,
    name: Annotated[
        str | None,
        typer.Option("--name", help="Resolve by exact configuration_name."),
    ] = None,
    output: Annotated[
        OutputFormat | None,
        typer.Option("--output", "-o", help="Output format."),
    ] = None,
) -> None:
    """Get a single Jira instance by ID or configuration name."""
    get_dispatch(
        ctx,
        JIRA_INSTANCES_SPEC,
        resource_id=instance_id,
        name=name,
        output=output,
    )
