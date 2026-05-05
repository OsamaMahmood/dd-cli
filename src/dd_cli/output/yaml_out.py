"""PyYAML-based YAML renderer."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import yaml


class YamlRenderer:
    def render(
        self,
        data: Any,
        *,
        columns: Sequence[str] | None = None,
    ) -> str:
        return yaml.safe_dump(data, sort_keys=False, default_flow_style=False)
