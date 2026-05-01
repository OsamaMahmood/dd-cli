from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedNoteTypeRequest")


@_attrs_define
class PatchedNoteTypeRequest:
    """
    Attributes:
        name (str | Unset):
        description (str | Unset):
        is_single (bool | Unset):
        is_active (bool | Unset):
        is_mandatory (bool | Unset):
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    is_single: bool | Unset = UNSET
    is_active: bool | Unset = UNSET
    is_mandatory: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        is_single = self.is_single

        is_active = self.is_active

        is_mandatory = self.is_mandatory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if is_single is not UNSET:
            field_dict["is_single"] = is_single
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_mandatory is not UNSET:
            field_dict["is_mandatory"] = is_mandatory

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.is_single, Unset):
            files.append(("is_single", (None, str(self.is_single).encode(), "text/plain")))

        if not isinstance(self.is_active, Unset):
            files.append(("is_active", (None, str(self.is_active).encode(), "text/plain")))

        if not isinstance(self.is_mandatory, Unset):
            files.append(("is_mandatory", (None, str(self.is_mandatory).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        is_single = d.pop("is_single", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_mandatory = d.pop("is_mandatory", UNSET)

        patched_note_type_request = cls(
            name=name,
            description=description,
            is_single=is_single,
            is_active=is_active,
            is_mandatory=is_mandatory,
        )

        patched_note_type_request.additional_properties = d
        return patched_note_type_request

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
