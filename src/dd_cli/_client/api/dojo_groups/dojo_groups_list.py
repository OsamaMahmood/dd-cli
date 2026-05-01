from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dojo_groups_list_prefetch_item import DojoGroupsListPrefetchItem
from ...models.dojo_groups_list_social_authentication_provider import (
    DojoGroupsListSocialAuthenticationProvider,
)
from ...models.paginated_dojo_group_list import PaginatedDojoGroupList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[DojoGroupsListPrefetchItem] | Unset = UNSET,
    social_provider: DojoGroupsListSocialAuthenticationProvider | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

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

    json_social_provider: str | Unset = UNSET
    if not isinstance(social_provider, Unset):
        json_social_provider = social_provider.value

    params["social_provider"] = json_social_provider

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/dojo_groups/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedDojoGroupList | None:
    if response.status_code == 200:
        response_200 = PaginatedDojoGroupList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedDojoGroupList]:
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
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[DojoGroupsListPrefetchItem] | Unset = UNSET,
    social_provider: DojoGroupsListSocialAuthenticationProvider | Unset = UNSET,
) -> Response[PaginatedDojoGroupList]:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        prefetch (list[DojoGroupsListPrefetchItem] | Unset):
        social_provider (DojoGroupsListSocialAuthenticationProvider | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDojoGroupList]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        name=name,
        offset=offset,
        prefetch=prefetch,
        social_provider=social_provider,
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
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[DojoGroupsListPrefetchItem] | Unset = UNSET,
    social_provider: DojoGroupsListSocialAuthenticationProvider | Unset = UNSET,
) -> PaginatedDojoGroupList | None:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        prefetch (list[DojoGroupsListPrefetchItem] | Unset):
        social_provider (DojoGroupsListSocialAuthenticationProvider | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDojoGroupList
    """

    return sync_detailed(
        client=client,
        id=id,
        limit=limit,
        name=name,
        offset=offset,
        prefetch=prefetch,
        social_provider=social_provider,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[DojoGroupsListPrefetchItem] | Unset = UNSET,
    social_provider: DojoGroupsListSocialAuthenticationProvider | Unset = UNSET,
) -> Response[PaginatedDojoGroupList]:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        prefetch (list[DojoGroupsListPrefetchItem] | Unset):
        social_provider (DojoGroupsListSocialAuthenticationProvider | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDojoGroupList]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        name=name,
        offset=offset,
        prefetch=prefetch,
        social_provider=social_provider,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[DojoGroupsListPrefetchItem] | Unset = UNSET,
    social_provider: DojoGroupsListSocialAuthenticationProvider | Unset = UNSET,
) -> PaginatedDojoGroupList | None:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        prefetch (list[DojoGroupsListPrefetchItem] | Unset):
        social_provider (DojoGroupsListSocialAuthenticationProvider | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDojoGroupList
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            limit=limit,
            name=name,
            offset=offset,
            prefetch=prefetch,
            social_provider=social_provider,
        )
    ).parsed
