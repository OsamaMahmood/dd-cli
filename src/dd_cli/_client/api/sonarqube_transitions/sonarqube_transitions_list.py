from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_sonarqube_issue_transition_list import (
    PaginatedSonarqubeIssueTransitionList,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    finding_status: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sonarqube_issue: int | Unset = UNSET,
    sonarqube_status: str | Unset = UNSET,
    transitions: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["finding_status"] = finding_status

    params["id"] = id

    params["limit"] = limit

    params["offset"] = offset

    params["sonarqube_issue"] = sonarqube_issue

    params["sonarqube_status"] = sonarqube_status

    params["transitions"] = transitions

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/sonarqube_transitions/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedSonarqubeIssueTransitionList | None:
    if response.status_code == 200:
        response_200 = PaginatedSonarqubeIssueTransitionList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedSonarqubeIssueTransitionList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    finding_status: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sonarqube_issue: int | Unset = UNSET,
    sonarqube_status: str | Unset = UNSET,
    transitions: str | Unset = UNSET,
) -> Response[PaginatedSonarqubeIssueTransitionList]:
    """
    Args:
        finding_status (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        sonarqube_issue (int | Unset):
        sonarqube_status (str | Unset):
        transitions (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedSonarqubeIssueTransitionList]
    """

    kwargs = _get_kwargs(
        finding_status=finding_status,
        id=id,
        limit=limit,
        offset=offset,
        sonarqube_issue=sonarqube_issue,
        sonarqube_status=sonarqube_status,
        transitions=transitions,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    finding_status: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sonarqube_issue: int | Unset = UNSET,
    sonarqube_status: str | Unset = UNSET,
    transitions: str | Unset = UNSET,
) -> PaginatedSonarqubeIssueTransitionList | None:
    """
    Args:
        finding_status (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        sonarqube_issue (int | Unset):
        sonarqube_status (str | Unset):
        transitions (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedSonarqubeIssueTransitionList
    """

    return sync_detailed(
        client=client,
        finding_status=finding_status,
        id=id,
        limit=limit,
        offset=offset,
        sonarqube_issue=sonarqube_issue,
        sonarqube_status=sonarqube_status,
        transitions=transitions,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    finding_status: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sonarqube_issue: int | Unset = UNSET,
    sonarqube_status: str | Unset = UNSET,
    transitions: str | Unset = UNSET,
) -> Response[PaginatedSonarqubeIssueTransitionList]:
    """
    Args:
        finding_status (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        sonarqube_issue (int | Unset):
        sonarqube_status (str | Unset):
        transitions (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedSonarqubeIssueTransitionList]
    """

    kwargs = _get_kwargs(
        finding_status=finding_status,
        id=id,
        limit=limit,
        offset=offset,
        sonarqube_issue=sonarqube_issue,
        sonarqube_status=sonarqube_status,
        transitions=transitions,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    finding_status: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    sonarqube_issue: int | Unset = UNSET,
    sonarqube_status: str | Unset = UNSET,
    transitions: str | Unset = UNSET,
) -> PaginatedSonarqubeIssueTransitionList | None:
    """
    Args:
        finding_status (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        sonarqube_issue (int | Unset):
        sonarqube_status (str | Unset):
        transitions (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedSonarqubeIssueTransitionList
    """

    return (
        await asyncio_detailed(
            client=client,
            finding_status=finding_status,
            id=id,
            limit=limit,
            offset=offset,
            sonarqube_issue=sonarqube_issue,
            sonarqube_status=sonarqube_status,
            transitions=transitions,
        )
    ).parsed
