from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StatusStatistics")


@_attrs_define
class StatusStatistics:
    """
    Attributes:
        active (int):
        verified (int):
        duplicate (int):
        false_p (int):
        out_of_scope (int):
        is_mitigated (int):
        risk_accepted (int):
        total (int):
    """

    active: int
    verified: int
    duplicate: int
    false_p: int
    out_of_scope: int
    is_mitigated: int
    risk_accepted: int
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        verified = self.verified

        duplicate = self.duplicate

        false_p = self.false_p

        out_of_scope = self.out_of_scope

        is_mitigated = self.is_mitigated

        risk_accepted = self.risk_accepted

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "verified": verified,
                "duplicate": duplicate,
                "false_p": false_p,
                "out_of_scope": out_of_scope,
                "is_mitigated": is_mitigated,
                "risk_accepted": risk_accepted,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active")

        verified = d.pop("verified")

        duplicate = d.pop("duplicate")

        false_p = d.pop("false_p")

        out_of_scope = d.pop("out_of_scope")

        is_mitigated = d.pop("is_mitigated")

        risk_accepted = d.pop("risk_accepted")

        total = d.pop("total")

        status_statistics = cls(
            active=active,
            verified=verified,
            duplicate=duplicate,
            false_p=false_p,
            out_of_scope=out_of_scope,
            is_mitigated=is_mitigated,
            risk_accepted=risk_accepted,
            total=total,
        )

        status_statistics.additional_properties = d
        return status_statistics

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
