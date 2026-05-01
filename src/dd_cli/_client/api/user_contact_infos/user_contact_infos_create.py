from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_contact_info import UserContactInfo
from ...models.user_contact_info_request import UserContactInfoRequest
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: UserContactInfoRequest | UserContactInfoRequest | UserContactInfoRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/user_contact_infos/",
    }

    if isinstance(body, UserContactInfoRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UserContactInfoRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, UserContactInfoRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UserContactInfo | None:
    if response.status_code == 201:
        response_201 = UserContactInfo.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UserContactInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UserContactInfoRequest | UserContactInfoRequest | UserContactInfoRequest | Unset = UNSET,
) -> Response[UserContactInfo]:
    """
    Args:
        body (UserContactInfoRequest):
        body (UserContactInfoRequest):
        body (UserContactInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserContactInfo]
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
    body: UserContactInfoRequest | UserContactInfoRequest | UserContactInfoRequest | Unset = UNSET,
) -> UserContactInfo | None:
    """
    Args:
        body (UserContactInfoRequest):
        body (UserContactInfoRequest):
        body (UserContactInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserContactInfo
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UserContactInfoRequest | UserContactInfoRequest | UserContactInfoRequest | Unset = UNSET,
) -> Response[UserContactInfo]:
    """
    Args:
        body (UserContactInfoRequest):
        body (UserContactInfoRequest):
        body (UserContactInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserContactInfo]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UserContactInfoRequest | UserContactInfoRequest | UserContactInfoRequest | Unset = UNSET,
) -> UserContactInfo | None:
    """
    Args:
        body (UserContactInfoRequest):
        body (UserContactInfoRequest):
        body (UserContactInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserContactInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
