from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.note import Note


T = TypeVar("T", bound="EngagementToNotes")


@_attrs_define
class EngagementToNotes:
    """
    Attributes:
        engagement_id (int | None):
        notes (list[Note]):
    """

    engagement_id: int | None
    notes: list[Note]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        engagement_id: int | None
        engagement_id = self.engagement_id

        notes = []
        for notes_item_data in self.notes:
            notes_item = notes_item_data.to_dict()
            notes.append(notes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "engagement_id": engagement_id,
                "notes": notes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.note import Note

        d = dict(src_dict)

        def _parse_engagement_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        engagement_id = _parse_engagement_id(d.pop("engagement_id"))

        notes = []
        _notes = d.pop("notes")
        for notes_item_data in _notes:
            notes_item = Note.from_dict(notes_item_data)

            notes.append(notes_item)

        engagement_to_notes = cls(
            engagement_id=engagement_id,
            notes=notes,
        )

        engagement_to_notes.additional_properties = d
        return engagement_to_notes

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
