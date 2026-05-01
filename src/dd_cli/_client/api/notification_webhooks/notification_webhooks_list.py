import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.notification_webhooks_list_status import NotificationWebhooksListStatus
from ...models.paginated_notification_webhooks_list import PaginatedNotificationWebhooksList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    first_error: datetime.datetime | Unset = UNSET,
    header_name: str | Unset = UNSET,
    header_value: str | Unset = UNSET,
    last_error: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    note: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    owner: int | Unset = UNSET,
    status: NotificationWebhooksListStatus | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_first_error: str | Unset = UNSET
    if not isinstance(first_error, Unset):
        json_first_error = first_error.isoformat()
    params["first_error"] = json_first_error

    params["header_name"] = header_name

    params["header_value"] = header_value

    json_last_error: str | Unset = UNSET
    if not isinstance(last_error, Unset):
        json_last_error = last_error.isoformat()
    params["last_error"] = json_last_error

    params["limit"] = limit

    params["name"] = name

    params["note"] = note

    params["offset"] = offset

    params["owner"] = owner

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["url"] = url_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/notification_webhooks/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedNotificationWebhooksList | None:
    if response.status_code == 200:
        response_200 = PaginatedNotificationWebhooksList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedNotificationWebhooksList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    first_error: datetime.datetime | Unset = UNSET,
    header_name: str | Unset = UNSET,
    header_value: str | Unset = UNSET,
    last_error: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    note: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    owner: int | Unset = UNSET,
    status: NotificationWebhooksListStatus | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> Response[PaginatedNotificationWebhooksList]:
    """
    Args:
        first_error (datetime.datetime | Unset):
        header_name (str | Unset):
        header_value (str | Unset):
        last_error (datetime.datetime | Unset):
        limit (int | Unset):
        name (str | Unset):
        note (str | Unset):
        offset (int | Unset):
        owner (int | Unset):
        status (NotificationWebhooksListStatus | Unset):
        url_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedNotificationWebhooksList]
    """

    kwargs = _get_kwargs(
        first_error=first_error,
        header_name=header_name,
        header_value=header_value,
        last_error=last_error,
        limit=limit,
        name=name,
        note=note,
        offset=offset,
        owner=owner,
        status=status,
        url_query=url_query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    first_error: datetime.datetime | Unset = UNSET,
    header_name: str | Unset = UNSET,
    header_value: str | Unset = UNSET,
    last_error: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    note: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    owner: int | Unset = UNSET,
    status: NotificationWebhooksListStatus | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> PaginatedNotificationWebhooksList | None:
    """
    Args:
        first_error (datetime.datetime | Unset):
        header_name (str | Unset):
        header_value (str | Unset):
        last_error (datetime.datetime | Unset):
        limit (int | Unset):
        name (str | Unset):
        note (str | Unset):
        offset (int | Unset):
        owner (int | Unset):
        status (NotificationWebhooksListStatus | Unset):
        url_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedNotificationWebhooksList
    """

    return sync_detailed(
        client=client,
        first_error=first_error,
        header_name=header_name,
        header_value=header_value,
        last_error=last_error,
        limit=limit,
        name=name,
        note=note,
        offset=offset,
        owner=owner,
        status=status,
        url_query=url_query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    first_error: datetime.datetime | Unset = UNSET,
    header_name: str | Unset = UNSET,
    header_value: str | Unset = UNSET,
    last_error: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    note: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    owner: int | Unset = UNSET,
    status: NotificationWebhooksListStatus | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> Response[PaginatedNotificationWebhooksList]:
    """
    Args:
        first_error (datetime.datetime | Unset):
        header_name (str | Unset):
        header_value (str | Unset):
        last_error (datetime.datetime | Unset):
        limit (int | Unset):
        name (str | Unset):
        note (str | Unset):
        offset (int | Unset):
        owner (int | Unset):
        status (NotificationWebhooksListStatus | Unset):
        url_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedNotificationWebhooksList]
    """

    kwargs = _get_kwargs(
        first_error=first_error,
        header_name=header_name,
        header_value=header_value,
        last_error=last_error,
        limit=limit,
        name=name,
        note=note,
        offset=offset,
        owner=owner,
        status=status,
        url_query=url_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    first_error: datetime.datetime | Unset = UNSET,
    header_name: str | Unset = UNSET,
    header_value: str | Unset = UNSET,
    last_error: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    note: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    owner: int | Unset = UNSET,
    status: NotificationWebhooksListStatus | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> PaginatedNotificationWebhooksList | None:
    """
    Args:
        first_error (datetime.datetime | Unset):
        header_name (str | Unset):
        header_value (str | Unset):
        last_error (datetime.datetime | Unset):
        limit (int | Unset):
        name (str | Unset):
        note (str | Unset):
        offset (int | Unset):
        owner (int | Unset):
        status (NotificationWebhooksListStatus | Unset):
        url_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedNotificationWebhooksList
    """

    return (
        await asyncio_detailed(
            client=client,
            first_error=first_error,
            header_name=header_name,
            header_value=header_value,
            last_error=last_error,
            limit=limit,
            name=name,
            note=note,
            offset=offset,
            owner=owner,
            status=status,
            url_query=url_query,
        )
    ).parsed
