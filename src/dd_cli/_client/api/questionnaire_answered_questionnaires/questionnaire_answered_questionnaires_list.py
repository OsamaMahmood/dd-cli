from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_questionnaire_answered_survey_list import (
    PaginatedQuestionnaireAnsweredSurveyList,
)
from ...models.questionnaire_answered_questionnaires_list_prefetch_item import (
    QuestionnaireAnsweredQuestionnairesListPrefetchItem,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[QuestionnaireAnsweredQuestionnairesListPrefetchItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_prefetch: list[str] | Unset = UNSET
    if not isinstance(prefetch, Unset):
        json_prefetch = []
        for prefetch_item_data in prefetch:
            prefetch_item = prefetch_item_data.value
            json_prefetch.append(prefetch_item)

    params["prefetch"] = json_prefetch

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/questionnaire_answered_questionnaires/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedQuestionnaireAnsweredSurveyList | None:
    if response.status_code == 200:
        response_200 = PaginatedQuestionnaireAnsweredSurveyList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedQuestionnaireAnsweredSurveyList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[QuestionnaireAnsweredQuestionnairesListPrefetchItem] | Unset = UNSET,
) -> Response[PaginatedQuestionnaireAnsweredSurveyList]:
    """
    Args:
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[QuestionnaireAnsweredQuestionnairesListPrefetchItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedQuestionnaireAnsweredSurveyList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        prefetch=prefetch,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[QuestionnaireAnsweredQuestionnairesListPrefetchItem] | Unset = UNSET,
) -> PaginatedQuestionnaireAnsweredSurveyList | None:
    """
    Args:
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[QuestionnaireAnsweredQuestionnairesListPrefetchItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedQuestionnaireAnsweredSurveyList
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[QuestionnaireAnsweredQuestionnairesListPrefetchItem] | Unset = UNSET,
) -> Response[PaginatedQuestionnaireAnsweredSurveyList]:
    """
    Args:
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[QuestionnaireAnsweredQuestionnairesListPrefetchItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedQuestionnaireAnsweredSurveyList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        prefetch=prefetch,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[QuestionnaireAnsweredQuestionnairesListPrefetchItem] | Unset = UNSET,
) -> PaginatedQuestionnaireAnsweredSurveyList | None:
    """
    Args:
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[QuestionnaireAnsweredQuestionnairesListPrefetchItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedQuestionnaireAnsweredSurveyList
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            prefetch=prefetch,
        )
    ).parsed
