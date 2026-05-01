from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.questionnaire_engagement_survey import QuestionnaireEngagementSurvey


T = TypeVar("T", bound="QuestionnaireGeneralSurvey")


@_attrs_define
class QuestionnaireGeneralSurvey:
    """
    Attributes:
        id (int):
        survey (QuestionnaireEngagementSurvey):
        generated (datetime.datetime | None):
        num_responses (int | Unset):
        expiration (datetime.datetime | Unset):
    """

    id: int
    survey: QuestionnaireEngagementSurvey
    generated: datetime.datetime | None
    num_responses: int | Unset = UNSET
    expiration: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        survey = self.survey.to_dict()

        generated: None | str
        if isinstance(self.generated, datetime.datetime):
            generated = self.generated.isoformat()
        else:
            generated = self.generated

        num_responses = self.num_responses

        expiration: str | Unset = UNSET
        if not isinstance(self.expiration, Unset):
            expiration = self.expiration.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "survey": survey,
                "generated": generated,
            }
        )
        if num_responses is not UNSET:
            field_dict["num_responses"] = num_responses
        if expiration is not UNSET:
            field_dict["expiration"] = expiration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.questionnaire_engagement_survey import QuestionnaireEngagementSurvey

        d = dict(src_dict)
        id = d.pop("id")

        survey = QuestionnaireEngagementSurvey.from_dict(d.pop("survey"))

        def _parse_generated(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                generated_type_0 = isoparse(data)

                return generated_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        generated = _parse_generated(d.pop("generated"))

        num_responses = d.pop("num_responses", UNSET)

        _expiration = d.pop("expiration", UNSET)
        expiration: datetime.datetime | Unset
        if isinstance(_expiration, Unset):
            expiration = UNSET
        else:
            expiration = isoparse(_expiration)

        questionnaire_general_survey = cls(
            id=id,
            survey=survey,
            generated=generated,
            num_responses=num_responses,
            expiration=expiration,
        )

        questionnaire_general_survey.additional_properties = d
        return questionnaire_general_survey

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
