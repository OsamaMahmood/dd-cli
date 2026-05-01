from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_request import MetadataRequest


T = TypeVar("T", bound="PatchedMetaMainRequest")


@_attrs_define
class PatchedMetaMainRequest:
    """
    Attributes:
        product (int | None | Unset):
        endpoint (int | None | Unset):
        finding (int | None | Unset):
        metadata (list[MetadataRequest] | Unset):
    """

    product: int | None | Unset = UNSET
    endpoint: int | None | Unset = UNSET
    finding: int | None | Unset = UNSET
    metadata: list[MetadataRequest] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product: int | None | Unset
        if isinstance(self.product, Unset):
            product = UNSET
        else:
            product = self.product

        endpoint: int | None | Unset
        if isinstance(self.endpoint, Unset):
            endpoint = UNSET
        else:
            endpoint = self.endpoint

        finding: int | None | Unset
        if isinstance(self.finding, Unset):
            finding = UNSET
        else:
            finding = self.finding

        metadata: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = []
            for metadata_item_data in self.metadata:
                metadata_item = metadata_item_data.to_dict()
                metadata.append(metadata_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product is not UNSET:
            field_dict["product"] = product
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if finding is not UNSET:
            field_dict["finding"] = finding
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.product, Unset):
            if isinstance(self.product, int):
                files.append(("product", (None, str(self.product).encode(), "text/plain")))
            else:
                files.append(("product", (None, str(self.product).encode(), "text/plain")))

        if not isinstance(self.endpoint, Unset):
            if isinstance(self.endpoint, int):
                files.append(("endpoint", (None, str(self.endpoint).encode(), "text/plain")))
            else:
                files.append(("endpoint", (None, str(self.endpoint).encode(), "text/plain")))

        if not isinstance(self.finding, Unset):
            if isinstance(self.finding, int):
                files.append(("finding", (None, str(self.finding).encode(), "text/plain")))
            else:
                files.append(("finding", (None, str(self.finding).encode(), "text/plain")))

        if not isinstance(self.metadata, Unset):
            for metadata_item_element in self.metadata:
                files.append(
                    (
                        "metadata",
                        (
                            None,
                            json.dumps(metadata_item_element.to_dict()).encode(),
                            "application/json",
                        ),
                    )
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_request import MetadataRequest

        d = dict(src_dict)

        def _parse_product(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        product = _parse_product(d.pop("product", UNSET))

        def _parse_endpoint(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        endpoint = _parse_endpoint(d.pop("endpoint", UNSET))

        def _parse_finding(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        finding = _parse_finding(d.pop("finding", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: list[MetadataRequest] | Unset = UNSET
        if _metadata is not UNSET:
            metadata = []
            for metadata_item_data in _metadata:
                metadata_item = MetadataRequest.from_dict(metadata_item_data)

                metadata.append(metadata_item)

        patched_meta_main_request = cls(
            product=product,
            endpoint=endpoint,
            finding=finding,
            metadata=metadata,
        )

        patched_meta_main_request.additional_properties = d
        return patched_meta_main_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
