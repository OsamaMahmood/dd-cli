from __future__ import annotations

from enum import StrEnum
from typing import Annotated

import typer
from rich.console import Console

from dd_cli.version import __version__

console = Console()
err_console = Console(stderr=True)


class OutputFormat(StrEnum):
    table = "table"
    json = "json"
    yaml = "yaml"


app = typer.Typer(
    name="dd",
    help="Production-grade CLI for managing DefectDojo.",
    no_args_is_help=True,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
)


def _version_callback(value: bool) -> None:
    if value:
        console.print(f"dd {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    ctx: typer.Context,
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            "-V",
            help="Show the version and exit.",
            callback=_version_callback,
            is_eager=True,
        ),
    ] = False,
    profile: Annotated[
        str | None,
        typer.Option(
            "--profile",
            "-p",
            help="Configuration profile to use.",
            envvar="DD_PROFILE",
        ),
    ] = None,
    output: Annotated[
        OutputFormat,
        typer.Option(
            "--output",
            "-o",
            help="Output format.",
            envvar="DD_OUTPUT",
        ),
    ] = OutputFormat.table,
    verbose: Annotated[
        int,
        typer.Option(
            "--verbose",
            "-v",
            count=True,
            help="Increase verbosity (-v, -vv).",
        ),
    ] = 0,
) -> None:
    ctx.obj = {
        "profile": profile,
        "output": output,
        "verbose": verbose,
    }


if __name__ == "__main__":
    app()
