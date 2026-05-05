"""Top-level Typer app and `dd` entry point."""

from __future__ import annotations

from typing import Annotated

import typer
from rich.console import Console

from dd_cli.cli.config_cmd import config_app
from dd_cli.cli.configure import configure
from dd_cli.cli.engagements import engagements_app
from dd_cli.cli.findings import findings_app
from dd_cli.cli.ping import ping
from dd_cli.cli.product_types import product_types_app
from dd_cli.cli.products import products_app
from dd_cli.cli.tests_cmd import tests_app
from dd_cli.cli.users import users_app
from dd_cli.errors import DDCliError
from dd_cli.output import OutputFormat
from dd_cli.version import __version__

console = Console()
err_console = Console(stderr=True)


app = typer.Typer(
    name="dd",
    help="Production-grade CLI for managing DefectDojo.",
    no_args_is_help=True,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
)

app.add_typer(config_app)
app.add_typer(products_app)
app.add_typer(product_types_app)
app.add_typer(engagements_app)
app.add_typer(tests_app)
app.add_typer(findings_app)
app.add_typer(users_app)
app.command("configure", help="Interactively create or update a profile.")(configure)
app.command("ping", help="Verify connectivity and authentication against DefectDojo.")(ping)


def _version_callback(value: bool) -> None:
    if value:
        console.print(f"dd {__version__}")
        raise typer.Exit()


@app.callback()
def main_callback(
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
            envvar=["DD_CLI_PROFILE", "DD_PROFILE"],
        ),
    ] = None,
    output: Annotated[
        OutputFormat,
        typer.Option(
            "--output",
            "-o",
            help="Output format.",
            envvar=["DD_CLI_OUTPUT", "DD_OUTPUT"],
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


def main() -> None:
    """Entry point for the `dd` console script.

    Wraps `app()` so that typed `DDCliError` exceptions are mapped to
    stable exit codes per `PLAN.md` §5 instead of dumping a traceback.
    """
    try:
        app()
    except DDCliError as exc:
        err_console.print(f"[red bold]Error:[/red bold] {exc.message}")
        if exc.hint:
            err_console.print(f"[yellow]Hint:[/yellow] {exc.hint}")
        raise SystemExit(exc.exit_code) from None


if __name__ == "__main__":
    main()
