from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dojo_group_member import DojoGroupMember
from ...models.dojo_group_member_request import DojoGroupMemberRequest
from ...types import UNSET, Response


def _get_kwargs(
    id: int,
    *,
    body: DojoGroupMemberRequest | DojoGroupMemberRequest | DojoGroupMemberRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/dojo_group_members/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, DojoGroupMemberRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, DojoGroupMemberRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, DojoGroupMemberRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
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
    body: DojoGroupMemberRequest | DojoGroupMemberRequest | DojoGroupMemberRequest | Unset = UNSET,
) -> Response[DojoGroupMember]:
    """
    Args:
        id (int):
        body (DojoGroupMemberRequest):
        body (DojoGroupMemberRequest):
        body (DojoGroupMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DojoGroupMember]
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
    body: DojoGroupMemberRequest | DojoGroupMemberRequest | DojoGroupMemberRequest | Unset = UNSET,
) -> DojoGroupMember | None:
    """
    Args:
        id (int):
        body (DojoGroupMemberRequest):
        body (DojoGroupMemberRequest):
        body (DojoGroupMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DojoGroupMember
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
    body: DojoGroupMemberRequest | DojoGroupMemberRequest | DojoGroupMemberRequest | Unset = UNSET,
) -> Response[DojoGroupMember]:
    """
    Args:
        id (int):
        body (DojoGroupMemberRequest):
        body (DojoGroupMemberRequest):
        body (DojoGroupMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DojoGroupMember]
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
    body: DojoGroupMemberRequest | DojoGroupMemberRequest | DojoGroupMemberRequest | Unset = UNSET,
) -> DojoGroupMember | None:
    """
    Args:
        id (int):
        body (DojoGroupMemberRequest):
        body (DojoGroupMemberRequest):
        body (DojoGroupMemberRequest):

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
            body=body,
        )
    ).parsed
