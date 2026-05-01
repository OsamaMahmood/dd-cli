from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="TestTypeCreateRequest")


@_attrs_define
class TestTypeCreateRequest:
    """
    Attributes:
        name (str):
        static_tool (bool | Unset):
        dynamic_tool (bool | Unset):
        active (bool | Unset):
    """

    name: str
    static_tool: bool | Unset = UNSET
    dynamic_tool: bool | Unset = UNSET
    active: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        static_tool = self.static_tool

        dynamic_tool = self.dynamic_tool

        active = self.active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if static_tool is not UNSET:
            field_dict["static_tool"] = static_tool
        if dynamic_tool is not UNSET:
            field_dict["dynamic_tool"] = dynamic_tool
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

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
        name = d.pop("name")

        static_tool = d.pop("static_tool", UNSET)

        dynamic_tool = d.pop("dynamic_tool", UNSET)

        active = d.pop("active", UNSET)

        test_type_create_request = cls(
            name=name,
            static_tool=static_tool,
            dynamic_tool=dynamic_tool,
            active=active,
        )

        test_type_create_request.additional_properties = d
        return test_type_create_request

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
