from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ExecutiveSummary")


@_attrs_define
class ExecutiveSummary:
    """
    Attributes:
        engagement_name (str):
        engagement_target_start (datetime.date):
        engagement_target_end (datetime.date):
        test_type_name (str):
        test_target_start (datetime.datetime):
        test_target_end (datetime.datetime):
        test_environment_name (str):
        test_strategy_ref (str):
        total_findings (int):
    """

    engagement_name: str
    engagement_target_start: datetime.date
    engagement_target_end: datetime.date
    test_type_name: str
    test_target_start: datetime.datetime
    test_target_end: datetime.datetime
    test_environment_name: str
    test_strategy_ref: str
    total_findings: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        engagement_name = self.engagement_name

        engagement_target_start = self.engagement_target_start.isoformat()

        engagement_target_end = self.engagement_target_end.isoformat()

        test_type_name = self.test_type_name

        test_target_start = self.test_target_start.isoformat()

        test_target_end = self.test_target_end.isoformat()

        test_environment_name = self.test_environment_name

        test_strategy_ref = self.test_strategy_ref

        total_findings = self.total_findings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "engagement_name": engagement_name,
                "engagement_target_start": engagement_target_start,
                "engagement_target_end": engagement_target_end,
                "test_type_name": test_type_name,
                "test_target_start": test_target_start,
                "test_target_end": test_target_end,
                "test_environment_name": test_environment_name,
                "test_strategy_ref": test_strategy_ref,
                "total_findings": total_findings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        engagement_name = d.pop("engagement_name")

        engagement_target_start = isoparse(d.pop("engagement_target_start")).date()

        engagement_target_end = isoparse(d.pop("engagement_target_end")).date()

        test_type_name = d.pop("test_type_name")

        test_target_start = isoparse(d.pop("test_target_start"))

        test_target_end = isoparse(d.pop("test_target_end"))

        test_environment_name = d.pop("test_environment_name")

        test_strategy_ref = d.pop("test_strategy_ref")

        total_findings = d.pop("total_findings")

        executive_summary = cls(
            engagement_name=engagement_name,
            engagement_target_start=engagement_target_start,
            engagement_target_end=engagement_target_end,
            test_type_name=test_type_name,
            test_target_start=test_target_start,
            test_target_end=test_target_end,
            test_environment_name=test_environment_name,
            test_strategy_ref=test_strategy_ref,
            total_findings=total_findings,
        )

        executive_summary.additional_properties = d
        return executive_summary

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
