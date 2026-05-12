"""Tests for the Markdown renderer (Jinja2 → string).

The snapshot pins the template output for a deterministic fixture so
template changes are visible in PR diffs.
"""

from __future__ import annotations

import re
from typing import Any

import pytest

from dd_cli.reporting.context import build_context
from dd_cli.reporting.render import render_html, render_markdown

# `generated_at` is a UTC timestamp baked at build time — strip it from
# both Markdown (`**Generated:** ...`) and HTML (`<strong>Generated:</strong> ...`)
# so the snapshot stays stable across runs.
_GENERATED_AT_RE = re.compile(r"(\*\*Generated:\*\*|<strong>Generated:</strong>)\s.+? UTC")


@pytest.fixture
def fixture_context() -> dict[str, Any]:
    return build_context(
        product={
            "id": 42,
            "name": "Payments",
            "business_criticality": "high",
            "platform": "web",
            "lifecycle": "production",
            "prod_numeric_grade": 78,
            "description": "Internal payment processing service.",
        },
        engagements=[
            {
                "id": 1,
                "name": "Q4 2026 Pentest",
                "status": "In Progress",
                "version": "2.1.0",
                "target_start": "2026-10-01",
                "target_end": "2026-12-31",
                "branch_tag": "main",
                "commit_hash": "abc1234def5678",
            }
        ],
        tests_by_engagement={
            1: [
                {
                    "id": 10,
                    "test_type": 100,
                    "scan_type": "Trivy Scan",
                    "test_type_name": "Trivy Scan",
                    "title": "Container Trivy",
                    "target_start": "2026-10-01",
                    "target_end": "2026-10-01",
                    "branch_tag": "main",
                    "commit_hash": "abc1234def5678",
                },
                {
                    "id": 11,
                    "test_type": 101,
                    "scan_type": "Bandit Scan",
                    "test_type_name": "Bandit Scan",
                },
            ]
        },
        findings_by_test={
            10: [
                {
                    "id": 1,
                    "title": "Path traversal in /admin",
                    "severity": "Critical",
                    "numerical_severity": "S0",
                    "age": 12,
                    "cwe": 22,
                    "cve": "CVE-2026-12345",
                    "cvssv3_score": 9.1,
                    "epss_score": 0.8741,
                    "epss_percentile": 0.991,
                    "known_exploited": True,
                    "fix_available": True,
                    "fix_version": "2.1.1",
                    "sla_days_remaining": -3,
                    "date": "2026-09-28",
                    "description": "User input flows into a file open call without sanitisation.",
                    "mitigation": "Validate the path against an allowlist or canonicalise.",
                    "static_finding": True,
                    "sast_source_file_path": "src/admin/handler.py",
                    "sast_source_line": 142,
                },
                {
                    "id": 2,
                    "title": "Outdated lodash",
                    "severity": "Low",
                    "age": 60,
                    "sla_days_remaining": 30,
                    "date": "2026-09-10",
                    "fix_available": True,
                    "fix_version": "4.17.21",
                    "component_name": "lodash",
                    "component_version": "4.17.15",
                },
            ],
            11: [],  # empty test renders the "no active findings" block
        },
        test_type_names={100: "Trivy Scan", 101: "Bandit Scan"},
        dd_url="https://dd.example.com/",
        sla_configurations=[
            {"name": "Default", "critical": 7, "high": 30, "medium": 90, "low": 180}
        ],
        risk_acceptances=[],
    )


def _stable(text: str) -> str:
    """Strip the generated-at timestamp so snapshot diffs only show real changes."""
    return _GENERATED_AT_RE.sub(r"\1 <stamp>", text)


def test_render_markdown_returns_a_non_empty_string(fixture_context: dict[str, Any]) -> None:
    out = render_markdown(fixture_context)
    assert isinstance(out, str)
    assert len(out) > 100


def test_render_markdown_includes_product_name(fixture_context: dict[str, Any]) -> None:
    out = render_markdown(fixture_context)
    assert "# Security Report — Payments" in out


def test_render_markdown_includes_severity_totals(fixture_context: dict[str, Any]) -> None:
    out = render_markdown(fixture_context)
    assert "Active findings | 2" in out
    assert "Critical | 1" in out
    assert "Low | 1" in out


def test_render_markdown_marks_kev_finding(fixture_context: dict[str, Any]) -> None:
    out = render_markdown(fixture_context)
    assert "**[KEV]**" in out
    assert "*[Fix]*" in out or "*[Fix available]*" in out


def test_render_markdown_renders_empty_test_message(fixture_context: dict[str, Any]) -> None:
    out = render_markdown(fixture_context)
    assert "No active findings were identified for this test." in out


def test_render_markdown_snapshot(fixture_context: dict[str, Any], snapshot: object) -> None:
    """Pin the full rendered Markdown so future template tweaks show up in the diff."""
    assert _stable(render_markdown(fixture_context)) == snapshot


# ---------------------------- HTML rendering ------------------------------- #


def test_render_html_returns_a_non_empty_string(fixture_context: dict[str, Any]) -> None:
    out = render_html(fixture_context)
    assert isinstance(out, str)
    assert len(out) > 500  # template is large; less than this means something broke


def test_render_html_is_a_full_document(fixture_context: dict[str, Any]) -> None:
    """Self-contained HTML — the user opens it in a browser, no external assets."""
    out = render_html(fixture_context)
    assert "<!DOCTYPE html>" in out or "<!doctype html>" in out.lower()
    assert "<html" in out.lower()
    assert "</html>" in out.lower()
    assert "<style" in out.lower()  # CSS is inlined; no external stylesheet


def test_render_html_includes_product_name(fixture_context: dict[str, Any]) -> None:
    out = render_html(fixture_context)
    assert "Payments" in out


def test_render_html_renders_kev_badge(fixture_context: dict[str, Any]) -> None:
    out = render_html(fixture_context)
    # The KEV finding should produce a visible badge/marker; the exact CSS
    # class name is template-internal, but "KEV" must appear in the output.
    assert "KEV" in out


def test_render_html_snapshot(fixture_context: dict[str, Any], snapshot: object) -> None:
    """Pin the full rendered HTML so template tweaks show up in the diff."""
    assert _stable(render_html(fixture_context)) == snapshot
