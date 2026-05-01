from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EndpointMetaImporter")


@_attrs_define
class EndpointMetaImporter:
    """
    Attributes:
        file (str):
        product_id (int):
        create_endpoints (bool | Unset):  Default: True.
        create_tags (bool | Unset):  Default: True.
        create_dojo_meta (bool | Unset):  Default: False.
        product_name (str | Unset):
        product (int | Unset):
    """

    file: str
    product_id: int
    create_endpoints: bool | Unset = True
    create_tags: bool | Unset = True
    create_dojo_meta: bool | Unset = False
    product_name: str | Unset = UNSET
    product: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file

        product_id = self.product_id

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
                "product_id": product_id,
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

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = d.pop("file")

        product_id = d.pop("product_id")

        create_endpoints = d.pop("create_endpoints", UNSET)

        create_tags = d.pop("create_tags", UNSET)

        create_dojo_meta = d.pop("create_dojo_meta", UNSET)

        product_name = d.pop("product_name", UNSET)

        product = d.pop("product", UNSET)

        endpoint_meta_importer = cls(
            file=file,
            product_id=product_id,
            create_endpoints=create_endpoints,
            create_tags=create_tags,
            create_dojo_meta=create_dojo_meta,
            product_name=product_name,
            product=product,
        )

        endpoint_meta_importer.additional_properties = d
        return endpoint_meta_importer

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
