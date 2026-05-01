from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuestionnaireEngagementSurvey")


@_attrs_define
class QuestionnaireEngagementSurvey:
    """
    Attributes:
        id (int):
        questions (list[str]):
        name (str | Unset):
        description (str | Unset):
        active (bool | Unset):
    """

    id: int
    questions: list[str]
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    active: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        questions = self.questions

        name = self.name

        description = self.description

        active = self.active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "questions": questions,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        questions = cast(list[str], d.pop("questions"))

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        active = d.pop("active", UNSET)

        questionnaire_engagement_survey = cls(
            id=id,
            questions=questions,
            name=name,
            description=description,
            active=active,
        )

        questionnaire_engagement_survey.additional_properties = d
        return questionnaire_engagement_survey

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
