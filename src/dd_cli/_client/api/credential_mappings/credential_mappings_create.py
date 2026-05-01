from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.credential_mapping import CredentialMapping
from ...models.credential_mapping_request import CredentialMappingRequest
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: CredentialMappingRequest
    | CredentialMappingRequest
    | CredentialMappingRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/credential_mappings/",
    }

    if isinstance(body, CredentialMappingRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CredentialMappingRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, CredentialMappingRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CredentialMapping | None:
    if response.status_code == 201:
        response_201 = CredentialMapping.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CredentialMapping]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CredentialMappingRequest
    | CredentialMappingRequest
    | CredentialMappingRequest
    | Unset = UNSET,
) -> Response[CredentialMapping]:
    """
    Args:
        body (CredentialMappingRequest):
        body (CredentialMappingRequest):
        body (CredentialMappingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CredentialMapping]
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
    body: CredentialMappingRequest
    | CredentialMappingRequest
    | CredentialMappingRequest
    | Unset = UNSET,
) -> CredentialMapping | None:
    """
    Args:
        body (CredentialMappingRequest):
        body (CredentialMappingRequest):
        body (CredentialMappingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CredentialMapping
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CredentialMappingRequest
    | CredentialMappingRequest
    | CredentialMappingRequest
    | Unset = UNSET,
) -> Response[CredentialMapping]:
    """
    Args:
        body (CredentialMappingRequest):
        body (CredentialMappingRequest):
        body (CredentialMappingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CredentialMapping]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CredentialMappingRequest
    | CredentialMappingRequest
    | CredentialMappingRequest
    | Unset = UNSET,
) -> CredentialMapping | None:
    """
    Args:
        body (CredentialMappingRequest):
        body (CredentialMappingRequest):
        body (CredentialMappingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CredentialMapping
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
