from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.re_import_scan import ReImportScan
from ...models.re_import_scan_request import ReImportScanRequest
from ...types import Response


def _get_kwargs(
    *,
    body: ReImportScanRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/reimport-scan/",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ReImportScan | None:
    if response.status_code == 201:
        response_201 = ReImportScan.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ReImportScan]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ReImportScanRequest,
) -> Response[ReImportScan]:
    """Reimports a scan report into an existing test.

    By ID:
    - Create a Product (or use an existing product)
    - Create an Engagement inside the product
    - Import a scan report and find the id of the Test
    - Provide this in the `test` parameter

    By Names:
    - Create a Product (or use an existing product)
    - Create an Engagement inside the product
    - Import a report which will create a Test
    - Provide `product_name`
    - Provide `engagement_name`
    - Optional: Provide `test_title`

    In this scenario Defect Dojo will look up the Test by the provided details.
    If no `test_title` is provided, the latest test inside the engagement will be chosen based on
    scan_type.

    When using names you can let the importer automatically create Engagements, Products and
    Product_Types
    by using `auto_create_context=True`.

    When `auto_create_context` is set to `True` you can use `deduplication_on_engagement` to restrict
    deduplication for
    imported Findings to the newly created Engagement.

    Args:
        body (ReImportScanRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReImportScan]
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
    body: ReImportScanRequest,
) -> ReImportScan | None:
    """Reimports a scan report into an existing test.

    By ID:
    - Create a Product (or use an existing product)
    - Create an Engagement inside the product
    - Import a scan report and find the id of the Test
    - Provide this in the `test` parameter

    By Names:
    - Create a Product (or use an existing product)
    - Create an Engagement inside the product
    - Import a report which will create a Test
    - Provide `product_name`
    - Provide `engagement_name`
    - Optional: Provide `test_title`

    In this scenario Defect Dojo will look up the Test by the provided details.
    If no `test_title` is provided, the latest test inside the engagement will be chosen based on
    scan_type.

    When using names you can let the importer automatically create Engagements, Products and
    Product_Types
    by using `auto_create_context=True`.

    When `auto_create_context` is set to `True` you can use `deduplication_on_engagement` to restrict
    deduplication for
    imported Findings to the newly created Engagement.

    Args:
        body (ReImportScanRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReImportScan
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ReImportScanRequest,
) -> Response[ReImportScan]:
    """Reimports a scan report into an existing test.

    By ID:
    - Create a Product (or use an existing product)
    - Create an Engagement inside the product
    - Import a scan report and find the id of the Test
    - Provide this in the `test` parameter

    By Names:
    - Create a Product (or use an existing product)
    - Create an Engagement inside the product
    - Import a report which will create a Test
    - Provide `product_name`
    - Provide `engagement_name`
    - Optional: Provide `test_title`

    In this scenario Defect Dojo will look up the Test by the provided details.
    If no `test_title` is provided, the latest test inside the engagement will be chosen based on
    scan_type.

    When using names you can let the importer automatically create Engagements, Products and
    Product_Types
    by using `auto_create_context=True`.

    When `auto_create_context` is set to `True` you can use `deduplication_on_engagement` to restrict
    deduplication for
    imported Findings to the newly created Engagement.

    Args:
        body (ReImportScanRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReImportScan]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ReImportScanRequest,
) -> ReImportScan | None:
    """Reimports a scan report into an existing test.

    By ID:
    - Create a Product (or use an existing product)
    - Create an Engagement inside the product
    - Import a scan report and find the id of the Test
    - Provide this in the `test` parameter

    By Names:
    - Create a Product (or use an existing product)
    - Create an Engagement inside the product
    - Import a report which will create a Test
    - Provide `product_name`
    - Provide `engagement_name`
    - Optional: Provide `test_title`

    In this scenario Defect Dojo will look up the Test by the provided details.
    If no `test_title` is provided, the latest test inside the engagement will be chosen based on
    scan_type.

    When using names you can let the importer automatically create Engagements, Products and
    Product_Types
    by using `auto_create_context=True`.

    When `auto_create_context` is set to `True` you can use `deduplication_on_engagement` to restrict
    deduplication for
    imported Findings to the newly created Engagement.

    Args:
        body (ReImportScanRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReImportScan
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
