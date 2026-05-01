from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_language_type_list import PaginatedLanguageTypeList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    color: str | Unset = UNSET,
    id: int | Unset = UNSET,
    language: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["color"] = color

    params["id"] = id

    params["language"] = language

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/language_types/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedLanguageTypeList | None:
    if response.status_code == 200:
        response_200 = PaginatedLanguageTypeList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedLanguageTypeList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    color: str | Unset = UNSET,
    id: int | Unset = UNSET,
    language: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PaginatedLanguageTypeList]:
    """
    Args:
        color (str | Unset):
        id (int | Unset):
        language (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedLanguageTypeList]
    """

    kwargs = _get_kwargs(
        color=color,
        id=id,
        language=language,
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
    color: str | Unset = UNSET,
    id: int | Unset = UNSET,
    language: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PaginatedLanguageTypeList | None:
    """
    Args:
        color (str | Unset):
        id (int | Unset):
        language (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedLanguageTypeList
    """

    return sync_detailed(
        client=client,
        color=color,
        id=id,
        language=language,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    color: str | Unset = UNSET,
    id: int | Unset = UNSET,
    language: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PaginatedLanguageTypeList]:
    """
    Args:
        color (str | Unset):
        id (int | Unset):
        language (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedLanguageTypeList]
    """

    kwargs = _get_kwargs(
        color=color,
        id=id,
        language=language,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    color: str | Unset = UNSET,
    id: int | Unset = UNSET,
    language: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PaginatedLanguageTypeList | None:
    """
    Args:
        color (str | Unset):
        id (int | Unset):
        language (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedLanguageTypeList
    """

    return (
        await asyncio_detailed(
            client=client,
            color=color,
            id=id,
            language=language,
            limit=limit,
            offset=offset,
        )
    ).parsed
