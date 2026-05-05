"""Backward-compatibility tests for the dd-import DD_* connection env-vars.

These tests pin the behavior of the legacy `Environment` class for the
connection-level vars that M1 covers (DD_URL, DD_API_KEY, DD_SSL_VERIFY,
DD_EXTRA_HEADER_*). Workflow-specific vars (DD_PRODUCT_NAME, etc.) are
covered separately in M4.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from dd_cli.config import load_profile
from dd_cli.config.legacy_env import legacy_extra_headers

pytestmark = pytest.mark.compat


@pytest.fixture(autouse=True)
def _clear_legacy_env(monkeypatch: pytest.MonkeyPatch) -> None:
    for var in (
        "DD_URL",
        "DD_API_KEY",
        "DD_SSL_VERIFY",
        "DD_CLI_URL",
        "DD_CLI_API_KEY",
        "DD_CLI_SSL_VERIFY",
        "DD_EXTRA_HEADER_1",
        "DD_EXTRA_HEADER_1_VALUE",
        "DD_EXTRA_HEADER_2",
        "DD_EXTRA_HEADER_2_VALUE",
    ):
        monkeypatch.delenv(var, raising=False)


def test_dd_url_is_read_from_legacy_env(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("DD_URL", "https://legacy.example")
    profile = load_profile(config_path=tmp_path / "absent.toml")
    assert profile.url == "https://legacy.example"


def test_dd_api_key_is_read_from_legacy_env(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("DD_API_KEY", "legacy-key")
    profile = load_profile(config_path=tmp_path / "absent.toml")
    assert profile.api_key is not None
    assert profile.api_key.get_secret_value() == "legacy-key"


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("true", True),
        ("True", True),
        ("1", True),
        ("false", False),
        ("False", False),
        ("0", False),
    ],
)
def test_dd_ssl_verify_legacy_values(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    value: str,
    expected: bool,
) -> None:
    monkeypatch.setenv("DD_SSL_VERIFY", value)
    profile = load_profile(config_path=tmp_path / "absent.toml")
    assert profile.ssl_verify is expected


def test_extra_header_pair_becomes_dict_entry() -> None:
    env = {
        "DD_EXTRA_HEADER_1": "X-WAF-Token",
        "DD_EXTRA_HEADER_1_VALUE": "secret-1",
    }
    assert legacy_extra_headers(env) == {"X-WAF-Token": "secret-1"}


def test_extra_header_orphan_name_without_value_is_dropped() -> None:
    env = {"DD_EXTRA_HEADER_1": "X-Orphan"}  # no _VALUE
    assert legacy_extra_headers(env) == {}


def test_extra_header_two_slots() -> None:
    env = {
        "DD_EXTRA_HEADER_1": "X-A",
        "DD_EXTRA_HEADER_1_VALUE": "1",
        "DD_EXTRA_HEADER_2": "X-B",
        "DD_EXTRA_HEADER_2_VALUE": "2",
    }
    assert legacy_extra_headers(env) == {"X-A": "1", "X-B": "2"}


def test_legacy_extra_headers_falls_back_to_os_environ(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("DD_EXTRA_HEADER_1", "X-Real")
    monkeypatch.setenv("DD_EXTRA_HEADER_1_VALUE", "real-value")
    assert legacy_extra_headers() == {"X-Real": "real-value"}


def test_load_profile_merges_legacy_extra_headers(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("DD_EXTRA_HEADER_1", "X-WAF")
    monkeypatch.setenv("DD_EXTRA_HEADER_1_VALUE", "from-env")

    profile = load_profile(config_path=tmp_path / "absent.toml")
    assert profile.extra_headers == {"X-WAF": "from-env"}


def test_load_profile_merges_legacy_extra_headers_with_toml(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from dd_cli.config import Config, Profile, save_config

    save_config(
        Config(
            profiles={
                "default": Profile(extra_headers={"X-Tenant": "main", "X-WAF": "toml-fallback"}),
            },
        ),
        tmp_path / "config.toml",
    )

    monkeypatch.setenv("DD_EXTRA_HEADER_1", "X-WAF")
    monkeypatch.setenv("DD_EXTRA_HEADER_1_VALUE", "env-wins")

    profile = load_profile(config_path=tmp_path / "config.toml")
    # TOML's X-Tenant survives, env overrides X-WAF
    assert profile.extra_headers == {"X-Tenant": "main", "X-WAF": "env-wins"}
