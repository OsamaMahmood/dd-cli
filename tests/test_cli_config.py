from __future__ import annotations

import tomllib
from pathlib import Path

import pytest
from typer.testing import CliRunner

from dd_cli.cli.app import app


@pytest.fixture(autouse=True)
def config_path(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Point dd-cli at a per-test config dir and clear DD_* env vars."""
    monkeypatch.setenv("DD_CLI_CONFIG_DIR", str(tmp_path))
    for var in (
        "DD_URL",
        "DD_API_KEY",
        "DD_SSL_VERIFY",
        "DD_CLI_URL",
        "DD_CLI_API_KEY",
        "DD_CLI_SSL_VERIFY",
        "DD_CLI_PROFILE",
        "DD_PROFILE",
        "DD_EXTRA_HEADER_1",
        "DD_EXTRA_HEADER_1_VALUE",
        "DD_EXTRA_HEADER_2",
        "DD_EXTRA_HEADER_2_VALUE",
    ):
        monkeypatch.delenv(var, raising=False)
    return tmp_path / "config.toml"


# ---------------------------- set / get round-trip ------------------------ #


def test_set_then_get_url_round_trips(runner: CliRunner, config_path: Path) -> None:
    result = runner.invoke(app, ["config", "set", "url", "https://dd.example"])
    assert result.exit_code == 0, result.output

    result = runner.invoke(app, ["config", "get", "url"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "https://dd.example"


def test_set_api_key_round_trips_through_toml(runner: CliRunner, config_path: Path) -> None:
    result = runner.invoke(app, ["config", "set", "api_key", "the-secret-token"])
    assert result.exit_code == 0

    # Plain `get` masks the secret
    result = runner.invoke(app, ["config", "get", "api_key"])
    assert result.exit_code == 0
    assert "<set>" in result.stdout

    # `--show-secrets` reveals it
    result = runner.invoke(app, ["config", "get", "api_key", "--show-secrets"])
    assert result.exit_code == 0
    assert "the-secret-token" in result.stdout

    # Persisted to TOML
    with config_path.open("rb") as fh:
        data = tomllib.load(fh)
    assert data["profiles"]["default"]["api_key"] == "the-secret-token"


def test_set_ssl_verify_coerces_bool(runner: CliRunner, config_path: Path) -> None:
    result = runner.invoke(app, ["config", "set", "ssl_verify", "false"])
    assert result.exit_code == 0

    with config_path.open("rb") as fh:
        data = tomllib.load(fh)
    assert data["profiles"]["default"]["ssl_verify"] is False


def test_set_ssl_verify_rejects_garbage(runner: CliRunner) -> None:
    result = runner.invoke(app, ["config", "set", "ssl_verify", "maybe"])
    assert result.exit_code != 0
    assert result.exception is not None
    assert "ssl_verify" in str(result.exception)


def test_set_unknown_key_rejected(runner: CliRunner) -> None:
    result = runner.invoke(app, ["config", "set", "weird_key", "x"])
    assert result.exit_code != 0
    assert result.exception is not None
    assert "weird_key" in str(result.exception)


# ---------------------------- profile management ------------------------- #


def test_set_creates_named_profile(runner: CliRunner, config_path: Path) -> None:
    runner.invoke(app, ["config", "set", "url", "https://prod", "--profile", "prod"])
    runner.invoke(app, ["config", "set", "url", "https://staging", "--profile", "staging"])

    result = runner.invoke(app, ["config", "list", "--output", "json"])
    assert result.exit_code == 0
    assert "prod" in result.stdout
    assert "staging" in result.stdout


def test_use_sets_default_profile(runner: CliRunner, config_path: Path) -> None:
    runner.invoke(app, ["config", "set", "url", "https://a", "--profile", "a"])
    runner.invoke(app, ["config", "set", "url", "https://b", "--profile", "b"])
    result = runner.invoke(app, ["config", "use", "b"])
    assert result.exit_code == 0

    with config_path.open("rb") as fh:
        data = tomllib.load(fh)
    assert data["default_profile"] == "b"


def test_use_unknown_profile_fails(runner: CliRunner, config_path: Path) -> None:
    result = runner.invoke(app, ["config", "use", "ghost"])
    assert result.exit_code != 0
    assert result.exception is not None
    assert "ghost" in str(result.exception)


def test_delete_profile_removes_it(runner: CliRunner, config_path: Path) -> None:
    runner.invoke(app, ["config", "set", "url", "https://a", "--profile", "a"])
    runner.invoke(app, ["config", "set", "url", "https://b", "--profile", "b"])

    result = runner.invoke(app, ["config", "delete", "a", "--yes"])
    assert result.exit_code == 0

    with config_path.open("rb") as fh:
        data = tomllib.load(fh)
    assert "a" not in data.get("profiles", {})
    assert "b" in data["profiles"]


def test_delete_unknown_profile_fails(runner: CliRunner) -> None:
    result = runner.invoke(app, ["config", "delete", "ghost", "--yes"])
    assert result.exit_code != 0


def test_unset_clears_a_field(runner: CliRunner, config_path: Path) -> None:
    runner.invoke(app, ["config", "set", "url", "https://x"])
    runner.invoke(app, ["config", "set", "api_key", "k"])
    result = runner.invoke(app, ["config", "unset", "api_key"])
    assert result.exit_code == 0

    with config_path.open("rb") as fh:
        data = tomllib.load(fh)
    assert "api_key" not in data["profiles"]["default"]


# ---------------------------- show + env merging -------------------------- #


def test_show_reads_from_toml(runner: CliRunner, config_path: Path) -> None:
    runner.invoke(app, ["config", "set", "url", "https://from-toml"])
    runner.invoke(app, ["config", "set", "api_key", "k"])

    result = runner.invoke(app, ["config", "show", "--output", "json"])
    assert result.exit_code == 0
    assert "https://from-toml" in result.stdout
    assert "<set>" in result.stdout  # api_key masked


def test_show_reflects_env_override(
    runner: CliRunner,
    config_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    runner.invoke(app, ["config", "set", "url", "https://from-toml"])
    monkeypatch.setenv("DD_CLI_URL", "https://from-env")

    result = runner.invoke(app, ["config", "show", "--output", "json"])
    assert result.exit_code == 0
    assert "https://from-env" in result.stdout
    assert "https://from-toml" not in result.stdout


def test_show_legacy_dd_api_key_acceptance(
    runner: CliRunner,
    config_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """`DD_API_KEY=… dd config show` should reflect the legacy env var."""
    monkeypatch.setenv("DD_API_KEY", "legacy-token")
    monkeypatch.setenv("DD_URL", "https://legacy")

    result = runner.invoke(app, ["config", "show", "--output", "json"])
    assert result.exit_code == 0
    # api_key set from legacy env var → masked in output
    assert "<set>" in result.stdout
    assert "https://legacy" in result.stdout


# ---------------------------- list ---------------------------------------- #


def test_list_when_empty(runner: CliRunner, config_path: Path) -> None:
    result = runner.invoke(app, ["config", "list"])
    assert result.exit_code == 0
    assert "No profiles" in result.stdout


def test_list_shows_default_marker(runner: CliRunner, config_path: Path) -> None:
    runner.invoke(app, ["config", "set", "url", "https://x", "--profile", "alpha"])
    runner.invoke(app, ["config", "set", "url", "https://y", "--profile", "beta"])
    runner.invoke(app, ["config", "use", "beta"])

    result = runner.invoke(app, ["config", "list", "--output", "json"])
    assert result.exit_code == 0
    # JSON output: only `beta` should have default=true
    import json

    rows = json.loads(result.stdout)
    by_name = {r["name"]: r for r in rows}
    assert by_name["beta"]["default"] is True
    assert by_name["alpha"]["default"] is False
