from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EndpointStatus")


@_attrs_define
class EndpointStatus:
    """
    Attributes:
        id (int):
        last_modified (datetime.datetime | None):
        mitigated_time (datetime.datetime | None):
        endpoint (int):
        finding (int):
        date (datetime.date | Unset):
        mitigated (bool | Unset):
        false_positive (bool | Unset):
        out_of_scope (bool | Unset):
        risk_accepted (bool | Unset):
        mitigated_by (int | None | Unset):
    """

    id: int
    last_modified: datetime.datetime | None
    mitigated_time: datetime.datetime | None
    endpoint: int
    finding: int
    date: datetime.date | Unset = UNSET
    mitigated: bool | Unset = UNSET
    false_positive: bool | Unset = UNSET
    out_of_scope: bool | Unset = UNSET
    risk_accepted: bool | Unset = UNSET
    mitigated_by: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        last_modified: None | str
        if isinstance(self.last_modified, datetime.datetime):
            last_modified = self.last_modified.isoformat()
        else:
            last_modified = self.last_modified

        mitigated_time: None | str
        if isinstance(self.mitigated_time, datetime.datetime):
            mitigated_time = self.mitigated_time.isoformat()
        else:
            mitigated_time = self.mitigated_time

        endpoint = self.endpoint

        finding = self.finding

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        mitigated = self.mitigated

        false_positive = self.false_positive

        out_of_scope = self.out_of_scope

        risk_accepted = self.risk_accepted

        mitigated_by: int | None | Unset
        if isinstance(self.mitigated_by, Unset):
            mitigated_by = UNSET
        else:
            mitigated_by = self.mitigated_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "last_modified": last_modified,
                "mitigated_time": mitigated_time,
                "endpoint": endpoint,
                "finding": finding,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if mitigated is not UNSET:
            field_dict["mitigated"] = mitigated
        if false_positive is not UNSET:
            field_dict["false_positive"] = false_positive
        if out_of_scope is not UNSET:
            field_dict["out_of_scope"] = out_of_scope
        if risk_accepted is not UNSET:
            field_dict["risk_accepted"] = risk_accepted
        if mitigated_by is not UNSET:
            field_dict["mitigated_by"] = mitigated_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_last_modified(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_modified_type_0 = isoparse(data)

                return last_modified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_modified = _parse_last_modified(d.pop("last_modified"))

        def _parse_mitigated_time(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mitigated_time_type_0 = isoparse(data)

                return mitigated_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        mitigated_time = _parse_mitigated_time(d.pop("mitigated_time"))

        endpoint = d.pop("endpoint")

        finding = d.pop("finding")

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        mitigated = d.pop("mitigated", UNSET)

        false_positive = d.pop("false_positive", UNSET)

        out_of_scope = d.pop("out_of_scope", UNSET)

        risk_accepted = d.pop("risk_accepted", UNSET)

        def _parse_mitigated_by(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        mitigated_by = _parse_mitigated_by(d.pop("mitigated_by", UNSET))

        endpoint_status = cls(
            id=id,
            last_modified=last_modified,
            mitigated_time=mitigated_time,
            endpoint=endpoint,
            finding=finding,
            date=date,
            mitigated=mitigated,
            false_positive=false_positive,
            out_of_scope=out_of_scope,
            risk_accepted=risk_accepted,
            mitigated_by=mitigated_by,
        )

        endpoint_status.additional_properties = d
        return endpoint_status

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
