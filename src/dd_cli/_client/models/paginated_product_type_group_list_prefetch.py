from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_product_type_group_list_prefetch_group import (
        PaginatedProductTypeGroupListPrefetchGroup,
    )
    from ..models.paginated_product_type_group_list_prefetch_product_type import (
        PaginatedProductTypeGroupListPrefetchProductType,
    )
    from ..models.paginated_product_type_group_list_prefetch_role import (
        PaginatedProductTypeGroupListPrefetchRole,
    )


T = TypeVar("T", bound="PaginatedProductTypeGroupListPrefetch")


@_attrs_define
class PaginatedProductTypeGroupListPrefetch:
    """
    Attributes:
        group (PaginatedProductTypeGroupListPrefetchGroup | Unset):
        product_type (PaginatedProductTypeGroupListPrefetchProductType | Unset):
        role (PaginatedProductTypeGroupListPrefetchRole | Unset):
    """

    group: PaginatedProductTypeGroupListPrefetchGroup | Unset = UNSET
    product_type: PaginatedProductTypeGroupListPrefetchProductType | Unset = UNSET
    role: PaginatedProductTypeGroupListPrefetchRole | Unset = UNSET
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
        from ..models.paginated_product_type_group_list_prefetch_group import (
            PaginatedProductTypeGroupListPrefetchGroup,
        )
        from ..models.paginated_product_type_group_list_prefetch_product_type import (
            PaginatedProductTypeGroupListPrefetchProductType,
        )
        from ..models.paginated_product_type_group_list_prefetch_role import (
            PaginatedProductTypeGroupListPrefetchRole,
        )

        d = dict(src_dict)
        _group = d.pop("group", UNSET)
        group: PaginatedProductTypeGroupListPrefetchGroup | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = PaginatedProductTypeGroupListPrefetchGroup.from_dict(_group)

        _product_type = d.pop("product_type", UNSET)
        product_type: PaginatedProductTypeGroupListPrefetchProductType | Unset
        if isinstance(_product_type, Unset):
            product_type = UNSET
        else:
            product_type = PaginatedProductTypeGroupListPrefetchProductType.from_dict(_product_type)

        _role = d.pop("role", UNSET)
        role: PaginatedProductTypeGroupListPrefetchRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = PaginatedProductTypeGroupListPrefetchRole.from_dict(_role)

        paginated_product_type_group_list_prefetch = cls(
            group=group,
            product_type=product_type,
            role=role,
        )

        paginated_product_type_group_list_prefetch.additional_properties = d
        return paginated_product_type_group_list_prefetch

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
