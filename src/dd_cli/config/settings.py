"""Config models and TOML persistence for dd-cli.

`Profile` is the per-target configuration (URL, API key, etc.). `Config` is
the top-level structure stored on disk: a default-profile pointer plus a
`profiles` table.

Env-var overrides come from `_EnvOverrides`, which reads both the new
`DD_CLI_*` variables and the legacy `DD_*` ones (kept for backwards
compatibility with the original `dd-import` tool).
"""

from __future__ import annotations

import tomllib
from pathlib import Path
from typing import Any, cast

import tomli_w
from pydantic import AliasChoices, BaseModel, ConfigDict, Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from dd_cli.config.paths import default_config_path
from dd_cli.errors import ConfigError

DEFAULT_PROFILE_NAME = "default"


class Profile(BaseModel):
    """A single named target configuration."""

    model_config = ConfigDict(extra="forbid")

    name: str = DEFAULT_PROFILE_NAME
    url: str | None = None
    api_key: SecretStr | None = None
    ssl_verify: bool = True
    extra_headers: dict[str, str] = Field(default_factory=dict)

    def is_complete(self) -> bool:
        """True iff this profile has the minimum required fields to talk to DefectDojo."""
        return bool(self.url) and self.api_key is not None


class Config(BaseModel):
    """The on-disk structure of `~/.config/dd-cli/config.toml`."""

    model_config = ConfigDict(extra="forbid")

    default_profile: str = DEFAULT_PROFILE_NAME
    profiles: dict[str, Profile] = Field(default_factory=dict)

    def get_profile(self, name: str | None = None) -> Profile:
        """Return the named profile, falling back to default_profile, falling back to a fresh empty Profile."""
        target = name or self.default_profile
        return self.profiles.get(target) or Profile(name=target)


class _EnvOverrides(BaseSettings):
    """Env-var view of profile fields. Unset fields stay None."""

    model_config = SettingsConfigDict(case_sensitive=False, extra="ignore")

    url: str | None = Field(
        default=None,
        validation_alias=AliasChoices("DD_CLI_URL", "DD_URL"),
    )
    api_key: SecretStr | None = Field(
        default=None,
        validation_alias=AliasChoices("DD_CLI_API_KEY", "DD_API_KEY"),
    )
    ssl_verify: bool | None = Field(
        default=None,
        validation_alias=AliasChoices("DD_CLI_SSL_VERIFY", "DD_SSL_VERIFY"),
    )


def load_config(path: Path | None = None) -> Config:
    """Load `Config` from a TOML file. Returns an empty `Config` if the file is absent."""
    target = path or default_config_path()
    if not target.exists():
        return Config()
    try:
        with target.open("rb") as fh:
            data = tomllib.load(fh)
    except tomllib.TOMLDecodeError as exc:
        raise ConfigError(
            f"Invalid TOML in {target}: {exc}",
            hint="Run `dd configure` to rewrite the file from scratch.",
        ) from exc

    profiles_raw = data.get("profiles", {})
    if not isinstance(profiles_raw, dict):
        raise ConfigError(
            f"`profiles` must be a table in {target}",
            hint="Run `dd configure` to rewrite the file from scratch.",
        )

    profiles: dict[str, Profile] = {}
    for profile_name, profile_data in profiles_raw.items():
        if not isinstance(profile_data, dict):
            raise ConfigError(f"Profile `{profile_name}` is not a table in {target}")
        profile_data = cast(dict[str, Any], dict(profile_data))
        profile_data.setdefault("name", profile_name)
        profiles[profile_name] = Profile.model_validate(profile_data)

    return Config(
        default_profile=str(data.get("default_profile", DEFAULT_PROFILE_NAME)),
        profiles=profiles,
    )


def save_config(config: Config, path: Path | None = None) -> Path:
    """Persist `Config` to TOML, creating parent directories if needed."""
    target = path or default_config_path()
    target.parent.mkdir(parents=True, exist_ok=True)

    profiles_table: dict[str, Any] = {}
    for profile_name, profile in config.profiles.items():
        profile_dict = profile.model_dump(exclude={"name"}, exclude_none=True)
        if profile.api_key is not None:
            profile_dict["api_key"] = profile.api_key.get_secret_value()
        profiles_table[profile_name] = profile_dict

    payload: dict[str, Any] = {"default_profile": config.default_profile}
    if profiles_table:
        payload["profiles"] = profiles_table

    target.write_bytes(tomli_w.dumps(payload).encode("utf-8"))
    return target


def load_profile(
    name: str | None = None,
    *,
    config_path: Path | None = None,
    apply_env: bool = True,
) -> Profile:
    """Resolve the active profile by merging defaults, TOML, and env vars.

    Order (later wins):
        defaults → TOML profile → env-var overrides
    """
    config = load_config(config_path)
    profile = config.get_profile(name)

    if apply_env:
        overrides = _EnvOverrides().model_dump(exclude_none=True)
        if overrides:
            profile = profile.model_copy(update=overrides)

    return profile
