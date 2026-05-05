"""Rich-based table renderer."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from io import StringIO
from typing import Any

from rich.console import Console
from rich.table import Table

from dd_cli.output.base import _is_record_list


class TableRenderer:
    def render(
        self,
        data: Any,
        *,
        columns: Sequence[str] | None = None,
    ) -> str:
        if data is None:
            return ""
        if isinstance(data, Mapping):
            table = self._render_mapping(data)
        elif _is_record_list(data):
            table = self._render_records(list(data), columns)
        elif isinstance(data, Sequence) and not isinstance(data, (str, bytes)):
            table = self._render_scalars(list(data))
        else:
            return str(data)

        buf = StringIO()
        console = Console(file=buf, force_terminal=False, width=120)
        console.print(table)
        return buf.getvalue()

    @staticmethod
    def _render_mapping(data: Mapping[str, Any]) -> Table:
        table = Table(show_header=True, header_style="bold")
        table.add_column("Key", overflow="fold")
        table.add_column("Value", overflow="fold")
        for key, value in data.items():
            table.add_row(str(key), _stringify(value))
        return table

    @staticmethod
    def _render_records(rows: list[Mapping[str, Any]], columns: Sequence[str] | None) -> Table:
        cols = list(columns) if columns else list(rows[0].keys())
        table = Table(show_header=True, header_style="bold")
        for col in cols:
            table.add_column(col, overflow="fold")
        for row in rows:
            table.add_row(*(_stringify(row.get(col)) for col in cols))
        return table

    @staticmethod
    def _render_scalars(items: list[Any]) -> Table:
        table = Table(show_header=False)
        table.add_column("Value", overflow="fold")
        for item in items:
            table.add_row(_stringify(item))
        return table


def _stringify(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)
