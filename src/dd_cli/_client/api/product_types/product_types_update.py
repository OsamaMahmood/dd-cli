from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.product_type import ProductType
from ...models.product_type_request import ProductTypeRequest
from ...types import UNSET, Response


def _get_kwargs(
    id: int,
    *,
    body: ProductTypeRequest | ProductTypeRequest | ProductTypeRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/product_types/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, ProductTypeRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, ProductTypeRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ProductTypeRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProductType | None:
    if response.status_code == 200:
        response_200 = ProductType.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProductType]:
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
    body: ProductTypeRequest | ProductTypeRequest | ProductTypeRequest | Unset = UNSET,
) -> Response[ProductType]:
    """
    Args:
        id (int):
        body (ProductTypeRequest):
        body (ProductTypeRequest):
        body (ProductTypeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProductType]
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
    body: ProductTypeRequest | ProductTypeRequest | ProductTypeRequest | Unset = UNSET,
) -> ProductType | None:
    """
    Args:
        id (int):
        body (ProductTypeRequest):
        body (ProductTypeRequest):
        body (ProductTypeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProductType
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
    body: ProductTypeRequest | ProductTypeRequest | ProductTypeRequest | Unset = UNSET,
) -> Response[ProductType]:
    """
    Args:
        id (int):
        body (ProductTypeRequest):
        body (ProductTypeRequest):
        body (ProductTypeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProductType]
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
    body: ProductTypeRequest | ProductTypeRequest | ProductTypeRequest | Unset = UNSET,
) -> ProductType | None:
    """
    Args:
        id (int):
        body (ProductTypeRequest):
        body (ProductTypeRequest):
        body (ProductTypeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProductType
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
