from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_api_scan_configurations_list_prefetch_item import (
    AssetApiScanConfigurationsListPrefetchItem,
)
from ...models.paginated_asset_api_scan_configuration_list import (
    PaginatedAssetAPIScanConfigurationList,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    asset: int | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[AssetApiScanConfigurationsListPrefetchItem] | Unset = UNSET,
    service_key_1: str | Unset = UNSET,
    service_key_2: str | Unset = UNSET,
    service_key_3: str | Unset = UNSET,
    tool_configuration: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["asset"] = asset

    params["id"] = id

    params["limit"] = limit

    params["offset"] = offset

    json_prefetch: list[str] | Unset = UNSET
    if not isinstance(prefetch, Unset):
        json_prefetch = []
        for prefetch_item_data in prefetch:
            prefetch_item = prefetch_item_data.value
            json_prefetch.append(prefetch_item)

    params["prefetch"] = json_prefetch

    params["service_key_1"] = service_key_1

    params["service_key_2"] = service_key_2

    params["service_key_3"] = service_key_3

    params["tool_configuration"] = tool_configuration

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/asset_api_scan_configurations/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedAssetAPIScanConfigurationList | None:
    if response.status_code == 200:
        response_200 = PaginatedAssetAPIScanConfigurationList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedAssetAPIScanConfigurationList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    asset: int | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[AssetApiScanConfigurationsListPrefetchItem] | Unset = UNSET,
    service_key_1: str | Unset = UNSET,
    service_key_2: str | Unset = UNSET,
    service_key_3: str | Unset = UNSET,
    tool_configuration: int | Unset = UNSET,
) -> Response[PaginatedAssetAPIScanConfigurationList]:
    """
    Args:
        asset (int | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[AssetApiScanConfigurationsListPrefetchItem] | Unset):
        service_key_1 (str | Unset):
        service_key_2 (str | Unset):
        service_key_3 (str | Unset):
        tool_configuration (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAssetAPIScanConfigurationList]
    """

    kwargs = _get_kwargs(
        asset=asset,
        id=id,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        service_key_1=service_key_1,
        service_key_2=service_key_2,
        service_key_3=service_key_3,
        tool_configuration=tool_configuration,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    asset: int | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[AssetApiScanConfigurationsListPrefetchItem] | Unset = UNSET,
    service_key_1: str | Unset = UNSET,
    service_key_2: str | Unset = UNSET,
    service_key_3: str | Unset = UNSET,
    tool_configuration: int | Unset = UNSET,
) -> PaginatedAssetAPIScanConfigurationList | None:
    """
    Args:
        asset (int | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[AssetApiScanConfigurationsListPrefetchItem] | Unset):
        service_key_1 (str | Unset):
        service_key_2 (str | Unset):
        service_key_3 (str | Unset):
        tool_configuration (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAssetAPIScanConfigurationList
    """

    return sync_detailed(
        client=client,
        asset=asset,
        id=id,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        service_key_1=service_key_1,
        service_key_2=service_key_2,
        service_key_3=service_key_3,
        tool_configuration=tool_configuration,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    asset: int | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[AssetApiScanConfigurationsListPrefetchItem] | Unset = UNSET,
    service_key_1: str | Unset = UNSET,
    service_key_2: str | Unset = UNSET,
    service_key_3: str | Unset = UNSET,
    tool_configuration: int | Unset = UNSET,
) -> Response[PaginatedAssetAPIScanConfigurationList]:
    """
    Args:
        asset (int | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[AssetApiScanConfigurationsListPrefetchItem] | Unset):
        service_key_1 (str | Unset):
        service_key_2 (str | Unset):
        service_key_3 (str | Unset):
        tool_configuration (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAssetAPIScanConfigurationList]
    """

    kwargs = _get_kwargs(
        asset=asset,
        id=id,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        service_key_1=service_key_1,
        service_key_2=service_key_2,
        service_key_3=service_key_3,
        tool_configuration=tool_configuration,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    asset: int | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[AssetApiScanConfigurationsListPrefetchItem] | Unset = UNSET,
    service_key_1: str | Unset = UNSET,
    service_key_2: str | Unset = UNSET,
    service_key_3: str | Unset = UNSET,
    tool_configuration: int | Unset = UNSET,
) -> PaginatedAssetAPIScanConfigurationList | None:
    """
    Args:
        asset (int | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[AssetApiScanConfigurationsListPrefetchItem] | Unset):
        service_key_1 (str | Unset):
        service_key_2 (str | Unset):
        service_key_3 (str | Unset):
        tool_configuration (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAssetAPIScanConfigurationList
    """

    return (
        await asyncio_detailed(
            client=client,
            asset=asset,
            id=id,
            limit=limit,
            offset=offset,
            prefetch=prefetch,
            service_key_1=service_key_1,
            service_key_2=service_key_2,
            service_key_3=service_key_3,
            tool_configuration=tool_configuration,
        )
    ).parsed
