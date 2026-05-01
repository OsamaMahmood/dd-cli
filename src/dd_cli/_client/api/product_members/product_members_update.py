from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.product_member import ProductMember
from ...models.product_member_request import ProductMemberRequest
from ...types import UNSET, Response


def _get_kwargs(
    id: int,
    *,
    body: ProductMemberRequest | ProductMemberRequest | ProductMemberRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/product_members/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, ProductMemberRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, ProductMemberRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ProductMemberRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProductMember | None:
    if response.status_code == 200:
        response_200 = ProductMember.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProductMember]:
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
    body: ProductMemberRequest | ProductMemberRequest | ProductMemberRequest | Unset = UNSET,
) -> Response[ProductMember]:
    """
    Args:
        id (int):
        body (ProductMemberRequest):
        body (ProductMemberRequest):
        body (ProductMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProductMember]
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
    body: ProductMemberRequest | ProductMemberRequest | ProductMemberRequest | Unset = UNSET,
) -> ProductMember | None:
    """
    Args:
        id (int):
        body (ProductMemberRequest):
        body (ProductMemberRequest):
        body (ProductMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProductMember
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
    body: ProductMemberRequest | ProductMemberRequest | ProductMemberRequest | Unset = UNSET,
) -> Response[ProductMember]:
    """
    Args:
        id (int):
        body (ProductMemberRequest):
        body (ProductMemberRequest):
        body (ProductMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProductMember]
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
    body: ProductMemberRequest | ProductMemberRequest | ProductMemberRequest | Unset = UNSET,
) -> ProductMember | None:
    """
    Args:
        id (int):
        body (ProductMemberRequest):
        body (ProductMemberRequest):
        body (ProductMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProductMember
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
