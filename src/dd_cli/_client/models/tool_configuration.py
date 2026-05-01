from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tool_configuration_authentication_type_type_1 import (
    ToolConfigurationAuthenticationTypeType1,
)
from ..models.tool_configuration_authentication_type_type_2_type_1 import (
    ToolConfigurationAuthenticationTypeType2Type1,
)
from ..models.tool_configuration_authentication_type_type_3_type_1 import (
    ToolConfigurationAuthenticationTypeType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_configuration_prefetch import ToolConfigurationPrefetch


T = TypeVar("T", bound="ToolConfiguration")


@_attrs_define
class ToolConfiguration:
    """
    Attributes:
        id (int):
        name (str):
        tool_type (int):
        description (None | str | Unset):
        url (None | str | Unset):
        authentication_type (None | ToolConfigurationAuthenticationTypeType1 |
            ToolConfigurationAuthenticationTypeType2Type1 | ToolConfigurationAuthenticationTypeType3Type1 | Unset): * `API`
            - API Key
            * `Password` - Username/Password
            * `SSH` - SSH
        extras (None | str | Unset): Additional definitions that will be consumed by scanner
        username (None | str | Unset):
        auth_title (None | str | Unset):
        prefetch (ToolConfigurationPrefetch | Unset):
    """

    id: int
    name: str
    tool_type: int
    description: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    authentication_type: (
        None
        | ToolConfigurationAuthenticationTypeType1
        | ToolConfigurationAuthenticationTypeType2Type1
        | ToolConfigurationAuthenticationTypeType3Type1
        | Unset
    ) = UNSET
    extras: None | str | Unset = UNSET
    username: None | str | Unset = UNSET
    auth_title: None | str | Unset = UNSET
    prefetch: ToolConfigurationPrefetch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        tool_type = self.tool_type

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        authentication_type: None | str | Unset
        if isinstance(self.authentication_type, Unset):
            authentication_type = UNSET
        elif (
            isinstance(self.authentication_type, ToolConfigurationAuthenticationTypeType1)
            or isinstance(self.authentication_type, ToolConfigurationAuthenticationTypeType2Type1)
            or isinstance(self.authentication_type, ToolConfigurationAuthenticationTypeType3Type1)
        ):
            authentication_type = self.authentication_type.value
        else:
            authentication_type = self.authentication_type

        extras: None | str | Unset
        if isinstance(self.extras, Unset):
            extras = UNSET
        else:
            extras = self.extras

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        auth_title: None | str | Unset
        if isinstance(self.auth_title, Unset):
            auth_title = UNSET
        else:
            auth_title = self.auth_title

        prefetch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prefetch, Unset):
            prefetch = self.prefetch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "tool_type": tool_type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if url is not UNSET:
            field_dict["url"] = url
        if authentication_type is not UNSET:
            field_dict["authentication_type"] = authentication_type
        if extras is not UNSET:
            field_dict["extras"] = extras
        if username is not UNSET:
            field_dict["username"] = username
        if auth_title is not UNSET:
            field_dict["auth_title"] = auth_title
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_configuration_prefetch import ToolConfigurationPrefetch

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        tool_type = d.pop("tool_type")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_authentication_type(
            data: object,
        ) -> (
            None
            | ToolConfigurationAuthenticationTypeType1
            | ToolConfigurationAuthenticationTypeType2Type1
            | ToolConfigurationAuthenticationTypeType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                authentication_type_type_1 = ToolConfigurationAuthenticationTypeType1(data)

                return authentication_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                authentication_type_type_2_type_1 = ToolConfigurationAuthenticationTypeType2Type1(
                    data
                )

                return authentication_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                authentication_type_type_3_type_1 = ToolConfigurationAuthenticationTypeType3Type1(
                    data
                )

                return authentication_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | ToolConfigurationAuthenticationTypeType1
                | ToolConfigurationAuthenticationTypeType2Type1
                | ToolConfigurationAuthenticationTypeType3Type1
                | Unset,
                data,
            )

        authentication_type = _parse_authentication_type(d.pop("authentication_type", UNSET))

        def _parse_extras(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extras = _parse_extras(d.pop("extras", UNSET))

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

        def _parse_auth_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        auth_title = _parse_auth_title(d.pop("auth_title", UNSET))

        _prefetch = d.pop("prefetch", UNSET)
        prefetch: ToolConfigurationPrefetch | Unset
        if isinstance(_prefetch, Unset):
            prefetch = UNSET
        else:
            prefetch = ToolConfigurationPrefetch.from_dict(_prefetch)

        tool_configuration = cls(
            id=id,
            name=name,
            tool_type=tool_type,
            description=description,
            url=url,
            authentication_type=authentication_type,
            extras=extras,
            username=username,
            auth_title=auth_title,
            prefetch=prefetch,
        )

        tool_configuration.additional_properties = d
        return tool_configuration

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
