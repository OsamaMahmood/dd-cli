"""`dd configure` — interactive profile setup."""

from __future__ import annotations

from typing import Annotated

import typer
from rich.console import Console

from dd_cli.config import (
    Profile,
    load_config,
    save_config,
)

console = Console()


def configure(
    profile: Annotated[
        str | None,
        typer.Option(
            "--profile",
            "-p",
            help="Profile name to create or update.",
        ),
    ] = None,
    url: Annotated[
        str | None,
        typer.Option("--url", help="DefectDojo URL (skips the URL prompt).", show_default=False),
    ] = None,
    api_key: Annotated[
        str | None,
        typer.Option("--api-key", help="API token (skips the prompt).", show_default=False),
    ] = None,
    no_input: Annotated[
        bool,
        typer.Option("--no-input", help="Fail instead of prompting for missing values."),
    ] = False,
) -> None:
    """Interactive setup that writes a profile to ~/.config/dd-cli/config.toml."""
    config = load_config()

    profile_name = profile or _prompt_or_default(
        "Profile name",
        default="default",
        no_input=no_input,
    )
    existing = config.profiles.get(profile_name, Profile(name=profile_name))

    resolved_url = url or _prompt_or_default(
        "DefectDojo URL",
        default=existing.url or "",
        no_input=no_input,
        required=True,
    )

    if api_key is None:
        api_key = _prompt_secret(
            "API key",
            existing_present=existing.api_key is not None,
            no_input=no_input,
        )
    if not api_key and existing.api_key is not None:
        api_key = existing.api_key.get_secret_value()
    if not api_key:
        raise typer.BadParameter("API key is required.")

    ssl_verify = (
        existing.ssl_verify
        if no_input
        else typer.confirm("Verify TLS certificates?", default=existing.ssl_verify)
    )

    extra_headers = dict(existing.extra_headers)
    if not no_input and typer.confirm("Add extra HTTP headers (e.g. for WAF auth)?", default=False):
        while True:
            header_name = typer.prompt(
                "Header name (empty to finish)", default="", show_default=False
            )
            if not header_name:
                break
            header_value = typer.prompt(f"Value for {header_name}")
            extra_headers[header_name] = header_value

    new_profile = Profile(
        name=profile_name,
        url=resolved_url,
        api_key=api_key,  # type: ignore[arg-type]
        ssl_verify=ssl_verify,
        extra_headers=extra_headers,
    )
    config.profiles[profile_name] = new_profile
    if profile_name == "default" or len(config.profiles) == 1:
        config.default_profile = profile_name

    target = save_config(config)
    console.print(f"\n[green]✓[/green] Saved profile [bold]{profile_name}[/bold] to {target}")


def _prompt_or_default(
    prompt: str,
    *,
    default: str,
    no_input: bool,
    required: bool = False,
) -> str:
    if no_input:
        if required and not default:
            raise typer.BadParameter(f"{prompt} is required (no_input mode).")
        return default
    return str(typer.prompt(prompt, default=default, show_default=bool(default)))


def _prompt_secret(prompt: str, *, existing_present: bool, no_input: bool) -> str:
    if no_input:
        return ""
    suffix = " (press Enter to keep existing)" if existing_present else ""
    return str(typer.prompt(f"{prompt}{suffix}", default="", hide_input=True, show_default=False))
