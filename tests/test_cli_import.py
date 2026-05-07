"""Tests for `dd import findings` and `dd import languages` Typer commands."""

from __future__ import annotations

import os
from pathlib import Path

import pytest
from pytest_httpx import HTTPXMock
from typer.testing import CliRunner

from dd_cli.cli.app import app


@pytest.fixture(autouse=True)
def isolated_env(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DD_CLI_CONFIG_DIR", str(tmp_path))
    for var in list(os.environ.keys()):
        if var.startswith(("DD_", "DD_CLI_")):
            monkeypatch.delenv(var, raising=False)
    monkeypatch.setenv("DD_URL", "https://dd.example")
    monkeypatch.setenv("DD_API_KEY", "the-token")


def test_import_findings_dry_run_sends_no_http(runner: CliRunner, tmp_path: Path) -> None:
    scan = tmp_path / "trivy.json"
    scan.write_text("{}")

    result = runner.invoke(
        app,
        [
            "import",
            "findings",
            "--file",
            str(scan),
            "--scanner",
            "Trivy Scan",
            "--product-type",
            "Web",
            "--product",
            "Payments",
            "--engagement",
            "Q3",
            "--test-name",
            "Trivy",
            "--dry-run",
        ],
    )
    assert result.exit_code == 0, result.output
    assert "DRY RUN" in result.stdout
    assert "/api/v2/reimport-scan/" in result.stdout
    assert "Trivy Scan" in result.stdout


def test_import_findings_traditional_round_trip(
    runner: CliRunner,
    httpx_mock: HTTPXMock,
    tmp_path: Path,
) -> None:
    scan = tmp_path / "trivy.json"
    scan.write_text("{}")

    httpx_mock.add_response(
        url="https://dd.example/api/v2/product_types/?name=Web",
        json={"next": None, "results": [{"id": 1, "name": "Web"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/?name=Payments&prod_type=1",
        json={"next": None, "results": [{"id": 2, "name": "Payments"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/engagements/?name=Q3&product=2",
        json={"next": None, "results": [{"id": 3, "name": "Q3"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/tests/?title=Trivy&engagement=3",
        json={"next": None, "results": [{"id": 4, "title": "Trivy"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/reimport-scan/",
        method="POST",
        json={
            "test": 4,
            "scan_type": "Trivy Scan",
            "new_finding_count": 2,
            "closed_finding_count": 1,
            "reactivated_finding_count": 0,
        },
    )

    result = runner.invoke(
        app,
        [
            "import",
            "findings",
            "--file",
            str(scan),
            "--scanner",
            "Trivy Scan",
            "--product-type",
            "Web",
            "--product",
            "Payments",
            "--engagement",
            "Q3",
            "--test-name",
            "Trivy",
            "--yes",
        ],
    )
    assert result.exit_code == 0, result.output
    assert "Imported 'Trivy Scan' findings" in result.stdout
    assert "new=2" in result.stdout
    assert "closed=1" in result.stdout


def test_import_findings_auto_create(
    runner: CliRunner,
    httpx_mock: HTTPXMock,
    tmp_path: Path,
) -> None:
    scan = tmp_path / "trivy.json"
    scan.write_text("{}")
    httpx_mock.add_response(
        url="https://dd.example/api/v2/reimport-scan/",
        method="POST",
        json={"test": 9, "scan_type": "Trivy Scan", "new_finding_count": 3},
    )

    result = runner.invoke(
        app,
        [
            "import",
            "findings",
            "--file",
            str(scan),
            "--scanner",
            "Trivy Scan",
            "--product-type",
            "Web",
            "--product",
            "Payments",
            "--auto-create",
            "--yes",
        ],
    )
    assert result.exit_code == 0, result.output
    assert len(httpx_mock.get_requests()) == 1


def test_import_findings_legacy_dd_envvars(
    runner: CliRunner,
    httpx_mock: HTTPXMock,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    """Pinning the M4 backward-compat contract: legacy DD_* envvars drive the new command."""
    scan = tmp_path / "trivy.json"
    scan.write_text("{}")

    monkeypatch.setenv("DD_PRODUCT_TYPE_NAME", "Web")
    monkeypatch.setenv("DD_PRODUCT_NAME", "Payments")
    monkeypatch.setenv("DD_ENGAGEMENT_NAME", "Q3")
    monkeypatch.setenv("DD_TEST_NAME", "Trivy")
    monkeypatch.setenv("DD_TEST_TYPE_NAME", "Trivy Scan")
    monkeypatch.setenv("DD_FILE_NAME", str(scan))
    monkeypatch.setenv("DD_AUTO_CREATE_CONTEXT", "true")

    httpx_mock.add_response(
        url="https://dd.example/api/v2/reimport-scan/",
        method="POST",
        json={"test": 5, "scan_type": "Trivy Scan"},
    )

    # Note: NO CLI flags — everything from env vars
    result = runner.invoke(app, ["import", "findings", "--yes"])
    assert result.exit_code == 0, result.output


def test_import_findings_missing_required_options(runner: CliRunner) -> None:
    result = runner.invoke(app, ["import", "findings", "--yes"])
    assert result.exit_code != 0
    assert result.exception is not None
    assert "Missing required option" in str(result.exception)


def test_import_languages_dry_run(runner: CliRunner, tmp_path: Path) -> None:
    cloc = tmp_path / "cloc.json"
    cloc.write_text("{}")

    result = runner.invoke(
        app,
        [
            "import",
            "languages",
            "--file",
            str(cloc),
            "--product-type",
            "Web",
            "--product",
            "Payments",
            "--dry-run",
        ],
    )
    assert result.exit_code == 0, result.output
    assert "DRY RUN" in result.stdout
    assert "/api/v2/import-languages/" in result.stdout


def test_import_languages_round_trip(
    runner: CliRunner,
    httpx_mock: HTTPXMock,
    tmp_path: Path,
) -> None:
    cloc = tmp_path / "cloc.json"
    cloc.write_text('{"Python": {"code": 100}}')

    httpx_mock.add_response(
        url="https://dd.example/api/v2/product_types/?name=Web",
        json={"next": None, "results": [{"id": 1, "name": "Web"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/?name=Payments&prod_type=1",
        json={"next": None, "results": [{"id": 2, "name": "Payments"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/import-languages/",
        method="POST",
        json={"id": 7, "product": 2},
    )

    result = runner.invoke(
        app,
        [
            "import",
            "languages",
            "--file",
            str(cloc),
            "--product-type",
            "Web",
            "--product",
            "Payments",
            "--yes",
        ],
    )
    assert result.exit_code == 0, result.output
    assert "Languages imported for 'Payments'" in result.stdout


def test_import_findings_aborts_on_n(runner: CliRunner, tmp_path: Path) -> None:
    scan = tmp_path / "trivy.json"
    scan.write_text("{}")

    result = runner.invoke(
        app,
        [
            "import",
            "findings",
            "--file",
            str(scan),
            "--scanner",
            "Trivy Scan",
            "--product-type",
            "Web",
            "--product",
            "Payments",
            "--engagement",
            "Q3",
            "--test-name",
            "Trivy",
        ],
        input="n\n",
    )
    assert result.exit_code == 0
    assert "Aborted" in result.stdout
    # No HTTP requests should have been made.


def test_import_findings_help_text_documents_dd_compat(runner: CliRunner) -> None:
    """Sanity: the import command's help output mentions the DefectDojo concept names."""
    result = runner.invoke(app, ["import", "findings", "--help"])
    assert result.exit_code == 0
    assert "scanner" in result.output.lower()
    assert "auto-create" in result.output.lower()
