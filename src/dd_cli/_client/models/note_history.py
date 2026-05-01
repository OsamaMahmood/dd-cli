from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.note_type import NoteType
    from ..models.user_stub import UserStub


T = TypeVar("T", bound="NoteHistory")


@_attrs_define
class NoteHistory:
    """
    Attributes:
        id (int):
        current_editor (UserStub):
        note_type (NoteType):
        data (str):
        time (datetime.datetime | None):
    """

    id: int
    current_editor: UserStub
    note_type: NoteType
    data: str
    time: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        current_editor = self.current_editor.to_dict()

        note_type = self.note_type.to_dict()

        data = self.data

        time: None | str
        if isinstance(self.time, datetime.datetime):
            time = self.time.isoformat()
        else:
            time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "current_editor": current_editor,
                "note_type": note_type,
                "data": data,
                "time": time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.note_type import NoteType
        from ..models.user_stub import UserStub

        d = dict(src_dict)
        id = d.pop("id")

        current_editor = UserStub.from_dict(d.pop("current_editor"))

        note_type = NoteType.from_dict(d.pop("note_type"))

        data = d.pop("data")

        def _parse_time(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_type_0 = isoparse(data)

                return time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        time = _parse_time(d.pop("time"))

        note_history = cls(
            id=id,
            current_editor=current_editor,
            note_type=note_type,
            data=data,
            time=time,
        )

        note_history.additional_properties = d
        return note_history

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
