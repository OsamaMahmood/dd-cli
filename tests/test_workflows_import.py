"""Unit tests for the M4a import workflows.

Exercises both ImportFindingsWorkflow (traditional + auto-create) and
ImportLanguagesWorkflow against pytest-httpx mocks. The DD_* env-var
alias contract is also pinned here so the M4b legacy console-script
shim can rely on it.
"""

from __future__ import annotations

import json
from collections.abc import Iterator
from pathlib import Path

import pytest
from pytest_httpx import HTTPXMock

from dd_cli.client import DefectDojoClient
from dd_cli.config import Profile
from dd_cli.errors import ConfigError, ValidationError
from dd_cli.workflows.import_findings import (
    ImportFindingsOptions,
    ImportFindingsWorkflow,
)
from dd_cli.workflows.import_languages import (
    ImportLanguagesOptions,
    ImportLanguagesWorkflow,
)


@pytest.fixture(autouse=True)
def _clear_dd_env(monkeypatch: pytest.MonkeyPatch) -> None:
    """Clear every DD_* and DD_CLI_* env var so tests are hermetic."""
    for var in list(__import__("os").environ.keys()):
        if var.startswith(("DD_", "DD_CLI_")):
            monkeypatch.delenv(var, raising=False)


@pytest.fixture
def profile() -> Profile:
    return Profile(
        url="https://dd.example",
        api_key="the-token",  # type: ignore[arg-type]
        ssl_verify=True,
    )


@pytest.fixture
def client(profile: Profile) -> Iterator[DefectDojoClient]:
    c = DefectDojoClient(profile, sleep=lambda _: None)
    return c


# ============================ ImportFindingsOptions ===================== #


