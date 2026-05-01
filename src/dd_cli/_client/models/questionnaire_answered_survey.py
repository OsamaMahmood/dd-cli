from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.questionnaire_answered_survey_prefetch import QuestionnaireAnsweredSurveyPrefetch


T = TypeVar("T", bound="QuestionnaireAnsweredSurvey")


@_attrs_define
class QuestionnaireAnsweredSurvey:
    """
    Attributes:
        id (int):
        survey (int):
        completed (bool | Unset):
        answered_on (datetime.date | None | Unset):
        engagement (int | None | Unset):
        assignee (int | None | Unset):
        responder (int | None | Unset):
        prefetch (QuestionnaireAnsweredSurveyPrefetch | Unset):
    """

    id: int
    survey: int
    completed: bool | Unset = UNSET
    answered_on: datetime.date | None | Unset = UNSET
    engagement: int | None | Unset = UNSET
    assignee: int | None | Unset = UNSET
    responder: int | None | Unset = UNSET
    prefetch: QuestionnaireAnsweredSurveyPrefetch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        survey = self.survey

        completed = self.completed

        answered_on: None | str | Unset
        if isinstance(self.answered_on, Unset):
            answered_on = UNSET
        elif isinstance(self.answered_on, datetime.date):
            answered_on = self.answered_on.isoformat()
        else:
            answered_on = self.answered_on

        engagement: int | None | Unset
        if isinstance(self.engagement, Unset):
            engagement = UNSET
        else:
            engagement = self.engagement

        assignee: int | None | Unset
        if isinstance(self.assignee, Unset):
            assignee = UNSET
        else:
            assignee = self.assignee

        responder: int | None | Unset
        if isinstance(self.responder, Unset):
            responder = UNSET
        else:
            responder = self.responder

        prefetch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prefetch, Unset):
            prefetch = self.prefetch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "survey": survey,
            }
        )
        if completed is not UNSET:
            field_dict["completed"] = completed
        if answered_on is not UNSET:
            field_dict["answered_on"] = answered_on
        if engagement is not UNSET:
            field_dict["engagement"] = engagement
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if responder is not UNSET:
            field_dict["responder"] = responder
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.questionnaire_answered_survey_prefetch import (
            QuestionnaireAnsweredSurveyPrefetch,
        )

        d = dict(src_dict)
        id = d.pop("id")

        survey = d.pop("survey")

        completed = d.pop("completed", UNSET)

        def _parse_answered_on(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                answered_on_type_0 = isoparse(data).date()

                return answered_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        answered_on = _parse_answered_on(d.pop("answered_on", UNSET))

        def _parse_engagement(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        engagement = _parse_engagement(d.pop("engagement", UNSET))

        def _parse_assignee(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        assignee = _parse_assignee(d.pop("assignee", UNSET))

        def _parse_responder(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        responder = _parse_responder(d.pop("responder", UNSET))

        _prefetch = d.pop("prefetch", UNSET)
        prefetch: QuestionnaireAnsweredSurveyPrefetch | Unset
        if isinstance(_prefetch, Unset):
            prefetch = UNSET
        else:
            prefetch = QuestionnaireAnsweredSurveyPrefetch.from_dict(_prefetch)

        questionnaire_answered_survey = cls(
            id=id,
            survey=survey,
            completed=completed,
            answered_on=answered_on,
            engagement=engagement,
            assignee=assignee,
            responder=responder,
            prefetch=prefetch,
        )

        questionnaire_answered_survey.additional_properties = d
        return questionnaire_answered_survey

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
