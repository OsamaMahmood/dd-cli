"""Backward-compatibility layer for the original `dd-import` `DD_*` env vars.

The legacy tool uses paired env vars `DD_EXTRA_HEADER_<N>` (header *name*) and
`DD_EXTRA_HEADER_<N>_VALUE` (header *value*). pydantic-settings can't model
that pairing directly, so this module reads them and returns a clean
`{name: value}` dict to merge into `Profile.extra_headers`.

Other connection-level legacy vars (DD_URL, DD_API_KEY, DD_SSL_VERIFY) are
handled directly by `_EnvOverrides` in `settings.py` via `AliasChoices`.

Workflow-specific `DD_*` vars (DD_PRODUCT_NAME, DD_TEST_TYPE_NAME, etc.)
are NOT covered here — those belong to the import workflows and will be
wired in M4 alongside the legacy `dd-reimport-findings` shim.
"""

from __future__ import annotations

import os
from collections.abc import Mapping

LEGACY_HEADER_SLOTS = (1, 2)


def legacy_extra_headers(env: Mapping[str, str] | None = None) -> dict[str, str]:
    """Return `{header_name: header_value}` for any DD_EXTRA_HEADER_N pairs.

    Mirrors the behavior of `dd_import.dd_api.Api.__init__`: a slot
    contributes a header only when both name and value are set.
    """
    source: Mapping[str, str] = env if env is not None else os.environ
    result: dict[str, str] = {}
    for slot in LEGACY_HEADER_SLOTS:
        name = source.get(f"DD_EXTRA_HEADER_{slot}")
        value = source.get(f"DD_EXTRA_HEADER_{slot}_VALUE")
        if name and value is not None:
            result[name] = value
    return result
