"""`dd products` — list and get DefectDojo products."""

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

PRODUCTS_SPEC = ResourceSpec(
    name="product",
    plural="products",
    path="/api/v2/products/",
    columns=("id", "name", "prod_type", "business_criticality", "lifecycle"),
)


products_app = typer.Typer(
    name="products",
    help="List and get DefectDojo products.",
    no_args_is_help=True,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@products_app.command("list")
def products_list(
    ctx: typer.Context,
    name: Annotated[
        str | None, typer.Option("--name", help="Filter by exact product name.")
    ] = None,
    prod_type: Annotated[
        int | None,
        typer.Option("--prod-type", help="Filter by product type ID."),
    ] = None,
    tag: Annotated[
        str | None,
        typer.Option("--tag", help="Filter by tag (exact match)."),
    ] = None,
    limit: Annotated[
        int,
        typer.Option(
            "--limit", help=f"Maximum rows. Ignored with --all. Default: {DEFAULT_LIMIT}."
        ),
    ] = DEFAULT_LIMIT,
    all_pages: Annotated[
        bool,
        typer.Option("--all", help="Stream every page from DefectDojo (overrides --limit)."),
    ] = False,
    output: Annotated[
        OutputFormat | None,
        typer.Option("--output", "-o", help="Output format."),
    ] = None,
) -> None:
    """List products with optional filters."""
    list_resource(
        ctx,
        PRODUCTS_SPEC,
        filters={"name": name, "prod_type": prod_type, "tag": tag},
        limit=limit,
        all_pages=all_pages,
        output=output,
    )


@products_app.command("get")
def products_get(
    ctx: typer.Context,
    product_id: Annotated[
        int | None,
        typer.Argument(help="Product ID (omit if using --name)."),
    ] = None,
    name: Annotated[
        str | None,
        typer.Option("--name", help="Resolve by exact product name."),
    ] = None,
    output: Annotated[
        OutputFormat | None,
        typer.Option("--output", "-o", help="Output format."),
    ] = None,
) -> None:
    """Get a single product by ID or name."""
    get_dispatch(ctx, PRODUCTS_SPEC, resource_id=product_id, name=name, output=output)
