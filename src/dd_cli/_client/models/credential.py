from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credential_authentication import CredentialAuthentication
from ..models.credential_http_authentication_type_1 import CredentialHttpAuthenticationType1
from ..models.credential_http_authentication_type_2_type_1 import (
    CredentialHttpAuthenticationType2Type1,
)
from ..models.credential_http_authentication_type_3_type_1 import (
    CredentialHttpAuthenticationType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credential_prefetch import CredentialPrefetch


T = TypeVar("T", bound="Credential")


@_attrs_define
class Credential:
    """
    Attributes:
        id (int):
        name (str):
        username (str):
        role (str):
        url (str):
        environment (int):
        notes (list[int]):
        authentication (CredentialAuthentication | Unset): * `Form` - Form Authentication
            * `SSO` - SSO Redirect
        http_authentication (CredentialHttpAuthenticationType1 | CredentialHttpAuthenticationType2Type1 |
            CredentialHttpAuthenticationType3Type1 | None | Unset): * `Basic` - Basic
            * `NTLM` - NTLM
        description (None | str | Unset):
        login_regex (None | str | Unset):
        logout_regex (None | str | Unset):
        is_valid (bool | Unset):
        prefetch (CredentialPrefetch | Unset):
    """

    id: int
    name: str
    username: str
    role: str
    url: str
    environment: int
    notes: list[int]
    authentication: CredentialAuthentication | Unset = UNSET
    http_authentication: (
        CredentialHttpAuthenticationType1
        | CredentialHttpAuthenticationType2Type1
        | CredentialHttpAuthenticationType3Type1
        | None
        | Unset
    ) = UNSET
    description: None | str | Unset = UNSET
    login_regex: None | str | Unset = UNSET
    logout_regex: None | str | Unset = UNSET
    is_valid: bool | Unset = UNSET
    prefetch: CredentialPrefetch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        username = self.username

        role = self.role

        url = self.url

        environment = self.environment

        notes = self.notes

        authentication: str | Unset = UNSET
        if not isinstance(self.authentication, Unset):
            authentication = self.authentication.value

        http_authentication: None | str | Unset
        if isinstance(self.http_authentication, Unset):
            http_authentication = UNSET
        elif (
            isinstance(self.http_authentication, CredentialHttpAuthenticationType1)
            or isinstance(self.http_authentication, CredentialHttpAuthenticationType2Type1)
            or isinstance(self.http_authentication, CredentialHttpAuthenticationType3Type1)
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

        prefetch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prefetch, Unset):
            prefetch = self.prefetch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "username": username,
                "role": role,
                "url": url,
                "environment": environment,
                "notes": notes,
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
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_prefetch import CredentialPrefetch

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        username = d.pop("username")

        role = d.pop("role")

        url = d.pop("url")

        environment = d.pop("environment")

        notes = cast(list[int], d.pop("notes"))

        _authentication = d.pop("authentication", UNSET)
        authentication: CredentialAuthentication | Unset
        if isinstance(_authentication, Unset):
            authentication = UNSET
        else:
            authentication = CredentialAuthentication(_authentication)

        def _parse_http_authentication(
            data: object,
        ) -> (
            CredentialHttpAuthenticationType1
            | CredentialHttpAuthenticationType2Type1
            | CredentialHttpAuthenticationType3Type1
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
                http_authentication_type_1 = CredentialHttpAuthenticationType1(data)

                return http_authentication_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                http_authentication_type_2_type_1 = CredentialHttpAuthenticationType2Type1(data)

                return http_authentication_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                http_authentication_type_3_type_1 = CredentialHttpAuthenticationType3Type1(data)

                return http_authentication_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CredentialHttpAuthenticationType1
                | CredentialHttpAuthenticationType2Type1
                | CredentialHttpAuthenticationType3Type1
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

        _prefetch = d.pop("prefetch", UNSET)
        prefetch: CredentialPrefetch | Unset
        if isinstance(_prefetch, Unset):
            prefetch = UNSET
        else:
            prefetch = CredentialPrefetch.from_dict(_prefetch)

        credential = cls(
            id=id,
            name=name,
            username=username,
            role=role,
            url=url,
            environment=environment,
            notes=notes,
            authentication=authentication,
            http_authentication=http_authentication,
            description=description,
            login_regex=login_regex,
            logout_regex=logout_regex,
            is_valid=is_valid,
            prefetch=prefetch,
        )

        credential.additional_properties = d
        return credential

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
