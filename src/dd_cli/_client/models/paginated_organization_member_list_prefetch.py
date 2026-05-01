from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_organization_member_list_prefetch_product_type import (
        PaginatedOrganizationMemberListPrefetchProductType,
    )
    from ..models.paginated_organization_member_list_prefetch_role import (
        PaginatedOrganizationMemberListPrefetchRole,
    )
    from ..models.paginated_organization_member_list_prefetch_user import (
        PaginatedOrganizationMemberListPrefetchUser,
    )


T = TypeVar("T", bound="PaginatedOrganizationMemberListPrefetch")


@_attrs_define
class PaginatedOrganizationMemberListPrefetch:
    """
    Attributes:
        product_type (PaginatedOrganizationMemberListPrefetchProductType | Unset):
        role (PaginatedOrganizationMemberListPrefetchRole | Unset):
        user (PaginatedOrganizationMemberListPrefetchUser | Unset):
    """

    product_type: PaginatedOrganizationMemberListPrefetchProductType | Unset = UNSET
    role: PaginatedOrganizationMemberListPrefetchRole | Unset = UNSET
    user: PaginatedOrganizationMemberListPrefetchUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_type, Unset):
            product_type = self.product_type.to_dict()

        role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_type is not UNSET:
            field_dict["product_type"] = product_type
        if role is not UNSET:
            field_dict["role"] = role
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_organization_member_list_prefetch_product_type import (
            PaginatedOrganizationMemberListPrefetchProductType,
        )
        from ..models.paginated_organization_member_list_prefetch_role import (
            PaginatedOrganizationMemberListPrefetchRole,
        )
        from ..models.paginated_organization_member_list_prefetch_user import (
            PaginatedOrganizationMemberListPrefetchUser,
        )

        d = dict(src_dict)
        _product_type = d.pop("product_type", UNSET)
        product_type: PaginatedOrganizationMemberListPrefetchProductType | Unset
        if isinstance(_product_type, Unset):
            product_type = UNSET
        else:
            product_type = PaginatedOrganizationMemberListPrefetchProductType.from_dict(
                _product_type
            )

        _role = d.pop("role", UNSET)
        role: PaginatedOrganizationMemberListPrefetchRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = PaginatedOrganizationMemberListPrefetchRole.from_dict(_role)

        _user = d.pop("user", UNSET)
        user: PaginatedOrganizationMemberListPrefetchUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = PaginatedOrganizationMemberListPrefetchUser.from_dict(_user)

        paginated_organization_member_list_prefetch = cls(
            product_type=product_type,
            role=role,
            user=user,
        )

        paginated_organization_member_list_prefetch.additional_properties = d
        return paginated_organization_member_list_prefetch

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
