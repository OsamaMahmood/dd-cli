from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="EndpointMetaImporterRequest")


@_attrs_define
class EndpointMetaImporterRequest:
    """
    Attributes:
        file (File):
        create_endpoints (bool | Unset):  Default: True.
        create_tags (bool | Unset):  Default: True.
        create_dojo_meta (bool | Unset):  Default: False.
        product_name (str | Unset):
        product (int | Unset):
    """

    file: File
    create_endpoints: bool | Unset = True
    create_tags: bool | Unset = True
    create_dojo_meta: bool | Unset = False
    product_name: str | Unset = UNSET
    product: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        create_endpoints = self.create_endpoints

        create_tags = self.create_tags

        create_dojo_meta = self.create_dojo_meta

        product_name = self.product_name

        product = self.product

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if create_endpoints is not UNSET:
            field_dict["create_endpoints"] = create_endpoints
        if create_tags is not UNSET:
            field_dict["create_tags"] = create_tags
        if create_dojo_meta is not UNSET:
            field_dict["create_dojo_meta"] = create_dojo_meta
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if product is not UNSET:
            field_dict["product"] = product

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

        if not isinstance(self.create_endpoints, Unset):
            files.append(
                ("create_endpoints", (None, str(self.create_endpoints).encode(), "text/plain"))
            )

        if not isinstance(self.create_tags, Unset):
            files.append(("create_tags", (None, str(self.create_tags).encode(), "text/plain")))

        if not isinstance(self.create_dojo_meta, Unset):
            files.append(
                ("create_dojo_meta", (None, str(self.create_dojo_meta).encode(), "text/plain"))
            )

        if not isinstance(self.product_name, Unset):
            files.append(("product_name", (None, str(self.product_name).encode(), "text/plain")))

        if not isinstance(self.product, Unset):
            files.append(("product", (None, str(self.product).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        create_endpoints = d.pop("create_endpoints", UNSET)

        create_tags = d.pop("create_tags", UNSET)

        create_dojo_meta = d.pop("create_dojo_meta", UNSET)

        product_name = d.pop("product_name", UNSET)

        product = d.pop("product", UNSET)

        endpoint_meta_importer_request = cls(
            file=file,
            create_endpoints=create_endpoints,
            create_tags=create_tags,
            create_dojo_meta=create_dojo_meta,
            product_name=product_name,
            product=product,
        )

        endpoint_meta_importer_request.additional_properties = d
        return endpoint_meta_importer_request

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
