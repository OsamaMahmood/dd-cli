"""Output renderer dispatch.

Renderers accept either a single mapping (rendered as a two-column
key/value table) or a sequence of mappings (rendered as a multi-row
table). JSON and YAML pass the data through untouched.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from enum import StrEnum
from typing import Any, Protocol


class OutputFormat(StrEnum):
    table = "table"
    json = "json"
    yaml = "yaml"


class Renderer(Protocol):
    def render(
        self,
        data: Any,
        *,
        columns: Sequence[str] | None = None,
    ) -> str: ...


def render(
    data: Any,
    fmt: OutputFormat = OutputFormat.table,
    *,
    columns: Sequence[str] | None = None,
) -> str:
    """Render `data` as a string in the requested format.

    `columns` is a hint for table rendering; ignored by JSON/YAML which
    preserve the input structure verbatim.
    """
    from dd_cli.output.json_out import JsonRenderer
    from dd_cli.output.table import TableRenderer
    from dd_cli.output.yaml_out import YamlRenderer

    renderers: dict[OutputFormat, Renderer] = {
        OutputFormat.table: TableRenderer(),
        OutputFormat.json: JsonRenderer(),
        OutputFormat.yaml: YamlRenderer(),
    }
    return renderers[fmt].render(data, columns=columns)


def _is_record_list(data: Any) -> bool:
    """True if `data` is a non-empty sequence of mappings."""
    return (
        isinstance(data, Sequence)
        and not isinstance(data, (str, bytes))
        and len(data) > 0
        and all(isinstance(row, Mapping) for row in data)
    )
