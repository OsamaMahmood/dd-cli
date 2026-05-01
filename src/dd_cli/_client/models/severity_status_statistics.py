from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.status_statistics import StatusStatistics


T = TypeVar("T", bound="SeverityStatusStatistics")


@_attrs_define
class SeverityStatusStatistics:
    """
    Attributes:
        info (StatusStatistics):
        low (StatusStatistics):
        medium (StatusStatistics):
        high (StatusStatistics):
        critical (StatusStatistics):
        total (StatusStatistics):
    """

    info: StatusStatistics
    low: StatusStatistics
    medium: StatusStatistics
    high: StatusStatistics
    critical: StatusStatistics
    total: StatusStatistics
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        info = self.info.to_dict()

        low = self.low.to_dict()

        medium = self.medium.to_dict()

        high = self.high.to_dict()

        critical = self.critical.to_dict()

        total = self.total.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "info": info,
                "low": low,
                "medium": medium,
                "high": high,
                "critical": critical,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_statistics import StatusStatistics

        d = dict(src_dict)
        info = StatusStatistics.from_dict(d.pop("info"))

        low = StatusStatistics.from_dict(d.pop("low"))

        medium = StatusStatistics.from_dict(d.pop("medium"))

        high = StatusStatistics.from_dict(d.pop("high"))

        critical = StatusStatistics.from_dict(d.pop("critical"))

        total = StatusStatistics.from_dict(d.pop("total"))

        severity_status_statistics = cls(
            info=info,
            low=low,
            medium=medium,
            high=high,
            critical=critical,
            total=total,
        )

        severity_status_statistics.additional_properties = d
        return severity_status_statistics

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
