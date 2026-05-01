from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_type_group_prefetch_group import ProductTypeGroupPrefetchGroup
    from ..models.product_type_group_prefetch_product_type import (
        ProductTypeGroupPrefetchProductType,
    )
    from ..models.product_type_group_prefetch_role import ProductTypeGroupPrefetchRole


T = TypeVar("T", bound="ProductTypeGroupPrefetch")


@_attrs_define
class ProductTypeGroupPrefetch:
    """
    Attributes:
        group (ProductTypeGroupPrefetchGroup | Unset):
        product_type (ProductTypeGroupPrefetchProductType | Unset):
        role (ProductTypeGroupPrefetchRole | Unset):
    """

    group: ProductTypeGroupPrefetchGroup | Unset = UNSET
    product_type: ProductTypeGroupPrefetchProductType | Unset = UNSET
    role: ProductTypeGroupPrefetchRole | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        product_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_type, Unset):
            product_type = self.product_type.to_dict()

        role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group is not UNSET:
            field_dict["group"] = group
        if product_type is not UNSET:
            field_dict["product_type"] = product_type
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_type_group_prefetch_group import ProductTypeGroupPrefetchGroup
        from ..models.product_type_group_prefetch_product_type import (
            ProductTypeGroupPrefetchProductType,
        )
        from ..models.product_type_group_prefetch_role import ProductTypeGroupPrefetchRole

        d = dict(src_dict)
        _group = d.pop("group", UNSET)
        group: ProductTypeGroupPrefetchGroup | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = ProductTypeGroupPrefetchGroup.from_dict(_group)

        _product_type = d.pop("product_type", UNSET)
        product_type: ProductTypeGroupPrefetchProductType | Unset
        if isinstance(_product_type, Unset):
            product_type = UNSET
        else:
            product_type = ProductTypeGroupPrefetchProductType.from_dict(_product_type)

        _role = d.pop("role", UNSET)
        role: ProductTypeGroupPrefetchRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = ProductTypeGroupPrefetchRole.from_dict(_role)

        product_type_group_prefetch = cls(
            group=group,
            product_type=product_type,
            role=role,
        )

        product_type_group_prefetch.additional_properties = d
        return product_type_group_prefetch

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
