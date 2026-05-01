from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_prefetch_authorization_groups import (
        OrganizationPrefetchAuthorizationGroups,
    )
    from ..models.organization_prefetch_members import OrganizationPrefetchMembers


T = TypeVar("T", bound="OrganizationPrefetch")


@_attrs_define
class OrganizationPrefetch:
    """
    Attributes:
        authorization_groups (OrganizationPrefetchAuthorizationGroups | Unset):
        members (OrganizationPrefetchMembers | Unset):
    """

    authorization_groups: OrganizationPrefetchAuthorizationGroups | Unset = UNSET
    members: OrganizationPrefetchMembers | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authorization_groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authorization_groups, Unset):
            authorization_groups = self.authorization_groups.to_dict()

        members: dict[str, Any] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = self.members.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authorization_groups is not UNSET:
            field_dict["authorization_groups"] = authorization_groups
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_prefetch_authorization_groups import (
            OrganizationPrefetchAuthorizationGroups,
        )
        from ..models.organization_prefetch_members import OrganizationPrefetchMembers

        d = dict(src_dict)
        _authorization_groups = d.pop("authorization_groups", UNSET)
        authorization_groups: OrganizationPrefetchAuthorizationGroups | Unset
        if isinstance(_authorization_groups, Unset):
            authorization_groups = UNSET
        else:
            authorization_groups = OrganizationPrefetchAuthorizationGroups.from_dict(
                _authorization_groups
            )

        _members = d.pop("members", UNSET)
        members: OrganizationPrefetchMembers | Unset
        if isinstance(_members, Unset):
            members = UNSET
        else:
            members = OrganizationPrefetchMembers.from_dict(_members)

        organization_prefetch = cls(
            authorization_groups=authorization_groups,
            members=members,
        )

        organization_prefetch.additional_properties = d
        return organization_prefetch

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
