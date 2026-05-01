from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.questionnaire_answered_survey import QuestionnaireAnsweredSurvey
from ...types import Response


def _get_kwargs(
    id: int,
    engagement_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/questionnaire_engagement_questionnaires/{id}/link_engagement/{engagement_id}/".format(
            id=quote(str(id), safe=""),
            engagement_id=quote(str(engagement_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> QuestionnaireAnsweredSurvey | None:
    if response.status_code == 200:
        response_200 = QuestionnaireAnsweredSurvey.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[QuestionnaireAnsweredSurvey]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    engagement_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[QuestionnaireAnsweredSurvey]:
    """
    Args:
        id (int):
        engagement_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QuestionnaireAnsweredSurvey]
    """

    kwargs = _get_kwargs(
        id=id,
        engagement_id=engagement_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    engagement_id: int,
    *,
    client: AuthenticatedClient,
) -> QuestionnaireAnsweredSurvey | None:
    """
    Args:
        id (int):
        engagement_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QuestionnaireAnsweredSurvey
    """

    return sync_detailed(
        id=id,
        engagement_id=engagement_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    engagement_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[QuestionnaireAnsweredSurvey]:
    """
    Args:
        id (int):
        engagement_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QuestionnaireAnsweredSurvey]
    """

    kwargs = _get_kwargs(
        id=id,
        engagement_id=engagement_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    engagement_id: int,
    *,
    client: AuthenticatedClient,
) -> QuestionnaireAnsweredSurvey | None:
    """
    Args:
        id (int):
        engagement_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QuestionnaireAnsweredSurvey
    """

    return (
        await asyncio_detailed(
            id=id,
            engagement_id=engagement_id,
            client=client,
        )
    ).parsed
