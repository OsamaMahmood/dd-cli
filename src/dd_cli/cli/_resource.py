"""Shared list / get / create / update / delete logic for resource subcommands.

Each `dd <resource>` module declares a `ResourceSpec` describing the API path,
default table columns, and identifying field. The `list_resource`, `get_by_id`,
`get_by_name`, `create_resource`, `update_resource`, and `delete_resource`
helpers in this module do the actual work, so each command file is little more
than wiring per-resource flags.

Write-side commands share a uniform safety surface:
- `--from-file PAYLOAD.{json,yaml}` to load a base payload
- `--field key=value` (repeatable) to overlay individual fields
- `--dry-run` to preview the request without sending HTTP
- `--yes` / `-y` to skip the confirmation prompt on destructive ops

`register_crud(sub_app, spec)` hangs `create` / `update` / `delete` commands
on a sub-app in one call — used by every resource module so we don't
repeat 36 boilerplate command bodies.
"""

from __future__ import annotations

import json
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Annotated, Any

import typer
import yaml

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
#  Write helpers                                                          #
# ----------------------------------------------------------------------- #


def create_resource(
    ctx: typer.Context,
    spec: ResourceSpec,
    *,
    from_file: Path | None,
    fields: Sequence[str],
    dry_run: bool,
    output: OutputFormat | None,
) -> None:
    """POST a new resource. Payload is the merge of `--from-file` then `--field`s."""
    payload = build_payload(from_file=from_file, fields=fields)
    if not payload:
        raise ValidationError(
            f"No payload provided for `{spec.name}`. "
            "Pass --from-file PATH and/or --field key=value.",
        )

    if dry_run:
        _print_dry_run("POST", spec.path, payload, ctx, output)
        return

    profile_name = _resolved_profile_name(ctx, None)
    fmt = _output_format(ctx, output)
    profile = load_profile(name=profile_name)
    _require_complete(profile_name or profile.name, profile)

    with DefectDojoClient(profile) as client:
        body = client.post(spec.path, json=payload)

    typer.echo(render(body, fmt), nl=False)


def update_resource(
    ctx: typer.Context,
    spec: ResourceSpec,
    resource_id: int,
    *,
    from_file: Path | None,
    fields: Sequence[str],
    dry_run: bool,
    output: OutputFormat | None,
) -> None:
    """PATCH an existing resource. Payload built from --from-file + --field overrides."""
    payload = build_payload(from_file=from_file, fields=fields)
    if not payload:
        raise ValidationError(
            f"Nothing to update on {spec.name} {resource_id}. "
            "Pass --from-file PATH and/or --field key=value.",
        )

    target = f"{spec.path}{resource_id}/"
    if dry_run:
        _print_dry_run("PATCH", target, payload, ctx, output)
        return

    profile_name = _resolved_profile_name(ctx, None)
    fmt = _output_format(ctx, output)
    profile = load_profile(name=profile_name)
    _require_complete(profile_name or profile.name, profile)

    with DefectDojoClient(profile) as client:
        body = client.patch(target, json=payload)

    typer.echo(render(body, fmt), nl=False)


def delete_resource(
    ctx: typer.Context,
    spec: ResourceSpec,
    resource_id: int,
    *,
    yes: bool,
    dry_run: bool,
) -> None:
    """DELETE a resource. Confirms unless `--yes` or `--dry-run`."""
    target = f"{spec.path}{resource_id}/"
    if dry_run:
        typer.echo(f"DRY RUN: would DELETE {target}")
        return

    if not yes and not typer.confirm(f"Delete {spec.name} with id {resource_id}?"):
        typer.echo("Aborted.")
        raise typer.Exit(code=0)

    profile_name = _resolved_profile_name(ctx, None)
    profile = load_profile(name=profile_name)
    _require_complete(profile_name or profile.name, profile)

    with DefectDojoClient(profile) as client:
        client.delete(target)

    typer.echo(f"Deleted {spec.name} {resource_id}.")


