from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestType")


@_attrs_define
class TestType:
    """
    Attributes:
        id (int):
        name (str):
        static_tool (bool | Unset):
        dynamic_tool (bool | Unset):
        active (bool | Unset):
    """

    id: int
    name: str
    static_tool: bool | Unset = UNSET
    dynamic_tool: bool | Unset = UNSET
    active: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        static_tool = self.static_tool

        dynamic_tool = self.dynamic_tool

        active = self.active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
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

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        static_tool = d.pop("static_tool", UNSET)

        dynamic_tool = d.pop("dynamic_tool", UNSET)

        active = d.pop("active", UNSET)

        test_type = cls(
            id=id,
            name=name,
            static_tool=static_tool,
            dynamic_tool=dynamic_tool,
            active=active,
        )

        test_type.additional_properties = d
        return test_type

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
