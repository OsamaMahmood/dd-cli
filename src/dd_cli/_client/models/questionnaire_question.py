from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuestionnaireQuestion")


@_attrs_define
class QuestionnaireQuestion:
    """
    Attributes:
        id (int):
        created (datetime.datetime):
        modified (datetime.datetime):
        order (int | Unset): The render order
        optional (bool | Unset): If selected, user doesn't have to answer this question
        text (str | Unset): The question text
    """

    id: int
    created: datetime.datetime
    modified: datetime.datetime
    order: int | Unset = UNSET
    optional: bool | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        order = self.order

        optional = self.optional

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created": created,
                "modified": modified,
            }
        )
        if order is not UNSET:
            field_dict["order"] = order
        if optional is not UNSET:
            field_dict["optional"] = optional
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        order = d.pop("order", UNSET)

        optional = d.pop("optional", UNSET)

        text = d.pop("text", UNSET)

        questionnaire_question = cls(
            id=id,
            created=created,
            modified=modified,
            order=order,
            optional=optional,
            text=text,
        )

        questionnaire_question.additional_properties = d
        return questionnaire_question

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
