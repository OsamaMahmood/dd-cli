from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.note_history import NoteHistory
    from ..models.note_type import NoteType
    from ..models.user_stub import UserStub


T = TypeVar("T", bound="Note")


@_attrs_define
class Note:
    """
    Attributes:
        id (int):
        author (UserStub):
        editor (None | UserStub):
        history (list[NoteHistory]):
        note_type (NoteType):
        entry (str):
        date (datetime.datetime):
        edit_time (datetime.datetime | None):
        private (bool | Unset):
        edited (bool | Unset):
    """

    id: int
    author: UserStub
    editor: None | UserStub
    history: list[NoteHistory]
    note_type: NoteType
    entry: str
    date: datetime.datetime
    edit_time: datetime.datetime | None
    private: bool | Unset = UNSET
    edited: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_stub import UserStub

        id = self.id

        author = self.author.to_dict()

        editor: dict[str, Any] | None
        if isinstance(self.editor, UserStub):
            editor = self.editor.to_dict()
        else:
            editor = self.editor

        history = []
        for history_item_data in self.history:
            history_item = history_item_data.to_dict()
            history.append(history_item)

        note_type = self.note_type.to_dict()

        entry = self.entry

        date = self.date.isoformat()

        edit_time: None | str
        if isinstance(self.edit_time, datetime.datetime):
            edit_time = self.edit_time.isoformat()
        else:
            edit_time = self.edit_time

        private = self.private

        edited = self.edited

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "author": author,
                "editor": editor,
                "history": history,
                "note_type": note_type,
                "entry": entry,
                "date": date,
                "edit_time": edit_time,
            }
        )
        if private is not UNSET:
            field_dict["private"] = private
        if edited is not UNSET:
            field_dict["edited"] = edited

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.note_history import NoteHistory
        from ..models.note_type import NoteType
        from ..models.user_stub import UserStub

        d = dict(src_dict)
        id = d.pop("id")

        author = UserStub.from_dict(d.pop("author"))

        def _parse_editor(data: object) -> None | UserStub:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                editor_type_1 = UserStub.from_dict(data)

                return editor_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UserStub, data)

        editor = _parse_editor(d.pop("editor"))

        history = []
        _history = d.pop("history")
        for history_item_data in _history:
            history_item = NoteHistory.from_dict(history_item_data)

            history.append(history_item)

        note_type = NoteType.from_dict(d.pop("note_type"))

        entry = d.pop("entry")

        date = isoparse(d.pop("date"))

        def _parse_edit_time(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                edit_time_type_0 = isoparse(data)

                return edit_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        edit_time = _parse_edit_time(d.pop("edit_time"))

        private = d.pop("private", UNSET)

        edited = d.pop("edited", UNSET)

        note = cls(
            id=id,
            author=author,
            editor=editor,
            history=history,
            note_type=note_type,
            entry=entry,
            date=date,
            edit_time=edit_time,
            private=private,
            edited=edited,
        )

        note.additional_properties = d
        return note

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
