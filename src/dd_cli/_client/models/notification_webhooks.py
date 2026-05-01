from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationWebhooks")


@_attrs_define
class NotificationWebhooks:
    """
    Attributes:
        id (int):
        status (str): Status of the incoming webhook
        first_error (datetime.datetime | None): If endpoint is active, when error happened first time
        last_error (datetime.datetime | None): If endpoint is active, when error happened last time
        note (None | str): Description of the latest error
        name (str | Unset): Name of the incoming webhook
        url (str | Unset): The full URL of the incoming webhook
        header_name (None | str | Unset): Name of the header required for interacting with Webhook endpoint
        header_value (None | str | Unset): Content of the header required for interacting with Webhook endpoint
        owner (int | None | Unset): Owner/receiver of notification, if empty processed as system notification
    """

    id: int
    status: str
    first_error: datetime.datetime | None
    last_error: datetime.datetime | None
    note: None | str
    name: str | Unset = UNSET
    url: str | Unset = UNSET
    header_name: None | str | Unset = UNSET
    header_value: None | str | Unset = UNSET
    owner: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        first_error: None | str
        if isinstance(self.first_error, datetime.datetime):
            first_error = self.first_error.isoformat()
        else:
            first_error = self.first_error

        last_error: None | str
        if isinstance(self.last_error, datetime.datetime):
            last_error = self.last_error.isoformat()
        else:
            last_error = self.last_error

        note: None | str
        note = self.note

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
        field_dict.update(
            {
                "id": id,
                "status": status,
                "first_error": first_error,
                "last_error": last_error,
                "note": note,
            }
        )
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

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        status = d.pop("status")

        def _parse_first_error(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_error_type_0 = isoparse(data)

                return first_error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        first_error = _parse_first_error(d.pop("first_error"))

        def _parse_last_error(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_error_type_0 = isoparse(data)

                return last_error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_error = _parse_last_error(d.pop("last_error"))

        def _parse_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        note = _parse_note(d.pop("note"))

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

        notification_webhooks = cls(
            id=id,
            status=status,
            first_error=first_error,
            last_error=last_error,
            note=note,
            name=name,
            url=url,
            header_name=header_name,
            header_value=header_value,
            owner=owner,
        )

        notification_webhooks.additional_properties = d
        return notification_webhooks

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
