from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedEndpointStatusRequest")


@_attrs_define
class PatchedEndpointStatusRequest:
    """
    Attributes:
        date (datetime.date | Unset):
        mitigated (bool | Unset):
        false_positive (bool | Unset):
        out_of_scope (bool | Unset):
        risk_accepted (bool | Unset):
        mitigated_by (int | None | Unset):
        endpoint (int | Unset):
        finding (int | Unset):
    """

    date: datetime.date | Unset = UNSET
    mitigated: bool | Unset = UNSET
    false_positive: bool | Unset = UNSET
    out_of_scope: bool | Unset = UNSET
    risk_accepted: bool | Unset = UNSET
    mitigated_by: int | None | Unset = UNSET
    endpoint: int | Unset = UNSET
    finding: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        endpoint = self.endpoint

        finding = self.finding

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if finding is not UNSET:
            field_dict["finding"] = finding

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.date, Unset):
            files.append(("date", (None, self.date.isoformat().encode(), "text/plain")))

        if not isinstance(self.mitigated, Unset):
            files.append(("mitigated", (None, str(self.mitigated).encode(), "text/plain")))

        if not isinstance(self.false_positive, Unset):
            files.append(
                ("false_positive", (None, str(self.false_positive).encode(), "text/plain"))
            )

        if not isinstance(self.out_of_scope, Unset):
            files.append(("out_of_scope", (None, str(self.out_of_scope).encode(), "text/plain")))

        if not isinstance(self.risk_accepted, Unset):
            files.append(("risk_accepted", (None, str(self.risk_accepted).encode(), "text/plain")))

        if not isinstance(self.mitigated_by, Unset):
            if isinstance(self.mitigated_by, int):
                files.append(
                    ("mitigated_by", (None, str(self.mitigated_by).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("mitigated_by", (None, str(self.mitigated_by).encode(), "text/plain"))
                )

        if not isinstance(self.endpoint, Unset):
            files.append(("endpoint", (None, str(self.endpoint).encode(), "text/plain")))

        if not isinstance(self.finding, Unset):
            files.append(("finding", (None, str(self.finding).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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

        endpoint = d.pop("endpoint", UNSET)

        finding = d.pop("finding", UNSET)

        patched_endpoint_status_request = cls(
            date=date,
            mitigated=mitigated,
            false_positive=false_positive,
            out_of_scope=out_of_scope,
            risk_accepted=risk_accepted,
            mitigated_by=mitigated_by,
            endpoint=endpoint,
            finding=finding,
        )

        patched_endpoint_status_request.additional_properties = d
        return patched_endpoint_status_request

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
