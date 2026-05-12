"""`dd report` — generate a security report for a DefectDojo product.

Walks the engagement → test → finding hierarchy for a product, enriches
with SLA / KEV / EPSS / risk-acceptance metadata, and renders the
bundled Jinja templates. Markdown and HTML output ship; PDF is out of
scope (render the Markdown or HTML with the tool of your choice).

Flags:
- ``--product N`` — DefectDojo product ID (required unless ``--sample``).
- ``--format md|html|both`` — pick output format(s). Default: both.
- ``--output-dir DIR`` — where to write. Default: ``./reports``.
- ``--test NAME`` (repeatable) — substring filter on test title /
  scan_type / test_type_name.
- ``--detailed`` — fetch per-finding notes, Jira mappings, and
  endpoint_status (3 fan-out reads per finding via ``map_concurrent``).
- ``--with-history`` — fetch ``test_imports`` per test to render the
  scan-delta block (created / closed / reactivated / untouched).
- ``--sample`` — render from bundled mock data; no API call, no profile
  required. Useful for previewing the layout.
"""

from __future__ import annotations

import re
from enum import StrEnum
from itertools import islice
from pathlib import Path
from typing import Annotated, Any

import typer

from dd_cli.cli._resource import get_active_profile
from dd_cli.client import DefectDojoClient
from dd_cli.errors import APIError, NotFoundError, ValidationError
from dd_cli.reporting import build_context, render_html, render_markdown

# Maximum tests to walk while resolving test_type_names — a defensive
# cap to keep the fan-out bounded for very large products.
TEST_TYPE_RESOLVE_CAP = 200

# URL used in `--sample` output. The fixture data is fake so the URL
# doesn't resolve to anything; it just needs to be present for the
# template's "Source:" line.
SAMPLE_DD_URL = "https://defectdojo.example.com"


class ReportFormat(StrEnum):
    md = "md"
    html = "html"
    both = "both"


