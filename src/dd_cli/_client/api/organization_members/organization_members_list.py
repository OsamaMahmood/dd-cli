from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.organization_members_list_prefetch_item import OrganizationMembersListPrefetchItem
from ...models.paginated_organization_member_list import PaginatedOrganizationMemberList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    organization_id: float | Unset = UNSET,
    prefetch: list[OrganizationMembersListPrefetchItem] | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params["limit"] = limit

    params["offset"] = offset

    params["organization_id"] = organization_id

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
        "url": "/api/v2/organization_members/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedOrganizationMemberList | None:
    if response.status_code == 200:
        response_200 = PaginatedOrganizationMemberList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedOrganizationMemberList]:
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
    organization_id: float | Unset = UNSET,
    prefetch: list[OrganizationMembersListPrefetchItem] | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> Response[PaginatedOrganizationMemberList]:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        organization_id (float | Unset):
        prefetch (list[OrganizationMembersListPrefetchItem] | Unset):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOrganizationMemberList]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        offset=offset,
        organization_id=organization_id,
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
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    organization_id: float | Unset = UNSET,
    prefetch: list[OrganizationMembersListPrefetchItem] | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> PaginatedOrganizationMemberList | None:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        organization_id (float | Unset):
        prefetch (list[OrganizationMembersListPrefetchItem] | Unset):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedOrganizationMemberList
    """

    return sync_detailed(
        client=client,
        id=id,
        limit=limit,
        offset=offset,
        organization_id=organization_id,
        prefetch=prefetch,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    organization_id: float | Unset = UNSET,
    prefetch: list[OrganizationMembersListPrefetchItem] | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> Response[PaginatedOrganizationMemberList]:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        organization_id (float | Unset):
        prefetch (list[OrganizationMembersListPrefetchItem] | Unset):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOrganizationMemberList]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        offset=offset,
        organization_id=organization_id,
        prefetch=prefetch,
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
    organization_id: float | Unset = UNSET,
    prefetch: list[OrganizationMembersListPrefetchItem] | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> PaginatedOrganizationMemberList | None:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        organization_id (float | Unset):
        prefetch (list[OrganizationMembersListPrefetchItem] | Unset):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedOrganizationMemberList
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            limit=limit,
            offset=offset,
            organization_id=organization_id,
            prefetch=prefetch,
            user_id=user_id,
        )
    ).parsed
