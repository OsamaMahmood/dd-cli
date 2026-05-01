from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.tool_configuration_request_authentication_type_type_1 import (
    ToolConfigurationRequestAuthenticationTypeType1,
)
from ..models.tool_configuration_request_authentication_type_type_2_type_1 import (
    ToolConfigurationRequestAuthenticationTypeType2Type1,
)
from ..models.tool_configuration_request_authentication_type_type_3_type_1 import (
    ToolConfigurationRequestAuthenticationTypeType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ToolConfigurationRequest")


@_attrs_define
class ToolConfigurationRequest:
    """
    Attributes:
        name (str):
        tool_type (int):
        description (None | str | Unset):
        url (None | str | Unset):
        authentication_type (None | ToolConfigurationRequestAuthenticationTypeType1 |
            ToolConfigurationRequestAuthenticationTypeType2Type1 | ToolConfigurationRequestAuthenticationTypeType3Type1 |
            Unset): * `API` - API Key
            * `Password` - Username/Password
            * `SSH` - SSH
        extras (None | str | Unset): Additional definitions that will be consumed by scanner
        username (None | str | Unset):
        password (None | str | Unset):
        auth_title (None | str | Unset):
        ssh (None | str | Unset):
        api_key (None | str | Unset):
    """

    name: str
    tool_type: int
    description: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    authentication_type: (
        None
        | ToolConfigurationRequestAuthenticationTypeType1
        | ToolConfigurationRequestAuthenticationTypeType2Type1
        | ToolConfigurationRequestAuthenticationTypeType3Type1
        | Unset
    ) = UNSET
    extras: None | str | Unset = UNSET
    username: None | str | Unset = UNSET
    password: None | str | Unset = UNSET
    auth_title: None | str | Unset = UNSET
    ssh: None | str | Unset = UNSET
    api_key: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
            isinstance(self.authentication_type, ToolConfigurationRequestAuthenticationTypeType1)
            or isinstance(
                self.authentication_type, ToolConfigurationRequestAuthenticationTypeType2Type1
            )
            or isinstance(
                self.authentication_type, ToolConfigurationRequestAuthenticationTypeType3Type1
            )
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

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        auth_title: None | str | Unset
        if isinstance(self.auth_title, Unset):
            auth_title = UNSET
        else:
            auth_title = self.auth_title

        ssh: None | str | Unset
        if isinstance(self.ssh, Unset):
            ssh = UNSET
        else:
            ssh = self.ssh

        api_key: None | str | Unset
        if isinstance(self.api_key, Unset):
            api_key = UNSET
        else:
            api_key = self.api_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
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
        if password is not UNSET:
            field_dict["password"] = password
        if auth_title is not UNSET:
            field_dict["auth_title"] = auth_title
        if ssh is not UNSET:
            field_dict["ssh"] = ssh
        if api_key is not UNSET:
            field_dict["api_key"] = api_key

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("tool_type", (None, str(self.tool_type).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            if isinstance(self.description, str):
                files.append(("description", (None, str(self.description).encode(), "text/plain")))
            else:
                files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.url, Unset):
            if isinstance(self.url, str):
                files.append(("url", (None, str(self.url).encode(), "text/plain")))
            else:
                files.append(("url", (None, str(self.url).encode(), "text/plain")))

        if not isinstance(self.authentication_type, Unset):
            if self.authentication_type is None:
                files.append(
                    (
                        "authentication_type",
                        (None, str(self.authentication_type).encode(), "text/plain"),
                    )
                )
            elif isinstance(
                self.authentication_type, ToolConfigurationRequestAuthenticationTypeType1
            ) or isinstance(
                self.authentication_type, ToolConfigurationRequestAuthenticationTypeType2Type1
            ):
                files.append(
                    (
                        "authentication_type",
                        (None, str(self.authentication_type.value).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "authentication_type",
                        (None, str(self.authentication_type.value).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.extras, Unset):
            if isinstance(self.extras, str):
                files.append(("extras", (None, str(self.extras).encode(), "text/plain")))
            else:
                files.append(("extras", (None, str(self.extras).encode(), "text/plain")))

        if not isinstance(self.username, Unset):
            if isinstance(self.username, str):
                files.append(("username", (None, str(self.username).encode(), "text/plain")))
            else:
                files.append(("username", (None, str(self.username).encode(), "text/plain")))

        if not isinstance(self.password, Unset):
            if isinstance(self.password, str):
                files.append(("password", (None, str(self.password).encode(), "text/plain")))
            else:
                files.append(("password", (None, str(self.password).encode(), "text/plain")))

        if not isinstance(self.auth_title, Unset):
            if isinstance(self.auth_title, str):
                files.append(("auth_title", (None, str(self.auth_title).encode(), "text/plain")))
            else:
                files.append(("auth_title", (None, str(self.auth_title).encode(), "text/plain")))

        if not isinstance(self.ssh, Unset):
            if isinstance(self.ssh, str):
                files.append(("ssh", (None, str(self.ssh).encode(), "text/plain")))
            else:
                files.append(("ssh", (None, str(self.ssh).encode(), "text/plain")))

        if not isinstance(self.api_key, Unset):
            if isinstance(self.api_key, str):
                files.append(("api_key", (None, str(self.api_key).encode(), "text/plain")))
            else:
                files.append(("api_key", (None, str(self.api_key).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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
            | ToolConfigurationRequestAuthenticationTypeType1
            | ToolConfigurationRequestAuthenticationTypeType2Type1
            | ToolConfigurationRequestAuthenticationTypeType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                authentication_type_type_1 = ToolConfigurationRequestAuthenticationTypeType1(data)

                return authentication_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                authentication_type_type_2_type_1 = (
                    ToolConfigurationRequestAuthenticationTypeType2Type1(data)
                )

                return authentication_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                authentication_type_type_3_type_1 = (
                    ToolConfigurationRequestAuthenticationTypeType3Type1(data)
                )

                return authentication_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | ToolConfigurationRequestAuthenticationTypeType1
                | ToolConfigurationRequestAuthenticationTypeType2Type1
                | ToolConfigurationRequestAuthenticationTypeType3Type1
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

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_auth_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        auth_title = _parse_auth_title(d.pop("auth_title", UNSET))

        def _parse_ssh(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ssh = _parse_ssh(d.pop("ssh", UNSET))

        def _parse_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_key = _parse_api_key(d.pop("api_key", UNSET))

        tool_configuration_request = cls(
            name=name,
            tool_type=tool_type,
            description=description,
            url=url,
            authentication_type=authentication_type,
            extras=extras,
            username=username,
            password=password,
            auth_title=auth_title,
            ssh=ssh,
            api_key=api_key,
        )

        tool_configuration_request.additional_properties = d
        return tool_configuration_request

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
