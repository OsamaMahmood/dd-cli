from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.credential_mapping import CredentialMapping
from ...models.patched_credential_mapping_request import PatchedCredentialMappingRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: PatchedCredentialMappingRequest
    | PatchedCredentialMappingRequest
    | PatchedCredentialMappingRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/credential_mappings/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, PatchedCredentialMappingRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedCredentialMappingRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedCredentialMappingRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CredentialMapping | None:
    if response.status_code == 200:
        response_200 = CredentialMapping.from_dict(response.json())

        return response_200

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
    id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedCredentialMappingRequest
    | PatchedCredentialMappingRequest
    | PatchedCredentialMappingRequest
    | Unset = UNSET,
) -> Response[CredentialMapping]:
    """
    Args:
        id (int):
        body (PatchedCredentialMappingRequest | Unset):
        body (PatchedCredentialMappingRequest | Unset):
        body (PatchedCredentialMappingRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CredentialMapping]
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
    body: PatchedCredentialMappingRequest
    | PatchedCredentialMappingRequest
    | PatchedCredentialMappingRequest
    | Unset = UNSET,
) -> CredentialMapping | None:
    """
    Args:
        id (int):
        body (PatchedCredentialMappingRequest | Unset):
        body (PatchedCredentialMappingRequest | Unset):
        body (PatchedCredentialMappingRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CredentialMapping
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
    body: PatchedCredentialMappingRequest
    | PatchedCredentialMappingRequest
    | PatchedCredentialMappingRequest
    | Unset = UNSET,
) -> Response[CredentialMapping]:
    """
    Args:
        id (int):
        body (PatchedCredentialMappingRequest | Unset):
        body (PatchedCredentialMappingRequest | Unset):
        body (PatchedCredentialMappingRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CredentialMapping]
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
    body: PatchedCredentialMappingRequest
    | PatchedCredentialMappingRequest
    | PatchedCredentialMappingRequest
    | Unset = UNSET,
) -> CredentialMapping | None:
    """
    Args:
        id (int):
        body (PatchedCredentialMappingRequest | Unset):
        body (PatchedCredentialMappingRequest | Unset):
        body (PatchedCredentialMappingRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CredentialMapping
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
