"""`dd ping` — verify connectivity and authentication against DefectDojo."""

from __future__ import annotations

from typing import Annotated, Any

import typer

from dd_cli.client import DefectDojoClient
from dd_cli.config import load_profile
from dd_cli.errors import ConfigError
from dd_cli.output import OutputFormat, render


def _resolved_profile_name(ctx: typer.Context, override: str | None) -> str | None:
    if override:
        return override
    obj = ctx.obj or {}
    return obj.get("profile")


def _output_format(ctx: typer.Context, override: OutputFormat | None) -> OutputFormat:
    if override is not None:
        return override
    obj = ctx.obj or {}
    fmt = obj.get("output")
    return fmt if isinstance(fmt, OutputFormat) else OutputFormat.table


def ping(
    ctx: typer.Context,
    profile: Annotated[
        str | None,
        typer.Option("--profile", "-p", help="Profile to use."),
    ] = None,
    output: Annotated[
        OutputFormat | None,
        typer.Option("--output", "-o", help="Output format."),
    ] = None,
) -> None:
    """Hit /api/v2/user_profile/ to verify the active profile works."""
    name = _resolved_profile_name(ctx, profile)
    fmt = _output_format(ctx, output)

    resolved = load_profile(name=name)
    if not resolved.is_complete():
        raise ConfigError(
            f"Profile `{resolved.name}` is missing url and/or api_key.",
            hint="Run `dd configure` to set them.",
        )

    with DefectDojoClient(resolved) as client:
        body = client.whoami()

    summary: dict[str, Any] = {
        "profile": resolved.name,
        "url": resolved.url,
        "ok": True,
        "user": _extract_username(body),
    }
    typer.echo(render(summary, fmt), nl=False)


def _extract_username(body: dict[str, Any]) -> str:
    """DefectDojo's user_profile schema has changed shape across versions; cover both."""
    if isinstance(body.get("user"), dict):
        username = body["user"].get("username")
        if isinstance(username, str):
            return username
    if isinstance(body.get("username"), str):
        return str(body["username"])
    return "<unknown>"
