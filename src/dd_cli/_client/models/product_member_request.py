from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types

T = TypeVar("T", bound="ProductMemberRequest")


@_attrs_define
class ProductMemberRequest:
    """
    Attributes:
        product (int):
        user (int):
        role (int):
    """

    product: int
    user: int
    role: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product = self.product

        user = self.user

        role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product": product,
                "user": user,
                "role": role,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("product", (None, str(self.product).encode(), "text/plain")))

        files.append(("user", (None, str(self.user).encode(), "text/plain")))

        files.append(("role", (None, str(self.role).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product = d.pop("product")

        user = d.pop("user")

        role = d.pop("role")

        product_member_request = cls(
            product=product,
            user=user,
            role=role,
        )

        product_member_request.additional_properties = d
        return product_member_request

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