report_app = typer.Typer(
    name="report",
    help="Generate a security report for a DefectDojo product.",
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


def _fetch_finding_aux(
    client: DefectDojoClient,
    finding_ids: list[int],
) -> tuple[
    dict[int, list[dict[str, Any]]],
    dict[int, list[dict[str, Any]]],
    dict[int, list[dict[str, Any]]],
]:
    """Fan-out per-finding aux fetches for `--detailed` — notes, Jira, endpoint_status.

    Each finding triggers three independent reads; we parallelise via
    ``DefectDojoClient.map_concurrent`` to keep wall time bounded. Order
    is preserved so we can zip results back to finding IDs.
    """

    def _notes(fid: int) -> list[dict[str, Any]]:
        try:
            body = client.get(f"/api/v2/findings/{fid}/notes/")
        except NotFoundError:
            return []
        # DefectDojo has returned both list and {"results": [...]} shapes
        # for this endpoint across versions; handle both defensively.
        if isinstance(body.get("results"), list):
            return [n for n in body["results"] if isinstance(n, dict)]
        return []

    def _jira(fid: int) -> list[dict[str, Any]]:
        return list(
            client.paginate(
                "/api/v2/jira_finding_mappings/",
                params={"finding": fid},
            )
        )

    def _endpoint_status(fid: int) -> list[dict[str, Any]]:
        return list(
            client.paginate(
                "/api/v2/endpoint_status/",
                params={"finding": fid},
            )
        )

    notes_results = client.map_concurrent(_notes, finding_ids)
    jira_results = client.map_concurrent(_jira, finding_ids)
    ep_results = client.map_concurrent(_endpoint_status, finding_ids)

    notes_by: dict[int, list[dict[str, Any]]] = dict(zip(finding_ids, notes_results, strict=True))
    jira_by: dict[int, list[dict[str, Any]]] = dict(zip(finding_ids, jira_results, strict=True))
    ep_by: dict[int, list[dict[str, Any]]] = dict(zip(finding_ids, ep_results, strict=True))
    return notes_by, jira_by, ep_by


def _fetch_test_imports(
    client: DefectDojoClient, test_ids: list[int]
) -> dict[int, list[dict[str, Any]]]:
    """Fan-out `test_imports` for `--with-history`."""

    def _imports(tid: int) -> list[dict[str, Any]]:
        return list(client.paginate("/api/v2/test_imports/", params={"test": tid}))

    results = client.map_concurrent(_imports, test_ids)
    return dict(zip(test_ids, results, strict=True))


def _build_sample_context(filters: list[str], detailed: bool, with_history: bool) -> dict[str, Any]:
    """Construct the report context from bundled fixture data."""
    from dd_cli.reporting.fixtures import sample

    product = sample.sample_product()
    engagements = sample.sample_engagements()
    tests_by_engagement = sample.sample_tests_by_engagement()
    findings_by_test = sample.sample_findings_by_test()
    test_type_names = sample.sample_test_type_names()
    sla_configurations = sample.sample_sla_configurations()
    risk_acceptances = sample.sample_risk_acceptances()
    notes_by_finding = sample.sample_notes_by_finding() if detailed else {}
    jira_by_finding = sample.sample_jira_by_finding() if detailed else {}
    test_imports_by_test = sample.sample_test_imports_by_test() if with_history else {}

    if filters:
        kept_engagements: list[dict[str, Any]] = []
        for eng in engagements:
            kept_tests = [
                t for t in tests_by_engagement.get(eng["id"], []) if _test_matches(t, filters)
            ]
            if kept_tests:
                tests_by_engagement[eng["id"]] = kept_tests
                kept_engagements.append(eng)
        engagements = kept_engagements
        if not engagements:
            raise ValidationError(
                f"No sample tests matched filter(s) {filters!r}.",
                hint="Drop the --test flag to render the full sample.",
            )

    return build_context(
        product=product,
        engagements=engagements,
        tests_by_engagement=tests_by_engagement,
        findings_by_test=findings_by_test,
        test_type_names=test_type_names,
        dd_url=SAMPLE_DD_URL,
        test_filters=filters,
        sla_configurations=sla_configurations,
        risk_acceptances=risk_acceptances,
        notes_by_finding=notes_by_finding,
        jira_by_finding=jira_by_finding,
        test_imports_by_test=test_imports_by_test,
        detailed=detailed,
        with_history=with_history,
    )


@report_app.command("generate")
def report_generate(
    ctx: typer.Context,
    product: Annotated[
        int | None,
        typer.Option("--product", help="DefectDojo product ID. Required unless --sample."),
    ] = None,
    fmt: Annotated[
        ReportFormat,
        typer.Option(
            "--format",
            help="Output format(s). 'both' writes Markdown + HTML side-by-side.",
        ),
    ] = ReportFormat.both,
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
            help=(
                "Fetch per-finding notes, Jira mappings, and endpoint status. "
                "Adds 3 reads per finding (parallelised). Slower but richer output."
            ),
        ),
    ] = False,
    with_history: Annotated[
        bool,
        typer.Option(
            "--with-history",
            help=(
                "Fetch test_imports per test to render the scan-delta block "
                "(created / reactivated / closed / untouched since last scan)."
            ),
        ),
    ] = False,
    sample: Annotated[
        bool,
        typer.Option(
            "--sample",
            help=(
                "Render from bundled mock data — no API call. Useful for previewing "
                "the layout before configuring DefectDojo. Honours --test, --detailed, "
                "--with-history, and --format."
            ),
        ),
    ] = False,
) -> None:
    """Generate a Markdown and/or HTML report for a DefectDojo product."""
    filters = [t.strip().lower() for t in (test_filter or []) if t.strip()]
    output_dir.mkdir(parents=True, exist_ok=True)

    if sample:
        context = _build_sample_context(filters, detailed, with_history)
        base = "sample-report"
        if filters:
            base += "-" + _slug("-".join(filters))
        _write_outputs(base, output_dir, fmt, context)
        return

    if product is None:
        raise ValidationError(
            "Provide --product ID (or use --sample to render bundled fixtures).",
            hint="Run `dd products list` to find product IDs.",
        )

    profile = get_active_profile(ctx)
    assert profile.url is not None  # narrowed by get_active_profile's is_complete check

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
            tests = list(client.paginate("/api/v2/tests/", params={"engagement": eng["id"]}))
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

        notes_by_finding: dict[int, list[dict[str, Any]]] = {}
        jira_by_finding: dict[int, list[dict[str, Any]]] = {}
        endpoint_status_by_finding: dict[int, list[dict[str, Any]]] = {}
        if detailed:
            finding_ids = [f["id"] for findings in findings_by_test.values() for f in findings]
            typer.echo(
                f"fetching detail (notes, jira, endpoint status) for {len(finding_ids)} finding(s)",
                err=True,
            )
            notes_by_finding, jira_by_finding, endpoint_status_by_finding = _fetch_finding_aux(
                client, finding_ids
            )

        test_imports_by_test: dict[int, list[dict[str, Any]]] = {}
        if with_history:
            test_ids = [t["id"] for t in all_tests]
            typer.echo(f"fetching test_imports for {len(test_ids)} test(s)", err=True)
            test_imports_by_test = _fetch_test_imports(client, test_ids)

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
        notes_by_finding=notes_by_finding,
        jira_by_finding=jira_by_finding,
        endpoint_status_by_finding=endpoint_status_by_finding,
        test_imports_by_test=test_imports_by_test,
        detailed=detailed,
        with_history=with_history,
    )

    base = f"{product}-{_slug(product_data.get('name') or 'product')}"
    if filters:
        base += "-" + _slug("-".join(filters))
    _write_outputs(base, output_dir, fmt, context)


def _write_outputs(
    base: str,
    output_dir: Path,
    fmt: ReportFormat,
    context: dict[str, Any],
) -> None:
    """Write Markdown and/or HTML files to ``output_dir`` based on `fmt`."""
    if fmt in (ReportFormat.md, ReportFormat.both):
        md_path = output_dir / f"{base}.md"
        md_path.write_text(render_markdown(context), encoding="utf-8")
        typer.echo(f"wrote {md_path}", err=True)
    if fmt in (ReportFormat.html, ReportFormat.both):
        html_path = output_dir / f"{base}.html"
        html_path.write_text(render_html(context), encoding="utf-8")
        typer.echo(f"wrote {html_path}", err=True)
