from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedTestTypeRequest")


@_attrs_define
class PatchedTestTypeRequest:
    """
    Attributes:
        static_tool (bool | Unset):
        dynamic_tool (bool | Unset):
        active (bool | Unset):
    """

    static_tool: bool | Unset = UNSET
    dynamic_tool: bool | Unset = UNSET
    active: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        static_tool = self.static_tool

        dynamic_tool = self.dynamic_tool

        active = self.active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if static_tool is not UNSET:
            field_dict["static_tool"] = static_tool
        if dynamic_tool is not UNSET:
            field_dict["dynamic_tool"] = dynamic_tool
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.static_tool, Unset):
            files.append(("static_tool", (None, str(self.static_tool).encode(), "text/plain")))

        if not isinstance(self.dynamic_tool, Unset):
            files.append(("dynamic_tool", (None, str(self.dynamic_tool).encode(), "text/plain")))

        if not isinstance(self.active, Unset):
            files.append(("active", (None, str(self.active).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        static_tool = d.pop("static_tool", UNSET)

        dynamic_tool = d.pop("dynamic_tool", UNSET)

        active = d.pop("active", UNSET)

        patched_test_type_request = cls(
            static_tool=static_tool,
            dynamic_tool=dynamic_tool,
            active=active,
        )

        patched_test_type_request.additional_properties = d
        return patched_test_type_request

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
