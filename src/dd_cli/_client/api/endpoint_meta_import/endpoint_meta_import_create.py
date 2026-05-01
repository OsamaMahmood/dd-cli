from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.endpoint_meta_importer import EndpointMetaImporter
from ...models.endpoint_meta_importer_request import EndpointMetaImporterRequest
from ...types import Response


def _get_kwargs(
    *,
    body: EndpointMetaImporterRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/endpoint_meta_import/",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EndpointMetaImporter | None:
    if response.status_code == 201:
        response_201 = EndpointMetaImporter.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EndpointMetaImporter]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: EndpointMetaImporterRequest,
) -> Response[EndpointMetaImporter]:
    """Imports a CSV file into a product to propagate arbitrary meta and tags on endpoints.

    By Names:
    - Provide `product_name` of existing product

    By ID:
    - Provide the id of the product in the `product` parameter

    In this scenario Defect Dojo will look up the product by the provided details.

    Args:
        body (EndpointMetaImporterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EndpointMetaImporter]
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
    body: EndpointMetaImporterRequest,
) -> EndpointMetaImporter | None:
    """Imports a CSV file into a product to propagate arbitrary meta and tags on endpoints.

    By Names:
    - Provide `product_name` of existing product

    By ID:
    - Provide the id of the product in the `product` parameter

    In this scenario Defect Dojo will look up the product by the provided details.

    Args:
        body (EndpointMetaImporterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EndpointMetaImporter
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: EndpointMetaImporterRequest,
) -> Response[EndpointMetaImporter]:
    """Imports a CSV file into a product to propagate arbitrary meta and tags on endpoints.

    By Names:
    - Provide `product_name` of existing product

    By ID:
    - Provide the id of the product in the `product` parameter

    In this scenario Defect Dojo will look up the product by the provided details.

    Args:
        body (EndpointMetaImporterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EndpointMetaImporter]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: EndpointMetaImporterRequest,
) -> EndpointMetaImporter | None:
    """Imports a CSV file into a product to propagate arbitrary meta and tags on endpoints.

    By Names:
    - Provide `product_name` of existing product

    By ID:
    - Provide the id of the product in the `product` parameter

    In this scenario Defect Dojo will look up the product by the provided details.

    Args:
        body (EndpointMetaImporterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EndpointMetaImporter
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
