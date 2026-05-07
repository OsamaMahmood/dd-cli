"""Upload `cloc` JSON output for a product to DefectDojo.

Mirrors the legacy `dd-import-languages` flow: find or create the product
type and product, then POST the cloc JSON to ``/api/v2/import-languages/``.
Honours the same `DD_*` env vars the original tool read so the legacy
console-script shim in M4b is a thin call into this workflow.
"""

from __future__ import annotations

from collections.abc import Mapping
from itertools import islice
from pathlib import Path
from typing import Any

from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from dd_cli.client import DefectDojoClient
from dd_cli.errors import APIError, ConfigError, ValidationError


class ImportLanguagesOptions(BaseSettings):
    """Knobs for `dd import languages`. Reads CLI flags + DD_* env vars."""

    model_config = SettingsConfigDict(
        case_sensitive=False,
        extra="ignore",
        populate_by_name=True,
    )

    file: Path | None = Field(
        default=None,
        validation_alias=AliasChoices("DD_CLI_FILE", "DD_FILE_NAME"),
    )
    product_type_name: str | None = Field(
        default=None,
        validation_alias=AliasChoices("DD_CLI_PRODUCT_TYPE", "DD_PRODUCT_TYPE_NAME"),
    )
    product_name: str | None = Field(
        default=None,
        validation_alias=AliasChoices("DD_CLI_PRODUCT", "DD_PRODUCT_NAME"),
    )

    # Reused product-creation knobs (matches the legacy traditional behavior)
    product_description: str | None = Field(
        default=None, validation_alias=AliasChoices("DD_PRODUCT_DESCRIPTION")
    )
    product_type_description: str | None = Field(
        default=None, validation_alias=AliasChoices("DD_PRODUCT_TYPE_DESCRIPTION")
    )


class ImportLanguagesWorkflow:
    """Upload cloc language data to DefectDojo."""

    def __init__(self, client: DefectDojoClient, opts: ImportLanguagesOptions) -> None:
        self._client = client
        self._opts = opts
        self._validate()

    def run(self) -> dict[str, Any]:
        product_type_id = self._find_or_create_product_type()
        product_id = self._find_or_create_product(product_type_id)
        return self._upload(product_id)

    # ------------------------------------------------------------------ #
    #  Validation                                                        #
    # ------------------------------------------------------------------ #

    def _validate(self) -> None:
        opts = self._opts
        missing: list[str] = []
        if not opts.product_type_name:
            missing.append("product_type")
        if not opts.product_name:
            missing.append("product")
        if not opts.file:
            missing.append("file")
        if missing:
            raise ConfigError(
                f"Missing required option(s) for language import: {', '.join(missing)}",
                hint=(
                    "Pass them as CLI flags (--product-type, --product, "
                    "--file) or set the matching DD_* env vars."
                ),
            )

    # ------------------------------------------------------------------ #
    #  Resource resolution (mirrors the import-findings traditional flow)
    # ------------------------------------------------------------------ #

    def _find_or_create_product_type(self) -> int:
        opts = self._opts
        for item in islice(
            self._client.paginate(
                "/api/v2/product_types/", params={"name": opts.product_type_name}
            ),
            100,
        ):
            if item.get("name") == opts.product_type_name:
                pt_id = item.get("id")
                if isinstance(pt_id, int):
                    return pt_id
        payload: dict[str, Any] = {"name": opts.product_type_name}
        if opts.product_type_description is not None:
            payload["description"] = opts.product_type_description
        body = self._client.post("/api/v2/product_types/", json=payload)
        new_id = body.get("id")
        if not isinstance(new_id, int):
            raise APIError("New product type missing integer id")
        return new_id

    def _find_or_create_product(self, product_type_id: int) -> int:
        opts = self._opts
        for item in islice(
            self._client.paginate(
                "/api/v2/products/",
                params={"name": opts.product_name, "prod_type": product_type_id},
            ),
            100,
        ):
            if item.get("name") == opts.product_name:
                pid = item.get("id")
                if isinstance(pid, int):
                    return pid
        payload: dict[str, Any] = {
            "name": opts.product_name,
            "description": opts.product_description or opts.product_name,
            "prod_type": product_type_id,
        }
        body = self._client.post("/api/v2/products/", json=payload)
        new_id = body.get("id")
        if not isinstance(new_id, int):
            raise APIError("New product missing integer id")
        return new_id

    # ------------------------------------------------------------------ #
    #  Upload                                                            #
    # ------------------------------------------------------------------ #

    def _upload(self, product_id: int) -> dict[str, Any]:
        opts = self._opts
        assert opts.file is not None  # guarded in _validate
        path = Path(opts.file)
        if not path.exists():
            raise ValidationError(f"Languages file not found: {path}")
        return self._client.upload(
            "/api/v2/import-languages/",
            data={"product": product_id},
            file=(path.name, path.read_bytes()),
        )


def make_options_from_kwargs(**overrides: Any) -> ImportLanguagesOptions:
    base: Mapping[str, Any] = ImportLanguagesOptions().model_dump(exclude_none=False)
    merged = {**base}
    for key, value in overrides.items():
        if value is not None:
            merged[key] = value
    return ImportLanguagesOptions.model_validate(merged)


__all__ = [
    "ImportLanguagesOptions",
    "ImportLanguagesWorkflow",
    "make_options_from_kwargs",
]
