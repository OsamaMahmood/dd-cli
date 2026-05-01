from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductTypeRequest")


@_attrs_define
class ProductTypeRequest:
    """
    Attributes:
        name (str):
        description (None | str | Unset):
        critical_product (bool | Unset):
        key_product (bool | Unset):
    """

    name: str
    description: None | str | Unset = UNSET
    critical_product: bool | Unset = UNSET
    key_product: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        critical_product = self.critical_product

        key_product = self.key_product

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if critical_product is not UNSET:
            field_dict["critical_product"] = critical_product
        if key_product is not UNSET:
            field_dict["key_product"] = key_product

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            if isinstance(self.description, str):
                files.append(("description", (None, str(self.description).encode(), "text/plain")))
            else:
                files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.critical_product, Unset):
            files.append(
                ("critical_product", (None, str(self.critical_product).encode(), "text/plain"))
            )

        if not isinstance(self.key_product, Unset):
            files.append(("key_product", (None, str(self.key_product).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        critical_product = d.pop("critical_product", UNSET)

        key_product = d.pop("key_product", UNSET)

        product_type_request = cls(
            name=name,
            description=description,
            critical_product=critical_product,
            key_product=key_product,
        )

        product_type_request.additional_properties = d
        return product_type_request

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
