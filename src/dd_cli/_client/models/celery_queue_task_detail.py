from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CeleryQueueTaskDetail")


@_attrs_define
class CeleryQueueTaskDetail:
    """
    Attributes:
        task_name (str):
        count (int):
        oldest_position (int):
        newest_position (int):
        oldest_eta (None | str):
        newest_eta (None | str):
        earliest_expires (None | str):
        latest_expires (None | str):
    """

    task_name: str
    count: int
    oldest_position: int
    newest_position: int
    oldest_eta: None | str
    newest_eta: None | str
    earliest_expires: None | str
    latest_expires: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_name = self.task_name

        count = self.count

        oldest_position = self.oldest_position

        newest_position = self.newest_position

        oldest_eta: None | str
        oldest_eta = self.oldest_eta

        newest_eta: None | str
        newest_eta = self.newest_eta

        earliest_expires: None | str
        earliest_expires = self.earliest_expires

        latest_expires: None | str
        latest_expires = self.latest_expires

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_name": task_name,
                "count": count,
                "oldest_position": oldest_position,
                "newest_position": newest_position,
                "oldest_eta": oldest_eta,
                "newest_eta": newest_eta,
                "earliest_expires": earliest_expires,
                "latest_expires": latest_expires,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_name = d.pop("task_name")

        count = d.pop("count")

        oldest_position = d.pop("oldest_position")

        newest_position = d.pop("newest_position")

        def _parse_oldest_eta(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        oldest_eta = _parse_oldest_eta(d.pop("oldest_eta"))

        def _parse_newest_eta(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        newest_eta = _parse_newest_eta(d.pop("newest_eta"))

        def _parse_earliest_expires(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        earliest_expires = _parse_earliest_expires(d.pop("earliest_expires"))

        def _parse_latest_expires(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        latest_expires = _parse_latest_expires(d.pop("latest_expires"))

        celery_queue_task_detail = cls(
            task_name=task_name,
            count=count,
            oldest_position=oldest_position,
            newest_position=newest_position,
            oldest_eta=oldest_eta,
            newest_eta=newest_eta,
            earliest_expires=earliest_expires,
            latest_expires=latest_expires,
        )

        celery_queue_task_detail.additional_properties = d
        return celery_queue_task_detail

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
