"""CLI-level tests for `dd report` (M6a — Markdown only).

These mock the full endpoint chain (`products` → `engagements` → `tests`
→ `findings` → ancillary lookups) and assert the on-disk Markdown ends
up where it should with the right contents.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest
from pytest_httpx import HTTPXMock
from typer.testing import CliRunner

from dd_cli.cli.app import app
from dd_cli.errors import AuthError, NotFoundError, ValidationError


@pytest.fixture(autouse=True)
def isolated_env(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Per-test config dir + a known profile via env, no DD_*/DD_CLI_* leakage."""
    monkeypatch.setenv("DD_CLI_CONFIG_DIR", str(tmp_path))
    for var in (
        "DD_URL",
        "DD_API_KEY",
        "DD_API_TOKEN",
        "DD_CLI_URL",
        "DD_CLI_API_KEY",
        "DD_CLI_PROFILE",
        "DD_PROFILE",
    ):
        monkeypatch.delenv(var, raising=False)
    monkeypatch.setenv("DD_URL", "https://dd.example")
    monkeypatch.setenv("DD_API_KEY", "the-token")


def _mock_one_product_one_engagement_one_test(
    httpx_mock: HTTPXMock,
    *,
    product_id: int = 42,
    engagement_id: int = 1,
    test_id: int = 10,
    test_type_id: int = 100,
    test_type_name: str = "Trivy Scan",
) -> None:
    """Stub out the standard happy-path endpoint chain for a single product."""
    httpx_mock.add_response(
        url=f"https://dd.example/api/v2/products/{product_id}/",
        json={"id": product_id, "name": "Payments", "business_criticality": "high"},
    )
    httpx_mock.add_response(
        url=f"https://dd.example/api/v2/engagements/?product={product_id}&active=true",
        json={
            "next": None,
            "results": [{"id": engagement_id, "name": "Q4 2026", "status": "In Progress"}],
        },
    )
    httpx_mock.add_response(
        url=f"https://dd.example/api/v2/tests/?engagement={engagement_id}",
        json={
            "next": None,
            "results": [
                {
                    "id": test_id,
                    "test_type": test_type_id,
                    "test_type_name": test_type_name,
                    "scan_type": test_type_name,
                }
            ],
        },
    )
    httpx_mock.add_response(
        url=f"https://dd.example/api/v2/findings/?test={test_id}&active=true",
        json={
            "next": None,
            "results": [
                {
                    "id": 1,
                    "title": "Hard-coded credential",
                    "severity": "High",
                    "age": 21,
                    "sla_days_remaining": -1,
                    "date": "2026-04-20",
                }
            ],
        },
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/sla_configurations/",
        json={"next": None, "results": []},
    )
    httpx_mock.add_response(
        url=f"https://dd.example/api/v2/risk_acceptance/?engagement__product={product_id}",
        json={"next": None, "results": []},
    )


# ---------------------------- happy path ----------------------------------- #


def test_report_writes_markdown_for_product(
    runner: CliRunner, httpx_mock: HTTPXMock, tmp_path: Path
) -> None:
    _mock_one_product_one_engagement_one_test(httpx_mock)
    out_dir = tmp_path / "reports"

    result = runner.invoke(
        app,
        ["report", "generate", "--product", "42", "--output-dir", str(out_dir)],
    )

    assert result.exit_code == 0, result.output
    md = out_dir / "42-payments.md"
    assert md.exists()
    body = md.read_text(encoding="utf-8")
    assert "# Security Report — Payments" in body
    assert "Hard-coded credential" in body
    assert "**Generated:**" in body


def test_report_filename_includes_test_filter_slug(
    runner: CliRunner, httpx_mock: HTTPXMock, tmp_path: Path
) -> None:
    _mock_one_product_one_engagement_one_test(httpx_mock)
    out_dir = tmp_path / "reports"

    result = runner.invoke(
        app,
        [
            "report",
            "generate",
            "--product",
            "42",
            "--output-dir",
            str(out_dir),
            "--test",
            "Trivy",
        ],
    )

    assert result.exit_code == 0, result.output
    files = list(out_dir.glob("*.md"))
    assert len(files) == 1
    assert "trivy" in files[0].name.lower()


