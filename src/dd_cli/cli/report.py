"""`dd report` — generate a security report for a DefectDojo product.

M6a ships the core read-side flow:
- Markdown output only (HTML follows in M6b).
- `--product` plus optional `--test NAME` filters (repeatable).
- `--output DIR` controls the output directory (default `./reports`).

`--detailed`, `--with-history`, and `--sample` are M6b — accepted as
no-op options here so the CLI surface is stable, but they emit a
"not yet implemented in this milestone" notice and exit cleanly.
"""

from __future__ import annotations

import re
from itertools import islice
from pathlib import Path
from typing import Annotated, Any

import typer

from dd_cli.cli._resource import get_active_profile
from dd_cli.client import DefectDojoClient
from dd_cli.errors import APIError, NotFoundError, ValidationError
from dd_cli.reporting import build_context, render_markdown

# Maximum tests to walk while resolving test_type_names — a defensive
# cap to keep the cache fan-out bounded for very large products.
TEST_TYPE_RESOLVE_CAP = 200


report_app = typer.Typer(
    name="report",
    help="Generate a Markdown security report for a DefectDojo product.",
    no_args_is_help=True,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
)


def _slug(name: str) -> str:
    """Lowercase + collapse non-alphanum runs to single hyphens."""
    s = re.sub(r"[^\w\s-]", "", name).strip().lower()
    return re.sub(r"[-\s]+", "-", s) or "report"


def _test_matches(test: dict[str, Any], filters: list[str]) -> bool:
    """Case-insensitive substring match against title / test_type_name / scan_type."""
    haystack = " ".join(
        str(test.get(k) or "") for k in ("title", "test_type_name", "scan_type")
    ).lower()
    return any(needle in haystack for needle in filters)


def _resolve_test_type_names(
    client: DefectDojoClient, tests: list[dict[str, Any]]
) -> dict[int, str]:
    """Resolve test_type IDs → display names. Reuses inline `test_type_name` when present."""
    names: dict[int, str] = {}
    for test in tests:
        inline = test.get("test_type_name")
        tt_id = test.get("test_type")
        if inline and tt_id is not None:
            names[tt_id] = inline
    # For any tests that didn't include the inline name, fetch it. DefectDojo's
    # `/api/v2/test_types/?id=N` filter is supported, but fetching by path is
    # simpler and lets us cache hits per ID with no extra bookkeeping.
    missing: list[int] = [
        t["test_type"]
        for t in tests
        if t.get("test_type") is not None and t["test_type"] not in names
    ]
    for tt_id in islice(dict.fromkeys(missing), TEST_TYPE_RESOLVE_CAP):
        try:
            body = client.get(f"/api/v2/test_types/{tt_id}/")
        except NotFoundError:
            names[tt_id] = f"Test Type {tt_id}"
            continue
        name = body.get("name")
        names[tt_id] = name if isinstance(name, str) and name else f"Test Type {tt_id}"
    return names


@report_app.command("generate")
def report_generate(
    ctx: typer.Context,
    product: Annotated[
        int | None,
        typer.Option("--product", help="DefectDojo product ID. Required unless --sample."),
    ] = None,
    output_dir: Annotated[
        Path,
        typer.Option(
            "--output-dir",
            help="Output directory (created if it doesn't exist). Default: ./reports",
            file_okay=False,
            dir_okay=True,
            resolve_path=True,
        ),
    ] = Path("reports"),
    test_filter: Annotated[
        list[str] | None,
        typer.Option(
            "--test",
            help=(
                "Limit the report to tests whose title, test_type_name, or scan_type "
                "contains this string (case-insensitive). Repeatable."
            ),
        ),
    ] = None,
    detailed: Annotated[
        bool,
        typer.Option(
            "--detailed",
            help="(M6b — not yet implemented) Include per-finding notes, Jira, endpoint status.",
        ),
    ] = False,
    with_history: Annotated[
        bool,
        typer.Option(
            "--with-history",
            help="(M6b — not yet implemented) Include scan-delta block per test.",
        ),
    ] = False,
    sample: Annotated[
        bool,
        typer.Option(
            "--sample",
            help="(M6b — not yet implemented) Render from bundled mock data, no API call.",
        ),
    ] = False,
) -> None:
    """Generate a Markdown report for a DefectDojo product.

    Walks engagements → tests → active findings, enriches with SLA / KEV /
    EPSS data, and renders the bundled `report.md.j2` template. Output goes
    to `{output}/{product_id}-{slug}.md`.
    """
    if sample or detailed or with_history:
        raise ValidationError(
            "--sample, --detailed, and --with-history land in M6b. "
            "M6a ships the core --product → Markdown flow only.",
            hint="Track v2.1 progress in CHANGELOG.md or the GitHub releases page.",
        )

    if product is None:
        raise ValidationError(
            "Provide --product ID.",
            hint="Run `dd products list` to find product IDs.",
        )

    filters = [t.strip().lower() for t in (test_filter or []) if t.strip()]

    profile = get_active_profile(ctx)
    assert profile.url is not None  # narrowed by get_active_profile's is_complete check

    output_dir.mkdir(parents=True, exist_ok=True)

    with DefectDojoClient(profile) as client:
        typer.echo(f"fetching product {product}", err=True)
        product_data = client.get(f"/api/v2/products/{product}/")

        typer.echo("fetching active engagements", err=True)
        engagements = list(
            client.paginate(
                "/api/v2/engagements/",
                params={"product": product, "active": "true"},
            )
        )

        tests_by_engagement: dict[int, list[dict[str, Any]]] = {}
        findings_by_test: dict[int, list[dict[str, Any]]] = {}
        all_tests: list[dict[str, Any]] = []
        filtered_engagements: list[dict[str, Any]] = []

        for eng in engagements:
            tests = list(
                client.paginate(
                    "/api/v2/tests/",
                    params={"engagement": eng["id"]},
                )
            )
            if filters:
                tests = [t for t in tests if _test_matches(t, filters)]
                if not tests:
                    continue
            filtered_engagements.append(eng)
            tests_by_engagement[eng["id"]] = tests
            all_tests.extend(tests)
            for test in tests:
                findings_by_test[test["id"]] = list(
                    client.paginate(
                        "/api/v2/findings/",
                        params={"test": test["id"], "active": "true"},
                    )
                )

        if filters and not filtered_engagements:
            raise ValidationError(
                f"No tests matched filter(s) {filters!r} across {len(engagements)} "
                "active engagement(s).",
                hint="Try a shorter filter substring or omit --test to include all tests.",
            )

        test_type_names = _resolve_test_type_names(client, all_tests)

        try:
            sla_configurations = list(client.paginate("/api/v2/sla_configurations/"))
        except APIError:
            sla_configurations = []
        try:
            risk_acceptances = list(
                client.paginate(
                    "/api/v2/risk_acceptance/",
                    params={"engagement__product": product},
                )
            )
        except APIError:
            risk_acceptances = []

    context = build_context(
        product=product_data,
        engagements=filtered_engagements,
        tests_by_engagement=tests_by_engagement,
        findings_by_test=findings_by_test,
        test_type_names=test_type_names,
        dd_url=str(profile.url),
        test_filters=filters,
        sla_configurations=sla_configurations,
        risk_acceptances=risk_acceptances,
    )

    base = f"{product}-{_slug(product_data.get('name') or 'product')}"
    if filters:
        base += "-" + _slug("-".join(filters))

    md_path = output_dir / f"{base}.md"
    md_path.write_text(render_markdown(context), encoding="utf-8")
    typer.echo(f"wrote {md_path}", err=True)
