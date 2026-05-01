import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_product_type_list import PaginatedProductTypeList
from ...models.product_types_list_prefetch_item import ProductTypesListPrefetchItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created: datetime.datetime | Unset = UNSET,
    critical_product: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    key_product: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[ProductTypesListPrefetchItem] | Unset = UNSET,
    updated: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_created: str | Unset = UNSET
    if not isinstance(created, Unset):
        json_created = created.isoformat()
    params["created"] = json_created

    params["critical_product"] = critical_product

    params["id"] = id

    params["key_product"] = key_product

    params["limit"] = limit

    params["name"] = name

    params["offset"] = offset

    json_prefetch: list[str] | Unset = UNSET
    if not isinstance(prefetch, Unset):
        json_prefetch = []
        for prefetch_item_data in prefetch:
            prefetch_item = prefetch_item_data.value
            json_prefetch.append(prefetch_item)

    params["prefetch"] = json_prefetch

    json_updated: str | Unset = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/product_types/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedProductTypeList | None:
    if response.status_code == 200:
        response_200 = PaginatedProductTypeList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedProductTypeList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    created: datetime.datetime | Unset = UNSET,
    critical_product: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    key_product: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[ProductTypesListPrefetchItem] | Unset = UNSET,
    updated: datetime.datetime | Unset = UNSET,
) -> Response[PaginatedProductTypeList]:
    """
    Args:
        created (datetime.datetime | Unset):
        critical_product (bool | Unset):
        id (int | Unset):
        key_product (bool | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        prefetch (list[ProductTypesListPrefetchItem] | Unset):
        updated (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedProductTypeList]
    """

    kwargs = _get_kwargs(
        created=created,
        critical_product=critical_product,
        id=id,
        key_product=key_product,
        limit=limit,
        name=name,
        offset=offset,
        prefetch=prefetch,
        updated=updated,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    created: datetime.datetime | Unset = UNSET,
    critical_product: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    key_product: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[ProductTypesListPrefetchItem] | Unset = UNSET,
    updated: datetime.datetime | Unset = UNSET,
) -> PaginatedProductTypeList | None:
    """
    Args:
        created (datetime.datetime | Unset):
        critical_product (bool | Unset):
        id (int | Unset):
        key_product (bool | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        prefetch (list[ProductTypesListPrefetchItem] | Unset):
        updated (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedProductTypeList
    """

    return sync_detailed(
        client=client,
        created=created,
        critical_product=critical_product,
        id=id,
        key_product=key_product,
        limit=limit,
        name=name,
        offset=offset,
        prefetch=prefetch,
        updated=updated,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    created: datetime.datetime | Unset = UNSET,
    critical_product: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    key_product: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[ProductTypesListPrefetchItem] | Unset = UNSET,
    updated: datetime.datetime | Unset = UNSET,
) -> Response[PaginatedProductTypeList]:
    """
    Args:
        created (datetime.datetime | Unset):
        critical_product (bool | Unset):
        id (int | Unset):
        key_product (bool | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        prefetch (list[ProductTypesListPrefetchItem] | Unset):
        updated (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedProductTypeList]
    """

    kwargs = _get_kwargs(
        created=created,
        critical_product=critical_product,
        id=id,
        key_product=key_product,
        limit=limit,
        name=name,
        offset=offset,
        prefetch=prefetch,
        updated=updated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    created: datetime.datetime | Unset = UNSET,
    critical_product: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    key_product: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[ProductTypesListPrefetchItem] | Unset = UNSET,
    updated: datetime.datetime | Unset = UNSET,
) -> PaginatedProductTypeList | None:
    """
    Args:
        created (datetime.datetime | Unset):
        critical_product (bool | Unset):
        id (int | Unset):
        key_product (bool | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        prefetch (list[ProductTypesListPrefetchItem] | Unset):
        updated (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedProductTypeList
    """

    return (
        await asyncio_detailed(
            client=client,
            created=created,
            critical_product=critical_product,
            id=id,
            key_product=key_product,
            limit=limit,
            name=name,
            offset=offset,
            prefetch=prefetch,
            updated=updated,
        )
    ).parsed
