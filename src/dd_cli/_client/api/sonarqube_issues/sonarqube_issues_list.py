from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_sonarqube_issue_list import PaginatedSonarqubeIssueList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: int | Unset = UNSET,
    key: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params["key"] = key

    params["limit"] = limit

    params["offset"] = offset

    params["status"] = status

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/sonarqube_issues/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedSonarqubeIssueList | None:
    if response.status_code == 200:
        response_200 = PaginatedSonarqubeIssueList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedSonarqubeIssueList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    key: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Response[PaginatedSonarqubeIssueList]:
    """
    Args:
        id (int | Unset):
        key (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        status (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedSonarqubeIssueList]
    """

    kwargs = _get_kwargs(
        id=id,
        key=key,
        limit=limit,
        offset=offset,
        status=status,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    key: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> PaginatedSonarqubeIssueList | None:
    """
    Args:
        id (int | Unset):
        key (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        status (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedSonarqubeIssueList
    """

    return sync_detailed(
        client=client,
        id=id,
        key=key,
        limit=limit,
        offset=offset,
        status=status,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    key: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Response[PaginatedSonarqubeIssueList]:
    """
    Args:
        id (int | Unset):
        key (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        status (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedSonarqubeIssueList]
    """

    kwargs = _get_kwargs(
        id=id,
        key=key,
        limit=limit,
        offset=offset,
        status=status,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    key: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> PaginatedSonarqubeIssueList | None:
    """
    Args:
        id (int | Unset):
        key (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        status (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedSonarqubeIssueList
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            key=key,
            limit=limit,
            offset=offset,
            status=status,
            type_=type_,
        )
    ).parsed
