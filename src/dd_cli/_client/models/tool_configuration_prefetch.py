from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_configuration_prefetch_tool_type import ToolConfigurationPrefetchToolType


T = TypeVar("T", bound="ToolConfigurationPrefetch")


@_attrs_define
class ToolConfigurationPrefetch:
    """
    Attributes:
        tool_type (ToolConfigurationPrefetchToolType | Unset):
    """

    tool_type: ToolConfigurationPrefetchToolType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tool_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tool_type, Unset):
            tool_type = self.tool_type.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tool_type is not UNSET:
            field_dict["tool_type"] = tool_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_configuration_prefetch_tool_type import ToolConfigurationPrefetchToolType

        d = dict(src_dict)
        _tool_type = d.pop("tool_type", UNSET)
        tool_type: ToolConfigurationPrefetchToolType | Unset
        if isinstance(_tool_type, Unset):
            tool_type = UNSET
        else:
            tool_type = ToolConfigurationPrefetchToolType.from_dict(_tool_type)

        tool_configuration_prefetch = cls(
            tool_type=tool_type,
        )

        tool_configuration_prefetch.additional_properties = d
        return tool_configuration_prefetch

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
