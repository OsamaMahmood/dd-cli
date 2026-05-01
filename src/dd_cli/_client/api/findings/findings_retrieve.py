from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.finding import Finding
from ...models.findings_retrieve_prefetch_item import FindingsRetrievePrefetchItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    prefetch: list[FindingsRetrievePrefetchItem] | Unset = UNSET,
    related_fields: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_prefetch: list[str] | Unset = UNSET
    if not isinstance(prefetch, Unset):
        json_prefetch = []
        for prefetch_item_data in prefetch:
            prefetch_item = prefetch_item_data.value
            json_prefetch.append(prefetch_item)

    params["prefetch"] = json_prefetch

    params["related_fields"] = related_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/findings/{id}/".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Finding | None:
    if response.status_code == 200:
        response_200 = Finding.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Finding]:
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
    prefetch: list[FindingsRetrievePrefetchItem] | Unset = UNSET,
    related_fields: bool | Unset = UNSET,
) -> Response[Finding]:
    """
    Args:
        id (int):
        prefetch (list[FindingsRetrievePrefetchItem] | Unset):
        related_fields (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Finding]
    """

    kwargs = _get_kwargs(
        id=id,
        prefetch=prefetch,
        related_fields=related_fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    prefetch: list[FindingsRetrievePrefetchItem] | Unset = UNSET,
    related_fields: bool | Unset = UNSET,
) -> Finding | None:
    """
    Args:
        id (int):
        prefetch (list[FindingsRetrievePrefetchItem] | Unset):
        related_fields (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Finding
    """

    return sync_detailed(
        id=id,
        client=client,
        prefetch=prefetch,
        related_fields=related_fields,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    prefetch: list[FindingsRetrievePrefetchItem] | Unset = UNSET,
    related_fields: bool | Unset = UNSET,
) -> Response[Finding]:
    """
    Args:
        id (int):
        prefetch (list[FindingsRetrievePrefetchItem] | Unset):
        related_fields (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Finding]
    """

    kwargs = _get_kwargs(
        id=id,
        prefetch=prefetch,
        related_fields=related_fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    prefetch: list[FindingsRetrievePrefetchItem] | Unset = UNSET,
    related_fields: bool | Unset = UNSET,
) -> Finding | None:
    """
    Args:
        id (int):
        prefetch (list[FindingsRetrievePrefetchItem] | Unset):
        related_fields (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Finding
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            prefetch=prefetch,
            related_fields=related_fields,
        )
    ).parsed
