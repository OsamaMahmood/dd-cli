"""`dd config` subcommands: show / get / set / list / use / unset.

All operations work on the on-disk TOML at `~/.config/dd-cli/config.toml`
(or `DD_CLI_CONFIG_DIR/config.toml`), except `show` which renders the
fully-resolved profile after env-var overrides are applied.
"""

from __future__ import annotations

from typing import Annotated, Any

import typer

from dd_cli.config import (
    Profile,
    load_config,
    load_profile,
    save_config,
)
from dd_cli.errors import ConfigError, ValidationError
from dd_cli.output import OutputFormat, render

config_app = typer.Typer(
    name="config",
    help="Manage dd-cli profiles and on-disk configuration.",
    no_args_is_help=True,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
)

SETTABLE_KEYS = {"url", "api_key", "ssl_verify"}


def _resolved_profile_name(ctx: typer.Context, override: str | None) -> str | None:
    """Resolve the active profile name from (in order): explicit flag → ctx.obj → None."""
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


def _coerce_value(key: str, raw: str) -> Any:
    if key == "ssl_verify":
        truthy = {"true", "yes", "1", "on"}
        falsy = {"false", "no", "0", "off"}
        v = raw.lower()
        if v in truthy:
            return True
        if v in falsy:
            return False
        raise ValidationError(f"`ssl_verify` must be one of {sorted(truthy | falsy)}, got {raw!r}")
    return raw


def _mask_secret(profile_dict: dict[str, Any]) -> dict[str, Any]:
    masked = dict(profile_dict)
    if masked.get("api_key"):
        masked["api_key"] = "<set>"
    elif "api_key" in masked:
        masked["api_key"] = "<not set>"
    return masked


def _profile_to_display(profile: Profile) -> dict[str, Any]:
    data = profile.model_dump(exclude_none=False)
    if profile.api_key is not None:
        data["api_key"] = "<set>"
    else:
        data["api_key"] = "<not set>"
    return data


@config_app.command("show")
def show(
    ctx: typer.Context,
    profile: Annotated[
        str | None,
        typer.Option("--profile", "-p", help="Profile to show. Defaults to the active profile."),
    ] = None,
    output: Annotated[
        OutputFormat | None,
        typer.Option("--output", "-o", help="Output format."),
    ] = None,
) -> None:
    """Show the resolved configuration for a profile (env vars merged in)."""
    name = _resolved_profile_name(ctx, profile)
    fmt = _output_format(ctx, output)
    resolved = load_profile(name=name)
    typer.echo(render(_profile_to_display(resolved), fmt), nl=False)


@config_app.command("get")
def get(
    ctx: typer.Context,
    key: Annotated[str, typer.Argument(help="Field to read.")],
    profile: Annotated[
        str | None,
        typer.Option("--profile", "-p"),
    ] = None,
    show_secrets: Annotated[
        bool,
        typer.Option("--show-secrets", help="Reveal secret values like api_key."),
    ] = False,
) -> None:
    """Print one field from the active profile (env-merged)."""
    name = _resolved_profile_name(ctx, profile)
    resolved = load_profile(name=name)
    data = resolved.model_dump()
    if key not in data:
        raise ValidationError(f"Unknown key `{key}`")
    value = data[key]
    if key == "api_key" and resolved.api_key is not None:
        value = resolved.api_key.get_secret_value() if show_secrets else "<set>"
    if isinstance(value, dict):
        typer.echo(render(value, OutputFormat.table), nl=False)
    else:
        typer.echo("" if value is None else str(value))


