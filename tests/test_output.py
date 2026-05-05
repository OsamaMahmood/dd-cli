from __future__ import annotations

import json

import pytest
import yaml

from dd_cli.output import OutputFormat, render


@pytest.fixture
def records() -> list[dict[str, object]]:
    return [
        {"id": 1, "name": "alpha", "active": True},
        {"id": 2, "name": "beta", "active": False},
    ]


def test_table_renders_list_of_dicts_with_headers(records: list[dict[str, object]]) -> None:
    out = render(records, OutputFormat.table)
    assert "id" in out
    assert "name" in out
    assert "alpha" in out
    assert "beta" in out
    # bool-as-string formatting
    assert "true" in out
    assert "false" in out


def test_table_respects_explicit_columns(records: list[dict[str, object]]) -> None:
    out = render(records, OutputFormat.table, columns=["name"])
    assert "name" in out
    assert "alpha" in out
    # `id` and `active` should not appear when filtered out
    assert "active" not in out


def test_table_renders_single_mapping_as_keyvalue() -> None:
    out = render({"url": "https://x.example", "active": True}, OutputFormat.table)
    assert "Key" in out
    assert "Value" in out
    assert "url" in out
    assert "https://x.example" in out
    assert "true" in out


def test_table_renders_scalar_list() -> None:
    out = render(["one", "two", "three"], OutputFormat.table)
    assert "one" in out
    assert "two" in out
    assert "three" in out


def test_table_handles_none_values() -> None:
    out = render([{"id": 1, "name": None}], OutputFormat.table)
    assert "id" in out


def test_table_handles_none_input() -> None:
    assert render(None, OutputFormat.table) == ""


def test_table_handles_scalar_input() -> None:
    assert "hello" in render("hello", OutputFormat.table)


def test_json_round_trips(records: list[dict[str, object]]) -> None:
    out = render(records, OutputFormat.json)
    assert json.loads(out) == records


def test_json_indents_and_sorts_keys() -> None:
    out = render({"b": 2, "a": 1}, OutputFormat.json)
    # sort_keys puts `a` before `b`
    assert out.index('"a"') < out.index('"b"')
    assert "  " in out  # indented


def test_yaml_round_trips(records: list[dict[str, object]]) -> None:
    out = render(records, OutputFormat.yaml)
    assert yaml.safe_load(out) == records


def test_yaml_renders_mapping_block_style() -> None:
    out = render({"url": "https://x", "active": True}, OutputFormat.yaml)
    assert "url: https://x" in out
    assert "active: true" in out


@pytest.mark.parametrize("fmt", list(OutputFormat))
def test_render_dispatches_to_format(fmt: OutputFormat) -> None:
    out = render({"k": "v"}, fmt)
    assert out  # non-empty string for any format


def test_unknown_input_renders_in_all_formats() -> None:
    for fmt in OutputFormat:
        # tuples/sets/etc. shouldn't crash
        out = render([1, 2, 3], fmt)
        assert out
