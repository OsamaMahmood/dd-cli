from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedUserRequest")


@_attrs_define
class PatchedUserRequest:
    """
    Attributes:
        username (str | Unset): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        first_name (str | Unset):
        last_name (str | Unset):
        email (str | Unset):
        is_active (bool | Unset): Designates whether this user should be treated as active. Unselect this instead of
            deleting accounts.
        is_superuser (bool | Unset): Designates that this user has all permissions without explicitly assigning them.
        password (str | Unset):
        configuration_permissions (list[int | None] | Unset):
    """

    username: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    email: str | Unset = UNSET
    is_active: bool | Unset = UNSET
    is_superuser: bool | Unset = UNSET
    password: str | Unset = UNSET
    configuration_permissions: list[int | None] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        first_name = self.first_name

        last_name = self.last_name

        email = self.email

        is_active = self.is_active

        is_superuser = self.is_superuser

        password = self.password

        configuration_permissions: list[int | None] | Unset = UNSET
        if not isinstance(self.configuration_permissions, Unset):
            configuration_permissions = []
            for configuration_permissions_item_data in self.configuration_permissions:
                configuration_permissions_item: int | None
                configuration_permissions_item = configuration_permissions_item_data
                configuration_permissions.append(configuration_permissions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_superuser is not UNSET:
            field_dict["is_superuser"] = is_superuser
        if password is not UNSET:
            field_dict["password"] = password
        if configuration_permissions is not UNSET:
            field_dict["configuration_permissions"] = configuration_permissions

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.username, Unset):
            files.append(("username", (None, str(self.username).encode(), "text/plain")))

        if not isinstance(self.first_name, Unset):
            files.append(("first_name", (None, str(self.first_name).encode(), "text/plain")))

        if not isinstance(self.last_name, Unset):
            files.append(("last_name", (None, str(self.last_name).encode(), "text/plain")))

        if not isinstance(self.email, Unset):
            files.append(("email", (None, str(self.email).encode(), "text/plain")))

        if not isinstance(self.is_active, Unset):
            files.append(("is_active", (None, str(self.is_active).encode(), "text/plain")))

        if not isinstance(self.is_superuser, Unset):
            files.append(("is_superuser", (None, str(self.is_superuser).encode(), "text/plain")))

        if not isinstance(self.password, Unset):
            files.append(("password", (None, str(self.password).encode(), "text/plain")))

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

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        email = d.pop("email", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_superuser = d.pop("is_superuser", UNSET)

        password = d.pop("password", UNSET)

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

        patched_user_request = cls(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_active=is_active,
            is_superuser=is_superuser,
            password=password,
            configuration_permissions=configuration_permissions,
        )

        patched_user_request.additional_properties = d
        return patched_user_request

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
