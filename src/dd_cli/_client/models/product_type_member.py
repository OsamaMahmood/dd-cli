from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_type_member_prefetch import ProductTypeMemberPrefetch


T = TypeVar("T", bound="ProductTypeMember")


@_attrs_define
class ProductTypeMember:
    """
    Attributes:
        id (int):
        product_type (int):
        user (int):
        role (int):
        prefetch (ProductTypeMemberPrefetch | Unset):
    """

    id: int
    product_type: int
    user: int
    role: int
    prefetch: ProductTypeMemberPrefetch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        product_type = self.product_type

        user = self.user

        role = self.role

        prefetch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prefetch, Unset):
            prefetch = self.prefetch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "product_type": product_type,
                "user": user,
                "role": role,
            }
        )
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_type_member_prefetch import ProductTypeMemberPrefetch

        d = dict(src_dict)
        id = d.pop("id")

        product_type = d.pop("product_type")

        user = d.pop("user")

        role = d.pop("role")

        _prefetch = d.pop("prefetch", UNSET)
        prefetch: ProductTypeMemberPrefetch | Unset
        if isinstance(_prefetch, Unset):
            prefetch = UNSET
        else:
            prefetch = ProductTypeMemberPrefetch.from_dict(_prefetch)

        product_type_member = cls(
            id=id,
            product_type=product_type,
            user=user,
            role=role,
            prefetch=prefetch,
        )

        product_type_member.additional_properties = d
        return product_type_member

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
