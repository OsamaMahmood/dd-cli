from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.development_environment import DevelopmentEnvironment
from ...models.development_environment_request import DevelopmentEnvironmentRequest
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: DevelopmentEnvironmentRequest
    | DevelopmentEnvironmentRequest
    | DevelopmentEnvironmentRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/development_environments/",
    }

    if isinstance(body, DevelopmentEnvironmentRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, DevelopmentEnvironmentRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, DevelopmentEnvironmentRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DevelopmentEnvironment | None:
    if response.status_code == 201:
        response_201 = DevelopmentEnvironment.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DevelopmentEnvironment]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DevelopmentEnvironmentRequest
    | DevelopmentEnvironmentRequest
    | DevelopmentEnvironmentRequest
    | Unset = UNSET,
) -> Response[DevelopmentEnvironment]:
    """
    Args:
        body (DevelopmentEnvironmentRequest):
        body (DevelopmentEnvironmentRequest):
        body (DevelopmentEnvironmentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DevelopmentEnvironment]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: DevelopmentEnvironmentRequest
    | DevelopmentEnvironmentRequest
    | DevelopmentEnvironmentRequest
    | Unset = UNSET,
) -> DevelopmentEnvironment | None:
    """
    Args:
        body (DevelopmentEnvironmentRequest):
        body (DevelopmentEnvironmentRequest):
        body (DevelopmentEnvironmentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DevelopmentEnvironment
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DevelopmentEnvironmentRequest
    | DevelopmentEnvironmentRequest
    | DevelopmentEnvironmentRequest
    | Unset = UNSET,
) -> Response[DevelopmentEnvironment]:
    """
    Args:
        body (DevelopmentEnvironmentRequest):
        body (DevelopmentEnvironmentRequest):
        body (DevelopmentEnvironmentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DevelopmentEnvironment]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: DevelopmentEnvironmentRequest
    | DevelopmentEnvironmentRequest
    | DevelopmentEnvironmentRequest
    | Unset = UNSET,
) -> DevelopmentEnvironment | None:
    """
    Args:
        body (DevelopmentEnvironmentRequest):
        body (DevelopmentEnvironmentRequest):
        body (DevelopmentEnvironmentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DevelopmentEnvironment
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
