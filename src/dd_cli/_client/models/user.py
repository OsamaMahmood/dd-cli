from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        id (int):
        username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        email (str):
        date_joined (datetime.datetime):
        last_login (datetime.datetime | None):
        token_last_reset (datetime.datetime | None):
        password_last_reset (datetime.datetime | None):
        first_name (str | Unset):
        last_name (str | Unset):
        is_active (bool | Unset): Designates whether this user should be treated as active. Unselect this instead of
            deleting accounts.
        is_superuser (bool | Unset): Designates that this user has all permissions without explicitly assigning them.
        configuration_permissions (list[int | None] | Unset):
    """

    id: int
    username: str
    email: str
    date_joined: datetime.datetime
    last_login: datetime.datetime | None
    token_last_reset: datetime.datetime | None
    password_last_reset: datetime.datetime | None
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    is_active: bool | Unset = UNSET
    is_superuser: bool | Unset = UNSET
    configuration_permissions: list[int | None] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        username = self.username

        email = self.email

        date_joined = self.date_joined.isoformat()

        last_login: None | str
        if isinstance(self.last_login, datetime.datetime):
            last_login = self.last_login.isoformat()
        else:
            last_login = self.last_login

        token_last_reset: None | str
        if isinstance(self.token_last_reset, datetime.datetime):
            token_last_reset = self.token_last_reset.isoformat()
        else:
            token_last_reset = self.token_last_reset

        password_last_reset: None | str
        if isinstance(self.password_last_reset, datetime.datetime):
            password_last_reset = self.password_last_reset.isoformat()
        else:
            password_last_reset = self.password_last_reset

        first_name = self.first_name

        last_name = self.last_name

        is_active = self.is_active

        is_superuser = self.is_superuser

        configuration_permissions: list[int | None] | Unset = UNSET
        if not isinstance(self.configuration_permissions, Unset):
            configuration_permissions = []
            for configuration_permissions_item_data in self.configuration_permissions:
                configuration_permissions_item: int | None
                configuration_permissions_item = configuration_permissions_item_data
                configuration_permissions.append(configuration_permissions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "username": username,
                "email": email,
                "date_joined": date_joined,
                "last_login": last_login,
                "token_last_reset": token_last_reset,
                "password_last_reset": password_last_reset,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_superuser is not UNSET:
            field_dict["is_superuser"] = is_superuser
        if configuration_permissions is not UNSET:
            field_dict["configuration_permissions"] = configuration_permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        username = d.pop("username")

        email = d.pop("email")

        date_joined = isoparse(d.pop("date_joined"))

        def _parse_last_login(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_login_type_0 = isoparse(data)

                return last_login_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_login = _parse_last_login(d.pop("last_login"))

        def _parse_token_last_reset(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                token_last_reset_type_0 = isoparse(data)

                return token_last_reset_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        token_last_reset = _parse_token_last_reset(d.pop("token_last_reset"))

        def _parse_password_last_reset(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                password_last_reset_type_0 = isoparse(data)

                return password_last_reset_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        password_last_reset = _parse_password_last_reset(d.pop("password_last_reset"))

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_superuser = d.pop("is_superuser", UNSET)

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

        user = cls(
            id=id,
            username=username,
            email=email,
            date_joined=date_joined,
            last_login=last_login,
            token_last_reset=token_last_reset,
            password_last_reset=password_last_reset,
            first_name=first_name,
            last_name=last_name,
            is_active=is_active,
            is_superuser=is_superuser,
            configuration_permissions=configuration_permissions,
        )

        user.additional_properties = d
        return user

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
