"""`dd endpoints` — list and get DefectDojo endpoints.

Endpoints have no single "name" field; they are identified by the URL
composition (host + port + path + query etc.). For convenience `--name`
resolves against the host, but multiple endpoints can share a host so the
result may be ambiguous — use the numeric ID when in doubt.
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

ENDPOINTS_SPEC = ResourceSpec(
    name="endpoint",
    plural="endpoints",
    path="/api/v2/endpoints/",
    columns=("id", "host", "port", "path", "protocol", "product"),
    name_field="host",
)


endpoints_app = typer.Typer(
    name="endpoints",
    help="List and get DefectDojo endpoints.",
    no_args_is_help=True,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@endpoints_app.command("list")
def endpoints_list(
    ctx: typer.Context,
    host: Annotated[str | None, typer.Option("--host", help="Filter by host.")] = None,
    port: Annotated[int | None, typer.Option("--port", help="Filter by port.")] = None,
    path: Annotated[str | None, typer.Option("--path", help="Filter by path.")] = None,
    protocol: Annotated[
        str | None,
        typer.Option("--protocol", help="Filter by protocol (e.g. 'http', 'https')."),
    ] = None,
    product: Annotated[
        int | None,
        typer.Option("--product", help="Filter by owning product ID."),
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
    """List endpoints with optional filters."""
    list_resource(
        ctx,
        ENDPOINTS_SPEC,
        filters={
            "host": host,
            "port": port,
            "path": path,
            "protocol": protocol,
            "product": product,
            "tag": tag,
        },
        limit=limit,
        all_pages=all_pages,
        output=output,
    )


@endpoints_app.command("get")
def endpoints_get(
    ctx: typer.Context,
    endpoint_id: Annotated[
        int | None,
        typer.Argument(help="Endpoint ID (omit if using --name)."),
    ] = None,
    name: Annotated[
        str | None,
        typer.Option("--name", help="Resolve by host (exact match)."),
    ] = None,
    output: Annotated[
        OutputFormat | None,
        typer.Option("--output", "-o", help="Output format."),
    ] = None,
) -> None:
    """Get a single endpoint by ID or host."""
    get_dispatch(ctx, ENDPOINTS_SPEC, resource_id=endpoint_id, name=name, output=output)


register_crud(endpoints_app, ENDPOINTS_SPEC)
