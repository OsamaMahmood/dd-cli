from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_tool_product_settings_list import PaginatedToolProductSettingsList
from ...models.tool_product_settings_list_prefetch_item import ToolProductSettingsListPrefetchItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[ToolProductSettingsListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
    tool_configuration: int | Unset = UNSET,
    tool_project_id: str | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params["limit"] = limit

    params["name"] = name

    params["offset"] = offset

    json_prefetch: list[str] | Unset = UNSET
    if not isinstance(prefetch, Unset):
        json_prefetch = []
        for prefetch_item_data in prefetch:
            prefetch_item = prefetch_item_data.value
            json_prefetch.append(prefetch_item)

    params["prefetch"] = json_prefetch

    params["product"] = product

    params["tool_configuration"] = tool_configuration

    params["tool_project_id"] = tool_project_id

    params["url"] = url_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/tool_product_settings/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedToolProductSettingsList | None:
    if response.status_code == 200:
        response_200 = PaginatedToolProductSettingsList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedToolProductSettingsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[ToolProductSettingsListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
    tool_configuration: int | Unset = UNSET,
    tool_project_id: str | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> Response[PaginatedToolProductSettingsList]:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        prefetch (list[ToolProductSettingsListPrefetchItem] | Unset):
        product (int | Unset):
        tool_configuration (int | Unset):
        tool_project_id (str | Unset):
        url_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedToolProductSettingsList]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        name=name,
        offset=offset,
        prefetch=prefetch,
        product=product,
        tool_configuration=tool_configuration,
        tool_project_id=tool_project_id,
        url_query=url_query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[ToolProductSettingsListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
    tool_configuration: int | Unset = UNSET,
    tool_project_id: str | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> PaginatedToolProductSettingsList | None:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        prefetch (list[ToolProductSettingsListPrefetchItem] | Unset):
        product (int | Unset):
        tool_configuration (int | Unset):
        tool_project_id (str | Unset):
        url_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedToolProductSettingsList
    """

    return sync_detailed(
        client=client,
        id=id,
        limit=limit,
        name=name,
        offset=offset,
        prefetch=prefetch,
        product=product,
        tool_configuration=tool_configuration,
        tool_project_id=tool_project_id,
        url_query=url_query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[ToolProductSettingsListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
    tool_configuration: int | Unset = UNSET,
    tool_project_id: str | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> Response[PaginatedToolProductSettingsList]:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        prefetch (list[ToolProductSettingsListPrefetchItem] | Unset):
        product (int | Unset):
        tool_configuration (int | Unset):
        tool_project_id (str | Unset):
        url_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedToolProductSettingsList]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        name=name,
        offset=offset,
        prefetch=prefetch,
        product=product,
        tool_configuration=tool_configuration,
        tool_project_id=tool_project_id,
        url_query=url_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[ToolProductSettingsListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
    tool_configuration: int | Unset = UNSET,
    tool_project_id: str | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> PaginatedToolProductSettingsList | None:
    """
    Args:
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        prefetch (list[ToolProductSettingsListPrefetchItem] | Unset):
        product (int | Unset):
        tool_configuration (int | Unset):
        tool_project_id (str | Unset):
        url_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedToolProductSettingsList
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            limit=limit,
            name=name,
            offset=offset,
            prefetch=prefetch,
            product=product,
            tool_configuration=tool_configuration,
            tool_project_id=tool_project_id,
            url_query=url_query,
        )
    ).parsed
