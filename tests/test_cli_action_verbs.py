"""Tests for the M3b action verbs and the editor-driven update flow.

Covers:
- dd findings close / reopen / risk-accept
- dd engagements close / reopen
- dd users deactivate / activate
- dd <resource> edit (using a stubbed typer.edit)
"""

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
    for var in (
        "DD_URL",
        "DD_API_KEY",
        "DD_CLI_URL",
        "DD_CLI_API_KEY",
        "DD_CLI_PROFILE",
        "DD_PROFILE",
    ):
        monkeypatch.delenv(var, raising=False)
    monkeypatch.setenv("DD_URL", "https://dd.example")
    monkeypatch.setenv("DD_API_KEY", "the-token")


# ============================ findings close ============================ #


def test_findings_close_happy_path(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/findings/42/close/",
        method="POST",
        json={"id": 42, "is_mitigated": True},
    )
    result = runner.invoke(app, ["findings", "close", "42", "--yes"])
    assert result.exit_code == 0, result.output
    assert "Closed finding 42" in result.stdout

    sent = httpx_mock.get_request()
    assert sent is not None
    payload = json.loads(sent.read())
    assert payload == {"is_mitigated": True}


def test_findings_close_with_flags(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/findings/42/close/",
        method="POST",
        json={"id": 42},
    )
    result = runner.invoke(
        app,
        [
            "findings",
            "close",
            "42",
            "--yes",
            "--note",
            "Out of band fix",
            "--false-positive",
            "--out-of-scope",
            "--duplicate",
        ],
    )
    assert result.exit_code == 0, result.output

    sent = httpx_mock.get_request()
    assert sent is not None
    payload = json.loads(sent.read())
    assert payload == {
        "is_mitigated": True,
        "note": "Out of band fix",
        "false_p": True,
        "out_of_scope": True,
        "duplicate": True,
    }


def test_findings_close_dry_run_sends_no_http(runner: CliRunner) -> None:
    result = runner.invoke(app, ["findings", "close", "42", "--dry-run"])
    assert result.exit_code == 0, result.output
    assert "DRY RUN" in result.stdout
    assert "POST" in result.stdout
    assert "/api/v2/findings/42/close/" in result.stdout


def test_findings_close_aborts_on_n(runner: CliRunner) -> None:
    result = runner.invoke(app, ["findings", "close", "42"], input="n\n")
    assert result.exit_code == 0
    assert "Aborted" in result.stdout


# ============================ findings reopen =========================== #


def test_findings_reopen_happy_path(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/findings/42/",
        method="PATCH",
        json={"id": 42, "is_mitigated": False, "active": True},
    )
    result = runner.invoke(app, ["findings", "reopen", "42", "--yes"])
    assert result.exit_code == 0, result.output
    assert "Reopened finding 42" in result.stdout

    sent = httpx_mock.get_request()
    assert sent is not None
    payload = json.loads(sent.read())
    assert payload == {"is_mitigated": False, "active": True, "mitigated": None}


def test_findings_reopen_dry_run(runner: CliRunner) -> None:
    result = runner.invoke(app, ["findings", "reopen", "42", "--dry-run"])
    assert result.exit_code == 0, result.output
    assert "DRY RUN" in result.stdout
    assert "PATCH" in result.stdout


# ============================ findings risk-accept ====================== #


def test_findings_risk_accept_with_owner(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/risk_acceptance/",
        method="POST",
        json={"id": 7, "name": "Risk acceptance for finding 42"},
        status_code=201,
    )
    result = runner.invoke(
        app,
        [
            "findings",
            "risk-accept",
            "42",
            "--yes",
            "--owner",
            "9",
            "--until",
            "2026-12-31",
            "--reason",
            "Compensating control X",
        ],
    )
    assert result.exit_code == 0, result.output
    assert "Risk-accepted finding 42 (acceptance id=7)" in result.stdout

    sent = httpx_mock.get_request()
    assert sent is not None
    payload = json.loads(sent.read())
    assert payload["accepted_findings"] == [42]
    assert payload["owner"] == 9
    assert payload["decision"] == "A"
    assert payload["reactivate_expired"] is True
    assert payload["expiration_date"] == "2026-12-31T00:00:00Z"
    assert payload["decision_details"] == "Compensating control X"


