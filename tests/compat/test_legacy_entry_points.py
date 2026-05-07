"""Backward-compatibility tests for the legacy ``dd-reimport-findings`` and
``dd-import-languages`` console scripts.

These pin the *contract* the original ``dd-import`` tool exposed:

- All configuration through ``DD_*`` env vars (no CLI flags).
- Print human progress to stdout and errors to stderr.
- Exit 0 on success, **1 on any failure** — irrespective of the typed
  exit codes the new ``dd import findings`` command uses.

The tests invoke the shim entry points directly (rather than spawning a
subprocess) so they exercise the same code path the installed console
scripts run while staying fast.
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest
from pytest_httpx import HTTPXMock

from dd_cli.cli import legacy

pytestmark = pytest.mark.compat


@pytest.fixture(autouse=True)
def _hermetic_env(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Clear all DD_* / DD_CLI_* env vars and isolate config dir."""
    monkeypatch.setenv("DD_CLI_CONFIG_DIR", str(tmp_path))
    for var in list(os.environ.keys()):
        if var.startswith(("DD_", "DD_CLI_")):
            monkeypatch.delenv(var, raising=False)


# ============================ dd-reimport-findings ====================== #


def test_reimport_findings_auto_create_happy_path(
    capsys: pytest.CaptureFixture[str],
    httpx_mock: HTTPXMock,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    """The auto-create flow with DD_AUTO_CREATE_CONTEXT=true matches legacy stdout."""
    scan = tmp_path / "trivy.json"
    scan.write_text("{}")

    monkeypatch.setenv("DD_URL", "https://dd.example")
    monkeypatch.setenv("DD_API_KEY", "the-token")
    monkeypatch.setenv("DD_PRODUCT_TYPE_NAME", "Web")
    monkeypatch.setenv("DD_PRODUCT_NAME", "Payments")
    monkeypatch.setenv("DD_TEST_TYPE_NAME", "Trivy Scan")
    monkeypatch.setenv("DD_FILE_NAME", str(scan))
    monkeypatch.setenv("DD_AUTO_CREATE_CONTEXT", "true")

    httpx_mock.add_response(
        url="https://dd.example/api/v2/reimport-scan/",
        method="POST",
        json={"test": 1, "scan_type": "Trivy Scan"},
    )

    with pytest.raises(SystemExit) as excinfo:
        legacy.dd_reimport_findings_main()
    assert excinfo.value.code == 0

    captured = capsys.readouterr()
    assert "AUTO-CREATE" in captured.out
    assert "Import completed successfully" in captured.out


def test_reimport_findings_traditional_happy_path(
    capsys: pytest.CaptureFixture[str],
    httpx_mock: HTTPXMock,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    scan = tmp_path / "scan.json"
    scan.write_text("{}")

    monkeypatch.setenv("DD_URL", "https://dd.example")
    monkeypatch.setenv("DD_API_KEY", "tok")
    monkeypatch.setenv("DD_PRODUCT_TYPE_NAME", "Web")
    monkeypatch.setenv("DD_PRODUCT_NAME", "Payments")
    monkeypatch.setenv("DD_ENGAGEMENT_NAME", "Q3")
    monkeypatch.setenv("DD_TEST_NAME", "Trivy")
    monkeypatch.setenv("DD_TEST_TYPE_NAME", "Trivy Scan")
    monkeypatch.setenv("DD_FILE_NAME", str(scan))

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
        json={"test": 4},
    )

    with pytest.raises(SystemExit) as excinfo:
        legacy.dd_reimport_findings_main()
    assert excinfo.value.code == 0

    captured = capsys.readouterr()
    assert "TRADITIONAL" in captured.out
    assert "Import completed successfully" in captured.out


def test_reimport_findings_missing_credentials_exits_1(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit) as excinfo:
        legacy.dd_reimport_findings_main()
    assert excinfo.value.code == 1
    captured = capsys.readouterr()
    # legacy contract: errors go to stderr with the ❌ prefix
    assert "❌" in captured.err
    assert "url and/or api_key" in captured.err


def test_reimport_findings_missing_required_envvars_exits_1(
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("DD_URL", "https://dd.example")
    monkeypatch.setenv("DD_API_KEY", "tok")
    # Missing DD_PRODUCT_TYPE_NAME, DD_PRODUCT_NAME, DD_TEST_TYPE_NAME
    with pytest.raises(SystemExit) as excinfo:
        legacy.dd_reimport_findings_main()
    assert excinfo.value.code == 1
    captured = capsys.readouterr()
    assert "❌" in captured.err


def test_reimport_findings_api_error_exits_1(
    capsys: pytest.CaptureFixture[str],
    httpx_mock: HTTPXMock,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    """Even typed errors (400, 401, etc.) exit 1 from the legacy shim."""
    scan = tmp_path / "x.json"
    scan.write_text("{}")
    monkeypatch.setenv("DD_URL", "https://dd.example")
    monkeypatch.setenv("DD_API_KEY", "tok")
    monkeypatch.setenv("DD_PRODUCT_TYPE_NAME", "Web")
    monkeypatch.setenv("DD_PRODUCT_NAME", "Payments")
    monkeypatch.setenv("DD_TEST_TYPE_NAME", "Trivy Scan")
    monkeypatch.setenv("DD_FILE_NAME", str(scan))
    monkeypatch.setenv("DD_AUTO_CREATE_CONTEXT", "true")

    httpx_mock.add_response(
        url="https://dd.example/api/v2/reimport-scan/",
        method="POST",
        status_code=401,
        json={"detail": "Invalid token."},
    )

    with pytest.raises(SystemExit) as excinfo:
        legacy.dd_reimport_findings_main()
    assert excinfo.value.code == 1
    captured = capsys.readouterr()
    assert "❌" in captured.err
    assert "Invalid token" in captured.err


# ============================ dd-import-languages ======================= #


def test_import_languages_happy_path(
    capsys: pytest.CaptureFixture[str],
    httpx_mock: HTTPXMock,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    cloc = tmp_path / "cloc.json"
    cloc.write_text("{}")

    monkeypatch.setenv("DD_URL", "https://dd.example")
    monkeypatch.setenv("DD_API_KEY", "tok")
    monkeypatch.setenv("DD_PRODUCT_TYPE_NAME", "Web")
    monkeypatch.setenv("DD_PRODUCT_NAME", "Payments")
    monkeypatch.setenv("DD_FILE_NAME", str(cloc))

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
        json={"id": 5, "product": 2},
    )

    with pytest.raises(SystemExit) as excinfo:
        legacy.dd_import_languages_main()
    assert excinfo.value.code == 0
    captured = capsys.readouterr()
    assert "Languages imported" in captured.out


def test_import_languages_missing_file_exits_1(
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("DD_URL", "https://dd.example")
    monkeypatch.setenv("DD_API_KEY", "tok")
    monkeypatch.setenv("DD_PRODUCT_TYPE_NAME", "Web")
    monkeypatch.setenv("DD_PRODUCT_NAME", "Payments")
    # Missing DD_FILE_NAME

    with pytest.raises(SystemExit) as excinfo:
        legacy.dd_import_languages_main()
    assert excinfo.value.code == 1


def test_import_languages_missing_credentials_exits_1(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit) as excinfo:
        legacy.dd_import_languages_main()
    assert excinfo.value.code == 1


# ============================ dd-cli vs shim contracts ================== #


def test_shim_uses_exit_1_not_typed_exit_codes(
    capsys: pytest.CaptureFixture[str],
    httpx_mock: HTTPXMock,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    """A 401 from DD: new `dd import findings` exits 3 (AuthError); shim exits 1."""
    scan = tmp_path / "x.json"
    scan.write_text("{}")
    monkeypatch.setenv("DD_URL", "https://dd.example")
    monkeypatch.setenv("DD_API_KEY", "tok")
    monkeypatch.setenv("DD_PRODUCT_TYPE_NAME", "Web")
    monkeypatch.setenv("DD_PRODUCT_NAME", "Payments")
    monkeypatch.setenv("DD_TEST_TYPE_NAME", "Trivy Scan")
    monkeypatch.setenv("DD_FILE_NAME", str(scan))
    monkeypatch.setenv("DD_AUTO_CREATE_CONTEXT", "true")

    httpx_mock.add_response(
        url="https://dd.example/api/v2/reimport-scan/",
        method="POST",
        status_code=401,
        json={"detail": "Bad token."},
    )

    with pytest.raises(SystemExit) as excinfo:
        legacy.dd_reimport_findings_main()
    # Specifically NOT 3 (AuthError exit code) — legacy contract is 1.
    assert excinfo.value.code == 1
