"""End-to-end integration tests against a real DefectDojo instance.

These tests are gated on `DD_URL` and `DD_API_KEY` env vars and the
`integration` pytest marker. They are skipped during regular CI runs.

Run them locally against your DefectDojo with:

    DD_URL=http://localhost:8080 \\
    DD_API_KEY=... \\
        pytest -m integration -v

or just `make smoke` after exporting the env vars.

What they verify (catches things mocked tests cannot):
- Real DefectDojo response shapes survive paginate / parse_response
- The `Token <key>` auth header is what DefectDojo actually expects
- DefectDojo's quirks around required-but-undocumented fields
  (e.g. `found_by` on findings create) are documented in the suite
- Round-trip CRUD + every M3b action verb actually flips state
- Resources are cleaned up so the instance ends in its original state
"""

from __future__ import annotations

import json

import pytest
from typer.testing import CliRunner

from dd_cli.cli.app import app

pytestmark = pytest.mark.integration


# ---------------------------- read surface --------------------------------- #


def test_ping_against_real_dd(runner: CliRunner, isolated_config: None) -> None:
    """`dd ping` against a real instance returns ok=true and a username."""
    result = runner.invoke(app, ["ping", "--output", "json"])
    assert result.exit_code == 0, result.output
    body = json.loads(result.stdout)
    assert body["ok"] is True
    assert isinstance(body["user"], str)
    assert body["user"]


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
def test_list_against_real_dd(runner: CliRunner, isolated_config: None, resource: str) -> None:
    """`dd <resource> list` against a real DD returns valid JSON."""
    result = runner.invoke(app, [resource, "list", "--limit", "3", "--output", "json"])
    assert result.exit_code == 0, f"{resource}: {result.output}"
    parsed = json.loads(result.stdout)
    assert isinstance(parsed, list)


# ---------------------------- write round-trip ---------------------------- #


def _create_json(result_output: str) -> dict[str, object]:
    """Robustly extract the JSON body from a CLI command that may include trailing text."""
    return json.loads(result_output.strip())


def test_product_round_trip(
    runner: CliRunner,
    isolated_config: None,
    cleanup_stack: list[tuple[str, int]],
) -> None:
    """create → update → get-by-name → delete on a real DD instance."""
    create = runner.invoke(
        app,
        [
            "products",
            "create",
            "--field",
            "name=dd-cli-it-product",
            "--field",
            "prod_type=1",
            "--field",
            "description=integration test",
            "--output",
            "json",
        ],
    )
    assert create.exit_code == 0, create.output
    created = _create_json(create.stdout)
    product_id = int(created["id"])  # type: ignore[arg-type]
    cleanup_stack.append(("products", product_id))
    assert created["name"] == "dd-cli-it-product"

    update = runner.invoke(
        app,
        [
            "products",
            "update",
            str(product_id),
            "--field",
            "business_criticality=high",
            "--output",
            "json",
        ],
    )
    assert update.exit_code == 0, update.output
    assert _create_json(update.stdout)["business_criticality"] == "high"

    by_name = runner.invoke(
        app,
        ["products", "get", "--name", "dd-cli-it-product", "--output", "json"],
    )
    assert by_name.exit_code == 0, by_name.output
    assert int(_create_json(by_name.stdout)["id"]) == product_id  # type: ignore[arg-type]


# ---------------------------- engagement action verbs --------------------- #


def test_engagement_close_reopen(
    runner: CliRunner,
    isolated_config: None,
    cleanup_stack: list[tuple[str, int]],
) -> None:
    """Real engagement state transitions via close + reopen."""
    product = runner.invoke(
        app,
        [
            "products",
            "create",
            "--field",
            "name=dd-cli-it-eng-host",
            "--field",
            "prod_type=1",
            "--field",
            "description=integration test",
            "--output",
            "json",
        ],
    )
    assert product.exit_code == 0, product.output
    product_id = int(_create_json(product.stdout)["id"])  # type: ignore[arg-type]
    cleanup_stack.append(("products", product_id))

    eng = runner.invoke(
        app,
        [
            "engagements",
            "create",
            "--field",
            "name=dd-cli-it-eng",
            "--field",
            f"product={product_id}",
            "--field",
            "target_start=2026-01-01",
            "--field",
            "target_end=2026-12-31",
            "--field",
            "engagement_type=Interactive",
            "--output",
            "json",
        ],
    )
    assert eng.exit_code == 0, eng.output
    eng_id = int(_create_json(eng.stdout)["id"])  # type: ignore[arg-type]
    cleanup_stack.append(("engagements", eng_id))

    close = runner.invoke(app, ["engagements", "close", str(eng_id), "--yes"])
    assert close.exit_code == 0, close.output

    after_close = runner.invoke(app, ["engagements", "get", str(eng_id), "--output", "json"])
    assert _create_json(after_close.stdout)["status"] == "Completed"

    reopen = runner.invoke(app, ["engagements", "reopen", str(eng_id), "--yes"])
    assert reopen.exit_code == 0, reopen.output

    after_reopen = runner.invoke(app, ["engagements", "get", str(eng_id), "--output", "json"])
    assert _create_json(after_reopen.stdout)["status"] == "In Progress"


# ---------------------------- finding action verbs ----------------------- #


