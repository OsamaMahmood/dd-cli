"""Integration tests for the M4a import workflows against a live DefectDojo.

Generates a synthetic "Generic Findings Import" JSON in-process — DefectDojo's
simplest stable scanner format — and uploads it via both the auto-create and
traditional flows. Cleanup tears down everything the tests created so the
live instance ends each run unchanged.
"""

from __future__ import annotations

import datetime as _dt
import json
import uuid
from pathlib import Path

import pytest
from typer.testing import CliRunner

from dd_cli.cli.app import app

GENERIC_SCANNER = "Generic Findings Import"

pytestmark = pytest.mark.integration


def _minimal_generic_findings_json() -> str:
    """Minimal Generic Findings Import payload DefectDojo accepts.

    Generic Findings Import is the most stable parser to test against — its
    schema is documented and unchanged across DefectDojo versions, so the
    integration test isn't fragile to DD upgrades.
    """
    today = _dt.date.today().isoformat()
    suffix = uuid.uuid4().hex[:8]
    return json.dumps(
        {
            "findings": [
                {
                    "title": f"dd-cli integration synthetic finding {suffix}",
                    "date": today,
                    "severity": "High",
                    "description": "Synthetic finding for dd-cli integration tests.",
                    "mitigation": "Delete the test product to remove this finding.",
                    "impact": "None — synthetic test data.",
                    "static_finding": True,
                    "dynamic_finding": False,
                }
            ]
        }
    )


@pytest.fixture
def trivy_payload(tmp_path: Path) -> Path:
    """Despite the legacy name, this generates a Generic Findings Import payload."""
    payload = tmp_path / "scan.json"
    payload.write_text(_minimal_generic_findings_json())
    return payload


def test_import_findings_auto_create_against_real_dd(
    runner: CliRunner,
    isolated_config: None,
    cleanup_stack: list[tuple[str, int]],
    trivy_payload: Path,
) -> None:
    """End-to-end: dd import findings --auto-create against a live DD instance."""
    suffix = uuid.uuid4().hex[:6]
    product_name = f"dd-cli-it-product-{suffix}"
    engagement_name = f"dd-cli-it-eng-{suffix}"

    result = runner.invoke(
        app,
        [
            "import",
            "findings",
            "--file",
            str(trivy_payload),
            "--scanner",
            GENERIC_SCANNER,
            "--product-type",
            "Research and Development",
            "--product",
            product_name,
            "--engagement",
            engagement_name,
            "--test-name",
            "dd-cli-it-trivy",
            "--auto-create",
            "--yes",
            "--output",
            "json",
        ],
    )
    assert result.exit_code == 0, result.output

    # Resolve the created product so cleanup can delete the whole tree.
    product_lookup = runner.invoke(
        app,
        ["products", "list", "--name", product_name, "--output", "json"],
    )
    rows = json.loads(product_lookup.stdout)
    if rows:
        cleanup_stack.append(("products", int(rows[0]["id"])))


def test_import_findings_traditional_against_real_dd(
    runner: CliRunner,
    isolated_config: None,
    cleanup_stack: list[tuple[str, int]],
    trivy_payload: Path,
) -> None:
    """End-to-end traditional flow: GET-or-create each resource explicitly."""
    suffix = uuid.uuid4().hex[:6]
    product_name = f"dd-cli-it-trad-{suffix}"
    engagement_name = f"dd-cli-it-trad-eng-{suffix}"
    test_name = f"dd-cli-it-trad-test-{suffix}"

    result = runner.invoke(
        app,
        [
            "import",
            "findings",
            "--file",
            str(trivy_payload),
            "--scanner",
            GENERIC_SCANNER,
            "--product-type",
            "Research and Development",
            "--product",
            product_name,
            "--engagement",
            engagement_name,
            "--test-name",
            test_name,
            "--traditional",
            "--yes",
        ],
    )
    assert result.exit_code == 0, result.output

    product_lookup = runner.invoke(
        app, ["products", "list", "--name", product_name, "--output", "json"]
    )
    rows = json.loads(product_lookup.stdout)
    if rows:
        cleanup_stack.append(("products", int(rows[0]["id"])))


def test_import_languages_against_real_dd(
    runner: CliRunner,
    isolated_config: None,
    cleanup_stack: list[tuple[str, int]],
    tmp_path: Path,
) -> None:
    """`dd import languages` uploads a cloc-shaped JSON for a real product."""
    suffix = uuid.uuid4().hex[:6]
    product_name = f"dd-cli-it-cloc-{suffix}"
    cloc_payload = tmp_path / "cloc.json"
    cloc_payload.write_text(
        json.dumps(
            {
                "header": {"cloc_url": "https://github.com/AlDanial/cloc"},
                "Python": {"nFiles": 12, "blank": 50, "comment": 30, "code": 1000},
                "JavaScript": {"nFiles": 4, "blank": 20, "comment": 5, "code": 250},
                "SUM": {"nFiles": 16, "blank": 70, "comment": 35, "code": 1250},
            }
        )
    )

    result = runner.invoke(
        app,
        [
            "import",
            "languages",
            "--file",
            str(cloc_payload),
            "--product-type",
            "Research and Development",
            "--product",
            product_name,
            "--yes",
        ],
    )
    assert result.exit_code == 0, result.output

    product_lookup = runner.invoke(
        app, ["products", "list", "--name", product_name, "--output", "json"]
    )
    rows = json.loads(product_lookup.stdout)
    if rows:
        cleanup_stack.append(("products", int(rows[0]["id"])))


def test_import_findings_dry_run_real_dd_makes_no_http(
    runner: CliRunner,
    isolated_config: None,
    trivy_payload: Path,
) -> None:
    """Dry-run path against a live DD: prints intent without contacting the server."""
    result = runner.invoke(
        app,
        [
            "import",
            "findings",
            "--file",
            str(trivy_payload),
            "--scanner",
            GENERIC_SCANNER,
            "--product-type",
            "X",
            "--product",
            "Y",
            "--auto-create",
            "--dry-run",
        ],
    )
    assert result.exit_code == 0, result.output
    assert "DRY RUN" in result.stdout
    assert "/api/v2/reimport-scan/" in result.stdout
