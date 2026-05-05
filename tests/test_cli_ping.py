from __future__ import annotations

import json
from pathlib import Path

import pytest
from pytest_httpx import HTTPXMock
from typer.testing import CliRunner

from dd_cli.cli.app import app


@pytest.fixture(autouse=True)
def isolated_env(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DD_CLI_CONFIG_DIR", str(tmp_path))
    for var in ("DD_URL", "DD_API_KEY", "DD_CLI_URL", "DD_CLI_API_KEY"):
        monkeypatch.delenv(var, raising=False)


def _seed_profile(runner: CliRunner) -> None:
    result = runner.invoke(
        app,
        [
            "configure",
            "--url",
            "https://dd.example",
            "--api-key",
            "the-token",
            "--no-input",
        ],
    )
    assert result.exit_code == 0, result.output


def test_ping_returns_ok_on_200(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    _seed_profile(runner)
    httpx_mock.add_response(
        url="https://dd.example/api/v2/user_profile/",
        json={"user": {"id": 1, "username": "alice"}},
    )

    result = runner.invoke(app, ["ping", "--output", "json"])
    assert result.exit_code == 0, result.output
    body = json.loads(result.stdout)
    assert body["ok"] is True
    assert body["user"] == "alice"
    assert body["url"] == "https://dd.example"


def test_ping_fails_when_profile_incomplete(runner: CliRunner) -> None:
    result = runner.invoke(app, ["ping"])
    assert result.exit_code != 0
    assert result.exception is not None


def test_ping_fails_with_auth_error_on_401(
    runner: CliRunner, httpx_mock: HTTPXMock
) -> None:
    _seed_profile(runner)
    httpx_mock.add_response(
        url="https://dd.example/api/v2/user_profile/",
        status_code=401,
        json={"detail": "Invalid token."},
    )

    result = runner.invoke(app, ["ping"])
    assert result.exit_code != 0
    assert result.exception is not None


def test_ping_uses_legacy_dd_env_vars(
    runner: CliRunner,
    httpx_mock: HTTPXMock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """`DD_URL=… DD_API_KEY=… dd ping` works even with no on-disk config."""
    monkeypatch.setenv("DD_URL", "https://legacy.example")
    monkeypatch.setenv("DD_API_KEY", "legacy-token")
    httpx_mock.add_response(
        url="https://legacy.example/api/v2/user_profile/",
        json={"user": {"username": "legacy-user"}},
    )

    result = runner.invoke(app, ["ping", "--output", "json"])
    assert result.exit_code == 0, result.output
    body = json.loads(result.stdout)
    assert body["url"] == "https://legacy.example"
    assert body["user"] == "legacy-user"


def test_ping_handles_alternate_username_shape(
    runner: CliRunner, httpx_mock: HTTPXMock
) -> None:
    _seed_profile(runner)
    # Some DD versions return a flat shape
    httpx_mock.add_response(
        url="https://dd.example/api/v2/user_profile/",
        json={"username": "flat-user"},
    )

    result = runner.invoke(app, ["ping", "--output", "json"])
    assert result.exit_code == 0
    body = json.loads(result.stdout)
    assert body["user"] == "flat-user"
