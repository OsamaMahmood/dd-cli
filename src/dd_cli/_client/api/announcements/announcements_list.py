from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.announcements_list_style import AnnouncementsListStyle
from ...models.paginated_announcement_list import PaginatedAnnouncementList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    dismissable: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    message: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    style: AnnouncementsListStyle | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["dismissable"] = dismissable

    params["limit"] = limit

    params["message"] = message

    params["offset"] = offset

    json_style: str | Unset = UNSET
    if not isinstance(style, Unset):
        json_style = style.value

    params["style"] = json_style

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/announcements/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedAnnouncementList | None:
    if response.status_code == 200:
        response_200 = PaginatedAnnouncementList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedAnnouncementList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    dismissable: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    message: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    style: AnnouncementsListStyle | Unset = UNSET,
) -> Response[PaginatedAnnouncementList]:
    """
    Args:
        dismissable (bool | Unset):
        limit (int | Unset):
        message (str | Unset):
        offset (int | Unset):
        style (AnnouncementsListStyle | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAnnouncementList]
    """

    kwargs = _get_kwargs(
        dismissable=dismissable,
        limit=limit,
        message=message,
        offset=offset,
        style=style,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    dismissable: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    message: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    style: AnnouncementsListStyle | Unset = UNSET,
) -> PaginatedAnnouncementList | None:
    """
    Args:
        dismissable (bool | Unset):
        limit (int | Unset):
        message (str | Unset):
        offset (int | Unset):
        style (AnnouncementsListStyle | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAnnouncementList
    """

    return sync_detailed(
        client=client,
        dismissable=dismissable,
        limit=limit,
        message=message,
        offset=offset,
        style=style,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    dismissable: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    message: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    style: AnnouncementsListStyle | Unset = UNSET,
) -> Response[PaginatedAnnouncementList]:
    """
    Args:
        dismissable (bool | Unset):
        limit (int | Unset):
        message (str | Unset):
        offset (int | Unset):
        style (AnnouncementsListStyle | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAnnouncementList]
    """

    kwargs = _get_kwargs(
        dismissable=dismissable,
        limit=limit,
        message=message,
        offset=offset,
        style=style,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    dismissable: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    message: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    style: AnnouncementsListStyle | Unset = UNSET,
) -> PaginatedAnnouncementList | None:
    """
    Args:
        dismissable (bool | Unset):
        limit (int | Unset):
        message (str | Unset):
        offset (int | Unset):
        style (AnnouncementsListStyle | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAnnouncementList
    """

    return (
        await asyncio_detailed(
            client=client,
            dismissable=dismissable,
            limit=limit,
            message=message,
            offset=offset,
            style=style,
        )
    ).parsed
