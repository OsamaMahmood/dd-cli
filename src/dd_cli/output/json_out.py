"""orjson-based JSON renderer."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import orjson


class JsonRenderer:
    def render(
        self,
        data: Any,
        *,
        columns: Sequence[str] | None = None,
    ) -> str:
        return orjson.dumps(data, option=orjson.OPT_INDENT_2 | orjson.OPT_SORT_KEYS).decode()
