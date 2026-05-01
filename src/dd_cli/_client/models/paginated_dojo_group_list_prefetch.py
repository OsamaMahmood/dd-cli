from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_dojo_group_list_prefetch_product_groups import (
        PaginatedDojoGroupListPrefetchProductGroups,
    )
    from ..models.paginated_dojo_group_list_prefetch_product_type_groups import (
        PaginatedDojoGroupListPrefetchProductTypeGroups,
    )
    from ..models.paginated_dojo_group_list_prefetch_users import (
        PaginatedDojoGroupListPrefetchUsers,
    )


T = TypeVar("T", bound="PaginatedDojoGroupListPrefetch")


@_attrs_define
class PaginatedDojoGroupListPrefetch:
    """
    Attributes:
        product_groups (PaginatedDojoGroupListPrefetchProductGroups | Unset):
        product_type_groups (PaginatedDojoGroupListPrefetchProductTypeGroups | Unset):
        users (PaginatedDojoGroupListPrefetchUsers | Unset):
    """

    product_groups: PaginatedDojoGroupListPrefetchProductGroups | Unset = UNSET
    product_type_groups: PaginatedDojoGroupListPrefetchProductTypeGroups | Unset = UNSET
    users: PaginatedDojoGroupListPrefetchUsers | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_groups, Unset):
            product_groups = self.product_groups.to_dict()

        product_type_groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_type_groups, Unset):
            product_type_groups = self.product_type_groups.to_dict()

        users: dict[str, Any] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = self.users.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_groups is not UNSET:
            field_dict["product_groups"] = product_groups
        if product_type_groups is not UNSET:
            field_dict["product_type_groups"] = product_type_groups
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_dojo_group_list_prefetch_product_groups import (
            PaginatedDojoGroupListPrefetchProductGroups,
        )
        from ..models.paginated_dojo_group_list_prefetch_product_type_groups import (
            PaginatedDojoGroupListPrefetchProductTypeGroups,
        )
        from ..models.paginated_dojo_group_list_prefetch_users import (
            PaginatedDojoGroupListPrefetchUsers,
        )

        d = dict(src_dict)
        _product_groups = d.pop("product_groups", UNSET)
        product_groups: PaginatedDojoGroupListPrefetchProductGroups | Unset
        if isinstance(_product_groups, Unset):
            product_groups = UNSET
        else:
            product_groups = PaginatedDojoGroupListPrefetchProductGroups.from_dict(_product_groups)

        _product_type_groups = d.pop("product_type_groups", UNSET)
        product_type_groups: PaginatedDojoGroupListPrefetchProductTypeGroups | Unset
        if isinstance(_product_type_groups, Unset):
            product_type_groups = UNSET
        else:
            product_type_groups = PaginatedDojoGroupListPrefetchProductTypeGroups.from_dict(
                _product_type_groups
            )

        _users = d.pop("users", UNSET)
        users: PaginatedDojoGroupListPrefetchUsers | Unset
        if isinstance(_users, Unset):
            users = UNSET
        else:
            users = PaginatedDojoGroupListPrefetchUsers.from_dict(_users)

        paginated_dojo_group_list_prefetch = cls(
            product_groups=product_groups,
            product_type_groups=product_type_groups,
            users=users,
        )

        paginated_dojo_group_list_prefetch.additional_properties = d
        return paginated_dojo_group_list_prefetch

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
