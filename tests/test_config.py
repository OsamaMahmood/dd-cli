from __future__ import annotations

from pathlib import Path

import pytest

from dd_cli.config import (
    Config,
    Profile,
    default_config_path,
    load_config,
    load_profile,
    save_config,
)
from dd_cli.config.paths import default_config_dir
from dd_cli.errors import ConfigError


@pytest.fixture
def tmp_config(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.setenv("DD_CLI_CONFIG_DIR", str(tmp_path))
    return tmp_path / "config.toml"


# ---------------------------- paths --------------------------------------- #


def test_default_config_dir_honours_override(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DD_CLI_CONFIG_DIR", "/some/where")
    assert default_config_dir() == Path("/some/where")


def test_default_config_path_includes_filename(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DD_CLI_CONFIG_DIR", "/some/where")
    assert default_config_path() == Path("/some/where/config.toml")


def test_default_config_dir_uses_xdg_when_set(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("DD_CLI_CONFIG_DIR", raising=False)
    monkeypatch.setenv("XDG_CONFIG_HOME", "/xdg/home")
    assert default_config_dir() == Path("/xdg/home/dd-cli")


# ---------------------------- TOML round-trip ----------------------------- #


def test_load_config_returns_empty_when_file_missing(tmp_path: Path) -> None:
    config = load_config(tmp_path / "nope.toml")
    assert config.default_profile == "default"
    assert config.profiles == {}


def test_save_then_load_round_trips(tmp_path: Path) -> None:
    config_path = tmp_path / "config.toml"
    config = Config(
        default_profile="prod",
        profiles={
            "prod": Profile(
                name="prod",
                url="https://prod.example",
                api_key="secret-prod",  # type: ignore[arg-type]
                ssl_verify=True,
                extra_headers={"X-Tenant": "main"},
            ),
            "staging": Profile(
                name="staging",
                url="https://staging.example",
                api_key="secret-staging",  # type: ignore[arg-type]
                ssl_verify=False,
            ),
        },
    )
    save_config(config, config_path)

    loaded = load_config(config_path)
    assert loaded.default_profile == "prod"
    assert set(loaded.profiles) == {"prod", "staging"}

    prod = loaded.profiles["prod"]
    assert prod.url == "https://prod.example"
    assert prod.api_key is not None
    assert prod.api_key.get_secret_value() == "secret-prod"
    assert prod.ssl_verify is True
    assert prod.extra_headers == {"X-Tenant": "main"}

    assert loaded.profiles["staging"].ssl_verify is False


def test_save_config_creates_parent_dirs(tmp_path: Path) -> None:
    target = tmp_path / "nested" / "dirs" / "config.toml"
    save_config(Config(), target)
    assert target.exists()


def test_load_config_rejects_invalid_toml(tmp_path: Path) -> None:
    bad = tmp_path / "config.toml"
    bad.write_text("not = valid = toml")
    with pytest.raises(ConfigError):
        load_config(bad)


def test_load_config_rejects_non_table_profiles(tmp_path: Path) -> None:
    bad = tmp_path / "config.toml"
    bad.write_text("profiles = 42\n")
    with pytest.raises(ConfigError):
        load_config(bad)


# ---------------------------- Config helpers ------------------------------ #


def test_get_profile_returns_named_when_present() -> None:
    config = Config(
        default_profile="dev",
        profiles={"dev": Profile(name="dev", url="https://dev")},
    )
    assert config.get_profile("dev").url == "https://dev"


def test_get_profile_falls_back_to_default() -> None:
    config = Config(
        default_profile="dev",
        profiles={"dev": Profile(name="dev", url="https://dev")},
    )
    assert config.get_profile().url == "https://dev"


def test_get_profile_returns_empty_for_unknown_name() -> None:
    config = Config()
    profile = config.get_profile("ghost")
    assert profile.name == "ghost"
    assert profile.url is None


def test_profile_is_complete_requires_url_and_api_key() -> None:
    assert not Profile().is_complete()
    assert not Profile(url="https://x").is_complete()
    assert Profile(url="https://x", api_key="k").is_complete()  # type: ignore[arg-type]


# ---------------------------- env-var overrides --------------------------- #


def test_env_vars_override_profile_values(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config = Config(
        default_profile="default",
        profiles={"default": Profile(url="https://from-toml", api_key="toml-key")},  # type: ignore[arg-type]
    )
    save_config(config, tmp_path / "config.toml")
    monkeypatch.setenv("DD_CLI_URL", "https://from-env")

    profile = load_profile(config_path=tmp_path / "config.toml")
    assert profile.url == "https://from-env"
    assert profile.api_key is not None
    # api_key was not overridden by env
    assert profile.api_key.get_secret_value() == "toml-key"


def test_legacy_dd_env_vars_are_honoured(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("DD_CLI_URL", raising=False)
    monkeypatch.delenv("DD_CLI_API_KEY", raising=False)
    monkeypatch.setenv("DD_URL", "https://legacy.example")
    monkeypatch.setenv("DD_API_KEY", "legacy-key")

    profile = load_profile(config_path=tmp_path / "absent.toml")
    assert profile.url == "https://legacy.example"
    assert profile.api_key is not None
    assert profile.api_key.get_secret_value() == "legacy-key"


def test_dd_cli_takes_precedence_over_dd(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("DD_CLI_URL", "https://new")
    monkeypatch.setenv("DD_URL", "https://legacy")

    profile = load_profile(config_path=tmp_path / "absent.toml")
    assert profile.url == "https://new"


def test_load_profile_can_skip_env(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    save_config(
        Config(profiles={"default": Profile(url="https://from-toml")}),
        tmp_path / "config.toml",
    )
    monkeypatch.setenv("DD_CLI_URL", "https://from-env")

    profile = load_profile(
        config_path=tmp_path / "config.toml",
        apply_env=False,
    )
    assert profile.url == "https://from-toml"


def test_ssl_verify_env_override(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("DD_SSL_VERIFY", "false")
    profile = load_profile(config_path=tmp_path / "absent.toml")
    assert profile.ssl_verify is False
