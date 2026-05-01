from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.credential_request_authentication import CredentialRequestAuthentication
from ..models.credential_request_http_authentication_type_1 import (
    CredentialRequestHttpAuthenticationType1,
)
from ..models.credential_request_http_authentication_type_2_type_1 import (
    CredentialRequestHttpAuthenticationType2Type1,
)
from ..models.credential_request_http_authentication_type_3_type_1 import (
    CredentialRequestHttpAuthenticationType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CredentialRequest")


@_attrs_define
class CredentialRequest:
    """
    Attributes:
        name (str):
        username (str):
        role (str):
        url (str):
        environment (int):
        authentication (CredentialRequestAuthentication | Unset): * `Form` - Form Authentication
            * `SSO` - SSO Redirect
        http_authentication (CredentialRequestHttpAuthenticationType1 | CredentialRequestHttpAuthenticationType2Type1 |
            CredentialRequestHttpAuthenticationType3Type1 | None | Unset): * `Basic` - Basic
            * `NTLM` - NTLM
        description (None | str | Unset):
        login_regex (None | str | Unset):
        logout_regex (None | str | Unset):
        is_valid (bool | Unset):
    """

    name: str
    username: str
    role: str
    url: str
    environment: int
    authentication: CredentialRequestAuthentication | Unset = UNSET
    http_authentication: (
        CredentialRequestHttpAuthenticationType1
        | CredentialRequestHttpAuthenticationType2Type1
        | CredentialRequestHttpAuthenticationType3Type1
        | None
        | Unset
    ) = UNSET
    description: None | str | Unset = UNSET
    login_regex: None | str | Unset = UNSET
    logout_regex: None | str | Unset = UNSET
    is_valid: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        username = self.username

        role = self.role

        url = self.url

        environment = self.environment

        authentication: str | Unset = UNSET
        if not isinstance(self.authentication, Unset):
            authentication = self.authentication.value

        http_authentication: None | str | Unset
        if isinstance(self.http_authentication, Unset):
            http_authentication = UNSET
        elif (
            isinstance(self.http_authentication, CredentialRequestHttpAuthenticationType1)
            or isinstance(self.http_authentication, CredentialRequestHttpAuthenticationType2Type1)
            or isinstance(self.http_authentication, CredentialRequestHttpAuthenticationType3Type1)
        ):
            http_authentication = self.http_authentication.value
        else:
            http_authentication = self.http_authentication

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        login_regex: None | str | Unset
        if isinstance(self.login_regex, Unset):
            login_regex = UNSET
        else:
            login_regex = self.login_regex

        logout_regex: None | str | Unset
        if isinstance(self.logout_regex, Unset):
            logout_regex = UNSET
        else:
            logout_regex = self.logout_regex

        is_valid = self.is_valid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "username": username,
                "role": role,
                "url": url,
                "environment": environment,
            }
        )
        if authentication is not UNSET:
            field_dict["authentication"] = authentication
        if http_authentication is not UNSET:
            field_dict["http_authentication"] = http_authentication
        if description is not UNSET:
            field_dict["description"] = description
        if login_regex is not UNSET:
            field_dict["login_regex"] = login_regex
        if logout_regex is not UNSET:
            field_dict["logout_regex"] = logout_regex
        if is_valid is not UNSET:
            field_dict["is_valid"] = is_valid

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("username", (None, str(self.username).encode(), "text/plain")))

        files.append(("role", (None, str(self.role).encode(), "text/plain")))

        files.append(("url", (None, str(self.url).encode(), "text/plain")))

        files.append(("environment", (None, str(self.environment).encode(), "text/plain")))

        if not isinstance(self.authentication, Unset):
            files.append(
                ("authentication", (None, str(self.authentication.value).encode(), "text/plain"))
            )

        if not isinstance(self.http_authentication, Unset):
            if self.http_authentication is None:
                files.append(
                    (
                        "http_authentication",
                        (None, str(self.http_authentication).encode(), "text/plain"),
                    )
                )
            elif isinstance(
                self.http_authentication, CredentialRequestHttpAuthenticationType1
            ) or isinstance(
                self.http_authentication, CredentialRequestHttpAuthenticationType2Type1
            ):
                files.append(
                    (
                        "http_authentication",
                        (None, str(self.http_authentication.value).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "http_authentication",
                        (None, str(self.http_authentication.value).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.description, Unset):
            if isinstance(self.description, str):
                files.append(("description", (None, str(self.description).encode(), "text/plain")))
            else:
                files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.login_regex, Unset):
            if isinstance(self.login_regex, str):
                files.append(("login_regex", (None, str(self.login_regex).encode(), "text/plain")))
            else:
                files.append(("login_regex", (None, str(self.login_regex).encode(), "text/plain")))

        if not isinstance(self.logout_regex, Unset):
            if isinstance(self.logout_regex, str):
                files.append(
                    ("logout_regex", (None, str(self.logout_regex).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("logout_regex", (None, str(self.logout_regex).encode(), "text/plain"))
                )

        if not isinstance(self.is_valid, Unset):
            files.append(("is_valid", (None, str(self.is_valid).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        username = d.pop("username")

        role = d.pop("role")

        url = d.pop("url")

        environment = d.pop("environment")

        _authentication = d.pop("authentication", UNSET)
        authentication: CredentialRequestAuthentication | Unset
        if isinstance(_authentication, Unset):
            authentication = UNSET
        else:
            authentication = CredentialRequestAuthentication(_authentication)

        def _parse_http_authentication(
            data: object,
        ) -> (
            CredentialRequestHttpAuthenticationType1
            | CredentialRequestHttpAuthenticationType2Type1
            | CredentialRequestHttpAuthenticationType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                http_authentication_type_1 = CredentialRequestHttpAuthenticationType1(data)

                return http_authentication_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                http_authentication_type_2_type_1 = CredentialRequestHttpAuthenticationType2Type1(
                    data
                )

                return http_authentication_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                http_authentication_type_3_type_1 = CredentialRequestHttpAuthenticationType3Type1(
                    data
                )

                return http_authentication_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CredentialRequestHttpAuthenticationType1
                | CredentialRequestHttpAuthenticationType2Type1
                | CredentialRequestHttpAuthenticationType3Type1
                | None
                | Unset,
                data,
            )

        http_authentication = _parse_http_authentication(d.pop("http_authentication", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_login_regex(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        login_regex = _parse_login_regex(d.pop("login_regex", UNSET))

        def _parse_logout_regex(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logout_regex = _parse_logout_regex(d.pop("logout_regex", UNSET))

        is_valid = d.pop("is_valid", UNSET)

        credential_request = cls(
            name=name,
            username=username,
            role=role,
            url=url,
            environment=environment,
            authentication=authentication,
            http_authentication=http_authentication,
            description=description,
            login_regex=login_regex,
            logout_regex=logout_regex,
            is_valid=is_valid,
        )

        credential_request.additional_properties = d
        return credential_request

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
