"""Tests for `build_context` — the renderer-ready context dict assembler."""

from __future__ import annotations

from typing import Any

import pytest

from dd_cli.reporting.context import TOP_RISK_LIMIT, build_context


@pytest.fixture
def minimal_inputs() -> dict[str, Any]:
    """One product, one engagement, one test, two findings, no SLA, no acceptances."""
    return {
        "product": {"id": 42, "name": "Payments"},
        "engagements": [{"id": 1, "name": "Q4 2026", "status": "In Progress"}],
        "tests_by_engagement": {1: [{"id": 10, "test_type": 100, "scan_type": "Trivy Scan"}]},
        "findings_by_test": {
            10: [
                {"id": 1, "title": "Critical bug", "severity": "Critical", "age": 5},
                {"id": 2, "title": "Low bug", "severity": "Low", "age": 200},
            ]
        },
        "test_type_names": {100: "Trivy Scan"},
        "dd_url": "https://dd.example/",
    }


def test_build_context_returns_required_top_level_keys(minimal_inputs: dict[str, Any]) -> None:
    ctx = build_context(**minimal_inputs)
    for key in (
        "generated_at",
        "dd_url",
        "product",
        "engagements",
        "test_filters",
        "sla_configurations",
        "risk_acceptances",
        "aging",
        "detailed",
        "with_history",
        "totals",
        "top_risk",
    ):
        assert key in ctx, f"missing key {key!r}"


def test_build_context_strips_trailing_slash_from_dd_url(minimal_inputs: dict[str, Any]) -> None:
    minimal_inputs["dd_url"] = "https://dd.example/////"
    ctx = build_context(**minimal_inputs)
    assert ctx["dd_url"] == "https://dd.example"


def test_build_context_counts_totals(minimal_inputs: dict[str, Any]) -> None:
    ctx = build_context(**minimal_inputs)
    totals = ctx["totals"]
    assert totals["engagements"] == 1
    assert totals["tests"] == 1
    assert totals["findings"] == 2
    assert totals["severity"]["Critical"] == 1
    assert totals["severity"]["Low"] == 1
    assert totals["severity"]["High"] == 0
    assert totals["kev"] == 0
    assert totals["sla_breach"] == 0


def test_build_context_counts_kev_and_sla_breach() -> None:
    ctx = build_context(
        product={"id": 1, "name": "x"},
        engagements=[{"id": 1, "name": "e"}],
        tests_by_engagement={1: [{"id": 10, "test_type": 100, "scan_type": "Trivy"}]},
        findings_by_test={
            10: [
                {
                    "id": 1,
                    "severity": "Critical",
                    "known_exploited": True,
                    "sla_days_remaining": -5,
                },
                {"id": 2, "severity": "Low", "sla_days_remaining": 30},
            ]
        },
        test_type_names={100: "Trivy"},
        dd_url="https://dd.example",
    )
    assert ctx["totals"]["kev"] == 1
    assert ctx["totals"]["sla_breach"] == 1


def test_build_context_sorts_findings_by_risk(minimal_inputs: dict[str, Any]) -> None:
    """The Critical finding outranks the Low one inside each test."""
    ctx = build_context(**minimal_inputs)
    findings = ctx["engagements"][0]["tests"][0]["findings"]
    assert [f["severity"] for f in findings] == ["Critical", "Low"]


def test_build_context_top_risk_capped_at_limit() -> None:
    findings = [
        {"id": i, "title": f"f-{i}", "severity": "High", "age": i}
        for i in range(TOP_RISK_LIMIT * 2)
    ]
    ctx = build_context(
        product={"id": 1, "name": "x"},
        engagements=[{"id": 1, "name": "e"}],
        tests_by_engagement={1: [{"id": 10, "test_type": 100, "scan_type": "t"}]},
        findings_by_test={10: findings},
        test_type_names={100: "t"},
        dd_url="https://dd.example",
    )
    assert len(ctx["top_risk"]) == TOP_RISK_LIMIT


def test_build_context_engagement_name_falls_back_to_id() -> None:
    ctx = build_context(
        product={"id": 1, "name": "x"},
        engagements=[{"id": 7}],  # no name
        tests_by_engagement={},
        findings_by_test={},
        test_type_names={},
        dd_url="https://dd.example",
    )
    assert ctx["engagements"][0]["name"] == "Engagement 7"


def test_build_context_resolves_test_type_name_from_inline_or_map() -> None:
    ctx = build_context(
        product={"id": 1, "name": "x"},
        engagements=[{"id": 1, "name": "e"}],
        tests_by_engagement={
            1: [
                {"id": 10, "test_type": 100, "test_type_name": "Inline Name"},
                {"id": 11, "test_type": 200},  # falls back to test_type_names map
                {"id": 12, "test_type": 999},  # missing entirely → "Unknown"
            ]
        },
        findings_by_test={10: [], 11: [], 12: []},
        test_type_names={200: "From Map"},
        dd_url="https://dd.example",
    )
    names = [t["test_type_name"] for t in ctx["engagements"][0]["tests"]]
    assert names == ["Inline Name", "From Map", "Unknown"]


def test_build_context_risk_accepted_total_counts_finding_ids() -> None:
    ctx = build_context(
        product={"id": 1, "name": "x"},
        engagements=[{"id": 1, "name": "e"}],
        tests_by_engagement={1: [{"id": 10, "test_type": 100, "scan_type": "t"}]},
        findings_by_test={
            10: [
                {"id": 1, "severity": "High"},
                {"id": 2, "severity": "Low"},
            ]
        },
        test_type_names={100: "t"},
        dd_url="https://dd.example",
        risk_acceptances=[
            {"id": 1, "accepted_findings": [1], "decision": "Accept"},
            {"id": 2, "accepted_findings": [2, 3], "decision": "Accept"},
        ],
    )
    # 3 IDs across 2 acceptance records, even though id=3 isn't in our finding meta.
    assert ctx["totals"]["risk_accepted"] == 3


def test_build_context_detailed_off_means_empty_per_finding_aux() -> None:
    ctx = build_context(
        product={"id": 1, "name": "x"},
        engagements=[{"id": 1, "name": "e"}],
        tests_by_engagement={1: [{"id": 10, "test_type": 100, "scan_type": "t"}]},
        findings_by_test={10: [{"id": 99, "severity": "High"}]},
        test_type_names={100: "t"},
        dd_url="https://dd.example",
        notes_by_finding={99: [{"entry": "should be ignored"}]},
        jira_by_finding={99: [{"jira_key": "ignored"}]},
        endpoint_status_by_finding={99: [{"endpoint": "ignored"}]},
        detailed=False,
    )
    f = ctx["engagements"][0]["tests"][0]["findings"][0]
    assert f["notes"] == []
    assert f["jira"] == []
    assert f["endpoint_status"] == []


def test_build_context_detailed_on_passes_aux_through() -> None:
    ctx = build_context(
        product={"id": 1, "name": "x"},
        engagements=[{"id": 1, "name": "e"}],
        tests_by_engagement={1: [{"id": 10, "test_type": 100, "scan_type": "t"}]},
        findings_by_test={10: [{"id": 99, "severity": "High"}]},
        test_type_names={100: "t"},
        dd_url="https://dd.example",
        notes_by_finding={99: [{"entry": "kept"}]},
        detailed=True,
    )
    f = ctx["engagements"][0]["tests"][0]["findings"][0]
    assert f["notes"] == [{"entry": "kept"}]
