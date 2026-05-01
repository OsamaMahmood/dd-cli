from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.jira_issue import JIRAIssue


T = TypeVar("T", bound="FindingGroup")


@_attrs_define
class FindingGroup:
    """
    Attributes:
        id (int):
        name (str):
        test (int):
        jira_issue (JIRAIssue | None):
    """

    id: int
    name: str
    test: int
    jira_issue: JIRAIssue | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.jira_issue import JIRAIssue

        id = self.id

        name = self.name

        test = self.test

        jira_issue: dict[str, Any] | None
        if isinstance(self.jira_issue, JIRAIssue):
            jira_issue = self.jira_issue.to_dict()
        else:
            jira_issue = self.jira_issue

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "test": test,
                "jira_issue": jira_issue,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jira_issue import JIRAIssue

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        test = d.pop("test")

        def _parse_jira_issue(data: object) -> JIRAIssue | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                jira_issue_type_1 = JIRAIssue.from_dict(data)

                return jira_issue_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JIRAIssue | None, data)

        jira_issue = _parse_jira_issue(d.pop("jira_issue"))

        finding_group = cls(
            id=id,
            name=name,
            test=test,
            jira_issue=jira_issue,
        )

        finding_group.additional_properties = d
        return finding_group

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
