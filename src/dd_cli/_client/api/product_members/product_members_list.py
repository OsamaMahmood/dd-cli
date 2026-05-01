from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_product_member_list import PaginatedProductMemberList
from ...models.product_members_list_prefetch_item import ProductMembersListPrefetchItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[ProductMembersListPrefetchItem] | Unset = UNSET,
    product_id: int | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params["limit"] = limit

    params["offset"] = offset

    json_prefetch: list[str] | Unset = UNSET
    if not isinstance(prefetch, Unset):
        json_prefetch = []
        for prefetch_item_data in prefetch:
            prefetch_item = prefetch_item_data.value
            json_prefetch.append(prefetch_item)

    params["prefetch"] = json_prefetch

    params["product_id"] = product_id

    params["user_id"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/product_members/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedProductMemberList | None:
    if response.status_code == 200:
        response_200 = PaginatedProductMemberList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedProductMemberList]:
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
    prefetch: list[ProductMembersListPrefetchItem] | Unset = UNSET,
    product_id: int | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> Response[PaginatedProductMemberList]:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[ProductMembersListPrefetchItem] | Unset):
        product_id (int | Unset):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedProductMemberList]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        product_id=product_id,
        user_id=user_id,
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
    prefetch: list[ProductMembersListPrefetchItem] | Unset = UNSET,
    product_id: int | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> PaginatedProductMemberList | None:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[ProductMembersListPrefetchItem] | Unset):
        product_id (int | Unset):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedProductMemberList
    """

    return sync_detailed(
        client=client,
        id=id,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        product_id=product_id,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[ProductMembersListPrefetchItem] | Unset = UNSET,
    product_id: int | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> Response[PaginatedProductMemberList]:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[ProductMembersListPrefetchItem] | Unset):
        product_id (int | Unset):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedProductMemberList]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        product_id=product_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[ProductMembersListPrefetchItem] | Unset = UNSET,
    product_id: int | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> PaginatedProductMemberList | None:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[ProductMembersListPrefetchItem] | Unset):
        product_id (int | Unset):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedProductMemberList
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            limit=limit,
            offset=offset,
            prefetch=prefetch,
            product_id=product_id,
            user_id=user_id,
        )
    ).parsed
