"""Tests for the pure enrichment helpers used by the report context builder."""

from __future__ import annotations

import pytest

from dd_cli.reporting.enrich import (
    aging_buckets,
    enrich_finding,
    resolve_risk_acceptance,
    risk_key,
    scan_delta,
    sla_status,
)

# ---------------------------- risk_key ------------------------------------- #


def test_risk_key_orders_by_severity_first() -> None:
    critical = {"severity": "Critical"}
    high = {"severity": "High"}
    info = {"severity": "Info"}
    ordered = sorted([info, critical, high], key=risk_key)
    assert [f["severity"] for f in ordered] == ["Critical", "High", "Info"]


def test_risk_key_breaks_tie_on_kev_exposure() -> None:
    a = {"severity": "High", "known_exploited": False}
    b = {"severity": "High", "known_exploited": True}
    ordered = sorted([a, b], key=risk_key)
    assert ordered[0] is b  # KEV ranks first within the same severity


def test_risk_key_breaks_tie_on_epss_desc() -> None:
    a = {"severity": "High", "epss_score": 0.1}
    b = {"severity": "High", "epss_score": 0.9}
    ordered = sorted([a, b], key=risk_key)
    assert ordered[0] is b  # higher EPSS ranks first


def test_risk_key_breaks_tie_on_age_desc() -> None:
    a = {"severity": "Medium", "age": 5}
    b = {"severity": "Medium", "age": 200}
    ordered = sorted([a, b], key=risk_key)
    assert ordered[0] is b  # older finding ranks first


def test_risk_key_handles_missing_fields() -> None:
    sparse: dict[str, object] = {}
    # Must not raise; falls back to "Info" bucket.
    risk_key(sparse)


# ---------------------------- sla_status ----------------------------------- #


@pytest.mark.parametrize(
    ("finding", "expected_label", "expected_css"),
    [
        ({}, "No SLA", "sla-none"),
        ({"sla_expiration_date": "2026-12-31"}, "Active", "sla-ok"),
        ({"sla_days_remaining": 30}, "On track (30d left)", "sla-ok"),
        ({"sla_days_remaining": 7}, "Due in 7d", "sla-warn"),
        ({"sla_days_remaining": 0}, "Due in 0d", "sla-warn"),
        ({"sla_days_remaining": -3}, "BREACHED by 3d", "sla-breach"),
    ],
)
def test_sla_status_classifies(
    finding: dict[str, object], expected_label: str, expected_css: str
) -> None:
    result = sla_status(finding)
    assert result["label"] == expected_label
    assert result["css"] == expected_css


# ---------------------------- enrich_finding ------------------------------- #


def test_enrich_finding_adds_sla_and_epss_pct() -> None:
    f = {"severity": "High", "epss_score": 0.42, "epss_percentile": 0.987, "sla_days_remaining": 14}
    out = enrich_finding(f)
    assert out["sla"]["label"] == "On track (14d left)"
    assert out["epss_pct"] == 42.0
    assert out["epss_percentile_pct"] == 98.7


def test_enrich_finding_endpoint_count_from_list() -> None:
    f = {"endpoints": [1, 2, 3]}
    assert enrich_finding(f)["endpoint_count"] == 3


def test_enrich_finding_endpoint_count_zero_when_missing() -> None:
    assert enrich_finding({})["endpoint_count"] == 0


def test_enrich_finding_evidence_flags() -> None:
    dast = {"url": "https://x.example/login", "param": "username"}
    sast = {"sast_source_file_path": "src/auth.py"}
    plain: dict[str, object] = {}
    assert enrich_finding(dast)["has_dast_evidence"] is True
    assert enrich_finding(sast)["has_sast_evidence"] is True
    assert enrich_finding(plain)["has_dast_evidence"] is False
    assert enrich_finding(plain)["has_sast_evidence"] is False


def test_enrich_finding_does_not_mutate_input() -> None:
    f = {"severity": "Low"}
    enrich_finding(f)
    assert "sla" not in f  # the returned dict is a copy


# ---------------------------- aging_buckets -------------------------------- #


def test_aging_buckets_partitions_by_age() -> None:
    findings = [
        {"severity": "Critical", "age": 1},
        {"severity": "High", "age": 45},
        {"severity": "Medium", "age": 100},
        {"severity": "Low", "age": 365},
        {"severity": "Info"},  # missing age -> bucket 0-30
    ]
    rows = aging_buckets(findings)
    by_label = {r["label"]: r for r in rows}
    assert by_label["0-30 days"]["total"] == 2  # Critical + Info
    assert by_label["30-90 days"]["total"] == 1  # High
    assert by_label["90-180 days"]["total"] == 1  # Medium
    assert by_label["180+ days"]["total"] == 1  # Low
    assert by_label["0-30 days"]["severity"]["Critical"] == 1
    assert by_label["0-30 days"]["severity"]["Info"] == 1


# ---------------------------- scan_delta ----------------------------------- #


def test_scan_delta_none_for_empty_imports() -> None:
    assert scan_delta([]) is None


def test_scan_delta_picks_latest_and_counts_actions() -> None:
    imports = [
        {
            "created": "2026-05-01T00:00:00Z",
            "test_import_finding_action_set": [
                {"action": "Created"},
                {"action": "closed"},
            ],
            "build_id": "old-build",
        },
        {
            "created": "2026-05-09T00:00:00Z",  # latest
            "test_import_finding_action_set": [
                {"action": "Created"},
                {"action": "Created"},
                {"action": "Reactivated"},
                {"action": "Untouched"},
            ],
            "build_id": "new-build",
            "commit_hash": "abc1234",
            "branch_tag": "main",
        },
    ]
    delta = scan_delta(imports)
    assert delta is not None
    assert delta["created"] == 2
    assert delta["reactivated"] == 1
    assert delta["untouched"] == 1
    assert delta["closed"] == 0
    assert delta["total_imports"] == 2
    assert delta["latest_build"] == "new-build"
    assert delta["latest_commit"] == "abc1234"
    assert delta["latest_branch"] == "main"


# ---------------------------- resolve_risk_acceptance ---------------------- #


def test_resolve_risk_acceptance_joins_meta() -> None:
    acceptances = [
        {
            "id": 7,
            "name": "Q4 false-positives batch",
            "accepted_findings": [1, 2],
            "decision": "Accept",
            "accepted_by": "alice",
            "expiration_date": "2026-12-31",
        }
    ]
    meta = {
        1: {"title": "SQLi", "severity": "High", "_test_name": "ZAP", "_engagement_name": "Q4"},
        2: {"title": "XSS", "severity": "Medium", "_test_name": "ZAP", "_engagement_name": "Q4"},
    }
    out = resolve_risk_acceptance(acceptances, meta)
    assert len(out) == 1
    assert out[0]["finding_count"] == 2
    assert [f["title"] for f in out[0]["findings"]] == ["SQLi", "XSS"]


def test_resolve_risk_acceptance_drops_unknown_finding_ids() -> None:
    acceptances = [{"id": 1, "accepted_findings": [1, 999], "decision": "Accept"}]
    meta = {1: {"title": "A", "severity": "Low", "_test_name": "t", "_engagement_name": "e"}}
    out = resolve_risk_acceptance(acceptances, meta)
    assert len(out[0]["findings"]) == 1  # 999 isn't in meta → dropped
    assert out[0]["finding_count"] == 2  # but the raw count is preserved
