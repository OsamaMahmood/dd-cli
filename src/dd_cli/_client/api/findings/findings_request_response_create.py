from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.burp_raw_request_response import BurpRawRequestResponse
from ...models.burp_raw_request_response_request import BurpRawRequestResponseRequest
from ...types import UNSET, Response


def _get_kwargs(
    id: int,
    *,
    body: BurpRawRequestResponseRequest
    | BurpRawRequestResponseRequest
    | BurpRawRequestResponseRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/findings/{id}/request_response/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, BurpRawRequestResponseRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, BurpRawRequestResponseRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, BurpRawRequestResponseRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BurpRawRequestResponse | None:
    if response.status_code == 201:
        response_201 = BurpRawRequestResponse.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BurpRawRequestResponse]:
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
    body: BurpRawRequestResponseRequest
    | BurpRawRequestResponseRequest
    | BurpRawRequestResponseRequest
    | Unset = UNSET,
) -> Response[BurpRawRequestResponse]:
    """
    Args:
        id (int):
        body (BurpRawRequestResponseRequest):
        body (BurpRawRequestResponseRequest):
        body (BurpRawRequestResponseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BurpRawRequestResponse]
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
    body: BurpRawRequestResponseRequest
    | BurpRawRequestResponseRequest
    | BurpRawRequestResponseRequest
    | Unset = UNSET,
) -> BurpRawRequestResponse | None:
    """
    Args:
        id (int):
        body (BurpRawRequestResponseRequest):
        body (BurpRawRequestResponseRequest):
        body (BurpRawRequestResponseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BurpRawRequestResponse
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
    body: BurpRawRequestResponseRequest
    | BurpRawRequestResponseRequest
    | BurpRawRequestResponseRequest
    | Unset = UNSET,
) -> Response[BurpRawRequestResponse]:
    """
    Args:
        id (int):
        body (BurpRawRequestResponseRequest):
        body (BurpRawRequestResponseRequest):
        body (BurpRawRequestResponseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BurpRawRequestResponse]
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
    body: BurpRawRequestResponseRequest
    | BurpRawRequestResponseRequest
    | BurpRawRequestResponseRequest
    | Unset = UNSET,
) -> BurpRawRequestResponse | None:
    """
    Args:
        id (int):
        body (BurpRawRequestResponseRequest):
        body (BurpRawRequestResponseRequest):
        body (BurpRawRequestResponseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BurpRawRequestResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
