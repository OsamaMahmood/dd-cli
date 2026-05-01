from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.global_role_prefetch import GlobalRolePrefetch


T = TypeVar("T", bound="GlobalRole")


@_attrs_define
class GlobalRole:
    """
    Attributes:
        id (int):
        user (int | None | Unset):
        group (int | None | Unset):
        role (int | None | Unset): The global role will be applied to all product types and products.
        prefetch (GlobalRolePrefetch | Unset):
    """

    id: int
    user: int | None | Unset = UNSET
    group: int | None | Unset = UNSET
    role: int | None | Unset = UNSET
    prefetch: GlobalRolePrefetch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

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

        prefetch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prefetch, Unset):
            prefetch = self.prefetch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user
        if group is not UNSET:
            field_dict["group"] = group
        if role is not UNSET:
            field_dict["role"] = role
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.global_role_prefetch import GlobalRolePrefetch

        d = dict(src_dict)
        id = d.pop("id")

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

        _prefetch = d.pop("prefetch", UNSET)
        prefetch: GlobalRolePrefetch | Unset
        if isinstance(_prefetch, Unset):
            prefetch = UNSET
        else:
            prefetch = GlobalRolePrefetch.from_dict(_prefetch)

        global_role = cls(
            id=id,
            user=user,
            group=group,
            role=role,
            prefetch=prefetch,
        )

        global_role.additional_properties = d
        return global_role

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
