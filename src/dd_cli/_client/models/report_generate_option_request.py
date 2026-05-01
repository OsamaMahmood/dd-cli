from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportGenerateOptionRequest")


@_attrs_define
class ReportGenerateOptionRequest:
    """
    Attributes:
        include_finding_notes (bool | Unset):  Default: False.
        include_finding_images (bool | Unset):  Default: False.
        include_executive_summary (bool | Unset):  Default: False.
        include_table_of_contents (bool | Unset):  Default: False.
    """

    include_finding_notes: bool | Unset = False
    include_finding_images: bool | Unset = False
    include_executive_summary: bool | Unset = False
    include_table_of_contents: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        include_finding_notes = self.include_finding_notes

        include_finding_images = self.include_finding_images

        include_executive_summary = self.include_executive_summary

        include_table_of_contents = self.include_table_of_contents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include_finding_notes is not UNSET:
            field_dict["include_finding_notes"] = include_finding_notes
        if include_finding_images is not UNSET:
            field_dict["include_finding_images"] = include_finding_images
        if include_executive_summary is not UNSET:
            field_dict["include_executive_summary"] = include_executive_summary
        if include_table_of_contents is not UNSET:
            field_dict["include_table_of_contents"] = include_table_of_contents

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.include_finding_notes, Unset):
            files.append(
                (
                    "include_finding_notes",
                    (None, str(self.include_finding_notes).encode(), "text/plain"),
                )
            )

        if not isinstance(self.include_finding_images, Unset):
            files.append(
                (
                    "include_finding_images",
                    (None, str(self.include_finding_images).encode(), "text/plain"),
                )
            )

        if not isinstance(self.include_executive_summary, Unset):
            files.append(
                (
                    "include_executive_summary",
                    (None, str(self.include_executive_summary).encode(), "text/plain"),
                )
            )

        if not isinstance(self.include_table_of_contents, Unset):
            files.append(
                (
                    "include_table_of_contents",
                    (None, str(self.include_table_of_contents).encode(), "text/plain"),
                )
            )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        include_finding_notes = d.pop("include_finding_notes", UNSET)

        include_finding_images = d.pop("include_finding_images", UNSET)

        include_executive_summary = d.pop("include_executive_summary", UNSET)

        include_table_of_contents = d.pop("include_table_of_contents", UNSET)

        report_generate_option_request = cls(
            include_finding_notes=include_finding_notes,
            include_finding_images=include_finding_images,
            include_executive_summary=include_executive_summary,
            include_table_of_contents=include_table_of_contents,
        )

        report_generate_option_request.additional_properties = d
        return report_generate_option_request

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