@config_app.command("set")
def set_value(
    ctx: typer.Context,
    key: Annotated[str, typer.Argument(help=f"One of {sorted(SETTABLE_KEYS)}.")],
    value: Annotated[str, typer.Argument(help="New value.")],
    profile: Annotated[
        str | None,
        typer.Option("--profile", "-p"),
    ] = None,
) -> None:
    """Set a field in a TOML profile. Creates the profile if it does not exist."""
    if key not in SETTABLE_KEYS:
        raise ValidationError(
            f"Cannot set `{key}` via `dd config set`. Settable keys: {sorted(SETTABLE_KEYS)}.",
            hint="For extra_headers, use `dd configure` (interactive setup).",
        )
    coerced = _coerce_value(key, value)
    name = _resolved_profile_name(ctx, profile) or "default"

    config = load_config()
    profile_dict = (
        config.profiles[name].model_dump(exclude_none=False)
        if name in config.profiles
        else {"name": name}
    )
    if key == "api_key" and config.profiles.get(name) is not None:
        # Preserve existing secret unless we're overwriting it
        existing = config.profiles[name].api_key
        if existing is not None:
            profile_dict["api_key"] = existing.get_secret_value()
    profile_dict[key] = coerced
    config.profiles[name] = Profile.model_validate(profile_dict)
    if not config.profiles or len(config.profiles) == 1:
        config.default_profile = name
    save_config(config)
    typer.echo(f"Set {key} for profile `{name}`.")


@config_app.command("list")
def list_profiles(
    ctx: typer.Context,
    output: Annotated[
        OutputFormat | None,
        typer.Option("--output", "-o", help="Output format."),
    ] = None,
) -> None:
    """List all profiles in the on-disk config."""
    fmt = _output_format(ctx, output)
    config = load_config()
    if not config.profiles:
        typer.echo("No profiles configured. Run `dd configure` to create one.")
        return
    rows = [
        {"name": pname, "default": pname == config.default_profile, "url": p.url or ""}
        for pname, p in sorted(config.profiles.items())
    ]
    typer.echo(render(rows, fmt), nl=False)


@config_app.command("use")
def use(
    name: Annotated[str, typer.Argument(help="Profile name to make default.")],
) -> None:
    """Set the default profile used when no `--profile` is given."""
    config = load_config()
    if name not in config.profiles:
        raise ConfigError(
            f"Cannot set default to unknown profile `{name}`.",
            hint="Run `dd config list` to see available profiles.",
        )
    config.default_profile = name
    save_config(config)
    typer.echo(f"Default profile set to `{name}`.")


@config_app.command("unset")
def unset(
    ctx: typer.Context,
    key: Annotated[str, typer.Argument(help="Field to clear.")],
    profile: Annotated[
        str | None,
        typer.Option("--profile", "-p"),
    ] = None,
) -> None:
    """Clear a field in a profile (resets it to the model default)."""
    if key not in SETTABLE_KEYS:
        raise ValidationError(f"Cannot unset `{key}`. Settable keys: {sorted(SETTABLE_KEYS)}.")
    name = _resolved_profile_name(ctx, profile) or "default"
    config = load_config()
    if name not in config.profiles:
        raise ConfigError(f"Profile `{name}` does not exist.")
    profile_dict = config.profiles[name].model_dump(exclude_none=False)
    profile_dict[key] = None if key != "ssl_verify" else True
    if key == "api_key":
        profile_dict["api_key"] = None
    config.profiles[name] = Profile.model_validate(profile_dict)
    save_config(config)
    typer.echo(f"Unset {key} for profile `{name}`.")


@config_app.command("delete")
def delete(
    name: Annotated[str, typer.Argument(help="Profile to delete.")],
    yes: Annotated[
        bool,
        typer.Option("--yes", "-y", help="Skip confirmation prompt."),
    ] = False,
) -> None:
    """Delete a profile from the on-disk config."""
    config = load_config()
    if name not in config.profiles:
        raise ConfigError(f"Profile `{name}` does not exist.")
    if not yes:
        confirm = typer.confirm(f"Delete profile `{name}`?")
        if not confirm:
            typer.echo("Aborted.")
            raise typer.Exit(code=0)
    del config.profiles[name]
    if config.default_profile == name:
        remaining = sorted(config.profiles)
        config.default_profile = remaining[0] if remaining else "default"
    save_config(config)
    typer.echo(f"Deleted profile `{name}`.")
