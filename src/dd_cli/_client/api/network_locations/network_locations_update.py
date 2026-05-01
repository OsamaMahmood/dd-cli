from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.network_locations import NetworkLocations
from ...models.network_locations_request import NetworkLocationsRequest
from ...types import UNSET, Response


def _get_kwargs(
    id: int,
    *,
    body: NetworkLocationsRequest
    | NetworkLocationsRequest
    | NetworkLocationsRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/network_locations/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, NetworkLocationsRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, NetworkLocationsRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, NetworkLocationsRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> NetworkLocations | None:
    if response.status_code == 200:
        response_200 = NetworkLocations.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[NetworkLocations]:
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
    body: NetworkLocationsRequest
    | NetworkLocationsRequest
    | NetworkLocationsRequest
    | Unset = UNSET,
) -> Response[NetworkLocations]:
    """
    Args:
        id (int):
        body (NetworkLocationsRequest):
        body (NetworkLocationsRequest):
        body (NetworkLocationsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NetworkLocations]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: NetworkLocationsRequest
    | NetworkLocationsRequest
    | NetworkLocationsRequest
    | Unset = UNSET,
) -> NetworkLocations | None:
    """
    Args:
        id (int):
        body (NetworkLocationsRequest):
        body (NetworkLocationsRequest):
        body (NetworkLocationsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NetworkLocations
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: NetworkLocationsRequest
    | NetworkLocationsRequest
    | NetworkLocationsRequest
    | Unset = UNSET,
) -> Response[NetworkLocations]:
    """
    Args:
        id (int):
        body (NetworkLocationsRequest):
        body (NetworkLocationsRequest):
        body (NetworkLocationsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NetworkLocations]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: NetworkLocationsRequest
    | NetworkLocationsRequest
    | NetworkLocationsRequest
    | Unset = UNSET,
) -> NetworkLocations | None:
    """
    Args:
        id (int):
        body (NetworkLocationsRequest):
        body (NetworkLocationsRequest):
        body (NetworkLocationsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NetworkLocations
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
