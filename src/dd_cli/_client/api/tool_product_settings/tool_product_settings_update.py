from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tool_product_settings import ToolProductSettings
from ...models.tool_product_settings_request import ToolProductSettingsRequest
from ...types import UNSET, Response


def _get_kwargs(
    id: int,
    *,
    body: ToolProductSettingsRequest
    | ToolProductSettingsRequest
    | ToolProductSettingsRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/tool_product_settings/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, ToolProductSettingsRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, ToolProductSettingsRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ToolProductSettingsRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ToolProductSettings | None:
    if response.status_code == 200:
        response_200 = ToolProductSettings.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ToolProductSettings]:
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
    body: ToolProductSettingsRequest
    | ToolProductSettingsRequest
    | ToolProductSettingsRequest
    | Unset = UNSET,
) -> Response[ToolProductSettings]:
    """
    Args:
        id (int):
        body (ToolProductSettingsRequest):
        body (ToolProductSettingsRequest):
        body (ToolProductSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ToolProductSettings]
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
    body: ToolProductSettingsRequest
    | ToolProductSettingsRequest
    | ToolProductSettingsRequest
    | Unset = UNSET,
) -> ToolProductSettings | None:
    """
    Args:
        id (int):
        body (ToolProductSettingsRequest):
        body (ToolProductSettingsRequest):
        body (ToolProductSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ToolProductSettings
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
    body: ToolProductSettingsRequest
    | ToolProductSettingsRequest
    | ToolProductSettingsRequest
    | Unset = UNSET,
) -> Response[ToolProductSettings]:
    """
    Args:
        id (int):
        body (ToolProductSettingsRequest):
        body (ToolProductSettingsRequest):
        body (ToolProductSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ToolProductSettings]
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
    body: ToolProductSettingsRequest
    | ToolProductSettingsRequest
    | ToolProductSettingsRequest
    | Unset = UNSET,
) -> ToolProductSettings | None:
    """
    Args:
        id (int):
        body (ToolProductSettingsRequest):
        body (ToolProductSettingsRequest):
        body (ToolProductSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ToolProductSettings
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
