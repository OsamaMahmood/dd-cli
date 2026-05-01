from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.patched_dojo_group_request_social_authentication_provider import (
    PatchedDojoGroupRequestSocialAuthenticationProvider,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedDojoGroupRequest")


@_attrs_define
class PatchedDojoGroupRequest:
    """
    Attributes:
        configuration_permissions (list[int | None] | Unset):
        name (str | Unset):
        description (None | str | Unset):
        social_provider (None | PatchedDojoGroupRequestSocialAuthenticationProvider | Unset): Group imported from a
            social provider.

            * `AzureAD` - AzureAD
            * `Remote` - Remote
    """

    configuration_permissions: list[int | None] | Unset = UNSET
    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    social_provider: None | PatchedDojoGroupRequestSocialAuthenticationProvider | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration_permissions: list[int | None] | Unset = UNSET
        if not isinstance(self.configuration_permissions, Unset):
            configuration_permissions = []
            for configuration_permissions_item_data in self.configuration_permissions:
                configuration_permissions_item: int | None
                configuration_permissions_item = configuration_permissions_item_data
                configuration_permissions.append(configuration_permissions_item)

        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        social_provider: None | str | Unset
        if isinstance(self.social_provider, Unset):
            social_provider = UNSET
        elif isinstance(self.social_provider, PatchedDojoGroupRequestSocialAuthenticationProvider):
            social_provider = self.social_provider.value
        else:
            social_provider = self.social_provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configuration_permissions is not UNSET:
            field_dict["configuration_permissions"] = configuration_permissions
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if social_provider is not UNSET:
            field_dict["social_provider"] = social_provider

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.configuration_permissions, Unset):
            for configuration_permissions_item_element in self.configuration_permissions:
                if isinstance(configuration_permissions_item_element, int):
                    files.append(
                        (
                            "configuration_permissions",
                            (
                                None,
                                str(configuration_permissions_item_element).encode(),
                                "text/plain",
                            ),
                        )
                    )
                else:
                    files.append(
                        (
                            "configuration_permissions",
                            (
                                None,
                                str(configuration_permissions_item_element).encode(),
                                "text/plain",
                            ),
                        )
                    )

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            if isinstance(self.description, str):
                files.append(("description", (None, str(self.description).encode(), "text/plain")))
            else:
                files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.social_provider, Unset):
            if self.social_provider is None:
                files.append(
                    ("social_provider", (None, str(self.social_provider).encode(), "text/plain"))
                )
            else:
                files.append(
                    (
                        "social_provider",
                        (None, str(self.social_provider.value).encode(), "text/plain"),
                    )
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_social_provider(
            data: object,
        ) -> None | PatchedDojoGroupRequestSocialAuthenticationProvider | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                social_provider_type_1 = PatchedDojoGroupRequestSocialAuthenticationProvider(data)

                return social_provider_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchedDojoGroupRequestSocialAuthenticationProvider | Unset, data)

        social_provider = _parse_social_provider(d.pop("social_provider", UNSET))

        patched_dojo_group_request = cls(
            configuration_permissions=configuration_permissions,
            name=name,
            description=description,
            social_provider=social_provider,
        )

        patched_dojo_group_request.additional_properties = d
        return patched_dojo_group_request

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
