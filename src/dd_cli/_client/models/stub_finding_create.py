from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="StubFindingCreate")


@_attrs_define
class StubFindingCreate:
    """
    Attributes:
        id (int):
        test (int):
        title (str):
        reporter (int):
        date (datetime.date | Unset):
        severity (None | str | Unset):
        description (None | str | Unset):
    """

    id: int
    test: int
    title: str
    reporter: int
    date: datetime.date | Unset = UNSET
    severity: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        test = self.test

        title = self.title

        reporter = self.reporter

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        severity: None | str | Unset
        if isinstance(self.severity, Unset):
            severity = UNSET
        else:
            severity = self.severity

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "test": test,
                "title": title,
                "reporter": reporter,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if severity is not UNSET:
            field_dict["severity"] = severity
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        test = d.pop("test")

        title = d.pop("title")

        reporter = d.pop("reporter")

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        def _parse_severity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        severity = _parse_severity(d.pop("severity", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        stub_finding_create = cls(
            id=id,
            test=test,
            title=title,
            reporter=reporter,
            date=date,
            severity=severity,
            description=description,
        )

        stub_finding_create.additional_properties = d
        return stub_finding_create

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
