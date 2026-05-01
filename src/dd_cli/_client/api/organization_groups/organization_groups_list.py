from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.organization_groups_list_prefetch_item import OrganizationGroupsListPrefetchItem
from ...models.paginated_organization_group_list import PaginatedOrganizationGroupList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    asset_type_id: float | Unset = UNSET,
    group_id: int | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[OrganizationGroupsListPrefetchItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["asset_type_id"] = asset_type_id

    params["group_id"] = group_id

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/organization_groups/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedOrganizationGroupList | None:
    if response.status_code == 200:
        response_200 = PaginatedOrganizationGroupList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedOrganizationGroupList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    asset_type_id: float | Unset = UNSET,
    group_id: int | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[OrganizationGroupsListPrefetchItem] | Unset = UNSET,
) -> Response[PaginatedOrganizationGroupList]:
    """
    Args:
        asset_type_id (float | Unset):
        group_id (int | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[OrganizationGroupsListPrefetchItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOrganizationGroupList]
    """

    kwargs = _get_kwargs(
        asset_type_id=asset_type_id,
        group_id=group_id,
        id=id,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    asset_type_id: float | Unset = UNSET,
    group_id: int | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[OrganizationGroupsListPrefetchItem] | Unset = UNSET,
) -> PaginatedOrganizationGroupList | None:
    """
    Args:
        asset_type_id (float | Unset):
        group_id (int | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[OrganizationGroupsListPrefetchItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedOrganizationGroupList
    """

    return sync_detailed(
        client=client,
        asset_type_id=asset_type_id,
        group_id=group_id,
        id=id,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    asset_type_id: float | Unset = UNSET,
    group_id: int | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[OrganizationGroupsListPrefetchItem] | Unset = UNSET,
) -> Response[PaginatedOrganizationGroupList]:
    """
    Args:
        asset_type_id (float | Unset):
        group_id (int | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[OrganizationGroupsListPrefetchItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOrganizationGroupList]
    """

    kwargs = _get_kwargs(
        asset_type_id=asset_type_id,
        group_id=group_id,
        id=id,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    asset_type_id: float | Unset = UNSET,
    group_id: int | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[OrganizationGroupsListPrefetchItem] | Unset = UNSET,
) -> PaginatedOrganizationGroupList | None:
    """
    Args:
        asset_type_id (float | Unset):
        group_id (int | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[OrganizationGroupsListPrefetchItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedOrganizationGroupList
    """

    return (
        await asyncio_detailed(
            client=client,
            asset_type_id=asset_type_id,
            group_id=group_id,
            id=id,
            limit=limit,
            offset=offset,
            prefetch=prefetch,
        )
    ).parsed
