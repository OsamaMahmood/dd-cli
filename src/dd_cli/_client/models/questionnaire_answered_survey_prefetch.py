from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.questionnaire_answered_survey_prefetch_assignee import (
        QuestionnaireAnsweredSurveyPrefetchAssignee,
    )
    from ..models.questionnaire_answered_survey_prefetch_engagement import (
        QuestionnaireAnsweredSurveyPrefetchEngagement,
    )
    from ..models.questionnaire_answered_survey_prefetch_responder import (
        QuestionnaireAnsweredSurveyPrefetchResponder,
    )
    from ..models.questionnaire_answered_survey_prefetch_survey import (
        QuestionnaireAnsweredSurveyPrefetchSurvey,
    )


T = TypeVar("T", bound="QuestionnaireAnsweredSurveyPrefetch")


@_attrs_define
class QuestionnaireAnsweredSurveyPrefetch:
    """
    Attributes:
        assignee (QuestionnaireAnsweredSurveyPrefetchAssignee | Unset):
        engagement (QuestionnaireAnsweredSurveyPrefetchEngagement | Unset):
        responder (QuestionnaireAnsweredSurveyPrefetchResponder | Unset):
        survey (QuestionnaireAnsweredSurveyPrefetchSurvey | Unset):
    """

    assignee: QuestionnaireAnsweredSurveyPrefetchAssignee | Unset = UNSET
    engagement: QuestionnaireAnsweredSurveyPrefetchEngagement | Unset = UNSET
    responder: QuestionnaireAnsweredSurveyPrefetchResponder | Unset = UNSET
    survey: QuestionnaireAnsweredSurveyPrefetchSurvey | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        engagement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.engagement, Unset):
            engagement = self.engagement.to_dict()

        responder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.responder, Unset):
            responder = self.responder.to_dict()

        survey: dict[str, Any] | Unset = UNSET
        if not isinstance(self.survey, Unset):
            survey = self.survey.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if engagement is not UNSET:
            field_dict["engagement"] = engagement
        if responder is not UNSET:
            field_dict["responder"] = responder
        if survey is not UNSET:
            field_dict["survey"] = survey

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.questionnaire_answered_survey_prefetch_assignee import (
            QuestionnaireAnsweredSurveyPrefetchAssignee,
        )
        from ..models.questionnaire_answered_survey_prefetch_engagement import (
            QuestionnaireAnsweredSurveyPrefetchEngagement,
        )
        from ..models.questionnaire_answered_survey_prefetch_responder import (
            QuestionnaireAnsweredSurveyPrefetchResponder,
        )
        from ..models.questionnaire_answered_survey_prefetch_survey import (
            QuestionnaireAnsweredSurveyPrefetchSurvey,
        )

        d = dict(src_dict)
        _assignee = d.pop("assignee", UNSET)
        assignee: QuestionnaireAnsweredSurveyPrefetchAssignee | Unset
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = QuestionnaireAnsweredSurveyPrefetchAssignee.from_dict(_assignee)

        _engagement = d.pop("engagement", UNSET)
        engagement: QuestionnaireAnsweredSurveyPrefetchEngagement | Unset
        if isinstance(_engagement, Unset):
            engagement = UNSET
        else:
            engagement = QuestionnaireAnsweredSurveyPrefetchEngagement.from_dict(_engagement)

        _responder = d.pop("responder", UNSET)
        responder: QuestionnaireAnsweredSurveyPrefetchResponder | Unset
        if isinstance(_responder, Unset):
            responder = UNSET
        else:
            responder = QuestionnaireAnsweredSurveyPrefetchResponder.from_dict(_responder)

        _survey = d.pop("survey", UNSET)
        survey: QuestionnaireAnsweredSurveyPrefetchSurvey | Unset
        if isinstance(_survey, Unset):
            survey = UNSET
        else:
            survey = QuestionnaireAnsweredSurveyPrefetchSurvey.from_dict(_survey)

        questionnaire_answered_survey_prefetch = cls(
            assignee=assignee,
            engagement=engagement,
            responder=responder,
            survey=survey,
        )

        questionnaire_answered_survey_prefetch.additional_properties = d
        return questionnaire_answered_survey_prefetch

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
