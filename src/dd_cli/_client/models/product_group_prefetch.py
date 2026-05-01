from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_group_prefetch_group import ProductGroupPrefetchGroup
    from ..models.product_group_prefetch_product import ProductGroupPrefetchProduct
    from ..models.product_group_prefetch_role import ProductGroupPrefetchRole


T = TypeVar("T", bound="ProductGroupPrefetch")


@_attrs_define
class ProductGroupPrefetch:
    """
    Attributes:
        group (ProductGroupPrefetchGroup | Unset):
        product (ProductGroupPrefetchProduct | Unset):
        role (ProductGroupPrefetchRole | Unset):
    """

    group: ProductGroupPrefetchGroup | Unset = UNSET
    product: ProductGroupPrefetchProduct | Unset = UNSET
    role: ProductGroupPrefetchRole | Unset = UNSET
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
        from ..models.product_group_prefetch_group import ProductGroupPrefetchGroup
        from ..models.product_group_prefetch_product import ProductGroupPrefetchProduct
        from ..models.product_group_prefetch_role import ProductGroupPrefetchRole

        d = dict(src_dict)
        _group = d.pop("group", UNSET)
        group: ProductGroupPrefetchGroup | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = ProductGroupPrefetchGroup.from_dict(_group)

        _product = d.pop("product", UNSET)
        product: ProductGroupPrefetchProduct | Unset
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = ProductGroupPrefetchProduct.from_dict(_product)

        _role = d.pop("role", UNSET)
        role: ProductGroupPrefetchRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = ProductGroupPrefetchRole.from_dict(_role)

        product_group_prefetch = cls(
            group=group,
            product=product,
            role=role,
        )

        product_group_prefetch.additional_properties = d
        return product_group_prefetch

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
