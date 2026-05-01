from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddNewNoteOptionRequest")


@_attrs_define
class AddNewNoteOptionRequest:
    """
    Attributes:
        entry (str):
        private (bool | Unset):
        note_type (int | None | Unset):
    """

    entry: str
    private: bool | Unset = UNSET
    note_type: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entry = self.entry

        private = self.private

        note_type: int | None | Unset
        if isinstance(self.note_type, Unset):
            note_type = UNSET
        else:
            note_type = self.note_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entry": entry,
            }
        )
        if private is not UNSET:
            field_dict["private"] = private
        if note_type is not UNSET:
            field_dict["note_type"] = note_type

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("entry", (None, str(self.entry).encode(), "text/plain")))

        if not isinstance(self.private, Unset):
            files.append(("private", (None, str(self.private).encode(), "text/plain")))

        if not isinstance(self.note_type, Unset):
            if isinstance(self.note_type, int):
                files.append(("note_type", (None, str(self.note_type).encode(), "text/plain")))
            else:
                files.append(("note_type", (None, str(self.note_type).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entry = d.pop("entry")

        private = d.pop("private", UNSET)

        def _parse_note_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        note_type = _parse_note_type(d.pop("note_type", UNSET))

        add_new_note_option_request = cls(
            entry=entry,
            private=private,
            note_type=note_type,
        )

        add_new_note_option_request.additional_properties = d
        return add_new_note_option_request

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
