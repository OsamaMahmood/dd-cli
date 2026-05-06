"""`dd product-types` — list and get DefectDojo product types."""

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

PRODUCT_TYPES_SPEC = ResourceSpec(
    name="product type",
    plural="product types",
    path="/api/v2/product_types/",
    columns=("id", "name", "critical_product", "key_product"),
)


product_types_app = typer.Typer(
    name="product-types",
    help="List and get DefectDojo product types.",
    no_args_is_help=True,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@product_types_app.command("list")
def product_types_list(
    ctx: typer.Context,
    name: Annotated[str | None, typer.Option("--name", help="Filter by exact name.")] = None,
    critical: Annotated[
        bool | None,
        typer.Option(
            "--critical/--non-critical",
            help="Filter by critical_product flag.",
        ),
    ] = None,
    key_product: Annotated[
        bool | None,
        typer.Option(
            "--key/--non-key",
            help="Filter by key_product flag.",
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
    """List product types."""
    list_resource(
        ctx,
        PRODUCT_TYPES_SPEC,
        filters={"name": name, "critical_product": critical, "key_product": key_product},
        limit=limit,
        all_pages=all_pages,
        output=output,
    )


@product_types_app.command("get")
def product_types_get(
    ctx: typer.Context,
    product_type_id: Annotated[
        int | None,
        typer.Argument(help="Product type ID (omit if using --name)."),
    ] = None,
    name: Annotated[
        str | None,
        typer.Option("--name", help="Resolve by exact product type name."),
    ] = None,
    output: Annotated[
        OutputFormat | None,
        typer.Option("--output", "-o", help="Output format."),
    ] = None,
) -> None:
    """Get a single product type by ID or name."""
    get_dispatch(
        ctx,
        PRODUCT_TYPES_SPEC,
        resource_id=product_type_id,
        name=name,
        output=output,
    )


register_crud(product_types_app, PRODUCT_TYPES_SPEC)
