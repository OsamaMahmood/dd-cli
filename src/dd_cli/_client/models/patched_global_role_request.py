from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedGlobalRoleRequest")


@_attrs_define
class PatchedGlobalRoleRequest:
    """
    Attributes:
        user (int | None | Unset):
        group (int | None | Unset):
        role (int | None | Unset): The global role will be applied to all product types and products.
    """

    user: int | None | Unset = UNSET
    group: int | None | Unset = UNSET
    role: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user: int | None | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        group: int | None | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        role: int | None | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if group is not UNSET:
            field_dict["group"] = group
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.user, Unset):
            if isinstance(self.user, int):
                files.append(("user", (None, str(self.user).encode(), "text/plain")))
            else:
                files.append(("user", (None, str(self.user).encode(), "text/plain")))

        if not isinstance(self.group, Unset):
            if isinstance(self.group, int):
                files.append(("group", (None, str(self.group).encode(), "text/plain")))
            else:
                files.append(("group", (None, str(self.group).encode(), "text/plain")))

        if not isinstance(self.role, Unset):
            if isinstance(self.role, int):
                files.append(("role", (None, str(self.role).encode(), "text/plain")))
            else:
                files.append(("role", (None, str(self.role).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_user(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user = _parse_user(d.pop("user", UNSET))

        def _parse_group(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        group = _parse_group(d.pop("group", UNSET))

        def _parse_role(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        role = _parse_role(d.pop("role", UNSET))

        patched_global_role_request = cls(
            user=user,
            group=group,
            role=role,
        )

        patched_global_role_request.additional_properties = d
        return patched_global_role_request

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
