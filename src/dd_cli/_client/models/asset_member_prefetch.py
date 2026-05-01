from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_member_prefetch_product import AssetMemberPrefetchProduct
    from ..models.asset_member_prefetch_role import AssetMemberPrefetchRole
    from ..models.asset_member_prefetch_user import AssetMemberPrefetchUser


T = TypeVar("T", bound="AssetMemberPrefetch")


@_attrs_define
class AssetMemberPrefetch:
    """
    Attributes:
        product (AssetMemberPrefetchProduct | Unset):
        role (AssetMemberPrefetchRole | Unset):
        user (AssetMemberPrefetchUser | Unset):
    """

    product: AssetMemberPrefetchProduct | Unset = UNSET
    role: AssetMemberPrefetchRole | Unset = UNSET
    user: AssetMemberPrefetchUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product is not UNSET:
            field_dict["product"] = product
        if role is not UNSET:
            field_dict["role"] = role
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_member_prefetch_product import AssetMemberPrefetchProduct
        from ..models.asset_member_prefetch_role import AssetMemberPrefetchRole
        from ..models.asset_member_prefetch_user import AssetMemberPrefetchUser

        d = dict(src_dict)
        _product = d.pop("product", UNSET)
        product: AssetMemberPrefetchProduct | Unset
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = AssetMemberPrefetchProduct.from_dict(_product)

        _role = d.pop("role", UNSET)
        role: AssetMemberPrefetchRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = AssetMemberPrefetchRole.from_dict(_role)

        _user = d.pop("user", UNSET)
        user: AssetMemberPrefetchUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = AssetMemberPrefetchUser.from_dict(_user)

        asset_member_prefetch = cls(
            product=product,
            role=role,
            user=user,
        )

        asset_member_prefetch.additional_properties = d
        return asset_member_prefetch

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
