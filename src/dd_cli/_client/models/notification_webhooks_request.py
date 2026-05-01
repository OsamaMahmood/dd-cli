from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationWebhooksRequest")


@_attrs_define
class NotificationWebhooksRequest:
    """
    Attributes:
        name (str | Unset): Name of the incoming webhook
        url (str | Unset): The full URL of the incoming webhook
        header_name (None | str | Unset): Name of the header required for interacting with Webhook endpoint
        header_value (None | str | Unset): Content of the header required for interacting with Webhook endpoint
        owner (int | None | Unset): Owner/receiver of notification, if empty processed as system notification
    """

    name: str | Unset = UNSET
    url: str | Unset = UNSET
    header_name: None | str | Unset = UNSET
    header_value: None | str | Unset = UNSET
    owner: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        url = self.url

        header_name: None | str | Unset
        if isinstance(self.header_name, Unset):
            header_name = UNSET
        else:
            header_name = self.header_name

        header_value: None | str | Unset
        if isinstance(self.header_value, Unset):
            header_value = UNSET
        else:
            header_value = self.header_value

        owner: int | None | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if header_name is not UNSET:
            field_dict["header_name"] = header_name
        if header_value is not UNSET:
            field_dict["header_value"] = header_value
        if owner is not UNSET:
            field_dict["owner"] = owner

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.url, Unset):
            files.append(("url", (None, str(self.url).encode(), "text/plain")))

        if not isinstance(self.header_name, Unset):
            if isinstance(self.header_name, str):
                files.append(("header_name", (None, str(self.header_name).encode(), "text/plain")))
            else:
                files.append(("header_name", (None, str(self.header_name).encode(), "text/plain")))

        if not isinstance(self.header_value, Unset):
            if isinstance(self.header_value, str):
                files.append(
                    ("header_value", (None, str(self.header_value).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("header_value", (None, str(self.header_value).encode(), "text/plain"))
                )

        if not isinstance(self.owner, Unset):
            if isinstance(self.owner, int):
                files.append(("owner", (None, str(self.owner).encode(), "text/plain")))
            else:
                files.append(("owner", (None, str(self.owner).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        def _parse_header_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        header_name = _parse_header_name(d.pop("header_name", UNSET))

        def _parse_header_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        header_value = _parse_header_value(d.pop("header_value", UNSET))

        def _parse_owner(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        notification_webhooks_request = cls(
            name=name,
            url=url,
            header_name=header_name,
            header_value=header_value,
            owner=owner,
        )

        notification_webhooks_request.additional_properties = d
        return notification_webhooks_request

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
