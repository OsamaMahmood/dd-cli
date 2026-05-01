from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_regulation_list import PaginatedRegulationList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    description: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["description"] = description

    params["id"] = id

    params["limit"] = limit

    params["name"] = name

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/regulations/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedRegulationList | None:
    if response.status_code == 200:
        response_200 = PaginatedRegulationList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedRegulationList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    description: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PaginatedRegulationList]:
    """
    Args:
        description (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRegulationList]
    """

    kwargs = _get_kwargs(
        description=description,
        id=id,
        limit=limit,
        name=name,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    description: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PaginatedRegulationList | None:
    """
    Args:
        description (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRegulationList
    """

    return sync_detailed(
        client=client,
        description=description,
        id=id,
        limit=limit,
        name=name,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    description: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PaginatedRegulationList]:
    """
    Args:
        description (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRegulationList]
    """

    kwargs = _get_kwargs(
        description=description,
        id=id,
        limit=limit,
        name=name,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    description: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PaginatedRegulationList | None:
    """
    Args:
        description (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRegulationList
    """

    return (
        await asyncio_detailed(
            client=client,
            description=description,
            id=id,
            limit=limit,
            name=name,
            offset=offset,
        )
    ).parsed
