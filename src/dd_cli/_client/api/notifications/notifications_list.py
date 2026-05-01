from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.notifications_list_prefetch_item import NotificationsListPrefetchItem
from ...models.paginated_notifications_list import PaginatedNotificationsList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[NotificationsListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
    template: bool | Unset = UNSET,
    user: int | Unset = UNSET,
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

    params["product"] = product

    params["template"] = template

    params["user"] = user

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/notifications/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedNotificationsList | None:
    if response.status_code == 200:
        response_200 = PaginatedNotificationsList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedNotificationsList]:
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
    prefetch: list[NotificationsListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
    template: bool | Unset = UNSET,
    user: int | Unset = UNSET,
) -> Response[PaginatedNotificationsList]:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[NotificationsListPrefetchItem] | Unset):
        product (int | Unset):
        template (bool | Unset):
        user (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedNotificationsList]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        product=product,
        template=template,
        user=user,
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
    prefetch: list[NotificationsListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
    template: bool | Unset = UNSET,
    user: int | Unset = UNSET,
) -> PaginatedNotificationsList | None:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[NotificationsListPrefetchItem] | Unset):
        product (int | Unset):
        template (bool | Unset):
        user (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedNotificationsList
    """

    return sync_detailed(
        client=client,
        id=id,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        product=product,
        template=template,
        user=user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[NotificationsListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
    template: bool | Unset = UNSET,
    user: int | Unset = UNSET,
) -> Response[PaginatedNotificationsList]:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[NotificationsListPrefetchItem] | Unset):
        product (int | Unset):
        template (bool | Unset):
        user (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedNotificationsList]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        product=product,
        template=template,
        user=user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[NotificationsListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
    template: bool | Unset = UNSET,
    user: int | Unset = UNSET,
) -> PaginatedNotificationsList | None:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[NotificationsListPrefetchItem] | Unset):
        product (int | Unset):
        template (bool | Unset):
        user (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedNotificationsList
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            limit=limit,
            offset=offset,
            prefetch=prefetch,
            product=product,
            template=template,
            user=user,
        )
    ).parsed
