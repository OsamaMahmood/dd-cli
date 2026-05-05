"""Tests for the M2 read-side commands.

Covers the shared `_resource` helpers via behavioural tests against each
sub-app (products / product-types / engagements / tests / findings / users)
and pins table-formatted output via syrupy snapshots.
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
    """Per-test config dir + a complete profile via env vars, no DD_*/DD_CLI_* leakage."""
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


# ---------------------------- products ----------------------------------- #


def test_products_list_renders_table(
    runner: CliRunner, httpx_mock: HTTPXMock, snapshot: object
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/",
        json={
            "next": None,
            "results": [
                {
                    "id": 1,
                    "name": "alpha",
                    "prod_type": 2,
                    "business_criticality": "high",
                    "lifecycle": "production",
                },
                {
                    "id": 2,
                    "name": "beta",
                    "prod_type": 2,
                    "business_criticality": "low",
                    "lifecycle": "construction",
                },
            ],
        },
    )

    result = runner.invoke(app, ["products", "list"])
    assert result.exit_code == 0, result.output
    assert result.stdout == snapshot


def test_products_list_with_filters_passes_params(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/?name=alpha&prod_type=3",
        json={"next": None, "results": []},
    )
    result = runner.invoke(app, ["products", "list", "--name", "alpha", "--prod-type", "3"])
    assert result.exit_code == 0, result.output


def test_products_list_json_output(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/",
        json={
            "next": None,
            "results": [{"id": 1, "name": "x", "prod_type": 2, "business_criticality": "high"}],
        },
    )
    result = runner.invoke(app, ["products", "list", "--output", "json"])
    assert result.exit_code == 0, result.output
    data = json.loads(result.stdout)
    assert data == [
        {
            "id": 1,
            "name": "x",
            "prod_type": 2,
            "business_criticality": "high",
            "lifecycle": None,
        }
    ]


def test_products_get_by_id(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/42/",
        json={"id": 42, "name": "deep-thought", "prod_type": 1},
    )
    result = runner.invoke(app, ["products", "get", "42", "--output", "json"])
    assert result.exit_code == 0, result.output
    body = json.loads(result.stdout)
    assert body["id"] == 42
    assert body["name"] == "deep-thought"


def test_products_get_by_name(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/?name=deep-thought",
        json={
            "next": None,
            "results": [{"id": 42, "name": "deep-thought"}, {"id": 7, "name": "other"}],
        },
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/42/",
        json={"id": 42, "name": "deep-thought", "lifecycle": "production"},
    )
    result = runner.invoke(app, ["products", "get", "--name", "deep-thought", "--output", "json"])
    assert result.exit_code == 0, result.output
    body = json.loads(result.stdout)
    assert body["id"] == 42


def test_products_get_requires_id_or_name(runner: CliRunner) -> None:
    result = runner.invoke(app, ["products", "get"])
    assert result.exit_code != 0
    assert result.exception is not None


def test_products_get_rejects_both_id_and_name(runner: CliRunner) -> None:
    result = runner.invoke(app, ["products", "get", "1", "--name", "x"])
    assert result.exit_code != 0


def test_products_get_by_name_not_found(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/?name=ghost",
        json={"next": None, "results": []},
    )
    result = runner.invoke(app, ["products", "get", "--name", "ghost"])
    assert result.exit_code != 0
    assert result.exception is not None


def test_products_get_by_name_ambiguous(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/?name=dup",
        json={
            "next": None,
            "results": [{"id": 1, "name": "dup"}, {"id": 2, "name": "dup"}],
        },
    )
    result = runner.invoke(app, ["products", "get", "--name", "dup"])
    assert result.exit_code != 0


# ---------------------------- product types ------------------------------- #


def test_product_types_list_table(
    runner: CliRunner, httpx_mock: HTTPXMock, snapshot: object
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/product_types/",
        json={
            "next": None,
            "results": [
                {"id": 1, "name": "Web Apps", "critical_product": True, "key_product": True},
                {"id": 2, "name": "Mobile", "critical_product": False, "key_product": False},
            ],
        },
    )
    result = runner.invoke(app, ["product-types", "list"])
    assert result.exit_code == 0, result.output
    assert result.stdout == snapshot


def test_product_types_get_by_id(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/product_types/3/",
        json={"id": 3, "name": "API"},
    )
    result = runner.invoke(app, ["product-types", "get", "3", "--output", "json"])
    assert result.exit_code == 0, result.output


# ---------------------------- engagements --------------------------------- #


def test_engagements_list_table(runner: CliRunner, httpx_mock: HTTPXMock, snapshot: object) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/engagements/",
        json={
            "next": None,
            "results": [
                {
                    "id": 100,
                    "name": "Q4 Pen Test",
                    "product": 1,
                    "target_start": "2026-01-01",
                    "target_end": "2026-03-31",
                    "status": "In Progress",
                },
            ],
        },
    )
    result = runner.invoke(app, ["engagements", "list"])
    assert result.exit_code == 0, result.output
    assert result.stdout == snapshot


def test_engagements_list_filters_passed(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/engagements/?product=5&status=Completed",
        json={"next": None, "results": []},
    )
    result = runner.invoke(
        app,
        ["engagements", "list", "--product", "5", "--status", "Completed"],
    )
    assert result.exit_code == 0, result.output


# ---------------------------- tests --------------------------------------- #


def test_tests_list_table(runner: CliRunner, httpx_mock: HTTPXMock, snapshot: object) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/tests/",
        json={
            "next": None,
            "results": [
                {
                    "id": 1,
                    "title": "Trivy",
                    "engagement": 100,
                    "test_type": 5,
                    "target_start": "2026-04-01",
                    "target_end": "2026-04-02",
                },
            ],
        },
    )
    result = runner.invoke(app, ["tests", "list"])
    assert result.exit_code == 0, result.output
    assert result.stdout == snapshot


def test_tests_get_by_title(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/tests/?title=Trivy",
        json={"next": None, "results": [{"id": 1, "title": "Trivy"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/tests/1/",
        json={"id": 1, "title": "Trivy", "test_type": 5},
    )
    result = runner.invoke(app, ["tests", "get", "--name", "Trivy", "--output", "json"])
    assert result.exit_code == 0, result.output


# ---------------------------- findings (M2 acceptance) ------------------- #


def test_findings_list_severity_critical_json(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    """M2 acceptance: `dd findings list --severity critical --output json | jq` works."""
    httpx_mock.add_response(
        url="https://dd.example/api/v2/findings/?severity=Critical",
        json={
            "next": None,
            "results": [
                {
                    "id": 1,
                    "title": "SQLi",
                    "severity": "Critical",
                    "active": True,
                    "verified": True,
                    "found_by": [3],
                },
                {
                    "id": 2,
                    "title": "Path Traversal",
                    "severity": "Critical",
                    "active": True,
                    "verified": False,
                    "found_by": [3],
                },
            ],
        },
    )
    result = runner.invoke(
        app,
        ["findings", "list", "--severity", "critical", "--output", "json"],
    )
    assert result.exit_code == 0, result.output
    parsed = json.loads(result.stdout)
    assert isinstance(parsed, list)
    assert {row["severity"] for row in parsed} == {"Critical"}
    assert {row["id"] for row in parsed} == {1, 2}


def test_findings_list_table(runner: CliRunner, httpx_mock: HTTPXMock, snapshot: object) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/findings/?severity=High",
        json={
            "next": None,
            "results": [
                {
                    "id": 9,
                    "title": "XSS",
                    "severity": "High",
                    "active": True,
                    "verified": True,
                    "found_by": [3],
                },
            ],
        },
    )
    result = runner.invoke(app, ["findings", "list", "--severity", "High"])
    assert result.exit_code == 0, result.output
    assert result.stdout == snapshot


def test_findings_severity_normalised_in_request(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    """The CLI canonicalises `critical` -> `Critical` before hitting the API."""
    httpx_mock.add_response(
        url="https://dd.example/api/v2/findings/?severity=Critical",
        json={"next": None, "results": []},
    )
    result = runner.invoke(app, ["findings", "list", "--severity", "critical"])
    assert result.exit_code == 0
    request = httpx_mock.get_request()
    assert request is not None
    # request.url has the encoded params
    assert "severity=Critical" in str(request.url)


def test_findings_severity_invalid_rejected(runner: CliRunner) -> None:
    result = runner.invoke(app, ["findings", "list", "--severity", "Catastrophic"])
    assert result.exit_code != 0
    assert result.exception is not None
    assert "severity" in str(result.exception).lower()


def test_findings_list_with_active_filter(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/findings/?active=true",
        json={"next": None, "results": []},
    )
    result = runner.invoke(app, ["findings", "list", "--active"])
    assert result.exit_code == 0, result.output


# ---------------------------- users --------------------------------------- #


def test_users_list_table(runner: CliRunner, httpx_mock: HTTPXMock, snapshot: object) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/users/",
        json={
            "next": None,
            "results": [
                {
                    "id": 1,
                    "username": "alice",
                    "first_name": "Alice",
                    "last_name": "Anderson",
                    "email": "alice@example.com",
                    "is_active": True,
                },
                {
                    "id": 2,
                    "username": "bob",
                    "first_name": "Bob",
                    "last_name": "Brown",
                    "email": "bob@example.com",
                    "is_active": False,
                },
            ],
        },
    )
    result = runner.invoke(app, ["users", "list"])
    assert result.exit_code == 0, result.output
    assert result.stdout == snapshot


def test_users_get_by_username(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/users/?username=alice",
        json={"next": None, "results": [{"id": 1, "username": "alice"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/users/1/",
        json={"id": 1, "username": "alice", "is_active": True},
    )
    result = runner.invoke(app, ["users", "get", "--name", "alice", "--output", "json"])
    assert result.exit_code == 0, result.output


# ---------------------------- pagination + limits ------------------------ #


def test_list_walks_multiple_pages_when_under_limit(
    runner: CliRunner, httpx_mock: HTTPXMock
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/",
        json={
            "next": "https://dd.example/api/v2/products/?page=2",
            "results": [{"id": i, "name": f"p{i}"} for i in range(1, 11)],
        },
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/?page=2",
        json={
            "next": None,
            "results": [{"id": i, "name": f"p{i}"} for i in range(11, 16)],
        },
    )
    result = runner.invoke(app, ["products", "list", "--output", "json"])
    assert result.exit_code == 0, result.output
    rows = json.loads(result.stdout)
    assert len(rows) == 15  # both pages combined, well under default --limit of 50


def test_list_respects_limit(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/",
        json={
            "next": "https://dd.example/api/v2/products/?page=2",
            "results": [{"id": i, "name": f"p{i}"} for i in range(1, 11)],
        },
    )
    result = runner.invoke(app, ["products", "list", "--limit", "3", "--output", "json"])
    assert result.exit_code == 0, result.output
    rows = json.loads(result.stdout)
    assert len(rows) == 3


# ---------------------------- profile guards ----------------------------- #


def test_list_fails_when_profile_incomplete(
    runner: CliRunner, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.delenv("DD_URL", raising=False)
    monkeypatch.delenv("DD_API_KEY", raising=False)
    result = runner.invoke(app, ["products", "list"])
    assert result.exit_code != 0
    assert result.exception is not None
