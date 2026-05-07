"""`dd import findings` and `dd import languages`.

Wraps the workflow modules in `dd_cli.workflows`. Every CLI flag has a
matching `DD_*` env-var alias on the workflow's options model, so users
migrating from the original `dd-import` tool can keep their pipelines
unchanged or progressively switch to flags.
"""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from dd_cli.cli._resource import (
    confirm_or_abort,
    get_active_profile,
    get_output_format,
    print_dry_run,
    render_response,
)
from dd_cli.client import DefectDojoClient
from dd_cli.output import OutputFormat
from dd_cli.workflows.import_findings import (
    ImportFindingsWorkflow,
)
from dd_cli.workflows.import_findings import (
    make_options_from_kwargs as make_findings_options,
)
from dd_cli.workflows.import_languages import (
    ImportLanguagesWorkflow,
)
from dd_cli.workflows.import_languages import (
    make_options_from_kwargs as make_languages_options,
)

import_app = typer.Typer(
    name="import",
    help="Import scanner findings or language data into DefectDojo.",
    no_args_is_help=True,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@import_app.command("findings")
def import_findings(
    ctx: typer.Context,
    file: Annotated[
        Path | None,
        typer.Option(
            "--file",
            "-f",
            help="Path to the scanner output file (JSON, XML, etc.).",
            exists=False,
            dir_okay=False,
            resolve_path=True,
        ),
    ] = None,
    scanner: Annotated[
        str | None,
        typer.Option(
            "--scanner",
            help="Test type name from DefectDojo (e.g. 'Trivy Scan', 'Bandit Scan').",
        ),
    ] = None,
    product_type: Annotated[
        str | None,
        typer.Option("--product-type", help="Product type name (created if missing)."),
    ] = None,
    product: Annotated[
        str | None,
        typer.Option("--product", help="Product name (created if missing)."),
    ] = None,
    engagement: Annotated[
        str | None,
        typer.Option(
            "--engagement",
            help=("Engagement name (required for traditional flow, optional for --auto-create)."),
        ),
    ] = None,
    test_name: Annotated[
        str | None,
        typer.Option(
            "--test-name",
            help=("Test title (required for traditional flow, optional for --auto-create)."),
        ),
    ] = None,
    auto_create: Annotated[
        bool | None,
        typer.Option(
            "--auto-create/--traditional",
            help=(
                "Use DefectDojo's single-call auto-create flow instead of "
                "find-or-create per resource."
            ),
        ),
    ] = None,
    minimum_severity: Annotated[
        str | None,
        typer.Option(
            "--minimum-severity",
            help="Drop findings below this severity (Info|Low|Medium|High|Critical).",
        ),
    ] = None,
    push_to_jira: Annotated[
        bool | None,
        typer.Option("--push-to-jira/--no-push-to-jira"),
    ] = None,
    close_old_findings: Annotated[
        bool | None,
        typer.Option("--close-old-findings/--keep-old-findings"),
    ] = None,
    yes: Annotated[bool, typer.Option("--yes", "-y", help="Skip the confirmation prompt.")] = False,
    dry_run: Annotated[
        bool,
        typer.Option(
            "--dry-run",
            help="Validate options and print intent without contacting DefectDojo.",
        ),
    ] = False,
    output: Annotated[
        OutputFormat | None,
        typer.Option("--output", "-o", help="Output format."),
    ] = None,
) -> None:
    """Import scanner output into DefectDojo (replaces `dd-reimport-findings`)."""
    opts = make_findings_options(
        file=file,
        scanner=scanner,
        product_type_name=product_type,
        product_name=product,
        engagement_name=engagement,
        test_name=test_name,
        auto_create_context=auto_create,
        minimum_severity=minimum_severity,
        push_to_jira=push_to_jira,
        close_old_findings=close_old_findings,
    )

    if dry_run:
        print_dry_run(
            "POST",
            "/api/v2/reimport-scan/",
            _summarise_findings_options(opts),
            ctx,
            output,
        )
        return

    confirm_or_abort(
        f"Import {opts.scanner!r} findings into product {opts.product_name!r}?",
        yes=yes,
    )

    profile = get_active_profile(ctx)
    with DefectDojoClient(profile) as client:
        result = ImportFindingsWorkflow(client, opts).run()

    typer.echo(_findings_summary_line(opts, result))
    render_response(_pick_findings_summary_fields(result), ctx, output)


@import_app.command("languages")
def import_languages(
    ctx: typer.Context,
    file: Annotated[
        Path | None,
        typer.Option(
            "--file",
            "-f",
            help="Path to the cloc JSON output.",
            exists=False,
            dir_okay=False,
            resolve_path=True,
        ),
    ] = None,
    product_type: Annotated[
        str | None,
        typer.Option("--product-type", help="Product type name (created if missing)."),
    ] = None,
    product: Annotated[
        str | None,
        typer.Option("--product", help="Product name (created if missing)."),
    ] = None,
    yes: Annotated[bool, typer.Option("--yes", "-y", help="Skip the confirmation prompt.")] = False,
    dry_run: Annotated[
        bool, typer.Option("--dry-run", help="Validate options and print intent.")
    ] = False,
    output: Annotated[
        OutputFormat | None,
        typer.Option("--output", "-o", help="Output format."),
    ] = None,
) -> None:
    """Upload cloc JSON output to DefectDojo (replaces `dd-import-languages`)."""
    opts = make_languages_options(
        file=file,
        product_type_name=product_type,
        product_name=product,
    )

    if dry_run:
        print_dry_run(
            "POST",
            "/api/v2/import-languages/",
            {
                "product_type": opts.product_type_name,
                "product": opts.product_name,
                "file": str(opts.file) if opts.file else None,
            },
            ctx,
            output,
        )
        return

    confirm_or_abort(
        f"Import language data for {opts.product_name!r}?",
        yes=yes,
    )

    profile = get_active_profile(ctx)
    with DefectDojoClient(profile) as client:
        result = ImportLanguagesWorkflow(client, opts).run()

    typer.echo(f"Languages imported for {opts.product_name!r}.")
    fmt = get_output_format(ctx, output)  # noqa: F841 — kept for parity
    render_response(result, ctx, output)


# ----------------------------------------------------------------------- #
#  Output helpers                                                         #
# ----------------------------------------------------------------------- #


def _summarise_findings_options(opts: object) -> dict[str, object]:
    """Produce a dict of just the fields that matter for a dry-run preview."""
    keys = (
        "scanner",
        "product_type_name",
        "product_name",
        "engagement_name",
        "test_name",
        "file",
        "auto_create_context",
        "minimum_severity",
        "push_to_jira",
        "close_old_findings",
    )
    summary: dict[str, object] = {}
    for key in keys:
        value = getattr(opts, key, None)
        if value is None:
            continue
        if hasattr(value, "__fspath__"):
            summary[key] = str(value)
        else:
            summary[key] = value
    return summary


def _pick_findings_summary_fields(result: dict[str, object]) -> dict[str, object]:
    """The reimport-scan response is large; keep only the fields users care about."""
    keys = (
        "test",
        "engagement",
        "scan_type",
        "scan_date",
        "engagement_name",
        "product_name",
        "product_type_name",
        "test_id",
        "test_title",
        "imported_findings_count",
        "new_finding_count",
        "closed_finding_count",
        "reactivated_finding_count",
    )
    return {k: result[k] for k in keys if k in result}


def _findings_summary_line(opts: object, result: dict[str, object]) -> str:
    new_ = result.get("new_finding_count")
    closed = result.get("closed_finding_count")
    reactivated = result.get("reactivated_finding_count")
    test_id = result.get("test") or result.get("test_id")
    parts = [f"Imported {getattr(opts, 'scanner', '<scanner>')!r} findings"]
    if test_id is not None:
        parts.append(f"into test {test_id}")
    if new_ is not None or closed is not None or reactivated is not None:
        counts = []
        if new_ is not None:
            counts.append(f"new={new_}")
        if closed is not None:
            counts.append(f"closed={closed}")
        if reactivated is not None:
            counts.append(f"reactivated={reactivated}")
        parts.append("(" + ", ".join(counts) + ")")
    return " ".join(parts) + "."
