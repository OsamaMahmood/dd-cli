from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="FindingCloseRequest")


@_attrs_define
class FindingCloseRequest:
    """
    Attributes:
        is_mitigated (bool | Unset):
        mitigated (datetime.datetime | Unset):
        false_p (bool | Unset):
        out_of_scope (bool | Unset):
        duplicate (bool | Unset):
        mitigated_by (int | None | Unset):
        note (str | Unset):
        note_type (int | None | Unset):
    """

    is_mitigated: bool | Unset = UNSET
    mitigated: datetime.datetime | Unset = UNSET
    false_p: bool | Unset = UNSET
    out_of_scope: bool | Unset = UNSET
    duplicate: bool | Unset = UNSET
    mitigated_by: int | None | Unset = UNSET
    note: str | Unset = UNSET
    note_type: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_mitigated = self.is_mitigated

        mitigated: str | Unset = UNSET
        if not isinstance(self.mitigated, Unset):
            mitigated = self.mitigated.isoformat()

        false_p = self.false_p

        out_of_scope = self.out_of_scope

        duplicate = self.duplicate

        mitigated_by: int | None | Unset
        if isinstance(self.mitigated_by, Unset):
            mitigated_by = UNSET
        else:
            mitigated_by = self.mitigated_by

        note = self.note

        note_type: int | None | Unset
        if isinstance(self.note_type, Unset):
            note_type = UNSET
        else:
            note_type = self.note_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_mitigated is not UNSET:
            field_dict["is_mitigated"] = is_mitigated
        if mitigated is not UNSET:
            field_dict["mitigated"] = mitigated
        if false_p is not UNSET:
            field_dict["false_p"] = false_p
        if out_of_scope is not UNSET:
            field_dict["out_of_scope"] = out_of_scope
        if duplicate is not UNSET:
            field_dict["duplicate"] = duplicate
        if mitigated_by is not UNSET:
            field_dict["mitigated_by"] = mitigated_by
        if note is not UNSET:
            field_dict["note"] = note
        if note_type is not UNSET:
            field_dict["note_type"] = note_type

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.is_mitigated, Unset):
            files.append(("is_mitigated", (None, str(self.is_mitigated).encode(), "text/plain")))

        if not isinstance(self.mitigated, Unset):
            files.append(("mitigated", (None, self.mitigated.isoformat().encode(), "text/plain")))

        if not isinstance(self.false_p, Unset):
            files.append(("false_p", (None, str(self.false_p).encode(), "text/plain")))

        if not isinstance(self.out_of_scope, Unset):
            files.append(("out_of_scope", (None, str(self.out_of_scope).encode(), "text/plain")))

        if not isinstance(self.duplicate, Unset):
            files.append(("duplicate", (None, str(self.duplicate).encode(), "text/plain")))

        if not isinstance(self.mitigated_by, Unset):
            if isinstance(self.mitigated_by, int):
                files.append(
                    ("mitigated_by", (None, str(self.mitigated_by).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("mitigated_by", (None, str(self.mitigated_by).encode(), "text/plain"))
                )

        if not isinstance(self.note, Unset):
            files.append(("note", (None, str(self.note).encode(), "text/plain")))

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
        is_mitigated = d.pop("is_mitigated", UNSET)

        _mitigated = d.pop("mitigated", UNSET)
        mitigated: datetime.datetime | Unset
        if isinstance(_mitigated, Unset):
            mitigated = UNSET
        else:
            mitigated = isoparse(_mitigated)

        false_p = d.pop("false_p", UNSET)

        out_of_scope = d.pop("out_of_scope", UNSET)

        duplicate = d.pop("duplicate", UNSET)

        def _parse_mitigated_by(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        mitigated_by = _parse_mitigated_by(d.pop("mitigated_by", UNSET))

        note = d.pop("note", UNSET)

        def _parse_note_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        note_type = _parse_note_type(d.pop("note_type", UNSET))

        finding_close_request = cls(
            is_mitigated=is_mitigated,
            mitigated=mitigated,
            false_p=false_p,
            out_of_scope=out_of_scope,
            duplicate=duplicate,
            mitigated_by=mitigated_by,
            note=note,
            note_type=note_type,
        )

        finding_close_request.additional_properties = d
        return finding_close_request

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
