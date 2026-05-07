from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CeleryStatus")


@_attrs_define
class CeleryStatus:
    """
    Attributes:
        worker_status (bool):
        broker_status (bool):
        queue_length (int | None):
        task_time_limit (int | None):
        task_soft_time_limit (int | None):
        task_default_expires (int | None):
    """

    worker_status: bool
    broker_status: bool
    queue_length: int | None
    task_time_limit: int | None
    task_soft_time_limit: int | None
    task_default_expires: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        worker_status = self.worker_status

        broker_status = self.broker_status

        queue_length: int | None
        queue_length = self.queue_length

        task_time_limit: int | None
        task_time_limit = self.task_time_limit

        task_soft_time_limit: int | None
        task_soft_time_limit = self.task_soft_time_limit

        task_default_expires: int | None
        task_default_expires = self.task_default_expires

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "worker_status": worker_status,
                "broker_status": broker_status,
                "queue_length": queue_length,
                "task_time_limit": task_time_limit,
                "task_soft_time_limit": task_soft_time_limit,
                "task_default_expires": task_default_expires,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        worker_status = d.pop("worker_status")

        broker_status = d.pop("broker_status")

        def _parse_queue_length(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        queue_length = _parse_queue_length(d.pop("queue_length"))

        def _parse_task_time_limit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        task_time_limit = _parse_task_time_limit(d.pop("task_time_limit"))

        def _parse_task_soft_time_limit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        task_soft_time_limit = _parse_task_soft_time_limit(d.pop("task_soft_time_limit"))

        def _parse_task_default_expires(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        task_default_expires = _parse_task_default_expires(d.pop("task_default_expires"))

        celery_status = cls(
            worker_status=worker_status,
            broker_status=broker_status,
            queue_length=queue_length,
            task_time_limit=task_time_limit,
            task_soft_time_limit=task_soft_time_limit,
            task_default_expires=task_default_expires,
        )

        celery_status.additional_properties = d
        return celery_status

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
