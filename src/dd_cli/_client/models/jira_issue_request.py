from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="JIRAIssueRequest")


@_attrs_define
class JIRAIssueRequest:
    """
    Attributes:
        jira_id (str):
        jira_key (str):
        jira_creation (datetime.datetime | None | Unset): The date a Jira issue was created from this finding.
        jira_change (datetime.datetime | None | Unset): The date the linked Jira issue was last modified.
        jira_project (int | None | Unset):
        finding (int | None | Unset):
        engagement (int | None | Unset):
        finding_group (int | None | Unset):
    """

    jira_id: str
    jira_key: str
    jira_creation: datetime.datetime | None | Unset = UNSET
    jira_change: datetime.datetime | None | Unset = UNSET
    jira_project: int | None | Unset = UNSET
    finding: int | None | Unset = UNSET
    engagement: int | None | Unset = UNSET
    finding_group: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        jira_id = self.jira_id

        jira_key = self.jira_key

        jira_creation: None | str | Unset
        if isinstance(self.jira_creation, Unset):
            jira_creation = UNSET
        elif isinstance(self.jira_creation, datetime.datetime):
            jira_creation = self.jira_creation.isoformat()
        else:
            jira_creation = self.jira_creation

        jira_change: None | str | Unset
        if isinstance(self.jira_change, Unset):
            jira_change = UNSET
        elif isinstance(self.jira_change, datetime.datetime):
            jira_change = self.jira_change.isoformat()
        else:
            jira_change = self.jira_change

        jira_project: int | None | Unset
        if isinstance(self.jira_project, Unset):
            jira_project = UNSET
        else:
            jira_project = self.jira_project

        finding: int | None | Unset
        if isinstance(self.finding, Unset):
            finding = UNSET
        else:
            finding = self.finding

        engagement: int | None | Unset
        if isinstance(self.engagement, Unset):
            engagement = UNSET
        else:
            engagement = self.engagement

        finding_group: int | None | Unset
        if isinstance(self.finding_group, Unset):
            finding_group = UNSET
        else:
            finding_group = self.finding_group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jira_id": jira_id,
                "jira_key": jira_key,
            }
        )
        if jira_creation is not UNSET:
            field_dict["jira_creation"] = jira_creation
        if jira_change is not UNSET:
            field_dict["jira_change"] = jira_change
        if jira_project is not UNSET:
            field_dict["jira_project"] = jira_project
        if finding is not UNSET:
            field_dict["finding"] = finding
        if engagement is not UNSET:
            field_dict["engagement"] = engagement
        if finding_group is not UNSET:
            field_dict["finding_group"] = finding_group

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("jira_id", (None, str(self.jira_id).encode(), "text/plain")))

        files.append(("jira_key", (None, str(self.jira_key).encode(), "text/plain")))

        if not isinstance(self.jira_creation, Unset):
            if isinstance(self.jira_creation, datetime.datetime):
                files.append(
                    ("jira_creation", (None, self.jira_creation.isoformat().encode(), "text/plain"))
                )
            else:
                files.append(
                    ("jira_creation", (None, str(self.jira_creation).encode(), "text/plain"))
                )

        if not isinstance(self.jira_change, Unset):
            if isinstance(self.jira_change, datetime.datetime):
                files.append(
                    ("jira_change", (None, self.jira_change.isoformat().encode(), "text/plain"))
                )
            else:
                files.append(("jira_change", (None, str(self.jira_change).encode(), "text/plain")))

        if not isinstance(self.jira_project, Unset):
            if isinstance(self.jira_project, int):
                files.append(
                    ("jira_project", (None, str(self.jira_project).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("jira_project", (None, str(self.jira_project).encode(), "text/plain"))
                )

        if not isinstance(self.finding, Unset):
            if isinstance(self.finding, int):
                files.append(("finding", (None, str(self.finding).encode(), "text/plain")))
            else:
                files.append(("finding", (None, str(self.finding).encode(), "text/plain")))

        if not isinstance(self.engagement, Unset):
            if isinstance(self.engagement, int):
                files.append(("engagement", (None, str(self.engagement).encode(), "text/plain")))
            else:
                files.append(("engagement", (None, str(self.engagement).encode(), "text/plain")))

        if not isinstance(self.finding_group, Unset):
            if isinstance(self.finding_group, int):
                files.append(
                    ("finding_group", (None, str(self.finding_group).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("finding_group", (None, str(self.finding_group).encode(), "text/plain"))
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        jira_id = d.pop("jira_id")

        jira_key = d.pop("jira_key")

        def _parse_jira_creation(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                jira_creation_type_0 = isoparse(data)

                return jira_creation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        jira_creation = _parse_jira_creation(d.pop("jira_creation", UNSET))

        def _parse_jira_change(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                jira_change_type_0 = isoparse(data)

                return jira_change_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        jira_change = _parse_jira_change(d.pop("jira_change", UNSET))

        def _parse_jira_project(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        jira_project = _parse_jira_project(d.pop("jira_project", UNSET))

        def _parse_finding(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        finding = _parse_finding(d.pop("finding", UNSET))

        def _parse_engagement(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        engagement = _parse_engagement(d.pop("engagement", UNSET))

        def _parse_finding_group(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        finding_group = _parse_finding_group(d.pop("finding_group", UNSET))

        jira_issue_request = cls(
            jira_id=jira_id,
            jira_key=jira_key,
            jira_creation=jira_creation,
            jira_change=jira_change,
            jira_project=jira_project,
            finding=finding,
            engagement=engagement,
            finding_group=finding_group,
        )

        jira_issue_request.additional_properties = d
        return jira_issue_request

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
