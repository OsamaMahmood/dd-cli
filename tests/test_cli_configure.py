from __future__ import annotations

import tomllib
from pathlib import Path

import pytest
from typer.testing import CliRunner

from dd_cli.cli.app import app


@pytest.fixture(autouse=True)
def config_path(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.setenv("DD_CLI_CONFIG_DIR", str(tmp_path))
    for var in ("DD_URL", "DD_API_KEY", "DD_CLI_URL", "DD_CLI_API_KEY"):
        monkeypatch.delenv(var, raising=False)
    return tmp_path / "config.toml"


def test_configure_with_flags_no_prompts(runner: CliRunner, config_path: Path) -> None:
    result = runner.invoke(
        app,
        [
            "configure",
            "--profile",
            "default",
            "--url",
            "https://dd.example",
            "--api-key",
            "the-token",
            "--no-input",
        ],
    )
    assert result.exit_code == 0, result.output

    with config_path.open("rb") as fh:
        data = tomllib.load(fh)
    assert data["default_profile"] == "default"
    assert data["profiles"]["default"]["url"] == "https://dd.example"
    assert data["profiles"]["default"]["api_key"] == "the-token"


def test_configure_interactive_round_trip(runner: CliRunner, config_path: Path) -> None:
    # Prompts in order: profile name, URL, API key, ssl_verify, add extra headers
    user_input = "\n".join(
        [
            "default",  # profile name
            "https://dd.example",  # URL
            "the-token",  # API key
            "Y",  # ssl_verify
            "n",  # extra headers? no
        ]
    )
    result = runner.invoke(app, ["configure"], input=user_input)
    assert result.exit_code == 0, result.output

    with config_path.open("rb") as fh:
        data = tomllib.load(fh)
    profile = data["profiles"]["default"]
    assert profile["url"] == "https://dd.example"
    assert profile["api_key"] == "the-token"
    assert profile["ssl_verify"] is True


def test_configure_preserves_existing_api_key_on_empty_input(
    runner: CliRunner, config_path: Path
) -> None:
    # First seed a profile via flags
    runner.invoke(
        app,
        [
            "configure",
            "--profile",
            "default",
            "--url",
            "https://old.example",
            "--api-key",
            "old-token",
            "--no-input",
        ],
    )
    # Now reconfigure interactively, leaving API key blank to keep existing
    user_input = "\n".join(
        [
            "default",  # profile name
            "https://new.example",  # new URL
            "",  # blank API key → keep existing
            "Y",  # ssl_verify
            "n",  # extra headers? no
        ]
    )
    result = runner.invoke(app, ["configure"], input=user_input)
    assert result.exit_code == 0, result.output

    with config_path.open("rb") as fh:
        data = tomllib.load(fh)
    profile = data["profiles"]["default"]
    assert profile["url"] == "https://new.example"
    assert profile["api_key"] == "old-token"


def test_configure_collects_extra_headers(runner: CliRunner, config_path: Path) -> None:
    user_input = (
        "\n".join(
            [
                "default",
                "https://x",
                "tok",
                "Y",  # ssl_verify
                "y",  # add extra headers? yes
                "X-WAF",  # header name
                "secret-value",  # header value
                "",  # empty header name → finish
            ]
        )
        + "\n"
    )
    result = runner.invoke(app, ["configure"], input=user_input)
    assert result.exit_code == 0, result.output

    with config_path.open("rb") as fh:
        data = tomllib.load(fh)
    assert data["profiles"]["default"]["extra_headers"] == {"X-WAF": "secret-value"}


def test_configure_without_url_in_no_input_fails(
    runner: CliRunner, config_path: Path
) -> None:
    result = runner.invoke(
        app,
        ["configure", "--no-input", "--api-key", "k"],
    )
    assert result.exit_code != 0


def test_configure_creates_named_profile(runner: CliRunner, config_path: Path) -> None:
    runner.invoke(
        app,
        [
            "configure",
            "--profile",
            "staging",
            "--url",
            "https://staging",
            "--api-key",
            "k",
            "--no-input",
        ],
    )
    with config_path.open("rb") as fh:
        data = tomllib.load(fh)
    assert "staging" in data["profiles"]
