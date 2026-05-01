from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="QuestionnaireAnswer")


@_attrs_define
class QuestionnaireAnswer:
    """
    Attributes:
        id (int):
        created (datetime.datetime):
        modified (datetime.datetime):
        question (int):
        answered_survey (int):
    """

    id: int
    created: datetime.datetime
    modified: datetime.datetime
    question: int
    answered_survey: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        question = self.question

        answered_survey = self.answered_survey

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created": created,
                "modified": modified,
                "question": question,
                "answered_survey": answered_survey,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        question = d.pop("question")

        answered_survey = d.pop("answered_survey")

        questionnaire_answer = cls(
            id=id,
            created=created,
            modified=modified,
            question=question,
            answered_survey=answered_survey,
        )

        questionnaire_answer.additional_properties = d
        return questionnaire_answer

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