def test_finding_close_reopen_risk_accept(
    runner: CliRunner,
    isolated_config: None,
    cleanup_stack: list[tuple[str, int]],
) -> None:
    """End-to-end: create finding, close, reopen, risk-accept, all against real DD."""
    product = runner.invoke(
        app,
        [
            "products",
            "create",
            "--field",
            "name=dd-cli-it-finding-host",
            "--field",
            "prod_type=1",
            "--field",
            "description=integration test",
            "--output",
            "json",
        ],
    )
    assert product.exit_code == 0
    product_id = int(_create_json(product.stdout)["id"])  # type: ignore[arg-type]
    cleanup_stack.append(("products", product_id))

    eng = runner.invoke(
        app,
        [
            "engagements",
            "create",
            "--field",
            "name=dd-cli-it-finding-eng",
            "--field",
            f"product={product_id}",
            "--field",
            "target_start=2026-01-01",
            "--field",
            "target_end=2026-12-31",
            "--field",
            "engagement_type=Interactive",
            "--output",
            "json",
        ],
    )
    assert eng.exit_code == 0
    eng_id = int(_create_json(eng.stdout)["id"])  # type: ignore[arg-type]
    cleanup_stack.append(("engagements", eng_id))

    test = runner.invoke(
        app,
        [
            "tests",
            "create",
            "--field",
            "title=dd-cli-it-test",
            "--field",
            f"engagement={eng_id}",
            "--field",
            "test_type=1",
            "--field",
            "target_start=2026-01-01T00:00:00Z",
            "--field",
            "target_end=2026-01-02T00:00:00Z",
            "--output",
            "json",
        ],
    )
    assert test.exit_code == 0, test.output
    test_id = int(_create_json(test.stdout)["id"])  # type: ignore[arg-type]
    cleanup_stack.append(("tests", test_id))

    # `found_by` is required by the running server even though dd-api.json
    # marks it optional. Documented in PLAN/memory; passing it explicitly here.
    finding = runner.invoke(
        app,
        [
            "findings",
            "create",
            "--field",
            "title=dd-cli-it-finding",
            "--field",
            f"test={test_id}",
            "--field",
            "severity=High",
            "--field",
            "description=integration test finding",
            "--field",
            "active=true",
            "--field",
            "verified=true",
            "--field",
            "numerical_severity=S2",
            "--field",
            "found_by=[1]",
            "--output",
            "json",
        ],
    )
    assert finding.exit_code == 0, finding.output
    finding_id = int(_create_json(finding.stdout)["id"])  # type: ignore[arg-type]
    cleanup_stack.append(("findings", finding_id))

    # close
    close = runner.invoke(app, ["findings", "close", str(finding_id), "--yes", "--note", "fixed"])
    assert close.exit_code == 0, close.output
    after_close = runner.invoke(app, ["findings", "get", str(finding_id), "--output", "json"])
    body = _create_json(after_close.stdout)
    assert body["is_mitigated"] is True
    assert body["active"] is False

    # reopen
    reopen = runner.invoke(app, ["findings", "reopen", str(finding_id), "--yes"])
    assert reopen.exit_code == 0, reopen.output
    after_reopen = _create_json(
        runner.invoke(app, ["findings", "get", str(finding_id), "--output", "json"]).stdout
    )
    assert after_reopen["is_mitigated"] is False
    assert after_reopen["active"] is True

    # risk-accept (auto-resolves owner via /user_profile/)
    accept = runner.invoke(
        app,
        [
            "findings",
            "risk-accept",
            str(finding_id),
            "--yes",
            "--until",
            "2026-12-31",
            "--reason",
            "integration test compensating control",
            "--output",
            "json",
        ],
    )
    assert accept.exit_code == 0, accept.output
    # Output shape:  "Risk-accepted finding N (acceptance id=M).\n{...json...}"
    # Parse the JSON body that follows the friendly header line.
    json_start = accept.stdout.find("{")
    if json_start >= 0:
        accept_body = json.loads(accept.stdout[json_start:])
        if "id" in accept_body:
            cleanup_stack.append(("risk-acceptances", int(accept_body["id"])))


# ---------------------------- field-level error rendering ---------------- #


def test_findings_create_without_found_by_renders_useful_error(
    runner: CliRunner, isolated_config: None
) -> None:
    """Pin the error-rendering polish: DD's field-level 400 must not produce
    Python-repr garbage in the user-facing message."""
    # No setup needed — we expect this to fail before the server even creates anything
    result = runner.invoke(
        app,
        [
            "findings",
            "create",
            "--field",
            "title=dd-cli-it-missing-found_by",
            "--field",
            "test=999999999",  # almost certainly doesn't exist either; either way we get 400
            "--field",
            "severity=High",
            "--field",
            "numerical_severity=S2",
        ],
    )
    assert result.exit_code != 0
    assert result.exception is not None
    msg = str(result.exception)
    # Polished output: no Python repr of dicts, no DefectDojo Pro upsell
    assert "ErrorDetail(" not in msg
    assert "Pro comes with support" not in msg


# ---------------------------- profile cleanup --------------------------- #


def test_user_dry_run_against_real_dd(runner: CliRunner, isolated_config: None) -> None:
    """Dry-run for users activate doesn't mutate state; sanity check on real DD."""
    result = runner.invoke(app, ["users", "activate", "1", "--dry-run"])
    assert result.exit_code == 0, result.output
    assert "DRY RUN" in result.stdout
    assert "/api/v2/users/1/" in result.stdout
