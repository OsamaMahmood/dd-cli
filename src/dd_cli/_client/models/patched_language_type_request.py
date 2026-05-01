from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedLanguageTypeRequest")


@_attrs_define
class PatchedLanguageTypeRequest:
    """
    Attributes:
        language (str | Unset):
        color (None | str | Unset):
    """

    language: str | Unset = UNSET
    color: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        language = self.language

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if language is not UNSET:
            field_dict["language"] = language
        if color is not UNSET:
            field_dict["color"] = color

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.language, Unset):
            files.append(("language", (None, str(self.language).encode(), "text/plain")))

        if not isinstance(self.color, Unset):
            if isinstance(self.color, str):
                files.append(("color", (None, str(self.color).encode(), "text/plain")))
            else:
                files.append(("color", (None, str(self.color).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        language = d.pop("language", UNSET)

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        patched_language_type_request = cls(
            language=language,
            color=color,
        )

        patched_language_type_request.additional_properties = d
        return patched_language_type_request

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
