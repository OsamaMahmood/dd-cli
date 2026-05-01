from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="ToolProductSettingsRequest")


@_attrs_define
class ToolProductSettingsRequest:
    """
    Attributes:
        setting_url (str):
        product (int):
        name (str):
        tool_configuration (int):
        description (None | str | Unset):
        url (None | str | Unset):
        tool_project_id (None | str | Unset):
    """

    setting_url: str
    product: int
    name: str
    tool_configuration: int
    description: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    tool_project_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        setting_url = self.setting_url

        product = self.product

        name = self.name

        tool_configuration = self.tool_configuration

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "setting_url": setting_url,
                "product": product,
                "name": name,
                "tool_configuration": tool_configuration,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if url is not UNSET:
            field_dict["url"] = url
        if tool_project_id is not UNSET:
            field_dict["tool_project_id"] = tool_project_id

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("setting_url", (None, str(self.setting_url).encode(), "text/plain")))

        files.append(("product", (None, str(self.product).encode(), "text/plain")))

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(
            ("tool_configuration", (None, str(self.tool_configuration).encode(), "text/plain"))
        )

        if not isinstance(self.description, Unset):
            if isinstance(self.description, str):
                files.append(("description", (None, str(self.description).encode(), "text/plain")))
            else:
                files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.url, Unset):
            if isinstance(self.url, str):
                files.append(("url", (None, str(self.url).encode(), "text/plain")))
            else:
                files.append(("url", (None, str(self.url).encode(), "text/plain")))

        if not isinstance(self.tool_project_id, Unset):
            if isinstance(self.tool_project_id, str):
                files.append(
                    ("tool_project_id", (None, str(self.tool_project_id).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("tool_project_id", (None, str(self.tool_project_id).encode(), "text/plain"))
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        setting_url = d.pop("setting_url")

        product = d.pop("product")

        name = d.pop("name")

        tool_configuration = d.pop("tool_configuration")

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

        tool_product_settings_request = cls(
            setting_url=setting_url,
            product=product,
            name=name,
            tool_configuration=tool_configuration,
            description=description,
            url=url,
            tool_project_id=tool_project_id,
        )

        tool_product_settings_request.additional_properties = d
        return tool_product_settings_request

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