def test_report_creates_output_dir_when_missing(
    runner: CliRunner, httpx_mock: HTTPXMock, tmp_path: Path
) -> None:
    _mock_one_product_one_engagement_one_test(httpx_mock)
    out_dir = tmp_path / "nested" / "dir" / "reports"
    assert not out_dir.exists()

    result = runner.invoke(
        app,
        ["report", "generate", "--product", "42", "--output-dir", str(out_dir)],
    )

    assert result.exit_code == 0, result.output
    assert out_dir.is_dir()


# ---------------------------- input validation ----------------------------- #


def test_report_without_product_id_errors(
    runner: CliRunner, httpx_mock: HTTPXMock, tmp_path: Path
) -> None:
    result = runner.invoke(app, ["report", "generate", "--output-dir", str(tmp_path)])
    assert result.exit_code != 0
    assert isinstance(result.exception, ValidationError)
    assert "Provide --product ID" in result.exception.message


def test_report_with_test_filter_that_matches_nothing_errors(
    runner: CliRunner, httpx_mock: HTTPXMock, tmp_path: Path
) -> None:
    # The flow short-circuits at the filter check — only products/engagements/tests
    # are fetched, not findings/SLA/risk_acceptance. Don't mock what won't run.
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/42/",
        json={"id": 42, "name": "Payments"},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/engagements/?product=42&active=true",
        json={"next": None, "results": [{"id": 1, "name": "Q4 2026"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/tests/?engagement=1",
        json={
            "next": None,
            "results": [
                {
                    "id": 10,
                    "test_type": 100,
                    "scan_type": "Trivy Scan",
                    "test_type_name": "Trivy Scan",
                }
            ],
        },
    )

    result = runner.invoke(
        app,
        [
            "report",
            "generate",
            "--product",
            "42",
            "--output-dir",
            str(tmp_path / "r"),
            "--test",
            "no-such-scanner",
        ],
    )
    assert result.exit_code != 0
    assert isinstance(result.exception, ValidationError)
    assert re.search(r"no tests matched filter", result.exception.message.lower())


def test_report_m6b_flags_rejected_for_now(runner: CliRunner, tmp_path: Path) -> None:
    result = runner.invoke(
        app,
        [
            "report",
            "generate",
            "--product",
            "42",
            "--output-dir",
            str(tmp_path / "r"),
            "--detailed",
        ],
    )
    assert result.exit_code != 0
    assert isinstance(result.exception, ValidationError)
    assert "M6b" in result.exception.message


# ---------------------------- typed errors --------------------------------- #
#
# CliRunner.invoke goes through the Typer app directly (not the cli/app.py:main
# wrapper that maps DDCliError to typed exit codes), so we assert on the
# exception class. Exit-code mapping itself is covered by tests/test_errors.py.


def test_report_auth_error_raises_auth_error(
    runner: CliRunner, httpx_mock: HTTPXMock, tmp_path: Path
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/42/",
        status_code=401,
        json={"detail": "Invalid token."},
    )
    result = runner.invoke(
        app,
        ["report", "generate", "--product", "42", "--output-dir", str(tmp_path / "r")],
    )
    assert result.exit_code != 0
    assert isinstance(result.exception, AuthError)
    assert "Invalid token" in result.exception.message


def test_report_not_found_raises_not_found(
    runner: CliRunner, httpx_mock: HTTPXMock, tmp_path: Path
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/99/",
        status_code=404,
        json={"detail": "Not found."},
    )
    result = runner.invoke(
        app,
        ["report", "generate", "--product", "99", "--output-dir", str(tmp_path / "r")],
    )
    assert result.exit_code != 0
    assert isinstance(result.exception, NotFoundError)
