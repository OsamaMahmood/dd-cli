from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dojo_group_social_authentication_provider import DojoGroupSocialAuthenticationProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dojo_group_prefetch import DojoGroupPrefetch


T = TypeVar("T", bound="DojoGroup")


@_attrs_define
class DojoGroup:
    """
    Attributes:
        id (int):
        name (str):
        users (list[int]):
        configuration_permissions (list[int | None] | Unset):
        description (None | str | Unset):
        social_provider (DojoGroupSocialAuthenticationProvider | None | Unset): Group imported from a social provider.

            * `AzureAD` - AzureAD
            * `Remote` - Remote
        prefetch (DojoGroupPrefetch | Unset):
    """

    id: int
    name: str
    users: list[int]
    configuration_permissions: list[int | None] | Unset = UNSET
    description: None | str | Unset = UNSET
    social_provider: DojoGroupSocialAuthenticationProvider | None | Unset = UNSET
    prefetch: DojoGroupPrefetch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        users = self.users

        configuration_permissions: list[int | None] | Unset = UNSET
        if not isinstance(self.configuration_permissions, Unset):
            configuration_permissions = []
            for configuration_permissions_item_data in self.configuration_permissions:
                configuration_permissions_item: int | None
                configuration_permissions_item = configuration_permissions_item_data
                configuration_permissions.append(configuration_permissions_item)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        social_provider: None | str | Unset
        if isinstance(self.social_provider, Unset):
            social_provider = UNSET
        elif isinstance(self.social_provider, DojoGroupSocialAuthenticationProvider):
            social_provider = self.social_provider.value
        else:
            social_provider = self.social_provider

        prefetch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prefetch, Unset):
            prefetch = self.prefetch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "users": users,
            }
        )
        if configuration_permissions is not UNSET:
            field_dict["configuration_permissions"] = configuration_permissions
        if description is not UNSET:
            field_dict["description"] = description
        if social_provider is not UNSET:
            field_dict["social_provider"] = social_provider
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dojo_group_prefetch import DojoGroupPrefetch

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        users = cast(list[int], d.pop("users"))

        _configuration_permissions = d.pop("configuration_permissions", UNSET)
        configuration_permissions: list[int | None] | Unset = UNSET
        if _configuration_permissions is not UNSET:
            configuration_permissions = []
            for configuration_permissions_item_data in _configuration_permissions:

                def _parse_configuration_permissions_item(data: object) -> int | None:
                    if data is None:
                        return data
                    return cast(int | None, data)

                configuration_permissions_item = _parse_configuration_permissions_item(
                    configuration_permissions_item_data
                )

                configuration_permissions.append(configuration_permissions_item)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_social_provider(
            data: object,
        ) -> DojoGroupSocialAuthenticationProvider | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                social_provider_type_1 = DojoGroupSocialAuthenticationProvider(data)

                return social_provider_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DojoGroupSocialAuthenticationProvider | None | Unset, data)

        social_provider = _parse_social_provider(d.pop("social_provider", UNSET))

        _prefetch = d.pop("prefetch", UNSET)
        prefetch: DojoGroupPrefetch | Unset
        if isinstance(_prefetch, Unset):
            prefetch = UNSET
        else:
            prefetch = DojoGroupPrefetch.from_dict(_prefetch)

        dojo_group = cls(
            id=id,
            name=name,
            users=users,
            configuration_permissions=configuration_permissions,
            description=description,
            social_provider=social_provider,
            prefetch=prefetch,
        )

        dojo_group.additional_properties = d
        return dojo_group

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
