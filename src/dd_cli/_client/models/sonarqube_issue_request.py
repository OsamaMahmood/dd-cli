from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types

T = TypeVar("T", bound="SonarqubeIssueRequest")


@_attrs_define
class SonarqubeIssueRequest:
    """
    Attributes:
        key (str): SonarQube issue key
        status (str): SonarQube issue status
        type_ (str): SonarQube issue type
    """

    key: str
    status: str
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        status = self.status

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "status": status,
                "type": type_,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("key", (None, str(self.key).encode(), "text/plain")))

        files.append(("status", (None, str(self.status).encode(), "text/plain")))

        files.append(("type", (None, str(self.type_).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        status = d.pop("status")

        type_ = d.pop("type")

        sonarqube_issue_request = cls(
            key=key,
            status=status,
            type_=type_,
        )

        sonarqube_issue_request.additional_properties = d
        return sonarqube_issue_request

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
