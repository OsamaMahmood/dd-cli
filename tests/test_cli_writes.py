"""Tests for the M3a write commands (create / update / delete + safety rails).

Covers the shared helpers and a representative slice of resources end-to-end
via pytest-httpx. The round-trip test pins the M3 acceptance criterion:
`create -> update -> delete` works against mocked HTTP for every CRUD verb.
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


# ---------------------------- create ------------------------------------ #


def test_create_via_fields_only(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/",
        method="POST",
        json={"id": 99, "name": "shiny", "prod_type": 2},
        status_code=201,
    )
    result = runner.invoke(
        app,
        [
            "products",
            "create",
            "--field",
            "name=shiny",
            "--field",
            "prod_type=2",
            "--output",
            "json",
        ],
    )
    assert result.exit_code == 0, result.output
    body = json.loads(result.stdout)
    assert body["id"] == 99

    sent = httpx_mock.get_request()
    assert sent is not None
    assert sent.method == "POST"
    payload = json.loads(sent.read())
    # `prod_type=2` is JSON-coerced to int, not the string "2"
    assert payload == {"name": "shiny", "prod_type": 2}


def test_create_via_from_file_yaml(
    runner: CliRunner, httpx_mock: HTTPXMock, tmp_path: Path
) -> None:
    payload_file = tmp_path / "product.yaml"
    payload_file.write_text(
        "name: payments\nprod_type: 2\nbusiness_criticality: high\n",
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/",
        method="POST",
        json={"id": 1, "name": "payments"},
    )
    result = runner.invoke(app, ["products", "create", "--from-file", str(payload_file)])
    assert result.exit_code == 0, result.output

    sent = httpx_mock.get_request()
    assert sent is not None
    assert json.loads(sent.read()) == {
        "name": "payments",
        "prod_type": 2,
        "business_criticality": "high",
    }


def test_create_field_overrides_file(
    runner: CliRunner, httpx_mock: HTTPXMock, tmp_path: Path
) -> None:
    base = tmp_path / "base.json"
    base.write_text(json.dumps({"name": "from-file", "prod_type": 1}))
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/",
        method="POST",
        json={"id": 1},
    )
    result = runner.invoke(
        app,
        [
            "products",
            "create",
            "--from-file",
            str(base),
            "--field",
            "name=overridden",
        ],
    )
    assert result.exit_code == 0, result.output

    sent = httpx_mock.get_request()
    assert sent is not None
    payload = json.loads(sent.read())
    assert payload["name"] == "overridden"  # field beats file
    assert payload["prod_type"] == 1  # file value preserved


def test_create_dry_run_sends_no_http(runner: CliRunner) -> None:
    """--dry-run must not contact the server (no HTTPX mock = test fails if it tries)."""
    result = runner.invoke(
        app,
        [
            "products",
            "create",
            "--field",
            "name=dry",
            "--dry-run",
            "--output",
            "json",
        ],
    )
    assert result.exit_code == 0, result.output
    assert "DRY RUN" in result.stdout
    assert "POST" in result.stdout
    assert "/api/v2/products/" in result.stdout


def test_create_without_payload_fails(runner: CliRunner) -> None:
    result = runner.invoke(app, ["products", "create"])
    assert result.exit_code != 0
    assert result.exception is not None


def test_create_with_invalid_field_format_fails(runner: CliRunner) -> None:
    result = runner.invoke(app, ["products", "create", "--field", "no-equals"])
    assert result.exit_code != 0
    assert result.exception is not None


def test_create_with_missing_file_fails(runner: CliRunner, tmp_path: Path) -> None:
    result = runner.invoke(
        app,
        ["products", "create", "--from-file", str(tmp_path / "ghost.json")],
    )
    assert result.exit_code != 0


# ---------------------------- update ------------------------------------ #


def test_update_via_field(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/findings/42/",
        method="PATCH",
        json={"id": 42, "severity": "Low", "active": False},
    )
    result = runner.invoke(
        app,
        [
            "findings",
            "update",
            "42",
            "--field",
            "severity=Low",
            "--field",
            "active=false",
            "--output",
            "json",
        ],
    )
    assert result.exit_code == 0, result.output

    sent = httpx_mock.get_request()
    assert sent is not None
    assert sent.method == "PATCH"
    payload = json.loads(sent.read())
    assert payload == {"severity": "Low", "active": False}


def test_update_dry_run_sends_no_http(runner: CliRunner) -> None:
    result = runner.invoke(
        app,
        [
            "products",
            "update",
            "5",
            "--field",
            "name=renamed",
            "--dry-run",
        ],
    )
    assert result.exit_code == 0, result.output
    assert "DRY RUN" in result.stdout
    assert "PATCH" in result.stdout
    assert "/api/v2/products/5/" in result.stdout


def test_update_without_payload_fails(runner: CliRunner) -> None:
    result = runner.invoke(app, ["products", "update", "5"])
    assert result.exit_code != 0


# ---------------------------- delete ------------------------------------ #


def test_delete_with_yes_skips_prompt(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/7/",
        method="DELETE",
        status_code=204,
    )
    result = runner.invoke(app, ["products", "delete", "7", "--yes"])
    assert result.exit_code == 0, result.output
    assert "Deleted product 7" in result.stdout


def test_delete_prompts_and_aborts_on_n(runner: CliRunner) -> None:
    """Without --yes, the prompt fires; answering 'n' aborts with no HTTP."""
    result = runner.invoke(app, ["products", "delete", "7"], input="n\n")
    assert result.exit_code == 0
    assert "Aborted" in result.stdout


def test_delete_prompts_and_proceeds_on_y(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/7/",
        method="DELETE",
        status_code=204,
    )
    result = runner.invoke(app, ["products", "delete", "7"], input="y\n")
    assert result.exit_code == 0, result.output
    assert "Deleted product 7" in result.stdout


def test_delete_dry_run_sends_no_http(runner: CliRunner) -> None:
    result = runner.invoke(app, ["products", "delete", "7", "--dry-run"])
    assert result.exit_code == 0, result.output
    assert "DRY RUN" in result.stdout
    assert "DELETE" in result.stdout
    assert "/api/v2/products/7/" in result.stdout


def test_delete_404_maps_to_not_found(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/9999/",
        method="DELETE",
        status_code=404,
        json={"detail": "Not found."},
    )
    result = runner.invoke(app, ["products", "delete", "9999", "--yes"])
    assert result.exit_code != 0
    assert result.exception is not None


# ---------------------------- M3 acceptance: round trip ----------------- #


def test_round_trip_create_update_delete(runner: CliRunner, httpx_mock: HTTPXMock) -> None:
    """M3 acceptance: create -> update -> delete on the same resource works end to end."""
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/",
        method="POST",
        json={"id": 123, "name": "round-trip", "prod_type": 2},
        status_code=201,
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/123/",
        method="PATCH",
        json={"id": 123, "name": "round-trip-renamed", "prod_type": 2},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/123/",
        method="DELETE",
        status_code=204,
    )

    create = runner.invoke(
        app,
        [
            "products",
            "create",
            "--field",
            "name=round-trip",
            "--field",
            "prod_type=2",
            "--output",
            "json",
        ],
    )
    assert create.exit_code == 0, create.output
    created = json.loads(create.stdout)
    assert created["id"] == 123

    update = runner.invoke(
        app,
        [
            "products",
            "update",
            str(created["id"]),
            "--field",
            "name=round-trip-renamed",
            "--output",
            "json",
        ],
    )
    assert update.exit_code == 0, update.output
    assert json.loads(update.stdout)["name"] == "round-trip-renamed"

    delete = runner.invoke(app, ["products", "delete", str(created["id"]), "--yes"])
    assert delete.exit_code == 0, delete.output
    assert "Deleted product 123" in delete.stdout


# ---------------------------- breadth check ------------------------------ #


@pytest.mark.parametrize(
    ("resource", "path"),
    [
        ("products", "/api/v2/products/"),
        ("product-types", "/api/v2/product_types/"),
        ("engagements", "/api/v2/engagements/"),
        ("tests", "/api/v2/tests/"),
        ("findings", "/api/v2/findings/"),
        ("users", "/api/v2/users/"),
        ("dojo-groups", "/api/v2/dojo_groups/"),
        ("jira-instances", "/api/v2/jira_instances/"),
        ("risk-acceptances", "/api/v2/risk_acceptance/"),
        ("metadata", "/api/v2/metadata/"),
        ("endpoints", "/api/v2/endpoints/"),
        ("finding-templates", "/api/v2/finding_templates/"),
    ],
)
def test_each_resource_has_create_update_delete(
    runner: CliRunner, resource: str, path: str
) -> None:
    """Sanity: every M2 resource gained the M3 write trio."""
    for verb, expected_method in [
        ("create", "POST"),
        ("update", "PATCH"),
        ("delete", "DELETE"),
    ]:
        if verb == "delete":
            args = [resource, verb, "1", "--dry-run"]
        else:
            args = (
                [resource, verb]
                + (["1"] if verb == "update" else [])
                + [
                    "--field",
                    "name=x",
                    "--dry-run",
                ]
            )
        result = runner.invoke(app, args)
        assert result.exit_code == 0, f"{resource} {verb} failed: {result.output}"
        assert expected_method in result.stdout
        assert path in result.stdout
