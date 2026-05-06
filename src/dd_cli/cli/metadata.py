"""`dd metadata` — list and get DefectDojo metadata entries.

Metadata entries are key/value pairs attached to products, findings, or
endpoints. Note that names are not unique across owners (e.g. two products
can both have a `service_tier` metadata entry), so `--name` resolution is
ambiguous unless paired with the owning resource filter.
"""

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

METADATA_SPEC = ResourceSpec(
    name="metadata entry",
    plural="metadata entries",
    path="/api/v2/metadata/",
    columns=("id", "name", "value", "product", "finding", "endpoint"),
)


metadata_app = typer.Typer(
    name="metadata",
    help="List and get DefectDojo metadata entries.",
    no_args_is_help=True,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@metadata_app.command("list")
def metadata_list(
    ctx: typer.Context,
    name: Annotated[str | None, typer.Option("--name", help="Filter by exact key name.")] = None,
    value: Annotated[str | None, typer.Option("--value", help="Filter by value.")] = None,
    product: Annotated[
        int | None, typer.Option("--product", help="Filter by owning product ID.")
    ] = None,
    finding: Annotated[
        int | None, typer.Option("--finding", help="Filter by owning finding ID.")
    ] = None,
    endpoint: Annotated[
        int | None, typer.Option("--endpoint", help="Filter by owning endpoint ID.")
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
    """List metadata entries with optional filters."""
    list_resource(
        ctx,
        METADATA_SPEC,
        filters={
            "name": name,
            "value": value,
            "product": product,
            "finding": finding,
            "endpoint": endpoint,
        },
        limit=limit,
        all_pages=all_pages,
        output=output,
    )


@metadata_app.command("get")
def metadata_get(
    ctx: typer.Context,
    entry_id: Annotated[
        int | None,
        typer.Argument(help="Metadata entry ID (omit if using --name)."),
    ] = None,
    name: Annotated[
        str | None,
        typer.Option(
            "--name",
            help="Resolve by exact metadata key name (must be unique).",
        ),
    ] = None,
    output: Annotated[
        OutputFormat | None,
        typer.Option("--output", "-o", help="Output format."),
    ] = None,
) -> None:
    """Get a single metadata entry by ID or name."""
    get_dispatch(ctx, METADATA_SPEC, resource_id=entry_id, name=name, output=output)


register_crud(metadata_app, METADATA_SPEC)
