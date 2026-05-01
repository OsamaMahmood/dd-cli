from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="SonarqubeIssueTransition")


@_attrs_define
class SonarqubeIssueTransition:
    """
    Attributes:
        id (int):
        created (datetime.datetime):
        finding_status (str):
        sonarqube_status (str):
        transitions (str):
        sonarqube_issue (int):
    """

    id: int
    created: datetime.datetime
    finding_status: str
    sonarqube_status: str
    transitions: str
    sonarqube_issue: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created = self.created.isoformat()

        finding_status = self.finding_status

        sonarqube_status = self.sonarqube_status

        transitions = self.transitions

        sonarqube_issue = self.sonarqube_issue

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created": created,
                "finding_status": finding_status,
                "sonarqube_status": sonarqube_status,
                "transitions": transitions,
                "sonarqube_issue": sonarqube_issue,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        created = isoparse(d.pop("created"))

        finding_status = d.pop("finding_status")

        sonarqube_status = d.pop("sonarqube_status")

        transitions = d.pop("transitions")

        sonarqube_issue = d.pop("sonarqube_issue")

        sonarqube_issue_transition = cls(
            id=id,
            created=created,
            finding_status=finding_status,
            sonarqube_status=sonarqube_status,
            transitions=transitions,
            sonarqube_issue=sonarqube_issue,
        )

        sonarqube_issue_transition.additional_properties = d
        return sonarqube_issue_transition

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
