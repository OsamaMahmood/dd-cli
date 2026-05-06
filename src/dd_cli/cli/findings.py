"""`dd findings` — list, get, CRUD, plus close / reopen / risk-accept verbs."""

from __future__ import annotations

from typing import Annotated, Any

import typer

from dd_cli.cli._resource import (
    DEFAULT_LIMIT,
    ResourceSpec,
    confirm_or_abort,
    get_active_profile,
    get_dispatch,
    list_resource,
    print_dry_run,
    register_crud,
    render_response,
)
from dd_cli.client import DefectDojoClient
from dd_cli.errors import APIError, ValidationError
from dd_cli.output import OutputFormat

VALID_DECISIONS = {
    "A": "Accept",
    "V": "Avoid",
    "M": "Mitigate",
    "F": "Fix",
    "T": "Transfer",
}

FINDINGS_SPEC = ResourceSpec(
    name="finding",
    plural="findings",
    path="/api/v2/findings/",
    columns=("id", "title", "severity", "active", "verified", "found_by"),
    name_field="title",
)


VALID_SEVERITIES = {"Critical", "High", "Medium", "Low", "Info"}


findings_app = typer.Typer(
    name="findings",
    help="List and get DefectDojo findings.",
    no_args_is_help=True,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@findings_app.command("list")
def findings_list(
    ctx: typer.Context,
    title: Annotated[
        str | None,
        typer.Option("--title", help="Filter by exact finding title."),
    ] = None,
    product: Annotated[
        int | None,
        typer.Option("--product", help="Filter by product ID."),
    ] = None,
    engagement: Annotated[
        int | None,
        typer.Option("--engagement", help="Filter by engagement ID."),
    ] = None,
    test: Annotated[int | None, typer.Option("--test", help="Filter by test ID.")] = None,
    severity: Annotated[
        str | None,
        typer.Option(
            "--severity",
            help=f"Filter by severity. One of: {', '.join(sorted(VALID_SEVERITIES))}.",
        ),
    ] = None,
    active: Annotated[
        bool | None,
        typer.Option(
            "--active/--inactive",
            help="Filter by active flag.",
        ),
    ] = None,
    verified: Annotated[
        bool | None,
        typer.Option(
            "--verified/--unverified",
            help="Filter by verified flag.",
        ),
    ] = None,
    duplicate: Annotated[
        bool | None,
        typer.Option(
            "--duplicate/--non-duplicate",
            help="Filter by duplicate flag.",
        ),
    ] = None,
    tag: Annotated[str | None, typer.Option("--tag", help="Filter by tag (exact match).")] = None,
    limit: Annotated[
        int, typer.Option("--limit", help=f"Maximum rows. Default: {DEFAULT_LIMIT}.")
    ] = DEFAULT_LIMIT,
    all_pages: Annotated[bool, typer.Option("--all", help="Stream every page.")] = False,
    output: Annotated[
        OutputFormat | None,
        typer.Option("--output", "-o", help="Output format."),
    ] = None,
) -> None:
    """List findings with optional filters.

    Severity is case-insensitive on input but normalised to DefectDojo's
    canonical capitalisation (`Critical`, `High`, …) before the API call.
    """
    canonical_severity = _canonicalise_severity(severity)

    list_resource(
        ctx,
        FINDINGS_SPEC,
        filters={
            "title": title,
            "product": product,
            "test__engagement__product": product,
            "test__engagement": engagement,
            "test": test,
            "severity": canonical_severity,
            "active": active,
            "verified": verified,
            "duplicate": duplicate,
            "tag": tag,
        },
        limit=limit,
        all_pages=all_pages,
        output=output,
    )


@findings_app.command("get")
def findings_get(
    ctx: typer.Context,
    finding_id: Annotated[
        int | None,
        typer.Argument(help="Finding ID (omit if using --name)."),
    ] = None,
    name: Annotated[
        str | None,
        typer.Option("--name", help="Resolve by exact finding title."),
    ] = None,
    output: Annotated[
        OutputFormat | None,
        typer.Option("--output", "-o", help="Output format."),
    ] = None,
) -> None:
    """Get a single finding by ID or title."""
    get_dispatch(ctx, FINDINGS_SPEC, resource_id=finding_id, name=name, output=output)


def _canonicalise_severity(value: str | None) -> str | None:
    if value is None:
        return None
    by_lower = {s.lower(): s for s in VALID_SEVERITIES}
    canonical = by_lower.get(value.lower())
    if canonical is None:
        raise ValidationError(
            f"Unknown severity {value!r}. Expected one of {sorted(VALID_SEVERITIES)}.",
        )
    return canonical


register_crud(findings_app, FINDINGS_SPEC)


# ---------------------------- action verbs ------------------------------ #


@findings_app.command("close")
def findings_close(
    ctx: typer.Context,
    finding_id: Annotated[int, typer.Argument(help="Finding ID.")],
    note: Annotated[
        str | None, typer.Option("--note", help="Mitigation note attached to the closure.")
    ] = None,
    false_positive: Annotated[
        bool, typer.Option("--false-positive", help="Mark as a false positive.")
    ] = False,
    out_of_scope: Annotated[
        bool, typer.Option("--out-of-scope", help="Mark as out of scope.")
    ] = False,
    duplicate: Annotated[bool, typer.Option("--duplicate", help="Mark as a duplicate.")] = False,
    yes: Annotated[bool, typer.Option("--yes", "-y", help="Skip confirmation.")] = False,
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Print intent only.")] = False,
    output: Annotated[
        OutputFormat | None, typer.Option("--output", "-o", help="Output format.")
    ] = None,
) -> None:
    """Close a finding via DefectDojo's dedicated /close/ endpoint."""
    payload: dict[str, Any] = {"is_mitigated": True}
    if note:
        payload["note"] = note
    if false_positive:
        payload["false_p"] = True
    if out_of_scope:
        payload["out_of_scope"] = True
    if duplicate:
        payload["duplicate"] = True

    target = f"/api/v2/findings/{finding_id}/close/"

    if dry_run:
        print_dry_run("POST", target, payload, ctx, output)
        return

    confirm_or_abort(f"Close finding {finding_id}?", yes=yes)

    profile = get_active_profile(ctx)
    with DefectDojoClient(profile) as client:
        body = client.post(target, json=payload)

    typer.echo(f"Closed finding {finding_id}.")
    render_response(body, ctx, output)


@findings_app.command("reopen")
def findings_reopen(
    ctx: typer.Context,
    finding_id: Annotated[int, typer.Argument(help="Finding ID.")],
    yes: Annotated[bool, typer.Option("--yes", "-y", help="Skip confirmation.")] = False,
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Print intent only.")] = False,
    output: Annotated[
        OutputFormat | None, typer.Option("--output", "-o", help="Output format.")
    ] = None,
) -> None:
    """Reopen a closed finding (PATCH is_mitigated=false, active=true)."""
    payload: dict[str, Any] = {"is_mitigated": False, "active": True, "mitigated": None}
    target = f"/api/v2/findings/{finding_id}/"

    if dry_run:
        print_dry_run("PATCH", target, payload, ctx, output)
        return

    confirm_or_abort(f"Reopen finding {finding_id}?", yes=yes)

    profile = get_active_profile(ctx)
    with DefectDojoClient(profile) as client:
        body = client.patch(target, json=payload)

    typer.echo(f"Reopened finding {finding_id}.")
    render_response(body, ctx, output)


@findings_app.command("risk-accept")
def findings_risk_accept(
    ctx: typer.Context,
    finding_id: Annotated[int, typer.Argument(help="Finding ID to accept.")],
    until: Annotated[
        str | None,
        typer.Option(
            "--until",
            help="Expiration date (YYYY-MM-DD). Findings reactivate at expiry by default.",
        ),
    ] = None,
    name: Annotated[
        str | None,
        typer.Option(
            "--name",
            help="Risk-acceptance name (default: 'Risk acceptance for finding <id>').",
        ),
    ] = None,
    decision: Annotated[
        str,
        typer.Option(
            "--decision",
            help=f"Decision letter. One of {sorted(VALID_DECISIONS)} = "
            f"{', '.join(f'{k}={v}' for k, v in VALID_DECISIONS.items())}.",
        ),
    ] = "A",
    reason: Annotated[
        str | None,
        typer.Option(
            "--reason",
            help="Decision details (compensating controls, rationale).",
        ),
    ] = None,
    owner: Annotated[
        int | None,
        typer.Option(
            "--owner",
            help="Owner user ID. Defaults to the calling user.",
        ),
    ] = None,
    keep_expired: Annotated[
        bool,
        typer.Option(
            "--keep-expired",
            help="Do NOT reactivate findings when the acceptance expires.",
        ),
    ] = False,
    yes: Annotated[bool, typer.Option("--yes", "-y", help="Skip confirmation.")] = False,
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Print intent only.")] = False,
    output: Annotated[
        OutputFormat | None, typer.Option("--output", "-o", help="Output format.")
    ] = None,
) -> None:
    """Create a risk acceptance for a finding."""
    decision_canonical = decision.upper()
    if decision_canonical not in VALID_DECISIONS:
        raise ValidationError(
            f"Unknown decision {decision!r}. Expected one of {sorted(VALID_DECISIONS)}.",
        )

    payload: dict[str, Any] = {
        "name": name or f"Risk acceptance for finding {finding_id}",
        "accepted_findings": [finding_id],
        "decision": decision_canonical,
        "reactivate_expired": not keep_expired,
    }
    if until:
        payload["expiration_date"] = _parse_date_to_iso(until)
    if reason:
        payload["decision_details"] = reason

    target = "/api/v2/risk_acceptance/"

    if owner is not None:
        payload["owner"] = owner

    if dry_run:
        # Dry run with no resolved owner is fine — DefectDojo would reject without one,
        # but we honour the user's explicit "show me what you'd send" request.
        print_dry_run("POST", target, payload, ctx, output)
        return

    profile = get_active_profile(ctx)
    with DefectDojoClient(profile) as client:
        if owner is None:
            payload["owner"] = _resolve_current_user_id(client)
        confirm_or_abort(
            f"Risk-accept finding {finding_id} (decision={decision_canonical})?",
            yes=yes,
        )
        body = client.post(target, json=payload)

    typer.echo(f"Risk-accepted finding {finding_id} (acceptance id={body.get('id')}).")
    render_response(body, ctx, output)


def _parse_date_to_iso(value: str) -> str:
    """Accept YYYY-MM-DD and return an ISO 8601 datetime DefectDojo will accept."""
    import datetime

    try:
        d = datetime.date.fromisoformat(value)
    except ValueError as exc:
        raise ValidationError(
            f"--until expects YYYY-MM-DD, got {value!r}",
        ) from exc
    return f"{d.isoformat()}T00:00:00Z"


def _resolve_current_user_id(client: DefectDojoClient) -> int:
    body = client.whoami()
    user = body.get("user")
    if isinstance(user, dict):
        candidate = user.get("id")
        if isinstance(candidate, int):
            return candidate
    candidate = body.get("id")
    if isinstance(candidate, int):
        return candidate
    raise APIError(
        "Could not resolve current user ID from /api/v2/user_profile/",
        hint="Pass --owner USER_ID explicitly.",
    )