def edit_resource(
    ctx: typer.Context,
    spec: ResourceSpec,
    resource_id: int,
    *,
    dry_run: bool,
    output: OutputFormat | None,
) -> None:
    """Fetch resource, open as YAML in $EDITOR, PATCH the diff on save.

    Sends only fields the user actually changed; aborts cleanly if no
    edits were made or the user saved an empty file.
    """
    profile_name = _resolved_profile_name(ctx, None)
    fmt = _output_format(ctx, output)
    profile = load_profile(name=profile_name)
    _require_complete(profile_name or profile.name, profile)

    target = f"{spec.path}{resource_id}/"

    with DefectDojoClient(profile) as client:
        current = client.get(target)

        original_yaml = yaml.safe_dump(current, sort_keys=False, default_flow_style=False)
        edited_text = typer.edit(
            text=original_yaml,
            extension=".yaml",
            require_save=True,
        )
        if edited_text is None:
            typer.echo("No changes (file not saved).")
            return

        try:
            edited = yaml.safe_load(edited_text)
        except yaml.YAMLError as exc:
            raise ValidationError(f"Edited file is not valid YAML: {exc}") from exc
        if not isinstance(edited, dict):
            raise ValidationError(
                f"Edited file must be a YAML mapping, got {type(edited).__name__}",
            )

        patch = _diff_payload(current, edited)
        if not patch:
            typer.echo("No changes.")
            return

        if dry_run:
            _print_dry_run("PATCH", target, patch, ctx, output)
            return

        body = client.patch(target, json=patch)

    typer.echo(render(body, fmt), nl=False)


def _diff_payload(current: Mapping[str, Any], edited: Mapping[str, Any]) -> dict[str, Any]:
    """Return the subset of `edited` that differs from `current` (added or changed)."""
    return {key: value for key, value in edited.items() if current.get(key) != value}


# ----------------------------------------------------------------------- #
#  Payload construction                                                   #
# ----------------------------------------------------------------------- #


