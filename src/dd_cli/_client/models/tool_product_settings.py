from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_product_settings_prefetch import ToolProductSettingsPrefetch


T = TypeVar("T", bound="ToolProductSettings")


@_attrs_define
class ToolProductSettings:
    """
    Attributes:
        id (int):
        setting_url (str):
        product (int):
        name (str):
        tool_configuration (int):
        notes (list[int]):
        description (None | str | Unset):
        url (None | str | Unset):
        tool_project_id (None | str | Unset):
        prefetch (ToolProductSettingsPrefetch | Unset):
    """

    id: int
    setting_url: str
    product: int
    name: str
    tool_configuration: int
    notes: list[int]
    description: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    tool_project_id: None | str | Unset = UNSET
    prefetch: ToolProductSettingsPrefetch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        setting_url = self.setting_url

        product = self.product

        name = self.name

        tool_configuration = self.tool_configuration

        notes = self.notes

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        tool_project_id: None | str | Unset
        if isinstance(self.tool_project_id, Unset):
            tool_project_id = UNSET
        else:
            tool_project_id = self.tool_project_id

        prefetch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prefetch, Unset):
            prefetch = self.prefetch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "setting_url": setting_url,
                "product": product,
                "name": name,
                "tool_configuration": tool_configuration,
                "notes": notes,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if url is not UNSET:
            field_dict["url"] = url
        if tool_project_id is not UNSET:
            field_dict["tool_project_id"] = tool_project_id
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_product_settings_prefetch import ToolProductSettingsPrefetch

        d = dict(src_dict)
        id = d.pop("id")

        setting_url = d.pop("setting_url")

        product = d.pop("product")

        name = d.pop("name")

        tool_configuration = d.pop("tool_configuration")

        notes = cast(list[int], d.pop("notes"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_tool_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_project_id = _parse_tool_project_id(d.pop("tool_project_id", UNSET))

        _prefetch = d.pop("prefetch", UNSET)
        prefetch: ToolProductSettingsPrefetch | Unset
        if isinstance(_prefetch, Unset):
            prefetch = UNSET
        else:
            prefetch = ToolProductSettingsPrefetch.from_dict(_prefetch)

        tool_product_settings = cls(
            id=id,
            setting_url=setting_url,
            product=product,
            name=name,
            tool_configuration=tool_configuration,
            notes=notes,
            description=description,
            url=url,
            tool_project_id=tool_project_id,
            prefetch=prefetch,
        )

        tool_product_settings.additional_properties = d
        return tool_product_settings

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
