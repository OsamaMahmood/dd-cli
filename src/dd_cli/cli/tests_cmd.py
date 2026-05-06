"""`dd tests` — list and get DefectDojo tests.

Note: this module is named `tests_cmd.py` rather than `tests.py` so it does
not collide with the top-level `tests/` directory used by pytest.
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

TESTS_SPEC = ResourceSpec(
    name="test",
    plural="tests",
    path="/api/v2/tests/",
    columns=("id", "title", "engagement", "test_type", "target_start", "target_end"),
    name_field="title",
)


tests_app = typer.Typer(
    name="tests",
    help="List and get DefectDojo tests.",
    no_args_is_help=True,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@tests_app.command("list")
def tests_list(
    ctx: typer.Context,
    title: Annotated[
        str | None,
        typer.Option("--title", help="Filter by exact test title."),
    ] = None,
    engagement: Annotated[
        int | None,
        typer.Option("--engagement", help="Filter by engagement ID."),
    ] = None,
    test_type: Annotated[
        int | None,
        typer.Option("--test-type", help="Filter by test type ID."),
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
    """List tests with optional filters."""
    list_resource(
        ctx,
        TESTS_SPEC,
        filters={
            "title": title,
            "engagement": engagement,
            "test_type": test_type,
            "tag": tag,
        },
        limit=limit,
        all_pages=all_pages,
        output=output,
    )


@tests_app.command("get")
def tests_get(
    ctx: typer.Context,
    test_id: Annotated[
        int | None,
        typer.Argument(help="Test ID (omit if using --name)."),
    ] = None,
    name: Annotated[
        str | None,
        typer.Option("--name", help="Resolve by exact test title."),
    ] = None,
    output: Annotated[
        OutputFormat | None,
        typer.Option("--output", "-o", help="Output format."),
    ] = None,
) -> None:
    """Get a single test by ID or title."""
    get_dispatch(ctx, TESTS_SPEC, resource_id=test_id, name=name, output=output)


register_crud(tests_app, TESTS_SPEC)
