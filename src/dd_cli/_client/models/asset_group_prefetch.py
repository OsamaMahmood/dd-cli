from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_group_prefetch_group import AssetGroupPrefetchGroup
    from ..models.asset_group_prefetch_product import AssetGroupPrefetchProduct
    from ..models.asset_group_prefetch_role import AssetGroupPrefetchRole


T = TypeVar("T", bound="AssetGroupPrefetch")


@_attrs_define
class AssetGroupPrefetch:
    """
    Attributes:
        group (AssetGroupPrefetchGroup | Unset):
        product (AssetGroupPrefetchProduct | Unset):
        role (AssetGroupPrefetchRole | Unset):
    """

    group: AssetGroupPrefetchGroup | Unset = UNSET
    product: AssetGroupPrefetchProduct | Unset = UNSET
    role: AssetGroupPrefetchRole | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        product: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group is not UNSET:
            field_dict["group"] = group
        if product is not UNSET:
            field_dict["product"] = product
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_group_prefetch_group import AssetGroupPrefetchGroup
        from ..models.asset_group_prefetch_product import AssetGroupPrefetchProduct
        from ..models.asset_group_prefetch_role import AssetGroupPrefetchRole

        d = dict(src_dict)
        _group = d.pop("group", UNSET)
        group: AssetGroupPrefetchGroup | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = AssetGroupPrefetchGroup.from_dict(_group)

        _product = d.pop("product", UNSET)
        product: AssetGroupPrefetchProduct | Unset
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = AssetGroupPrefetchProduct.from_dict(_product)

        _role = d.pop("role", UNSET)
        role: AssetGroupPrefetchRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = AssetGroupPrefetchRole.from_dict(_role)

        asset_group_prefetch = cls(
            group=group,
            product=product,
            role=role,
        )

        asset_group_prefetch.additional_properties = d
        return asset_group_prefetch

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
