from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.languages_list_prefetch_item import LanguagesListPrefetchItem
from ...models.paginated_language_list import PaginatedLanguageList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: int | Unset = UNSET,
    language: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[LanguagesListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params["language"] = language

    params["limit"] = limit

    params["offset"] = offset

    json_prefetch: list[str] | Unset = UNSET
    if not isinstance(prefetch, Unset):
        json_prefetch = []
        for prefetch_item_data in prefetch:
            prefetch_item = prefetch_item_data.value
            json_prefetch.append(prefetch_item)

    params["prefetch"] = json_prefetch

    params["product"] = product

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/languages/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedLanguageList | None:
    if response.status_code == 200:
        response_200 = PaginatedLanguageList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedLanguageList]:
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
    language: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[LanguagesListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
) -> Response[PaginatedLanguageList]:
    """
    Args:
        id (int | Unset):
        language (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[LanguagesListPrefetchItem] | Unset):
        product (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedLanguageList]
    """

    kwargs = _get_kwargs(
        id=id,
        language=language,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        product=product,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    language: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[LanguagesListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
) -> PaginatedLanguageList | None:
    """
    Args:
        id (int | Unset):
        language (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[LanguagesListPrefetchItem] | Unset):
        product (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedLanguageList
    """

    return sync_detailed(
        client=client,
        id=id,
        language=language,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        product=product,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    language: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[LanguagesListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
) -> Response[PaginatedLanguageList]:
    """
    Args:
        id (int | Unset):
        language (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[LanguagesListPrefetchItem] | Unset):
        product (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedLanguageList]
    """

    kwargs = _get_kwargs(
        id=id,
        language=language,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        product=product,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    language: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[LanguagesListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
) -> PaginatedLanguageList | None:
    """
    Args:
        id (int | Unset):
        language (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[LanguagesListPrefetchItem] | Unset):
        product (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedLanguageList
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            language=language,
            limit=limit,
            offset=offset,
            prefetch=prefetch,
            product=product,
        )
    ).parsed
