"""Tests for the M2b read commands.

Covers the 6 remaining resource sub-apps that ride on the same
`_resource` helper as M2a: dojo-groups, jira-instances, risk-acceptances,
metadata, endpoints, finding-templates.
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


# ---------------------------- dojo-groups -------------------------------- #


def test_dojo_groups_list_table(runner: CliRunner, httpx_mock: HTTPXMock, snapshot: object) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/dojo_groups/",
        json={
            "next": None,
            "results": [
                {
                    "id": 1,
                    "name": "Platform",
                    "description": "Platform engineers",
                    "social_provider": None,
                },
                {
                    "id": 2,
                    "name": "Security",
                    "description": "AppSec team",
                    "social_provider": "AzureAD",
                },
            ],
        },
    )
    result = runner.invoke(app, ["dojo-groups", "list"])
    assert result.exit_code == 0, result.output
    assert result.stdout == snapshot


def test_dojo_groups_list_with_filters(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/dojo_groups/?name=Security&social_provider=AzureAD",
        json={"next": None, "results": []},
    )
    result = runner.invoke(
        app,
        ["dojo-groups", "list", "--name", "Security", "--social-provider", "AzureAD"],
    )
    assert result.exit_code == 0, result.output


def test_dojo_groups_get_by_id(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/dojo_groups/5/",
        json={"id": 5, "name": "Platform"},
    )
    result = runner.invoke(app, ["dojo-groups", "get", "5", "--output", "json"])
    assert result.exit_code == 0, result.output
    body = json.loads(result.stdout)
    assert body["id"] == 5


# ---------------------------- jira-instances ----------------------------- #


def test_jira_instances_list_table(
    runner: CliRunner, httpx_mock: HTTPXMock, snapshot: object
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/jira_instances/",
        json={
            "next": None,
            "results": [
                {
                    "id": 1,
                    "configuration_name": "Main Jira",
                    "url": "https://example.atlassian.net",
                    "username": "appsec-bot",
                    "default_issue_type": "Bug",
                },
            ],
        },
    )
    result = runner.invoke(app, ["jira-instances", "list"])
    assert result.exit_code == 0, result.output
    assert result.stdout == snapshot


def test_jira_instances_get_by_configuration_name(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/jira_instances/?configuration_name=Main+Jira",
        json={"next": None, "results": [{"id": 1, "configuration_name": "Main Jira"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/jira_instances/1/",
        json={"id": 1, "configuration_name": "Main Jira", "url": "https://x"},
    )
    result = runner.invoke(
        app,
        ["jira-instances", "get", "--name", "Main Jira", "--output", "json"],
    )
    assert result.exit_code == 0, result.output


# ---------------------------- risk-acceptances --------------------------- #


def test_risk_acceptances_list_table(
    runner: CliRunner, httpx_mock: HTTPXMock, snapshot: object
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/risk_acceptance/",
        json={
            "next": None,
            "results": [
                {
                    "id": 11,
                    "name": "Payment service deferral",
                    "owner": 7,
                    "decision": "Accept",
                    "expiration_date": "2026-09-30",
                    "reactivate_expired": True,
                },
            ],
        },
    )
    result = runner.invoke(app, ["risk-acceptances", "list"])
    assert result.exit_code == 0, result.output
    assert result.stdout == snapshot


def test_risk_acceptances_list_with_filters(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/risk_acceptance/?owner=7&decision=Accept",
        json={"next": None, "results": []},
    )
    result = runner.invoke(
        app,
        ["risk-acceptances", "list", "--owner", "7", "--decision", "Accept"],
    )
    assert result.exit_code == 0, result.output


def test_risk_acceptances_reactivate_expired_filter(
    runner: CliRunner, httpx_mock: HTTPXMock
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/risk_acceptance/?reactivate_expired=true",
        json={"next": None, "results": []},
    )
    result = runner.invoke(app, ["risk-acceptances", "list", "--reactivate-expired"])
    assert result.exit_code == 0, result.output


# ---------------------------- metadata ----------------------------------- #


def test_metadata_list_table(runner: CliRunner, httpx_mock: HTTPXMock, snapshot: object) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/metadata/",
        json={
            "next": None,
            "results": [
                {
                    "id": 1,
                    "name": "service_tier",
                    "value": "tier-1",
                    "product": 5,
                    "finding": None,
                    "endpoint": None,
                },
                {
                    "id": 2,
                    "name": "owner_team",
                    "value": "platform",
                    "product": 5,
                    "finding": None,
                    "endpoint": None,
                },
            ],
        },
    )
    result = runner.invoke(app, ["metadata", "list"])
    assert result.exit_code == 0, result.output
    assert result.stdout == snapshot


def test_metadata_list_filtered_by_product(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/metadata/?name=service_tier&product=5",
        json={"next": None, "results": []},
    )
    result = runner.invoke(
        app,
        ["metadata", "list", "--name", "service_tier", "--product", "5"],
    )
    assert result.exit_code == 0, result.output


# ---------------------------- endpoints ---------------------------------- #


def test_endpoints_list_table(runner: CliRunner, httpx_mock: HTTPXMock, snapshot: object) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/endpoints/",
        json={
            "next": None,
            "results": [
                {
                    "id": 1,
                    "host": "api.example.com",
                    "port": 443,
                    "path": "/v1/users",
                    "protocol": "https",
                    "product": 5,
                },
                {
                    "id": 2,
                    "host": "admin.example.com",
                    "port": 443,
                    "path": "/login",
                    "protocol": "https",
                    "product": 5,
                },
            ],
        },
    )
    result = runner.invoke(app, ["endpoints", "list"])
    assert result.exit_code == 0, result.output
    assert result.stdout == snapshot


def test_endpoints_list_with_host_filter(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/endpoints/?host=api.example.com&product=5",
        json={"next": None, "results": []},
    )
    result = runner.invoke(
        app,
        ["endpoints", "list", "--host", "api.example.com", "--product", "5"],
    )
    assert result.exit_code == 0, result.output


def test_endpoints_get_by_host(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/endpoints/?host=api.example.com",
        json={
            "next": None,
            "results": [{"id": 1, "host": "api.example.com"}],
        },
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/endpoints/1/",
        json={"id": 1, "host": "api.example.com", "port": 443},
    )
    result = runner.invoke(
        app,
        ["endpoints", "get", "--name", "api.example.com", "--output", "json"],
    )
    assert result.exit_code == 0, result.output


# ---------------------------- finding-templates -------------------------- #


def test_finding_templates_list_table(
    runner: CliRunner, httpx_mock: HTTPXMock, snapshot: object
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/finding_templates/",
        json={
            "next": None,
            "results": [
                {
                    "id": 1,
                    "title": "SQL Injection",
                    "severity": "High",
                    "cwe": 89,
                    "tags": ["owasp", "injection"],
                },
            ],
        },
    )
    result = runner.invoke(app, ["finding-templates", "list"])
    assert result.exit_code == 0, result.output
    assert result.stdout == snapshot


def test_finding_templates_severity_normalised(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/finding_templates/?severity=Critical",
        json={"next": None, "results": []},
    )
    result = runner.invoke(app, ["finding-templates", "list", "--severity", "critical"])
    assert result.exit_code == 0, result.output
    request = httpx_mock.get_request()
    assert request is not None
    assert "severity=Critical" in str(request.url)


def test_finding_templates_severity_invalid(runner: CliRunner) -> None:
    result = runner.invoke(app, ["finding-templates", "list", "--severity", "Catastrophic"])
    assert result.exit_code != 0
    assert result.exception is not None


def test_finding_templates_cwe_filter(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/finding_templates/?cwe=89",
        json={"next": None, "results": []},
    )
    result = runner.invoke(app, ["finding-templates", "list", "--cwe", "89"])
    assert result.exit_code == 0, result.output


# ---------------------------- shared helpers behaviour ------------------- #


def test_get_requires_id_or_name_for_each_resource(runner: CliRunner) -> None:
    """Sanity: each new sub-app uses get_dispatch correctly."""
    for resource in (
        "dojo-groups",
        "jira-instances",
        "risk-acceptances",
        "metadata",
        "endpoints",
        "finding-templates",
    ):
        result = runner.invoke(app, [resource, "get"])
        assert result.exit_code != 0, f"{resource} get should fail without id or --name"