def build_payload(
    *,
    from_file: Path | None,
    fields: Sequence[str],
    extra: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a JSON-ready payload from a base file, --field flags, and extra defaults.

    Resolution order (later wins): defaults from `extra` < file contents <
    explicit --field overrides. --field values are coerced from strings via
    JSON parsing when possible, falling back to plain strings.
    """
    payload: dict[str, Any] = dict(extra or {})

    if from_file is not None:
        payload.update(_load_payload_file(from_file))

    for raw in fields:
        key, value = _parse_field(raw)
        payload[key] = value

    return payload


def _load_payload_file(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ValidationError(f"Payload file not found: {path}")
    text = path.read_text()
    suffix = path.suffix.lower()
    try:
        data = yaml.safe_load(text) if suffix in {".yaml", ".yml"} else json.loads(text)
    except (json.JSONDecodeError, yaml.YAMLError) as exc:
        raise ValidationError(f"Failed to parse {path}: {exc}") from exc

    if not isinstance(data, dict):
        raise ValidationError(
            f"{path} must contain a JSON/YAML object, got {type(data).__name__}",
        )
    return dict(data)


def _parse_field(raw: str) -> tuple[str, Any]:
    if "=" not in raw:
        raise ValidationError(
            f"--field expects key=value, got {raw!r}",
        )
    key, _, value = raw.partition("=")
    if not key:
        raise ValidationError(f"--field has empty key: {raw!r}")
    # Try JSON first (handles ints, floats, bools, null, arrays, objects).
    try:
        return key, json.loads(value)
    except json.JSONDecodeError:
        return key, value


def _print_dry_run(
    method: str,
    path: str,
    payload: Mapping[str, Any],
    ctx: typer.Context,
    output: OutputFormat | None,
) -> None:
    fmt = _output_format(ctx, output)
    rendered = render(dict(payload), fmt)
    typer.echo(f"DRY RUN: would {method} {path} with payload:")
    typer.echo(rendered, nl=False)


# ----------------------------------------------------------------------- #
#  Public helpers reused by action-verb commands                          #
# ----------------------------------------------------------------------- #


def get_active_profile(ctx: typer.Context) -> Any:
    """Resolve the active profile from CLI context + config + env."""
    profile_name = _resolved_profile_name(ctx, None)
    profile = load_profile(name=profile_name)
    _require_complete(profile_name or profile.name, profile)
    return profile


def get_output_format(
    ctx: typer.Context,
    override: OutputFormat | None = None,
) -> OutputFormat:
    """Resolve the output format from CLI context + override."""
    return _output_format(ctx, override)


def confirm_or_abort(message: str, *, yes: bool) -> None:
    """Prompt for confirmation; exit cleanly with code 0 if user declines.

    No-op when `yes=True` (the standard `--yes`/`-y` skip).
    """
    if not yes and not typer.confirm(message):
        typer.echo("Aborted.")
        raise typer.Exit(code=0)


def print_dry_run(
    method: str,
    path: str,
    payload: Mapping[str, Any],
    ctx: typer.Context,
    output: OutputFormat | None = None,
) -> None:
    """Public alias of `_print_dry_run` for action-verb commands."""
    _print_dry_run(method, path, payload, ctx, output)


def render_response(
    body: Any,
    ctx: typer.Context,
    output: OutputFormat | None = None,
) -> None:
    """Echo `body` rendered in the active output format. Skips empty bodies."""
    if body is None or body == {}:
        return
    fmt = _output_format(ctx, output)
    typer.echo(render(body, fmt), nl=False)


# ----------------------------------------------------------------------- #
#  CRUD command registration                                              #
# ----------------------------------------------------------------------- #


def register_crud(sub_app: typer.Typer, spec: ResourceSpec) -> None:
    """Hang `create`, `update`, and `delete` commands on `sub_app` for `spec`.

    Each command gets the standard write-side flags (`--from-file`,
    `--field`, `--dry-run`, plus `--yes` for delete). Per-resource modules
    can still register additional, more ergonomic commands alongside these
    generic ones.
    """

    @sub_app.command("create", help=f"Create a new {spec.name}.")
    def _create(
        ctx: typer.Context,
        from_file: Annotated[
            Path | None,
            typer.Option(
                "--from-file",
                "-f",
                help="Path to a JSON or YAML file containing the payload.",
                exists=False,
                dir_okay=False,
                resolve_path=True,
            ),
        ] = None,
        field: Annotated[
            list[str] | None,
            typer.Option(
                "--field",
                help="key=value to set on the payload (repeatable). Overrides --from-file.",
            ),
        ] = None,
        dry_run: Annotated[
            bool,
            typer.Option(
                "--dry-run",
                help="Print the request that would be sent without contacting DefectDojo.",
            ),
        ] = False,
        output: Annotated[
            OutputFormat | None,
            typer.Option("--output", "-o", help="Output format."),
        ] = None,
    ) -> None:
        create_resource(
            ctx,
            spec,
            from_file=from_file,
            fields=field or [],
            dry_run=dry_run,
            output=output,
        )

    @sub_app.command("update", help=f"Update an existing {spec.name} by ID.")
    def _update(
        ctx: typer.Context,
        resource_id: Annotated[int, typer.Argument(help="Resource ID.")],
        from_file: Annotated[
            Path | None,
            typer.Option(
                "--from-file",
                "-f",
                help="Path to a JSON or YAML file containing the patch payload.",
                exists=False,
                dir_okay=False,
                resolve_path=True,
            ),
        ] = None,
        field: Annotated[
            list[str] | None,
            typer.Option(
                "--field",
                help="key=value to patch (repeatable). Overrides --from-file.",
            ),
        ] = None,
        dry_run: Annotated[
            bool,
            typer.Option("--dry-run", help="Print the request that would be sent."),
        ] = False,
        output: Annotated[
            OutputFormat | None,
            typer.Option("--output", "-o", help="Output format."),
        ] = None,
    ) -> None:
        update_resource(
            ctx,
            spec,
            resource_id,
            from_file=from_file,
            fields=field or [],
            dry_run=dry_run,
            output=output,
        )

    @sub_app.command("delete", help=f"Delete a {spec.name} by ID.")
    def _delete(
        ctx: typer.Context,
        resource_id: Annotated[int, typer.Argument(help="Resource ID.")],
        yes: Annotated[
            bool,
            typer.Option("--yes", "-y", help="Skip the confirmation prompt."),
        ] = False,
        dry_run: Annotated[
            bool,
            typer.Option(
                "--dry-run", help="Print what would happen without contacting DefectDojo."
            ),
        ] = False,
    ) -> None:
        delete_resource(ctx, spec, resource_id, yes=yes, dry_run=dry_run)

    @sub_app.command("edit", help=f"Open a {spec.name} as YAML in $EDITOR; PATCH the diff.")
    def _edit(
        ctx: typer.Context,
        resource_id: Annotated[int, typer.Argument(help="Resource ID.")],
        dry_run: Annotated[
            bool,
            typer.Option("--dry-run", help="Print the patch that would be sent."),
        ] = False,
        output: Annotated[
            OutputFormat | None,
            typer.Option("--output", "-o", help="Output format."),
        ] = None,
    ) -> None:
        edit_resource(ctx, spec, resource_id, dry_run=dry_run, output=output)


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
