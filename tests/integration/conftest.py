"""Integration-test fixtures.

These tests hit a real DefectDojo instance configured via env vars; they
are skipped automatically unless `DD_URL` and `DD_API_KEY` are set, and
are excluded from the default `pytest` run via the `integration` marker.

Run them explicitly with `make smoke` or `pytest -m integration`.
"""

from __future__ import annotations

import os
from collections.abc import Iterator
from pathlib import Path

import pytest
from typer.testing import CliRunner


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    """Skip every integration test if DD_URL or DD_API_KEY is missing."""
    if os.environ.get("DD_URL") and os.environ.get("DD_API_KEY"):
        return
    skip_marker = pytest.mark.skip(
        reason="Integration tests require DD_URL and DD_API_KEY env vars.",
    )
    for item in items:
        if "integration" in item.keywords:
            item.add_marker(skip_marker)


@pytest.fixture
def isolated_config(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Point dd-cli at a per-test config dir so the user's real config isn't touched."""
    monkeypatch.setenv("DD_CLI_CONFIG_DIR", str(tmp_path))


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


@pytest.fixture
def cleanup_stack() -> Iterator[list[tuple[str, int]]]:
    """Records `(resource, id)` pairs to delete via dd-cli at the end of the test.

    Tests should append `(resource, id)` to the returned list as they create
    things; the fixture's teardown deletes them in reverse order. Ensures
    the live DD instance ends each test in its starting state.
    """
    from typer.testing import CliRunner

    from dd_cli.cli.app import app

    stack: list[tuple[str, int]] = []
    yield stack
    teardown = CliRunner()
    for resource, resource_id in reversed(stack):
        teardown.invoke(app, [resource, "delete", str(resource_id), "--yes"])
