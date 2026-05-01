from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_prefetch import OrganizationPrefetch


T = TypeVar("T", bound="Organization")


@_attrs_define
class Organization:
    """
    Attributes:
        id (int):
        name (str):
        updated (datetime.datetime | None):
        created (datetime.datetime | None):
        members (list[int]):
        authorization_groups (list[int]):
        critical_asset (bool | Unset):  Default: False.
        key_asset (bool | Unset):  Default: False.
        description (None | str | Unset):
        prefetch (OrganizationPrefetch | Unset):
    """

    id: int
    name: str
    updated: datetime.datetime | None
    created: datetime.datetime | None
    members: list[int]
    authorization_groups: list[int]
    critical_asset: bool | Unset = False
    key_asset: bool | Unset = False
    description: None | str | Unset = UNSET
    prefetch: OrganizationPrefetch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        updated: None | str
        if isinstance(self.updated, datetime.datetime):
            updated = self.updated.isoformat()
        else:
            updated = self.updated

        created: None | str
        if isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        members = self.members

        authorization_groups = self.authorization_groups

        critical_asset = self.critical_asset

        key_asset = self.key_asset

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        prefetch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prefetch, Unset):
            prefetch = self.prefetch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "updated": updated,
                "created": created,
                "members": members,
                "authorization_groups": authorization_groups,
            }
        )
        if critical_asset is not UNSET:
            field_dict["critical_asset"] = critical_asset
        if key_asset is not UNSET:
            field_dict["key_asset"] = key_asset
        if description is not UNSET:
            field_dict["description"] = description
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_prefetch import OrganizationPrefetch

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_updated(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_type_0 = isoparse(data)

                return updated_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        updated = _parse_updated(d.pop("updated"))

        def _parse_created(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_type_0 = isoparse(data)

                return created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        created = _parse_created(d.pop("created"))

        members = cast(list[int], d.pop("members"))

        authorization_groups = cast(list[int], d.pop("authorization_groups"))

        critical_asset = d.pop("critical_asset", UNSET)

        key_asset = d.pop("key_asset", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _prefetch = d.pop("prefetch", UNSET)
        prefetch: OrganizationPrefetch | Unset
        if isinstance(_prefetch, Unset):
            prefetch = UNSET
        else:
            prefetch = OrganizationPrefetch.from_dict(_prefetch)

        organization = cls(
            id=id,
            name=name,
            updated=updated,
            created=created,
            members=members,
            authorization_groups=authorization_groups,
            critical_asset=critical_asset,
            key_asset=key_asset,
            description=description,
            prefetch=prefetch,
        )

        organization.additional_properties = d
        return organization

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
