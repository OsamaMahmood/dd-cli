"""Configuration management for dd-cli.

Layered precedence (highest wins):
1. Explicit CLI flags
2. Environment variables (DD_CLI_*, with DD_* legacy aliases)
3. Active profile in ~/.config/dd-cli/config.toml
4. Built-in defaults
"""

from dd_cli.config.paths import default_config_dir, default_config_path
from dd_cli.config.settings import (
    Config,
    Profile,
    load_config,
    load_profile,
    save_config,
)

__all__ = [
    "Config",
    "Profile",
    "default_config_dir",
    "default_config_path",
    "load_config",
    "load_profile",
    "save_config",
]
