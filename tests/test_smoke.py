from __future__ import annotations

from typer.testing import CliRunner

from dd_cli import __version__
from dd_cli.cli.app import app


def test_version_constant_is_set() -> None:
    assert __version__
    assert __version__ != "0.0.0"


def test_version_flag_prints_version(runner: CliRunner) -> None:
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout


def test_help_renders(runner: CliRunner) -> None:
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Production-grade CLI for managing DefectDojo" in result.stdout


def test_no_args_shows_help(runner: CliRunner) -> None:
    result = runner.invoke(app, [])
    assert result.exit_code != 0  # no_args_is_help exits non-zero by design
    assert "Usage" in result.stdout or "Usage" in result.stderr
