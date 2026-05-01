from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NoteType")


@_attrs_define
class NoteType:
    """
    Attributes:
        id (int):
        name (str):
        description (str):
        is_single (bool | Unset):
        is_active (bool | Unset):
        is_mandatory (bool | Unset):
    """

    id: int
    name: str
    description: str
    is_single: bool | Unset = UNSET
    is_active: bool | Unset = UNSET
    is_mandatory: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        is_single = self.is_single

        is_active = self.is_active

        is_mandatory = self.is_mandatory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
            }
        )
        if is_single is not UNSET:
            field_dict["is_single"] = is_single
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_mandatory is not UNSET:
            field_dict["is_mandatory"] = is_mandatory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        is_single = d.pop("is_single", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_mandatory = d.pop("is_mandatory", UNSET)

        note_type = cls(
            id=id,
            name=name,
            description=description,
            is_single=is_single,
            is_active=is_active,
            is_mandatory=is_mandatory,
        )

        note_type.additional_properties = d
        return note_type

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
