"""CLI-level tests for `dd report generate`.

These mock the full endpoint chain (`products` → `engagements` → `tests`
→ `findings` → ancillary lookups) and assert the on-disk reports end up
where they should with the right contents. The `--detailed`,
`--with-history`, and `--sample` paths get their own test groups below.
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


# ---------------------------- --format ------------------------------------ #


def test_report_default_format_writes_md_and_html(
    runner: CliRunner, httpx_mock: HTTPXMock, tmp_path: Path
) -> None:
    _mock_one_product_one_engagement_one_test(httpx_mock)
    out_dir = tmp_path / "reports"

    result = runner.invoke(
        app, ["report", "generate", "--product", "42", "--output-dir", str(out_dir)]
    )
    assert result.exit_code == 0, result.output
    assert (out_dir / "42-payments.md").exists()
    assert (out_dir / "42-payments.html").exists()


def test_report_format_html_writes_html_only(
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
            "--format",
            "html",
        ],
    )
    assert result.exit_code == 0, result.output
    assert (out_dir / "42-payments.html").exists()
    assert not (out_dir / "42-payments.md").exists()


def test_report_format_md_writes_md_only(
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
            "--format",
            "md",
        ],
    )
    assert result.exit_code == 0, result.output
    assert (out_dir / "42-payments.md").exists()
    assert not (out_dir / "42-payments.html").exists()


# ---------------------------- --detailed ---------------------------------- #


def test_report_detailed_fetches_notes_jira_endpoint_status(
    runner: CliRunner, httpx_mock: HTTPXMock, tmp_path: Path
) -> None:
    _mock_one_product_one_engagement_one_test(httpx_mock)
    # The single finding (id=1) triggers 3 extra fan-out reads under --detailed.
    httpx_mock.add_response(
        url="https://dd.example/api/v2/findings/1/notes/",
        json={
            "results": [
                {"id": 5, "entry": "Triage: investigated", "date": "2026-04-22"},
            ]
        },
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/jira_finding_mappings/?finding=1",
        json={
            "next": None,
            "results": [{"id": 1, "jira_key": "SEC-100", "url": "https://jira/SEC-100"}],
        },
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/endpoint_status/?finding=1",
        json={"next": None, "results": [{"id": 1, "endpoint": "https://x.example/login"}]},
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
            "--detailed",
            "--format",
            "md",
        ],
    )
    assert result.exit_code == 0, result.output
    body = (tmp_path / "r" / "42-payments.md").read_text()
    # The detailed sections in the template render Jira keys and endpoint blocks.
    assert "SEC-100" in body
    assert "https://x.example/login" in body
    assert "Triage: investigated" in body


# ---------------------------- --with-history ------------------------------ #


def test_report_with_history_fetches_test_imports(
    runner: CliRunner, httpx_mock: HTTPXMock, tmp_path: Path
) -> None:
    _mock_one_product_one_engagement_one_test(httpx_mock)
    httpx_mock.add_response(
        url="https://dd.example/api/v2/test_imports/?test=10",
        json={
            "next": None,
            "results": [
                {
                    "id": 1,
                    "created": "2026-04-20T00:00:00Z",
                    "build_id": "ci-1842",
                    "commit_hash": "abc1234",
                    "branch_tag": "main",
                    "test_import_finding_action_set": [
                        {"action": "Created"},
                        {"action": "Untouched"},
                    ],
                },
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
            "--with-history",
            "--format",
            "md",
        ],
    )
    assert result.exit_code == 0, result.output
    body = (tmp_path / "r" / "42-payments.md").read_text()
    assert "Scan delta" in body
    assert "ci-1842" in body or "abc1234" in body or "main" in body


# ---------------------------- --sample ------------------------------------- #


def test_report_sample_renders_without_api(runner: CliRunner, tmp_path: Path) -> None:
    """--sample skips the API entirely; httpx_mock would fail on any request."""
    result = runner.invoke(
        app,
        [
            "report",
            "generate",
            "--sample",
            "--output-dir",
            str(tmp_path / "r"),
        ],
    )
    assert result.exit_code == 0, result.output
    out_dir = tmp_path / "r"
    assert (out_dir / "sample-report.md").exists()
    assert (out_dir / "sample-report.html").exists()
    md = (out_dir / "sample-report.md").read_text()
    assert "sample-app" in md  # the bundled product fixture's name


def test_report_sample_honours_test_filter(runner: CliRunner, tmp_path: Path) -> None:
    result = runner.invoke(
        app,
        [
            "report",
            "generate",
            "--sample",
            "--output-dir",
            str(tmp_path / "r"),
            "--test",
            "SAST",
            "--format",
            "md",
        ],
    )
    assert result.exit_code == 0, result.output
    files = list((tmp_path / "r").glob("*.md"))
    assert len(files) == 1
    assert "sast" in files[0].name.lower()


def test_report_sample_no_match_errors(runner: CliRunner, tmp_path: Path) -> None:
    result = runner.invoke(
        app,
        [
            "report",
            "generate",
            "--sample",
            "--output-dir",
            str(tmp_path / "r"),
            "--test",
            "no-such-scanner",
        ],
    )
    assert result.exit_code != 0
    assert isinstance(result.exception, ValidationError)
    assert "No sample tests matched" in result.exception.message


def test_report_sample_with_detailed_and_history(runner: CliRunner, tmp_path: Path) -> None:
    """--detailed + --with-history with --sample exercise the fixture loaders for those fields."""
    result = runner.invoke(
        app,
        [
            "report",
            "generate",
            "--sample",
            "--detailed",
            "--with-history",
            "--output-dir",
            str(tmp_path / "r"),
            "--format",
            "md",
        ],
    )
    assert result.exit_code == 0, result.output
    body = (tmp_path / "r" / "sample-report.md").read_text()
    # The bundled fixtures include at least one finding with notes and one
    # with a scan-delta block; both should appear when both flags are on.
    assert "Scan delta" in body


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
