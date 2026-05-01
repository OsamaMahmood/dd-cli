from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_members_list_prefetch_item import AssetMembersListPrefetchItem
from ...models.paginated_asset_member_list import PaginatedAssetMemberList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    asset_id: float | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[AssetMembersListPrefetchItem] | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["asset_id"] = asset_id

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

    params["user_id"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/asset_members/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedAssetMemberList | None:
    if response.status_code == 200:
        response_200 = PaginatedAssetMemberList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedAssetMemberList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    asset_id: float | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[AssetMembersListPrefetchItem] | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> Response[PaginatedAssetMemberList]:
    """
    Args:
        asset_id (float | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[AssetMembersListPrefetchItem] | Unset):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAssetMemberList]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        id=id,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    asset_id: float | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[AssetMembersListPrefetchItem] | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> PaginatedAssetMemberList | None:
    """
    Args:
        asset_id (float | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[AssetMembersListPrefetchItem] | Unset):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAssetMemberList
    """

    return sync_detailed(
        client=client,
        asset_id=asset_id,
        id=id,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    asset_id: float | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[AssetMembersListPrefetchItem] | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> Response[PaginatedAssetMemberList]:
    """
    Args:
        asset_id (float | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[AssetMembersListPrefetchItem] | Unset):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAssetMemberList]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        id=id,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    asset_id: float | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[AssetMembersListPrefetchItem] | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> PaginatedAssetMemberList | None:
    """
    Args:
        asset_id (float | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[AssetMembersListPrefetchItem] | Unset):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAssetMemberList
    """

    return (
        await asyncio_detailed(
            client=client,
            asset_id=asset_id,
            id=id,
            limit=limit,
            offset=offset,
            prefetch=prefetch,
            user_id=user_id,
        )
    ).parsed
