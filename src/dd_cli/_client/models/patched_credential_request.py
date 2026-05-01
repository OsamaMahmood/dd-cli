from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.patched_credential_request_authentication import (
    PatchedCredentialRequestAuthentication,
)
from ..models.patched_credential_request_http_authentication_type_1 import (
    PatchedCredentialRequestHttpAuthenticationType1,
)
from ..models.patched_credential_request_http_authentication_type_2_type_1 import (
    PatchedCredentialRequestHttpAuthenticationType2Type1,
)
from ..models.patched_credential_request_http_authentication_type_3_type_1 import (
    PatchedCredentialRequestHttpAuthenticationType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedCredentialRequest")


@_attrs_define
class PatchedCredentialRequest:
    """
    Attributes:
        name (str | Unset):
        username (str | Unset):
        role (str | Unset):
        authentication (PatchedCredentialRequestAuthentication | Unset): * `Form` - Form Authentication
            * `SSO` - SSO Redirect
        http_authentication (None | PatchedCredentialRequestHttpAuthenticationType1 |
            PatchedCredentialRequestHttpAuthenticationType2Type1 | PatchedCredentialRequestHttpAuthenticationType3Type1 |
            Unset): * `Basic` - Basic
            * `NTLM` - NTLM
        description (None | str | Unset):
        url (str | Unset):
        login_regex (None | str | Unset):
        logout_regex (None | str | Unset):
        is_valid (bool | Unset):
        environment (int | Unset):
    """

    name: str | Unset = UNSET
    username: str | Unset = UNSET
    role: str | Unset = UNSET
    authentication: PatchedCredentialRequestAuthentication | Unset = UNSET
    http_authentication: (
        None
        | PatchedCredentialRequestHttpAuthenticationType1
        | PatchedCredentialRequestHttpAuthenticationType2Type1
        | PatchedCredentialRequestHttpAuthenticationType3Type1
        | Unset
    ) = UNSET
    description: None | str | Unset = UNSET
    url: str | Unset = UNSET
    login_regex: None | str | Unset = UNSET
    logout_regex: None | str | Unset = UNSET
    is_valid: bool | Unset = UNSET
    environment: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        username = self.username

        role = self.role

        authentication: str | Unset = UNSET
        if not isinstance(self.authentication, Unset):
            authentication = self.authentication.value

        http_authentication: None | str | Unset
        if isinstance(self.http_authentication, Unset):
            http_authentication = UNSET
        elif (
            isinstance(self.http_authentication, PatchedCredentialRequestHttpAuthenticationType1)
            or isinstance(
                self.http_authentication, PatchedCredentialRequestHttpAuthenticationType2Type1
            )
            or isinstance(
                self.http_authentication, PatchedCredentialRequestHttpAuthenticationType3Type1
            )
        ):
            http_authentication = self.http_authentication.value
        else:
            http_authentication = self.http_authentication

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        url = self.url

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

        environment = self.environment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if username is not UNSET:
            field_dict["username"] = username
        if role is not UNSET:
            field_dict["role"] = role
        if authentication is not UNSET:
            field_dict["authentication"] = authentication
        if http_authentication is not UNSET:
            field_dict["http_authentication"] = http_authentication
        if description is not UNSET:
            field_dict["description"] = description
        if url is not UNSET:
            field_dict["url"] = url
        if login_regex is not UNSET:
            field_dict["login_regex"] = login_regex
        if logout_regex is not UNSET:
            field_dict["logout_regex"] = logout_regex
        if is_valid is not UNSET:
            field_dict["is_valid"] = is_valid
        if environment is not UNSET:
            field_dict["environment"] = environment

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.username, Unset):
            files.append(("username", (None, str(self.username).encode(), "text/plain")))

        if not isinstance(self.role, Unset):
            files.append(("role", (None, str(self.role).encode(), "text/plain")))

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
                self.http_authentication, PatchedCredentialRequestHttpAuthenticationType1
            ) or isinstance(
                self.http_authentication, PatchedCredentialRequestHttpAuthenticationType2Type1
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

        if not isinstance(self.url, Unset):
            files.append(("url", (None, str(self.url).encode(), "text/plain")))

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

        if not isinstance(self.environment, Unset):
            files.append(("environment", (None, str(self.environment).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        username = d.pop("username", UNSET)

        role = d.pop("role", UNSET)

        _authentication = d.pop("authentication", UNSET)
        authentication: PatchedCredentialRequestAuthentication | Unset
        if isinstance(_authentication, Unset):
            authentication = UNSET
        else:
            authentication = PatchedCredentialRequestAuthentication(_authentication)

        def _parse_http_authentication(
            data: object,
        ) -> (
            None
            | PatchedCredentialRequestHttpAuthenticationType1
            | PatchedCredentialRequestHttpAuthenticationType2Type1
            | PatchedCredentialRequestHttpAuthenticationType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                http_authentication_type_1 = PatchedCredentialRequestHttpAuthenticationType1(data)

                return http_authentication_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                http_authentication_type_2_type_1 = (
                    PatchedCredentialRequestHttpAuthenticationType2Type1(data)
                )

                return http_authentication_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                http_authentication_type_3_type_1 = (
                    PatchedCredentialRequestHttpAuthenticationType3Type1(data)
                )

                return http_authentication_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PatchedCredentialRequestHttpAuthenticationType1
                | PatchedCredentialRequestHttpAuthenticationType2Type1
                | PatchedCredentialRequestHttpAuthenticationType3Type1
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

        url = d.pop("url", UNSET)

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

        environment = d.pop("environment", UNSET)

        patched_credential_request = cls(
            name=name,
            username=username,
            role=role,
            authentication=authentication,
            http_authentication=http_authentication,
            description=description,
            url=url,
            login_regex=login_regex,
            logout_regex=logout_regex,
            is_valid=is_valid,
            environment=environment,
        )

        patched_credential_request.additional_properties = d
        return patched_credential_request

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
