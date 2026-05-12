"""Per-finding enrichment + age-bucketing helpers for the report context."""

from __future__ import annotations

from typing import Any

SEVERITY_ORDER: dict[str, int] = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3, "Info": 4}

# (low_inclusive, high_exclusive, display_label) — covers every non-negative age.
AGE_BUCKETS: tuple[tuple[int, int, str], ...] = (
    (0, 30, "0-30 days"),
    (30, 90, "30-90 days"),
    (90, 180, "90-180 days"),
    (180, 10**9, "180+ days"),
)


def risk_key(finding: dict[str, Any]) -> tuple[int, int, float, int, int]:
    """Composite risk score for sorting findings (smaller = riskier).

    Ranks by, in order: severity -> KEV exposure -> EPSS desc -> age desc ->
    DefectDojo's numerical-severity (S0..S4). Used both for the "Top N
    riskiest findings" table and the per-test finding ordering.
    """
    sev = SEVERITY_ORDER.get(finding.get("severity") or "Info", 5)
    kev = 0 if finding.get("known_exploited") else 1
    epss = -float(finding.get("epss_score") or 0.0)
    age = -int(finding.get("age") or 0)
    num_rank = {"S0": 0, "S1": 1, "S2": 2, "S3": 3, "S4": 4}.get(
        finding.get("numerical_severity") or "",
        5,
    )
    return (sev, kev, epss, age, num_rank)


def sla_status(finding: dict[str, Any]) -> dict[str, Any]:
    """Compute a display-friendly SLA status from a finding's raw fields.

    DefectDojo populates ``sla_days_remaining`` and ``sla_expiration_date``
    when an SLA is configured; otherwise both are absent. We render:

    - "No SLA" — both fields missing.
    - "Active" — days unavailable but an expiration is set.
    - "BREACHED by Nd" — days negative.
    - "Due in Nd" — 0 ≤ days ≤ 7 (warning band).
    - "On track (Nd left)" — days > 7.

    The ``css`` key is used by the HTML template to colour the pill.
    """
    days = finding.get("sla_days_remaining")
    expiry = finding.get("sla_expiration_date")
    if days is None and not expiry:
        return {"label": "No SLA", "css": "sla-none", "days": None}
    if days is None:
        return {"label": "Active", "css": "sla-ok", "days": None}
    if days < 0:
        return {"label": f"BREACHED by {abs(days)}d", "css": "sla-breach", "days": days}
    if days <= 7:
        return {"label": f"Due in {days}d", "css": "sla-warn", "days": days}
    return {"label": f"On track ({days}d left)", "css": "sla-ok", "days": days}


def enrich_finding(finding: dict[str, Any]) -> dict[str, Any]:
    """Return a shallow copy of `finding` with template-ready computed fields.

    Added keys:

    - ``sla`` — see :func:`sla_status`.
    - ``epss_pct`` / ``epss_percentile_pct`` — EPSS score and percentile
      expressed as percentages (so the template doesn't have to do the
      ``* 100`` dance inside Jinja).
    - ``endpoint_count`` — len of the ``endpoints`` list.
    - ``has_dast_evidence`` / ``has_sast_evidence`` — boolean flags the
      template branches on to decide whether to render evidence blocks.
    """
    enriched = dict(finding)
    enriched["sla"] = sla_status(finding)
    enriched["epss_pct"] = (
        round(finding["epss_score"] * 100, 1) if finding.get("epss_score") is not None else None
    )
    enriched["epss_percentile_pct"] = (
        round(finding["epss_percentile"] * 100, 1)
        if finding.get("epss_percentile") is not None
        else None
    )
    enriched["endpoint_count"] = len(finding.get("endpoints") or [])
    enriched["has_dast_evidence"] = bool(
        finding.get("url") or finding.get("param") or finding.get("payload")
    )
    enriched["has_sast_evidence"] = bool(
        finding.get("sast_source_file_path") or finding.get("sast_source_object")
    )
    return enriched


def aging_buckets(findings: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Group findings into the four standard age buckets, with per-severity counts."""
    rows: list[dict[str, Any]] = []
    for lo, hi, label in AGE_BUCKETS:
        bucket = [f for f in findings if lo <= (f.get("age") or 0) < hi]
        severity_counts = dict.fromkeys(SEVERITY_ORDER, 0)
        for f in bucket:
            sev = f.get("severity") or "Info"
            if sev in severity_counts:
                severity_counts[sev] += 1
        rows.append({"label": label, "total": len(bucket), "severity": severity_counts})
    return rows


def scan_delta(imports: list[dict[str, Any]]) -> dict[str, Any] | None:
    """Summarise the most recent ``test_imports`` entry vs. the prior import.

    Returns ``None`` when no imports are present. Otherwise produces the
    counts the template renders into the per-test "scan delta" block
    (created / closed / reactivated / untouched) plus the build metadata
    of the latest import.
    """
    if not imports:
        return None
    sorted_imports = sorted(imports, key=lambda i: i.get("created") or "", reverse=True)
    latest = sorted_imports[0]
    actions = latest.get("test_import_finding_action_set") or []
    counts: dict[str, Any] = {"created": 0, "closed": 0, "reactivated": 0, "untouched": 0}
    for a in actions:
        action = (a.get("action") or "").lower()
        if action in counts:
            counts[action] = int(counts[action]) + 1
    counts["total_imports"] = len(imports)
    counts["latest_at"] = latest.get("created")
    counts["latest_build"] = latest.get("build_id")
    counts["latest_commit"] = latest.get("commit_hash")
    counts["latest_branch"] = latest.get("branch_tag")
    return counts


def resolve_risk_acceptance(
    risk_acceptances: list[dict[str, Any]],
    finding_id_to_meta: dict[int, dict[str, Any]],
) -> list[dict[str, Any]]:
    """Flatten DefectDojo's ``risk_acceptance`` records for the template.

    The API returns ``accepted_findings`` as a list of bare finding IDs; we
    join those against ``finding_id_to_meta`` (a map built while walking
    findings) so the template can render a table without a second fetch.
    """
    out: list[dict[str, Any]] = []
    for ra in risk_acceptances:
        finding_ids = ra.get("accepted_findings") or []
        items: list[dict[str, Any]] = []
        for fid in finding_ids:
            meta = finding_id_to_meta.get(fid)
            if meta:
                items.append({"id": fid, **meta})
        out.append(
            {
                "id": ra.get("id"),
                "name": ra.get("name") or f"Risk acceptance {ra.get('id')}",
                "decision": ra.get("decision") or "Accept",
                "decision_details": ra.get("decision_details") or "",
                "recommendation": ra.get("recommendation") or "",
                "recommendation_details": ra.get("recommendation_details") or "",
                "accepted_by": ra.get("accepted_by") or ra.get("owner") or "",
                "expiration_date": ra.get("expiration_date"),
                "expiration_date_handled": ra.get("expiration_date_handled"),
                "created": ra.get("created"),
                "findings": items,
                "finding_count": len(finding_ids),
            }
        )
    return out
