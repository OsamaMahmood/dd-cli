from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.global_roles_list_prefetch_item import GlobalRolesListPrefetchItem
from ...models.paginated_global_role_list import PaginatedGlobalRoleList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    group: int | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[GlobalRolesListPrefetchItem] | Unset = UNSET,
    role: int | Unset = UNSET,
    user: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["group"] = group

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

    params["role"] = role

    params["user"] = user

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/global_roles/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedGlobalRoleList | None:
    if response.status_code == 200:
        response_200 = PaginatedGlobalRoleList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedGlobalRoleList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    group: int | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[GlobalRolesListPrefetchItem] | Unset = UNSET,
    role: int | Unset = UNSET,
    user: int | Unset = UNSET,
) -> Response[PaginatedGlobalRoleList]:
    """
    Args:
        group (int | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[GlobalRolesListPrefetchItem] | Unset):
        role (int | Unset):
        user (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedGlobalRoleList]
    """

    kwargs = _get_kwargs(
        group=group,
        id=id,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        role=role,
        user=user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    group: int | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[GlobalRolesListPrefetchItem] | Unset = UNSET,
    role: int | Unset = UNSET,
    user: int | Unset = UNSET,
) -> PaginatedGlobalRoleList | None:
    """
    Args:
        group (int | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[GlobalRolesListPrefetchItem] | Unset):
        role (int | Unset):
        user (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedGlobalRoleList
    """

    return sync_detailed(
        client=client,
        group=group,
        id=id,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        role=role,
        user=user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    group: int | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[GlobalRolesListPrefetchItem] | Unset = UNSET,
    role: int | Unset = UNSET,
    user: int | Unset = UNSET,
) -> Response[PaginatedGlobalRoleList]:
    """
    Args:
        group (int | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[GlobalRolesListPrefetchItem] | Unset):
        role (int | Unset):
        user (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedGlobalRoleList]
    """

    kwargs = _get_kwargs(
        group=group,
        id=id,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        role=role,
        user=user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    group: int | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[GlobalRolesListPrefetchItem] | Unset = UNSET,
    role: int | Unset = UNSET,
    user: int | Unset = UNSET,
) -> PaginatedGlobalRoleList | None:
    """
    Args:
        group (int | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[GlobalRolesListPrefetchItem] | Unset):
        role (int | Unset):
        user (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedGlobalRoleList
    """

    return (
        await asyncio_detailed(
            client=client,
            group=group,
            id=id,
            limit=limit,
            offset=offset,
            prefetch=prefetch,
            role=role,
            user=user,
        )
    ).parsed
