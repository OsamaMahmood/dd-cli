from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.status_statistics_request import StatusStatisticsRequest


T = TypeVar("T", bound="SeverityStatusStatisticsRequest")


@_attrs_define
class SeverityStatusStatisticsRequest:
    """
    Attributes:
        info (StatusStatisticsRequest):
        low (StatusStatisticsRequest):
        medium (StatusStatisticsRequest):
        high (StatusStatisticsRequest):
        critical (StatusStatisticsRequest):
        total (StatusStatisticsRequest):
    """

    info: StatusStatisticsRequest
    low: StatusStatisticsRequest
    medium: StatusStatisticsRequest
    high: StatusStatisticsRequest
    critical: StatusStatisticsRequest
    total: StatusStatisticsRequest
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
        from ..models.status_statistics_request import StatusStatisticsRequest

        d = dict(src_dict)
        info = StatusStatisticsRequest.from_dict(d.pop("info"))

        low = StatusStatisticsRequest.from_dict(d.pop("low"))

        medium = StatusStatisticsRequest.from_dict(d.pop("medium"))

        high = StatusStatisticsRequest.from_dict(d.pop("high"))

        critical = StatusStatisticsRequest.from_dict(d.pop("critical"))

        total = StatusStatisticsRequest.from_dict(d.pop("total"))

        severity_status_statistics_request = cls(
            info=info,
            low=low,
            medium=medium,
            high=high,
            critical=critical,
            total=total,
        )

        severity_status_statistics_request.additional_properties = d
        return severity_status_statistics_request

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