def test_findings_risk_accept_resolves_owner_via_whoami(
    runner: CliRunner, httpx_mock: HTTPXMock
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/user_profile/",
        json={"user": {"id": 99, "username": "alice"}},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/risk_acceptance/",
        method="POST",
        json={"id": 1},
    )
    result = runner.invoke(app, ["findings", "risk-accept", "42", "--yes"])
    assert result.exit_code == 0, result.output

    risk_request = httpx_mock.get_requests(url="https://dd.example/api/v2/risk_acceptance/")[0]
    payload = json.loads(risk_request.read())
    assert payload["owner"] == 99


def test_findings_risk_accept_keep_expired_flag(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/risk_acceptance/",
        method="POST",
        json={"id": 1},
    )
    result = runner.invoke(
        app,
        [
            "findings",
            "risk-accept",
            "42",
            "--yes",
            "--owner",
            "1",
            "--keep-expired",
        ],
    )
    assert result.exit_code == 0, result.output
    payload = json.loads(httpx_mock.get_request().read())  # type: ignore[union-attr]
    assert payload["reactivate_expired"] is False


def test_findings_risk_accept_invalid_decision(runner: CliRunner) -> None:
    result = runner.invoke(
        app,
        [
            "findings",
            "risk-accept",
            "42",
            "--yes",
            "--owner",
            "1",
            "--decision",
            "Z",
        ],
    )
    assert result.exit_code != 0
    assert result.exception is not None


def test_findings_risk_accept_invalid_until_date(runner: CliRunner) -> None:
    result = runner.invoke(
        app,
        [
            "findings",
            "risk-accept",
            "42",
            "--yes",
            "--owner",
            "1",
            "--until",
            "tomorrow",
            "--dry-run",
        ],
    )
    assert result.exit_code != 0
    assert result.exception is not None


def test_findings_risk_accept_dry_run(runner: CliRunner) -> None:
    result = runner.invoke(
        app,
        [
            "findings",
            "risk-accept",
            "42",
            "--owner",
            "1",
            "--dry-run",
        ],
    )
    assert result.exit_code == 0, result.output
    assert "DRY RUN" in result.stdout
    assert "/api/v2/risk_acceptance/" in result.stdout


# ============================ engagements close / reopen ================= #


def test_engagements_close(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/engagements/100/close/",
        method="POST",
        json={"id": 100, "status": "Completed"},
    )
    result = runner.invoke(app, ["engagements", "close", "100", "--yes"])
    assert result.exit_code == 0, result.output
    assert "Closed engagement 100" in result.stdout

    sent = httpx_mock.get_request()
    assert sent is not None
    assert sent.method == "POST"
    assert json.loads(sent.read()) == {}


def test_engagements_reopen(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/engagements/100/reopen/",
        method="POST",
        json={"id": 100, "status": "In Progress"},
    )
    result = runner.invoke(app, ["engagements", "reopen", "100", "--yes"])
    assert result.exit_code == 0, result.output
    assert "Reopened engagement 100" in result.stdout


def test_engagements_close_dry_run(runner: CliRunner) -> None:
    result = runner.invoke(app, ["engagements", "close", "100", "--dry-run"])
    assert result.exit_code == 0
    assert "DRY RUN" in result.stdout
    assert "POST" in result.stdout
    assert "/api/v2/engagements/100/close/" in result.stdout


# ============================ users deactivate / activate ================ #


def test_users_deactivate_by_id(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/users/5/",
        method="PATCH",
        json={"id": 5, "is_active": False},
    )
    result = runner.invoke(app, ["users", "deactivate", "5", "--yes"])
    assert result.exit_code == 0, result.output
    assert "Deactivated user 5" in result.stdout

    sent = httpx_mock.get_request()
    assert sent is not None
    assert json.loads(sent.read()) == {"is_active": False}


def test_users_activate_by_id(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/users/5/",
        method="PATCH",
        json={"id": 5, "is_active": True},
    )
    result = runner.invoke(app, ["users", "activate", "5", "--yes"])
    assert result.exit_code == 0, result.output
    assert "Activated user 5" in result.stdout

    sent = httpx_mock.get_request()
    assert sent is not None
    assert json.loads(sent.read()) == {"is_active": True}


