from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedSonarqubeIssueTransitionRequest")


@_attrs_define
class PatchedSonarqubeIssueTransitionRequest:
    """
    Attributes:
        finding_status (str | Unset):
        sonarqube_status (str | Unset):
        transitions (str | Unset):
        sonarqube_issue (int | Unset):
    """

    finding_status: str | Unset = UNSET
    sonarqube_status: str | Unset = UNSET
    transitions: str | Unset = UNSET
    sonarqube_issue: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        finding_status = self.finding_status

        sonarqube_status = self.sonarqube_status

        transitions = self.transitions

        sonarqube_issue = self.sonarqube_issue

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if finding_status is not UNSET:
            field_dict["finding_status"] = finding_status
        if sonarqube_status is not UNSET:
            field_dict["sonarqube_status"] = sonarqube_status
        if transitions is not UNSET:
            field_dict["transitions"] = transitions
        if sonarqube_issue is not UNSET:
            field_dict["sonarqube_issue"] = sonarqube_issue

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.finding_status, Unset):
            files.append(
                ("finding_status", (None, str(self.finding_status).encode(), "text/plain"))
            )

        if not isinstance(self.sonarqube_status, Unset):
            files.append(
                ("sonarqube_status", (None, str(self.sonarqube_status).encode(), "text/plain"))
            )

        if not isinstance(self.transitions, Unset):
            files.append(("transitions", (None, str(self.transitions).encode(), "text/plain")))

        if not isinstance(self.sonarqube_issue, Unset):
            files.append(
                ("sonarqube_issue", (None, str(self.sonarqube_issue).encode(), "text/plain"))
            )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        finding_status = d.pop("finding_status", UNSET)

        sonarqube_status = d.pop("sonarqube_status", UNSET)

        transitions = d.pop("transitions", UNSET)

        sonarqube_issue = d.pop("sonarqube_issue", UNSET)

        patched_sonarqube_issue_transition_request = cls(
            finding_status=finding_status,
            sonarqube_status=sonarqube_status,
            transitions=transitions,
            sonarqube_issue=sonarqube_issue,
        )

        patched_sonarqube_issue_transition_request.additional_properties = d
        return patched_sonarqube_issue_transition_request

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
