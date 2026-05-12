"""Assemble the renderer-ready context dict from raw DefectDojo payloads.

`build_context` is a pure function: it does no I/O. The CLI layer fetches
every required resource via :class:`dd_cli.client.DefectDojoClient`, then
hands the resulting dicts here. Tests construct fixture dicts directly.

The dict returned is what the Jinja2 templates iterate over — keys must
stay stable; the templates are the schema.
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any

from dd_cli.reporting.enrich import (
    SEVERITY_ORDER,
    aging_buckets,
    enrich_finding,
    resolve_risk_acceptance,
    risk_key,
    scan_delta,
)

TOP_RISK_LIMIT = 10


def build_context(
    *,
    product: dict[str, Any],
    engagements: list[dict[str, Any]],
    tests_by_engagement: dict[int, list[dict[str, Any]]],
    findings_by_test: dict[int, list[dict[str, Any]]],
    test_type_names: dict[int, str],
    dd_url: str,
    test_filters: list[str] | None = None,
    sla_configurations: list[dict[str, Any]] | None = None,
    risk_acceptances: list[dict[str, Any]] | None = None,
    notes_by_finding: dict[int, list[dict[str, Any]]] | None = None,
    jira_by_finding: dict[int, list[dict[str, Any]]] | None = None,
    endpoint_status_by_finding: dict[int, list[dict[str, Any]]] | None = None,
    test_imports_by_test: dict[int, list[dict[str, Any]]] | None = None,
    detailed: bool = False,
    with_history: bool = False,
) -> dict[str, Any]:
    """Build the template context for a single product's report.

    Arguments mirror DefectDojo's resource shapes — `product` is the raw
    GET on `/api/v2/products/{id}/`, `engagements` is the list from
    `/api/v2/engagements/?product={id}&active=true`, etc. The `_by_*`
    mappings are keyed by parent ID.

    `detailed` and `with_history` are *flags* — they don't trigger fetches
    here (no I/O). They tell the function whether to include the extra
    per-finding / per-test data when it's already in `notes_by_finding`
    et al. The CLI layer decides whether to populate those mappings.
    """
    notes_by_finding = notes_by_finding or {}
    jira_by_finding = jira_by_finding or {}
    endpoint_status_by_finding = endpoint_status_by_finding or {}
    test_imports_by_test = test_imports_by_test or {}

    severity_totals = dict.fromkeys(SEVERITY_ORDER, 0)
    test_count = 0
    finding_count = 0
    kev_count = 0
    sla_breach_count = 0
    all_enriched: list[dict[str, Any]] = []
    finding_meta: dict[int, dict[str, Any]] = {}

    eng_views: list[dict[str, Any]] = []
    for eng in engagements:
        tests = tests_by_engagement.get(eng["id"], [])
        test_views: list[dict[str, Any]] = []
        for test in tests:
            test_count += 1
            raw_findings = findings_by_test.get(test["id"], [])
            findings = sorted(
                (enrich_finding(f) for f in raw_findings),
                key=risk_key,
            )
            tt_id = test.get("test_type")
            test_type_name = test.get("test_type_name") or (
                test_type_names.get(tt_id, "Unknown") if isinstance(tt_id, int) else "Unknown"
            )
            engagement_name = eng.get("name") or f"Engagement {eng['id']}"
            for f in findings:
                sev = f.get("severity") or "Info"
                if sev in severity_totals:
                    severity_totals[sev] += 1
                finding_count += 1
                if f.get("known_exploited"):
                    kev_count += 1
                if f.get("sla", {}).get("css") == "sla-breach":
                    sla_breach_count += 1
                f["_test_id"] = test["id"]
                f["_test_name"] = test_type_name
                f["_engagement_name"] = engagement_name
                f["notes"] = notes_by_finding.get(f["id"], []) if detailed else []
                f["jira"] = jira_by_finding.get(f["id"], []) if detailed else []
                f["endpoint_status"] = (
                    endpoint_status_by_finding.get(f["id"], []) if detailed else []
                )
                all_enriched.append(f)
                finding_meta[f["id"]] = {
                    "title": f.get("title"),
                    "severity": f.get("severity"),
                    "_test_name": f["_test_name"],
                    "_engagement_name": f["_engagement_name"],
                }

            delta = scan_delta(test_imports_by_test.get(test["id"], [])) if with_history else None
            test_views.append(
                {
                    "id": test["id"],
                    "title": test.get("title") or "",
                    "scan_type": test.get("scan_type") or "",
                    "test_type_name": test_type_name,
                    "target_start": test.get("target_start"),
                    "target_end": test.get("target_end"),
                    "branch_tag": test.get("branch_tag"),
                    "commit_hash": test.get("commit_hash"),
                    "build_id": test.get("build_id"),
                    "version": test.get("version"),
                    "findings": findings,
                    "finding_count": len(findings),
                    "scan_delta": delta,
                }
            )
        eng_views.append(
            {
                "id": eng["id"],
                "name": eng.get("name") or f"Engagement {eng['id']}",
                "description": eng.get("description") or "",
                "status": eng.get("status") or "",
                "version": eng.get("version") or "",
                "target_start": eng.get("target_start"),
                "target_end": eng.get("target_end"),
                "branch_tag": eng.get("branch_tag"),
                "commit_hash": eng.get("commit_hash"),
                "build_id": eng.get("build_id"),
                "engagement_type": eng.get("engagement_type"),
                "tests": test_views,
                "test_count": len(test_views),
            }
        )

    top_risk = sorted(all_enriched, key=risk_key)[:TOP_RISK_LIMIT]
    aging = aging_buckets(all_enriched)
    risk_acceptance_view = resolve_risk_acceptance(risk_acceptances or [], finding_meta)

    return {
        "generated_at": datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "dd_url": dd_url.rstrip("/"),
        "product": product,
        "engagements": eng_views,
        "test_filters": test_filters or [],
        "sla_configurations": sla_configurations or [],
        "risk_acceptances": risk_acceptance_view,
        "aging": aging,
        "detailed": detailed,
        "with_history": with_history,
        "totals": {
            "engagements": len(eng_views),
            "tests": test_count,
            "findings": finding_count,
            "severity": severity_totals,
            "kev": kev_count,
            "sla_breach": sla_breach_count,
            "risk_accepted": sum(ra["finding_count"] for ra in risk_acceptance_view),
        },
        "top_risk": top_risk,
    }
