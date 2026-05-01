from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_group_prefetch import OrganizationGroupPrefetch


T = TypeVar("T", bound="OrganizationGroup")


@_attrs_define
class OrganizationGroup:
    """
    Attributes:
        id (int):
        organization (int):
        group (int):
        role (int):
        prefetch (OrganizationGroupPrefetch | Unset):
    """

    id: int
    organization: int
    group: int
    role: int
    prefetch: OrganizationGroupPrefetch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        organization = self.organization

        group = self.group

        role = self.role

        prefetch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prefetch, Unset):
            prefetch = self.prefetch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "organization": organization,
                "group": group,
                "role": role,
            }
        )
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_group_prefetch import OrganizationGroupPrefetch

        d = dict(src_dict)
        id = d.pop("id")

        organization = d.pop("organization")

        group = d.pop("group")

        role = d.pop("role")

        _prefetch = d.pop("prefetch", UNSET)
        prefetch: OrganizationGroupPrefetch | Unset
        if isinstance(_prefetch, Unset):
            prefetch = UNSET
        else:
            prefetch = OrganizationGroupPrefetch.from_dict(_prefetch)

        organization_group = cls(
            id=id,
            organization=organization,
            group=group,
            role=role,
            prefetch=prefetch,
        )

        organization_group.additional_properties = d
        return organization_group

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
