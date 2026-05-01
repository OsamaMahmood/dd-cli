from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_questionnaire_answered_survey_list_prefetch_assignee import (
        PaginatedQuestionnaireAnsweredSurveyListPrefetchAssignee,
    )
    from ..models.paginated_questionnaire_answered_survey_list_prefetch_engagement import (
        PaginatedQuestionnaireAnsweredSurveyListPrefetchEngagement,
    )
    from ..models.paginated_questionnaire_answered_survey_list_prefetch_responder import (
        PaginatedQuestionnaireAnsweredSurveyListPrefetchResponder,
    )
    from ..models.paginated_questionnaire_answered_survey_list_prefetch_survey import (
        PaginatedQuestionnaireAnsweredSurveyListPrefetchSurvey,
    )


T = TypeVar("T", bound="PaginatedQuestionnaireAnsweredSurveyListPrefetch")


@_attrs_define
class PaginatedQuestionnaireAnsweredSurveyListPrefetch:
    """
    Attributes:
        assignee (PaginatedQuestionnaireAnsweredSurveyListPrefetchAssignee | Unset):
        engagement (PaginatedQuestionnaireAnsweredSurveyListPrefetchEngagement | Unset):
        responder (PaginatedQuestionnaireAnsweredSurveyListPrefetchResponder | Unset):
        survey (PaginatedQuestionnaireAnsweredSurveyListPrefetchSurvey | Unset):
    """

    assignee: PaginatedQuestionnaireAnsweredSurveyListPrefetchAssignee | Unset = UNSET
    engagement: PaginatedQuestionnaireAnsweredSurveyListPrefetchEngagement | Unset = UNSET
    responder: PaginatedQuestionnaireAnsweredSurveyListPrefetchResponder | Unset = UNSET
    survey: PaginatedQuestionnaireAnsweredSurveyListPrefetchSurvey | Unset = UNSET
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
        from ..models.paginated_questionnaire_answered_survey_list_prefetch_assignee import (
            PaginatedQuestionnaireAnsweredSurveyListPrefetchAssignee,
        )
        from ..models.paginated_questionnaire_answered_survey_list_prefetch_engagement import (
            PaginatedQuestionnaireAnsweredSurveyListPrefetchEngagement,
        )
        from ..models.paginated_questionnaire_answered_survey_list_prefetch_responder import (
            PaginatedQuestionnaireAnsweredSurveyListPrefetchResponder,
        )
        from ..models.paginated_questionnaire_answered_survey_list_prefetch_survey import (
            PaginatedQuestionnaireAnsweredSurveyListPrefetchSurvey,
        )

        d = dict(src_dict)
        _assignee = d.pop("assignee", UNSET)
        assignee: PaginatedQuestionnaireAnsweredSurveyListPrefetchAssignee | Unset
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = PaginatedQuestionnaireAnsweredSurveyListPrefetchAssignee.from_dict(_assignee)

        _engagement = d.pop("engagement", UNSET)
        engagement: PaginatedQuestionnaireAnsweredSurveyListPrefetchEngagement | Unset
        if isinstance(_engagement, Unset):
            engagement = UNSET
        else:
            engagement = PaginatedQuestionnaireAnsweredSurveyListPrefetchEngagement.from_dict(
                _engagement
            )

        _responder = d.pop("responder", UNSET)
        responder: PaginatedQuestionnaireAnsweredSurveyListPrefetchResponder | Unset
        if isinstance(_responder, Unset):
            responder = UNSET
        else:
            responder = PaginatedQuestionnaireAnsweredSurveyListPrefetchResponder.from_dict(
                _responder
            )

        _survey = d.pop("survey", UNSET)
        survey: PaginatedQuestionnaireAnsweredSurveyListPrefetchSurvey | Unset
        if isinstance(_survey, Unset):
            survey = UNSET
        else:
            survey = PaginatedQuestionnaireAnsweredSurveyListPrefetchSurvey.from_dict(_survey)

        paginated_questionnaire_answered_survey_list_prefetch = cls(
            assignee=assignee,
            engagement=engagement,
            responder=responder,
            survey=survey,
        )

        paginated_questionnaire_answered_survey_list_prefetch.additional_properties = d
        return paginated_questionnaire_answered_survey_list_prefetch

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
