from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dojo_group_member import DojoGroupMember
from ...models.dojo_group_members_retrieve_prefetch_item import DojoGroupMembersRetrievePrefetchItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    prefetch: list[DojoGroupMembersRetrievePrefetchItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

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
        "url": "/api/v2/dojo_group_members/{id}/".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DojoGroupMember | None:
    if response.status_code == 200:
        response_200 = DojoGroupMember.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DojoGroupMember]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    prefetch: list[DojoGroupMembersRetrievePrefetchItem] | Unset = UNSET,
) -> Response[DojoGroupMember]:
    """
    Args:
        id (int):
        prefetch (list[DojoGroupMembersRetrievePrefetchItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DojoGroupMember]
    """

    kwargs = _get_kwargs(
        id=id,
        prefetch=prefetch,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    prefetch: list[DojoGroupMembersRetrievePrefetchItem] | Unset = UNSET,
) -> DojoGroupMember | None:
    """
    Args:
        id (int):
        prefetch (list[DojoGroupMembersRetrievePrefetchItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DojoGroupMember
    """

    return sync_detailed(
        id=id,
        client=client,
        prefetch=prefetch,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    prefetch: list[DojoGroupMembersRetrievePrefetchItem] | Unset = UNSET,
) -> Response[DojoGroupMember]:
    """
    Args:
        id (int):
        prefetch (list[DojoGroupMembersRetrievePrefetchItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DojoGroupMember]
    """

    kwargs = _get_kwargs(
        id=id,
        prefetch=prefetch,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    prefetch: list[DojoGroupMembersRetrievePrefetchItem] | Unset = UNSET,
) -> DojoGroupMember | None:
    """
    Args:
        id (int):
        prefetch (list[DojoGroupMembersRetrievePrefetchItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DojoGroupMember
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            prefetch=prefetch,
        )
    ).parsed
