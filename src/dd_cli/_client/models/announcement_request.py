from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.announcement_request_style import AnnouncementRequestStyle
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnnouncementRequest")


@_attrs_define
class AnnouncementRequest:
    """
    Attributes:
        message (str | Unset): This dismissable message will be displayed on all pages for authenticated users. It can
            contain basic html tags, for example <a href='https://www.fred.com' style='color: #337ab7;'
            target='_blank'>https://example.com</a>
        style (AnnouncementRequestStyle | Unset): The style of banner to display. (info, success, warning, danger)

            * `info` - Info
            * `success` - Success
            * `warning` - Warning
            * `danger` - Danger
        dismissable (bool | Unset): Ticking this box allows users to dismiss the current announcement
    """

    message: str | Unset = UNSET
    style: AnnouncementRequestStyle | Unset = UNSET
    dismissable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        style: str | Unset = UNSET
        if not isinstance(self.style, Unset):
            style = self.style.value

        dismissable = self.dismissable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if style is not UNSET:
            field_dict["style"] = style
        if dismissable is not UNSET:
            field_dict["dismissable"] = dismissable

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.message, Unset):
            files.append(("message", (None, str(self.message).encode(), "text/plain")))

        if not isinstance(self.style, Unset):
            files.append(("style", (None, str(self.style.value).encode(), "text/plain")))

        if not isinstance(self.dismissable, Unset):
            files.append(("dismissable", (None, str(self.dismissable).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        _style = d.pop("style", UNSET)
        style: AnnouncementRequestStyle | Unset
        if isinstance(_style, Unset):
            style = UNSET
        else:
            style = AnnouncementRequestStyle(_style)

        dismissable = d.pop("dismissable", UNSET)

        announcement_request = cls(
            message=message,
            style=style,
            dismissable=dismissable,
        )

        announcement_request.additional_properties = d
        return announcement_request

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
