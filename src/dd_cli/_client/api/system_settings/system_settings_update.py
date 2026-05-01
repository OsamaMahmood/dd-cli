from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.system_settings import SystemSettings
from ...models.system_settings_request import SystemSettingsRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: SystemSettingsRequest | SystemSettingsRequest | SystemSettingsRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/system_settings/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, SystemSettingsRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, SystemSettingsRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, SystemSettingsRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SystemSettings | None:
    if response.status_code == 200:
        response_200 = SystemSettings.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SystemSettings]:
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
    body: SystemSettingsRequest | SystemSettingsRequest | SystemSettingsRequest | Unset = UNSET,
) -> Response[SystemSettings]:
    """Basic control over System Settings. Use 'id' 1 for PUT, PATCH operations

    Args:
        id (int):
        body (SystemSettingsRequest | Unset):
        body (SystemSettingsRequest | Unset):
        body (SystemSettingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SystemSettings]
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
    body: SystemSettingsRequest | SystemSettingsRequest | SystemSettingsRequest | Unset = UNSET,
) -> SystemSettings | None:
    """Basic control over System Settings. Use 'id' 1 for PUT, PATCH operations

    Args:
        id (int):
        body (SystemSettingsRequest | Unset):
        body (SystemSettingsRequest | Unset):
        body (SystemSettingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SystemSettings
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
    body: SystemSettingsRequest | SystemSettingsRequest | SystemSettingsRequest | Unset = UNSET,
) -> Response[SystemSettings]:
    """Basic control over System Settings. Use 'id' 1 for PUT, PATCH operations

    Args:
        id (int):
        body (SystemSettingsRequest | Unset):
        body (SystemSettingsRequest | Unset):
        body (SystemSettingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SystemSettings]
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
    body: SystemSettingsRequest | SystemSettingsRequest | SystemSettingsRequest | Unset = UNSET,
) -> SystemSettings | None:
    """Basic control over System Settings. Use 'id' 1 for PUT, PATCH operations

    Args:
        id (int):
        body (SystemSettingsRequest | Unset):
        body (SystemSettingsRequest | Unset):
        body (SystemSettingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SystemSettings
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
