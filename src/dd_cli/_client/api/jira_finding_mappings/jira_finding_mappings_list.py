from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_jira_issue_list import PaginatedJIRAIssueList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    engagement: int | Unset = UNSET,
    finding: int | Unset = UNSET,
    finding_group: int | Unset = UNSET,
    id: int | Unset = UNSET,
    jira_id: str | Unset = UNSET,
    jira_key: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["engagement"] = engagement

    params["finding"] = finding

    params["finding_group"] = finding_group

    params["id"] = id

    params["jira_id"] = jira_id

    params["jira_key"] = jira_key

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/jira_finding_mappings/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedJIRAIssueList | None:
    if response.status_code == 200:
        response_200 = PaginatedJIRAIssueList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedJIRAIssueList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    engagement: int | Unset = UNSET,
    finding: int | Unset = UNSET,
    finding_group: int | Unset = UNSET,
    id: int | Unset = UNSET,
    jira_id: str | Unset = UNSET,
    jira_key: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PaginatedJIRAIssueList]:
    """
    Args:
        engagement (int | Unset):
        finding (int | Unset):
        finding_group (int | Unset):
        id (int | Unset):
        jira_id (str | Unset):
        jira_key (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedJIRAIssueList]
    """

    kwargs = _get_kwargs(
        engagement=engagement,
        finding=finding,
        finding_group=finding_group,
        id=id,
        jira_id=jira_id,
        jira_key=jira_key,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    engagement: int | Unset = UNSET,
    finding: int | Unset = UNSET,
    finding_group: int | Unset = UNSET,
    id: int | Unset = UNSET,
    jira_id: str | Unset = UNSET,
    jira_key: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PaginatedJIRAIssueList | None:
    """
    Args:
        engagement (int | Unset):
        finding (int | Unset):
        finding_group (int | Unset):
        id (int | Unset):
        jira_id (str | Unset):
        jira_key (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedJIRAIssueList
    """

    return sync_detailed(
        client=client,
        engagement=engagement,
        finding=finding,
        finding_group=finding_group,
        id=id,
        jira_id=jira_id,
        jira_key=jira_key,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    engagement: int | Unset = UNSET,
    finding: int | Unset = UNSET,
    finding_group: int | Unset = UNSET,
    id: int | Unset = UNSET,
    jira_id: str | Unset = UNSET,
    jira_key: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PaginatedJIRAIssueList]:
    """
    Args:
        engagement (int | Unset):
        finding (int | Unset):
        finding_group (int | Unset):
        id (int | Unset):
        jira_id (str | Unset):
        jira_key (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedJIRAIssueList]
    """

    kwargs = _get_kwargs(
        engagement=engagement,
        finding=finding,
        finding_group=finding_group,
        id=id,
        jira_id=jira_id,
        jira_key=jira_key,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    engagement: int | Unset = UNSET,
    finding: int | Unset = UNSET,
    finding_group: int | Unset = UNSET,
    id: int | Unset = UNSET,
    jira_id: str | Unset = UNSET,
    jira_key: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PaginatedJIRAIssueList | None:
    """
    Args:
        engagement (int | Unset):
        finding (int | Unset):
        finding_group (int | Unset):
        id (int | Unset):
        jira_id (str | Unset):
        jira_key (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedJIRAIssueList
    """

    return (
        await asyncio_detailed(
            client=client,
            engagement=engagement,
            finding=finding,
            finding_group=finding_group,
            id=id,
            jira_id=jira_id,
            jira_key=jira_key,
            limit=limit,
            offset=offset,
        )
    ).parsed