def test_findings_options_reads_legacy_dd_envvars(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DD_PRODUCT_TYPE_NAME", "Web")
    monkeypatch.setenv("DD_PRODUCT_NAME", "Payments")
    monkeypatch.setenv("DD_ENGAGEMENT_NAME", "Q3 Pen Test")
    monkeypatch.setenv("DD_TEST_TYPE_NAME", "Trivy Scan")
    monkeypatch.setenv("DD_TEST_NAME", "Trivy")
    monkeypatch.setenv("DD_AUTO_CREATE_CONTEXT", "true")
    monkeypatch.setenv("DD_FILE_NAME", "/tmp/scan.json")
    monkeypatch.setenv("DD_PUSH_TO_JIRA", "false")
    opts = ImportFindingsOptions()
    assert opts.product_type_name == "Web"
    assert opts.product_name == "Payments"
    assert opts.engagement_name == "Q3 Pen Test"
    assert opts.scanner == "Trivy Scan"
    assert opts.test_name == "Trivy"
    assert opts.auto_create_context is True
    assert opts.push_to_jira is False
    assert str(opts.file) == "/tmp/scan.json"


def test_findings_options_dd_cli_takes_precedence(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("DD_PRODUCT_NAME", "legacy-only")
    monkeypatch.setenv("DD_CLI_PRODUCT", "new-style")
    opts = ImportFindingsOptions()
    assert opts.product_name == "new-style"


# ============================ traditional flow ========================== #


def _trad_opts(file_path: Path) -> ImportFindingsOptions:
    return ImportFindingsOptions(
        product_type_name="Web Apps",
        product_name="Payments",
        engagement_name="Q3 Pen Test",
        scanner="Trivy Scan",
        test_name="Trivy",
        file=file_path,
    )


def test_findings_traditional_creates_resources_when_missing(
    client: DefectDojoClient,
    httpx_mock: HTTPXMock,
    tmp_path: Path,
) -> None:
    scan_file = tmp_path / "trivy.json"
    scan_file.write_text("{}")

    # find product type → empty list, then POST to create
    httpx_mock.add_response(
        url="https://dd.example/api/v2/product_types/?name=Web+Apps",
        json={"next": None, "results": []},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/product_types/",
        method="POST",
        json={"id": 11, "name": "Web Apps"},
    )
    # find product → empty, POST
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/?name=Payments&prod_type=11",
        json={"next": None, "results": []},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/",
        method="POST",
        json={"id": 21, "name": "Payments"},
    )
    # find engagement → empty, POST
    httpx_mock.add_response(
        url="https://dd.example/api/v2/engagements/?name=Q3+Pen+Test&product=21",
        json={"next": None, "results": []},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/engagements/",
        method="POST",
        json={"id": 31, "name": "Q3 Pen Test"},
    )
    # find test → empty, look up test_type, POST
    httpx_mock.add_response(
        url="https://dd.example/api/v2/tests/?title=Trivy&engagement=31",
        json={"next": None, "results": []},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/test_types/?name=Trivy+Scan",
        json={"next": None, "results": [{"id": 7, "name": "Trivy Scan"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/tests/",
        method="POST",
        json={"id": 41, "title": "Trivy"},
    )
    # finally reimport-scan
    httpx_mock.add_response(
        url="https://dd.example/api/v2/reimport-scan/",
        method="POST",
        json={"test": 41, "scan_type": "Trivy Scan"},
    )

    body = ImportFindingsWorkflow(client, _trad_opts(scan_file)).run()
    assert body["test"] == 41


def test_findings_traditional_reuses_existing_resources(
    client: DefectDojoClient,
    httpx_mock: HTTPXMock,
    tmp_path: Path,
) -> None:
    scan_file = tmp_path / "scan.json"
    scan_file.write_text("{}")

    httpx_mock.add_response(
        url="https://dd.example/api/v2/product_types/?name=Web+Apps",
        json={"next": None, "results": [{"id": 11, "name": "Web Apps"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/?name=Payments&prod_type=11",
        json={"next": None, "results": [{"id": 21, "name": "Payments"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/engagements/?name=Q3+Pen+Test&product=21",
        json={"next": None, "results": [{"id": 31, "name": "Q3 Pen Test"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/tests/?title=Trivy&engagement=31",
        json={"next": None, "results": [{"id": 41, "title": "Trivy"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/reimport-scan/",
        method="POST",
        json={"test": 41, "scan_type": "Trivy Scan"},
    )

    body = ImportFindingsWorkflow(client, _trad_opts(scan_file)).run()
    assert body["test"] == 41
    # No POSTs to product_types/products/engagements/tests should have fired;
    # only the GET-find calls + the final reimport POST. We sent 5 requests.
    assert len(httpx_mock.get_requests()) == 5


def test_findings_traditional_patches_engagement_with_build_metadata(
    client: DefectDojoClient,
    httpx_mock: HTTPXMock,
    tmp_path: Path,
) -> None:
    scan_file = tmp_path / "scan.json"
    scan_file.write_text("{}")

    # Pre-existing resources
    httpx_mock.add_response(
        url="https://dd.example/api/v2/product_types/?name=Web+Apps",
        json={"next": None, "results": [{"id": 11, "name": "Web Apps"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/?name=Payments&prod_type=11",
        json={"next": None, "results": [{"id": 21, "name": "Payments"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/engagements/?name=Q3+Pen+Test&product=21",
        json={"next": None, "results": [{"id": 31, "name": "Q3 Pen Test"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/tests/?title=Trivy&engagement=31",
        json={"next": None, "results": [{"id": 41, "title": "Trivy"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/reimport-scan/",
        method="POST",
        json={"test": 41},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/engagements/31/",
        method="PATCH",
        json={"id": 31},
    )

    opts = _trad_opts(scan_file).model_copy(
        update={"build_id": "ci-99", "commit_hash": "abc1234", "branch_tag": "main"}
    )
    ImportFindingsWorkflow(client, opts).run()

    patch_request = httpx_mock.get_requests(url="https://dd.example/api/v2/engagements/31/")[0]
    assert patch_request.method == "PATCH"
    payload = json.loads(patch_request.read())
    assert payload == {"build_id": "ci-99", "commit_hash": "abc1234", "branch_tag": "main"}


def test_findings_traditional_skips_engagement_patch_when_no_build_metadata(
    client: DefectDojoClient,
    httpx_mock: HTTPXMock,
    tmp_path: Path,
) -> None:
    scan_file = tmp_path / "scan.json"
    scan_file.write_text("{}")

    httpx_mock.add_response(
        url="https://dd.example/api/v2/product_types/?name=Web+Apps",
        json={"next": None, "results": [{"id": 11, "name": "Web Apps"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/?name=Payments&prod_type=11",
        json={"next": None, "results": [{"id": 21, "name": "Payments"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/engagements/?name=Q3+Pen+Test&product=21",
        json={"next": None, "results": [{"id": 31, "name": "Q3 Pen Test"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/tests/?title=Trivy&engagement=31",
        json={"next": None, "results": [{"id": 41, "title": "Trivy"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/reimport-scan/",
        method="POST",
        json={"test": 41},
    )

    ImportFindingsWorkflow(client, _trad_opts(scan_file)).run()
    # No PATCH to /engagements/31/ should have fired
    assert len(httpx_mock.get_requests(url="https://dd.example/api/v2/engagements/31/")) == 0


def test_findings_traditional_unknown_test_type_raises(
    client: DefectDojoClient,
    httpx_mock: HTTPXMock,
    tmp_path: Path,
) -> None:
    scan_file = tmp_path / "scan.json"
    scan_file.write_text("{}")

    httpx_mock.add_response(
        url="https://dd.example/api/v2/product_types/?name=Web+Apps",
        json={"next": None, "results": [{"id": 11, "name": "Web Apps"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/?name=Payments&prod_type=11",
        json={"next": None, "results": [{"id": 21, "name": "Payments"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/engagements/?name=Q3+Pen+Test&product=21",
        json={"next": None, "results": [{"id": 31, "name": "Q3 Pen Test"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/tests/?title=Trivy&engagement=31",
        json={"next": None, "results": []},
    )
    # Unknown test type — empty results
    httpx_mock.add_response(
        url="https://dd.example/api/v2/test_types/?name=Trivy+Scan",
        json={"next": None, "results": []},
    )
    with pytest.raises(ConfigError) as excinfo:
        ImportFindingsWorkflow(client, _trad_opts(scan_file)).run()
    assert "Trivy Scan" in str(excinfo.value)


# ============================ auto-create flow ========================== #


def test_findings_auto_create_single_call(
    client: DefectDojoClient,
    httpx_mock: HTTPXMock,
    tmp_path: Path,
) -> None:
    scan_file = tmp_path / "scan.json"
    scan_file.write_text('{"results": []}')

    httpx_mock.add_response(
        url="https://dd.example/api/v2/reimport-scan/",
        method="POST",
        json={"test": 99, "scan_type": "Trivy Scan"},
    )

    opts = ImportFindingsOptions(
        auto_create_context=True,
        product_type_name="Web Apps",
        product_name="Payments",
        scanner="Trivy Scan",
        engagement_name="Q3 Pen Test",
        test_name="Trivy",
        file=scan_file,
    )
    body = ImportFindingsWorkflow(client, opts).run()
    assert body["test"] == 99

    # Exactly one HTTP request should have been sent.
    assert len(httpx_mock.get_requests()) == 1
    request = httpx_mock.get_request()
    assert request is not None
    assert request.method == "POST"
    # multipart body — extract our form fields by string-search since
    # we don't have a dedicated parser and the values are reliable.
    body_text = request.content.decode("utf-8", errors="replace")
    assert "auto_create_context" in body_text
    assert "Trivy Scan" in body_text
    assert "Q3 Pen Test" in body_text


def test_findings_auto_create_omits_optional_engagement_and_test(
    client: DefectDojoClient,
    httpx_mock: HTTPXMock,
    tmp_path: Path,
) -> None:
    scan_file = tmp_path / "scan.json"
    scan_file.write_text("{}")

    httpx_mock.add_response(
        url="https://dd.example/api/v2/reimport-scan/",
        method="POST",
        json={"test": 1},
    )
    opts = ImportFindingsOptions(
        auto_create_context=True,
        product_type_name="X",
        product_name="Y",
        scanner="Z Scan",
        file=scan_file,
    )
    ImportFindingsWorkflow(client, opts).run()
    body_text = httpx_mock.get_request().content.decode("utf-8", errors="replace")  # type: ignore[union-attr]
    assert "engagement_name" not in body_text
    assert "test_title" not in body_text


# ============================ validation =============================== #


def test_findings_traditional_missing_engagement_raises() -> None:
    """Without --engagement (or DD_ENGAGEMENT_NAME), traditional flow must fail fast."""
    opts = ImportFindingsOptions(
        product_type_name="X",
        product_name="Y",
        scanner="Z Scan",
        # no engagement_name, no test_name
    )
    # _validate runs in __init__, so just constructing the workflow raises.
    with pytest.raises(ConfigError) as excinfo:
        ImportFindingsWorkflow(_stub_client(), opts)
    msg = str(excinfo.value)
    assert "engagement" in msg
    assert "test_name" in msg


def test_findings_invalid_business_criticality_raises() -> None:
    opts = ImportFindingsOptions(
        product_type_name="X",
        product_name="Y",
        scanner="Z Scan",
        engagement_name="E",
        test_name="T",
        product_business_criticality="ultra",
    )
    with pytest.raises(ValidationError) as excinfo:
        ImportFindingsWorkflow(_stub_client(), opts)
    assert "business_criticality" in str(excinfo.value)


def test_findings_invalid_lifecycle_raises() -> None:
    opts = ImportFindingsOptions(
        product_type_name="X",
        product_name="Y",
        scanner="Z Scan",
        engagement_name="E",
        test_name="T",
        product_lifecycle="staging",
    )
    with pytest.raises(ValidationError):
        ImportFindingsWorkflow(_stub_client(), opts)


def _stub_client() -> DefectDojoClient:
    """Minimal client whose construction doesn't try to talk to anything."""
    return DefectDojoClient(
        Profile(url="https://dd.example", api_key="x"),  # type: ignore[arg-type]
        sleep=lambda _: None,
    )


# ============================ ImportLanguagesWorkflow =================== #


def test_languages_happy_path(
    client: DefectDojoClient,
    httpx_mock: HTTPXMock,
    tmp_path: Path,
) -> None:
    cloc = tmp_path / "cloc.json"
    cloc.write_text('{"Python": {"nFiles": 10, "code": 1000}}')

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

    opts = ImportLanguagesOptions(
        product_type_name="Web",
        product_name="Payments",
        file=cloc,
    )
    body = ImportLanguagesWorkflow(client, opts).run()
    assert body["product"] == 2


def test_languages_creates_missing_resources(
    client: DefectDojoClient,
    httpx_mock: HTTPXMock,
    tmp_path: Path,
) -> None:
    cloc = tmp_path / "cloc.json"
    cloc.write_text("{}")

    httpx_mock.add_response(
        url="https://dd.example/api/v2/product_types/?name=Web",
        json={"next": None, "results": []},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/product_types/",
        method="POST",
        json={"id": 1, "name": "Web"},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/?name=Payments&prod_type=1",
        json={"next": None, "results": []},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/",
        method="POST",
        json={"id": 2, "name": "Payments"},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/import-languages/",
        method="POST",
        json={"id": 9},
    )

    opts = ImportLanguagesOptions(
        product_type_name="Web",
        product_name="Payments",
        file=cloc,
    )
    ImportLanguagesWorkflow(client, opts).run()


def test_languages_missing_file_raises(client: DefectDojoClient) -> None:
    opts = ImportLanguagesOptions(
        product_type_name="X",
        product_name="Y",
        # file missing
    )
    with pytest.raises(ConfigError):
        ImportLanguagesWorkflow(client, opts)


def test_languages_nonexistent_file_raises(
    client: DefectDojoClient,
    httpx_mock: HTTPXMock,
    tmp_path: Path,
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/product_types/?name=X",
        json={"next": None, "results": [{"id": 1, "name": "X"}]},
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/?name=Y&prod_type=1",
        json={"next": None, "results": [{"id": 2, "name": "Y"}]},
    )

    opts = ImportLanguagesOptions(
        product_type_name="X",
        product_name="Y",
        file=tmp_path / "ghost.json",
    )
    with pytest.raises(ValidationError):
        ImportLanguagesWorkflow(client, opts).run()
