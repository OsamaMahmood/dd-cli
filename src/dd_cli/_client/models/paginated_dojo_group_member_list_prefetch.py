from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_dojo_group_member_list_prefetch_group import (
        PaginatedDojoGroupMemberListPrefetchGroup,
    )
    from ..models.paginated_dojo_group_member_list_prefetch_role import (
        PaginatedDojoGroupMemberListPrefetchRole,
    )
    from ..models.paginated_dojo_group_member_list_prefetch_user import (
        PaginatedDojoGroupMemberListPrefetchUser,
    )


T = TypeVar("T", bound="PaginatedDojoGroupMemberListPrefetch")


@_attrs_define
class PaginatedDojoGroupMemberListPrefetch:
    """
    Attributes:
        group (PaginatedDojoGroupMemberListPrefetchGroup | Unset):
        role (PaginatedDojoGroupMemberListPrefetchRole | Unset):
        user (PaginatedDojoGroupMemberListPrefetchUser | Unset):
    """

    group: PaginatedDojoGroupMemberListPrefetchGroup | Unset = UNSET
    role: PaginatedDojoGroupMemberListPrefetchRole | Unset = UNSET
    user: PaginatedDojoGroupMemberListPrefetchUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group is not UNSET:
            field_dict["group"] = group
        if role is not UNSET:
            field_dict["role"] = role
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_dojo_group_member_list_prefetch_group import (
            PaginatedDojoGroupMemberListPrefetchGroup,
        )
        from ..models.paginated_dojo_group_member_list_prefetch_role import (
            PaginatedDojoGroupMemberListPrefetchRole,
        )
        from ..models.paginated_dojo_group_member_list_prefetch_user import (
            PaginatedDojoGroupMemberListPrefetchUser,
        )

        d = dict(src_dict)
        _group = d.pop("group", UNSET)
        group: PaginatedDojoGroupMemberListPrefetchGroup | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = PaginatedDojoGroupMemberListPrefetchGroup.from_dict(_group)

        _role = d.pop("role", UNSET)
        role: PaginatedDojoGroupMemberListPrefetchRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = PaginatedDojoGroupMemberListPrefetchRole.from_dict(_role)

        _user = d.pop("user", UNSET)
        user: PaginatedDojoGroupMemberListPrefetchUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = PaginatedDojoGroupMemberListPrefetchUser.from_dict(_user)

        paginated_dojo_group_member_list_prefetch = cls(
            group=group,
            role=role,
            user=user,
        )

        paginated_dojo_group_member_list_prefetch.additional_properties = d
        return paginated_dojo_group_member_list_prefetch

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
