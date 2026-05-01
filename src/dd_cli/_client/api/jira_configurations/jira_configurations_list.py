from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_jira_instance_list import PaginatedJIRAInstanceList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params["limit"] = limit

    params["offset"] = offset

    params["url"] = url_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/jira_configurations/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedJIRAInstanceList | None:
    if response.status_code == 200:
        response_200 = PaginatedJIRAInstanceList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedJIRAInstanceList]:
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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> Response[PaginatedJIRAInstanceList]:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        url_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedJIRAInstanceList]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        offset=offset,
        url_query=url_query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> PaginatedJIRAInstanceList | None:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        url_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedJIRAInstanceList
    """

    return sync_detailed(
        client=client,
        id=id,
        limit=limit,
        offset=offset,
        url_query=url_query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> Response[PaginatedJIRAInstanceList]:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        url_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedJIRAInstanceList]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        offset=offset,
        url_query=url_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> PaginatedJIRAInstanceList | None:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        url_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedJIRAInstanceList
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            limit=limit,
            offset=offset,
            url_query=url_query,
        )
    ).parsed
