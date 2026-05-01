from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delta_statistics import DeltaStatistics
    from ..models.severity_status_statistics import SeverityStatusStatistics


T = TypeVar("T", bound="ImportStatistics")


@_attrs_define
class ImportStatistics:
    """
    Attributes:
        after (SeverityStatusStatistics):
        before (SeverityStatusStatistics | Unset):
        delta (DeltaStatistics | Unset):
    """

    after: SeverityStatusStatistics
    before: SeverityStatusStatistics | Unset = UNSET
    delta: DeltaStatistics | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        after = self.after.to_dict()

        before: dict[str, Any] | Unset = UNSET
        if not isinstance(self.before, Unset):
            before = self.before.to_dict()

        delta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delta, Unset):
            delta = self.delta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "after": after,
            }
        )
        if before is not UNSET:
            field_dict["before"] = before
        if delta is not UNSET:
            field_dict["delta"] = delta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delta_statistics import DeltaStatistics
        from ..models.severity_status_statistics import SeverityStatusStatistics

        d = dict(src_dict)
        after = SeverityStatusStatistics.from_dict(d.pop("after"))

        _before = d.pop("before", UNSET)
        before: SeverityStatusStatistics | Unset
        if isinstance(_before, Unset):
            before = UNSET
        else:
            before = SeverityStatusStatistics.from_dict(_before)

        _delta = d.pop("delta", UNSET)
        delta: DeltaStatistics | Unset
        if isinstance(_delta, Unset):
            delta = UNSET
        else:
            delta = DeltaStatistics.from_dict(_delta)

        import_statistics = cls(
            after=after,
            before=before,
            delta=delta,
        )

        import_statistics.additional_properties = d
        return import_statistics

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
