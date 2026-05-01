from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="EngagementUpdateJiraEpicRequest")


@_attrs_define
class EngagementUpdateJiraEpicRequest:
    """
    Attributes:
        epic_name (str | Unset):
        epic_priority (None | str | Unset):
    """

    epic_name: str | Unset = UNSET
    epic_priority: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        epic_name = self.epic_name

        epic_priority: None | str | Unset
        if isinstance(self.epic_priority, Unset):
            epic_priority = UNSET
        else:
            epic_priority = self.epic_priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if epic_name is not UNSET:
            field_dict["epic_name"] = epic_name
        if epic_priority is not UNSET:
            field_dict["epic_priority"] = epic_priority

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.epic_name, Unset):
            files.append(("epic_name", (None, str(self.epic_name).encode(), "text/plain")))

        if not isinstance(self.epic_priority, Unset):
            if isinstance(self.epic_priority, str):
                files.append(
                    ("epic_priority", (None, str(self.epic_priority).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("epic_priority", (None, str(self.epic_priority).encode(), "text/plain"))
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        epic_name = d.pop("epic_name", UNSET)

        def _parse_epic_priority(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        epic_priority = _parse_epic_priority(d.pop("epic_priority", UNSET))

        engagement_update_jira_epic_request = cls(
            epic_name=epic_name,
            epic_priority=epic_priority,
        )

        engagement_update_jira_epic_request.additional_properties = d
        return engagement_update_jira_epic_request

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
