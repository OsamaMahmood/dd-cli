from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.severity_status_statistics import SeverityStatusStatistics


T = TypeVar("T", bound="DeltaStatistics")


@_attrs_define
class DeltaStatistics:
    """
    Attributes:
        created (SeverityStatusStatistics):
        closed (SeverityStatusStatistics):
        reactivated (SeverityStatusStatistics):
        untouched (SeverityStatusStatistics):
    """

    created: SeverityStatusStatistics
    closed: SeverityStatusStatistics
    reactivated: SeverityStatusStatistics
    untouched: SeverityStatusStatistics
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created.to_dict()

        closed = self.closed.to_dict()

        reactivated = self.reactivated.to_dict()

        untouched = self.untouched.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "closed": closed,
                "reactivated": reactivated,
                "untouched": untouched,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.severity_status_statistics import SeverityStatusStatistics

        d = dict(src_dict)
        created = SeverityStatusStatistics.from_dict(d.pop("created"))

        closed = SeverityStatusStatistics.from_dict(d.pop("closed"))

        reactivated = SeverityStatusStatistics.from_dict(d.pop("reactivated"))

        untouched = SeverityStatusStatistics.from_dict(d.pop("untouched"))

        delta_statistics = cls(
            created=created,
            closed=closed,
            reactivated=reactivated,
            untouched=untouched,
        )

        delta_statistics.additional_properties = d
        return delta_statistics

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
