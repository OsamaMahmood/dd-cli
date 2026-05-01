from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="NoteRequest")


@_attrs_define
class NoteRequest:
    """
    Attributes:
        entry (str):
        private (bool | Unset):
        edited (bool | Unset):
    """

    entry: str
    private: bool | Unset = UNSET
    edited: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entry = self.entry

        private = self.private

        edited = self.edited

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entry": entry,
            }
        )
        if private is not UNSET:
            field_dict["private"] = private
        if edited is not UNSET:
            field_dict["edited"] = edited

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("entry", (None, str(self.entry).encode(), "text/plain")))

        if not isinstance(self.private, Unset):
            files.append(("private", (None, str(self.private).encode(), "text/plain")))

        if not isinstance(self.edited, Unset):
            files.append(("edited", (None, str(self.edited).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entry = d.pop("entry")

        private = d.pop("private", UNSET)

        edited = d.pop("edited", UNSET)

        note_request = cls(
            entry=entry,
            private=private,
            edited=edited,
        )

        note_request.additional_properties = d
        return note_request

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