def test_users_deactivate_by_username(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/users/?username=alice",
        json={"next": None, "results": [{"id": 7, "username": "alice"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/users/7/",
        method="PATCH",
        json={"id": 7, "is_active": False},
    )
    result = runner.invoke(app, ["users", "deactivate", "alice", "--yes"])
    assert result.exit_code == 0, result.output
    assert "Deactivated user 7" in result.stdout


def test_users_deactivate_username_not_found(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/users/?username=ghost",
        json={"next": None, "results": []},
    )
    result = runner.invoke(app, ["users", "deactivate", "ghost", "--yes"])
    assert result.exit_code != 0
    assert result.exception is not None


def test_users_deactivate_dry_run_no_http_for_id(runner: CliRunner) -> None:
    """For numeric IDs we don't need to resolve, so dry-run sends zero requests."""
    result = runner.invoke(app, ["users", "deactivate", "5", "--dry-run"])
    assert result.exit_code == 0, result.output
    assert "DRY RUN" in result.stdout
    assert "PATCH" in result.stdout
    assert "/api/v2/users/5/" in result.stdout


# ============================ edit flow ================================== #


def test_edit_happy_path(
    runner: CliRunner,
    httpx_mock: HTTPXMock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/5/",
        json={"id": 5, "name": "old", "business_criticality": "low"},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/5/",
        method="PATCH",
        json={"id": 5, "name": "new", "business_criticality": "low"},
    )

    def fake_edit(text: str, **kwargs: object) -> str:
        # Simulate the user editing the YAML and saving.
        return text.replace("name: old", "name: new")

    monkeypatch.setattr("typer.edit", fake_edit)

    result = runner.invoke(app, ["products", "edit", "5", "--output", "json"])
    assert result.exit_code == 0, result.output

    patch_request = httpx_mock.get_requests(url="https://dd.example/api/v2/products/5/")[1]
    assert patch_request.method == "PATCH"
    payload = json.loads(patch_request.read())
    # Only the changed field should be in the diff.
    assert payload == {"name": "new"}


def test_edit_no_changes(
    runner: CliRunner,
    httpx_mock: HTTPXMock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/5/",
        json={"id": 5, "name": "same"},
    )
    monkeypatch.setattr("typer.edit", lambda text, **kwargs: text)

    result = runner.invoke(app, ["products", "edit", "5"])
    assert result.exit_code == 0
    assert "No changes" in result.stdout


def test_edit_user_aborts_without_save(
    runner: CliRunner,
    httpx_mock: HTTPXMock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/5/",
        json={"id": 5, "name": "x"},
    )
    monkeypatch.setattr("typer.edit", lambda text, **kwargs: None)

    result = runner.invoke(app, ["products", "edit", "5"])
    assert result.exit_code == 0
    assert "No changes" in result.stdout


def test_edit_invalid_yaml_rejected(
    runner: CliRunner,
    httpx_mock: HTTPXMock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/5/",
        json={"id": 5, "name": "x"},
    )
    monkeypatch.setattr("typer.edit", lambda text, **kwargs: ":\nfoo: [bar")

    result = runner.invoke(app, ["products", "edit", "5"])
    assert result.exit_code != 0
    assert result.exception is not None


def test_edit_dry_run(
    runner: CliRunner,
    httpx_mock: HTTPXMock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/5/",
        json={"id": 5, "name": "old"},
    )
    monkeypatch.setattr("typer.edit", lambda text, **kwargs: text.replace("old", "new"))

    result = runner.invoke(app, ["products", "edit", "5", "--dry-run"])
    assert result.exit_code == 0
    assert "DRY RUN" in result.stdout
    assert "PATCH" in result.stdout
    assert "/api/v2/products/5/" in result.stdout
    # Only one HTTP request should have been made: the GET to fetch current state.
    assert len(httpx_mock.get_requests()) == 1


@pytest.mark.parametrize(
    "resource",
    [
        "products",
        "product-types",
        "engagements",
        "tests",
        "findings",
        "users",
        "dojo-groups",
        "jira-instances",
        "risk-acceptances",
        "metadata",
        "endpoints",
        "finding-templates",
    ],
)
def test_every_resource_has_edit(runner: CliRunner, resource: str) -> None:
    """Sanity: register_crud added `edit` to every sub-app."""
    result = runner.invoke(app, [resource, "edit", "--help"])
    assert result.exit_code == 0, result.output
    assert "$EDITOR" in result.stdout
