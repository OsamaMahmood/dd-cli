import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.organizations_list_prefetch_item import OrganizationsListPrefetchItem
from ...models.paginated_organization_list import PaginatedOrganizationList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created: datetime.datetime | Unset = UNSET,
    critical_asset: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    key_asset: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[OrganizationsListPrefetchItem] | Unset = UNSET,
    updated: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_created: str | Unset = UNSET
    if not isinstance(created, Unset):
        json_created = created.isoformat()
    params["created"] = json_created

    params["critical_asset"] = critical_asset

    params["id"] = id

    params["key_asset"] = key_asset

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
        "url": "/api/v2/organizations/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedOrganizationList | None:
    if response.status_code == 200:
        response_200 = PaginatedOrganizationList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedOrganizationList]:
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
    critical_asset: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    key_asset: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[OrganizationsListPrefetchItem] | Unset = UNSET,
    updated: datetime.datetime | Unset = UNSET,
) -> Response[PaginatedOrganizationList]:
    """
    Args:
        created (datetime.datetime | Unset):
        critical_asset (bool | Unset):
        id (int | Unset):
        key_asset (bool | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        prefetch (list[OrganizationsListPrefetchItem] | Unset):
        updated (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOrganizationList]
    """

    kwargs = _get_kwargs(
        created=created,
        critical_asset=critical_asset,
        id=id,
        key_asset=key_asset,
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
    critical_asset: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    key_asset: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[OrganizationsListPrefetchItem] | Unset = UNSET,
    updated: datetime.datetime | Unset = UNSET,
) -> PaginatedOrganizationList | None:
    """
    Args:
        created (datetime.datetime | Unset):
        critical_asset (bool | Unset):
        id (int | Unset):
        key_asset (bool | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        prefetch (list[OrganizationsListPrefetchItem] | Unset):
        updated (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedOrganizationList
    """

    return sync_detailed(
        client=client,
        created=created,
        critical_asset=critical_asset,
        id=id,
        key_asset=key_asset,
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
    critical_asset: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    key_asset: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[OrganizationsListPrefetchItem] | Unset = UNSET,
    updated: datetime.datetime | Unset = UNSET,
) -> Response[PaginatedOrganizationList]:
    """
    Args:
        created (datetime.datetime | Unset):
        critical_asset (bool | Unset):
        id (int | Unset):
        key_asset (bool | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        prefetch (list[OrganizationsListPrefetchItem] | Unset):
        updated (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOrganizationList]
    """

    kwargs = _get_kwargs(
        created=created,
        critical_asset=critical_asset,
        id=id,
        key_asset=key_asset,
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
    critical_asset: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    key_asset: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[OrganizationsListPrefetchItem] | Unset = UNSET,
    updated: datetime.datetime | Unset = UNSET,
) -> PaginatedOrganizationList | None:
    """
    Args:
        created (datetime.datetime | Unset):
        critical_asset (bool | Unset):
        id (int | Unset):
        key_asset (bool | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        prefetch (list[OrganizationsListPrefetchItem] | Unset):
        updated (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedOrganizationList
    """

    return (
        await asyncio_detailed(
            client=client,
            created=created,
            critical_asset=critical_asset,
            id=id,
            key_asset=key_asset,
            limit=limit,
            name=name,
            offset=offset,
            prefetch=prefetch,
            updated=updated,
        )
    ).parsed
