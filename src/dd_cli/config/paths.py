"""XDG-compliant config path resolution."""

from __future__ import annotations

import os
import sys
from pathlib import Path

CONFIG_FILENAME = "config.toml"


def default_config_dir() -> Path:
    """Return the default config directory for dd-cli.

    Honours `DD_CLI_CONFIG_DIR` if set, otherwise follows the XDG Base
    Directory spec on Unix and uses `%APPDATA%` on Windows.
    """
    if override := os.environ.get("DD_CLI_CONFIG_DIR"):
        return Path(override).expanduser()

    if sys.platform == "win32":
        appdata = os.environ.get("APPDATA")
        base = Path(appdata) if appdata else Path.home() / "AppData" / "Roaming"
        return base / "dd-cli"

    xdg = os.environ.get("XDG_CONFIG_HOME")
    base = Path(xdg) if xdg else Path.home() / ".config"
    return base / "dd-cli"


def default_config_path() -> Path:
    """Path to the dd-cli config TOML."""
    return default_config_dir() / CONFIG_FILENAME
