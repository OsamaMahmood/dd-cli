"""Shared list/get logic for resource subcommands.

Each `dd <resource>` module declares a `ResourceSpec` describing the API path,
default table columns, and identifying field. The `list_resource`,
`get_by_id`, and `get_by_name` helpers in this module do the actual work, so
each command file is little more than wiring per-resource filters.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from itertools import islice
from typing import Any

import typer

from dd_cli.client import DefectDojoClient
from dd_cli.config import load_profile
from dd_cli.errors import APIError, ConfigError, NotFoundError, ValidationError
from dd_cli.output import OutputFormat, render

DEFAULT_LIMIT = 50


@dataclass(frozen=True)
class ResourceSpec:
    """Describes one DefectDojo resource type for the generic list/get helpers."""

    name: str
    """Singular name used in error/log messages, e.g. `product`."""

    plural: str
    """Plural name used in error/log messages, e.g. `products`."""

    path: str
    """REST collection path, e.g. `/api/v2/products/`. Must end with a slash."""

    columns: tuple[str, ...]
    """Default table columns when the user does not pass `--columns`."""

    name_field: str = "name"
    """Field used by `get_by_name` to resolve a name to an ID."""


def list_resource(
    ctx: typer.Context,
    spec: ResourceSpec,
    *,
    filters: Mapping[str, Any] | None = None,
    limit: int = DEFAULT_LIMIT,
    all_pages: bool = False,
    columns: Iterable[str] | None = None,
    output: OutputFormat | None = None,
) -> None:
    """Fetch + render a list of resources."""
    profile_name = _resolved_profile_name(ctx, None)
    fmt = _output_format(ctx, output)
    profile = load_profile(name=profile_name)
    _require_complete(profile_name or profile.name, profile)

    cols = list(columns) if columns is not None else list(spec.columns)
    request_params = _clean_filters(filters)

    with DefectDojoClient(profile) as client:
        iterator = client.paginate(spec.path, params=request_params)
        items = iterator if all_pages else islice(iterator, max(1, limit))
        records = [{col: item.get(col) for col in cols} for item in items]

    typer.echo(render(records, fmt, columns=cols), nl=False)


def get_by_id(
    ctx: typer.Context,
    spec: ResourceSpec,
    resource_id: int,
    *,
    output: OutputFormat | None = None,
) -> None:
    """Fetch + render a single resource by ID."""
    profile_name = _resolved_profile_name(ctx, None)
    fmt = _output_format(ctx, output)
    profile = load_profile(name=profile_name)
    _require_complete(profile_name or profile.name, profile)

    with DefectDojoClient(profile) as client:
        try:
            body = client.get(f"{spec.path}{resource_id}/")
        except NotFoundError as exc:
            raise NotFoundError(f"{spec.name} with id {resource_id} not found") from exc

    typer.echo(render(body, fmt), nl=False)


def get_by_name(
    ctx: typer.Context,
    spec: ResourceSpec,
    name: str,
    *,
    output: OutputFormat | None = None,
) -> None:
    """Resolve `name` to an ID via the list endpoint, then GET the full resource."""
    profile_name = _resolved_profile_name(ctx, None)
    fmt = _output_format(ctx, output)
    profile = load_profile(name=profile_name)
    _require_complete(profile_name or profile.name, profile)

    with DefectDojoClient(profile) as client:
        items = list(
            islice(
                client.paginate(spec.path, params={spec.name_field: name}),
                100,  # cap pagination during name resolution
            )
        )
        matches = [item for item in items if item.get(spec.name_field) == name]
        if not matches:
            raise NotFoundError(f"{spec.name} `{name}` not found")
        if len(matches) > 1:
            raise APIError(
                f"Found {len(matches)} {spec.plural} matching `{name}`",
                hint="Use the numeric ID instead of --name to disambiguate.",
            )
        resource_id = matches[0].get("id")
        if not isinstance(resource_id, int):
            raise APIError(f"Resolved {spec.name} `{name}` has no integer `id` field")
        body = client.get(f"{spec.path}{resource_id}/")

    typer.echo(render(body, fmt), nl=False)


def get_dispatch(
    ctx: typer.Context,
    spec: ResourceSpec,
    *,
    resource_id: int | None,
    name: str | None,
    output: OutputFormat | None,
) -> None:
    """Generic `<resource> get [ID] [--name NAME]` dispatcher."""
    if resource_id is None and not name:
        raise ValidationError(
            f"Provide either an ID or --name to identify the {spec.name}.",
        )
    if resource_id is not None and name:
        raise ValidationError("Pass either an ID or --name, not both.")
    if resource_id is not None:
        get_by_id(ctx, spec, resource_id, output=output)
    else:
        assert name is not None  # narrowed by the branches above
        get_by_name(ctx, spec, name, output=output)


# ----------------------------------------------------------------------- #
#  Helpers                                                                #
# ----------------------------------------------------------------------- #


def _resolved_profile_name(ctx: typer.Context, override: str | None) -> str | None:
    if override:
        return override
    obj = ctx.obj or {}
    return obj.get("profile")


def _output_format(ctx: typer.Context, override: OutputFormat | None) -> OutputFormat:
    if override is not None:
        return override
    obj = ctx.obj or {}
    fmt = obj.get("output")
    return fmt if isinstance(fmt, OutputFormat) else OutputFormat.table


def _require_complete(profile_name: str, profile: Any) -> None:
    if not profile.is_complete():
        raise ConfigError(
            f"Profile `{profile_name}` is missing url and/or api_key.",
            hint="Run `dd configure` to set them.",
        )


def _clean_filters(filters: Mapping[str, Any] | None) -> dict[str, Any]:
    """Drop entries with None values; pass everything else through to httpx params."""
    if not filters:
        return {}
    return {k: _coerce_filter_value(v) for k, v in filters.items() if v is not None}


def _coerce_filter_value(value: Any) -> Any:
    if isinstance(value, bool):
        return "true" if value else "false"
    return value
