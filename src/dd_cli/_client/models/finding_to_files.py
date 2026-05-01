from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.file import File


T = TypeVar("T", bound="FindingToFiles")


@_attrs_define
class FindingToFiles:
    """
    Attributes:
        finding_id (int | None):
        files (list[File]):
    """

    finding_id: int | None
    files: list[File]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        finding_id: int | None
        finding_id = self.finding_id

        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "finding_id": finding_id,
                "files": files,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file import File

        d = dict(src_dict)

        def _parse_finding_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        finding_id = _parse_finding_id(d.pop("finding_id"))

        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = File.from_dict(files_item_data)

            files.append(files_item)

        finding_to_files = cls(
            finding_id=finding_id,
            files=files,
        )

        finding_to_files.additional_properties = d
        return finding_to_files

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
