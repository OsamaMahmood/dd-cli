from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types

T = TypeVar("T", bound="ProductTypeGroupRequest")


@_attrs_define
class ProductTypeGroupRequest:
    """
    Attributes:
        product_type (int):
        group (int):
        role (int):
    """

    product_type: int
    group: int
    role: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_type = self.product_type

        group = self.group

        role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_type": product_type,
                "group": group,
                "role": role,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("product_type", (None, str(self.product_type).encode(), "text/plain")))

        files.append(("group", (None, str(self.group).encode(), "text/plain")))

        files.append(("role", (None, str(self.role).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_type = d.pop("product_type")

        group = d.pop("group")

        role = d.pop("role")

        product_type_group_request = cls(
            product_type=product_type,
            group=group,
            role=role,
        )

        product_type_group_request.additional_properties = d
        return product_type_group_request

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
