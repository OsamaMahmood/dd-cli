from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_tool_configuration_list import PaginatedToolConfigurationList
from ...models.tool_configurations_list_authentication_type import (
    ToolConfigurationsListAuthenticationType,
)
from ...models.tool_configurations_list_prefetch_item import ToolConfigurationsListPrefetchItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    authentication_type: ToolConfigurationsListAuthenticationType | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[ToolConfigurationsListPrefetchItem] | Unset = UNSET,
    tool_type: int | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_authentication_type: str | Unset = UNSET
    if not isinstance(authentication_type, Unset):
        json_authentication_type = authentication_type.value

    params["authentication_type"] = json_authentication_type

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

    params["tool_type"] = tool_type

    params["url"] = url_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/tool_configurations/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedToolConfigurationList | None:
    if response.status_code == 200:
        response_200 = PaginatedToolConfigurationList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedToolConfigurationList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    authentication_type: ToolConfigurationsListAuthenticationType | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[ToolConfigurationsListPrefetchItem] | Unset = UNSET,
    tool_type: int | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> Response[PaginatedToolConfigurationList]:
    """
    Args:
        authentication_type (ToolConfigurationsListAuthenticationType | Unset):
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        prefetch (list[ToolConfigurationsListPrefetchItem] | Unset):
        tool_type (int | Unset):
        url_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedToolConfigurationList]
    """

    kwargs = _get_kwargs(
        authentication_type=authentication_type,
        id=id,
        limit=limit,
        name=name,
        offset=offset,
        prefetch=prefetch,
        tool_type=tool_type,
        url_query=url_query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    authentication_type: ToolConfigurationsListAuthenticationType | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[ToolConfigurationsListPrefetchItem] | Unset = UNSET,
    tool_type: int | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> PaginatedToolConfigurationList | None:
    """
    Args:
        authentication_type (ToolConfigurationsListAuthenticationType | Unset):
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        prefetch (list[ToolConfigurationsListPrefetchItem] | Unset):
        tool_type (int | Unset):
        url_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedToolConfigurationList
    """

    return sync_detailed(
        client=client,
        authentication_type=authentication_type,
        id=id,
        limit=limit,
        name=name,
        offset=offset,
        prefetch=prefetch,
        tool_type=tool_type,
        url_query=url_query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    authentication_type: ToolConfigurationsListAuthenticationType | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[ToolConfigurationsListPrefetchItem] | Unset = UNSET,
    tool_type: int | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> Response[PaginatedToolConfigurationList]:
    """
    Args:
        authentication_type (ToolConfigurationsListAuthenticationType | Unset):
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        prefetch (list[ToolConfigurationsListPrefetchItem] | Unset):
        tool_type (int | Unset):
        url_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedToolConfigurationList]
    """

    kwargs = _get_kwargs(
        authentication_type=authentication_type,
        id=id,
        limit=limit,
        name=name,
        offset=offset,
        prefetch=prefetch,
        tool_type=tool_type,
        url_query=url_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    authentication_type: ToolConfigurationsListAuthenticationType | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[ToolConfigurationsListPrefetchItem] | Unset = UNSET,
    tool_type: int | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> PaginatedToolConfigurationList | None:
    """
    Args:
        authentication_type (ToolConfigurationsListAuthenticationType | Unset):
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        prefetch (list[ToolConfigurationsListPrefetchItem] | Unset):
        tool_type (int | Unset):
        url_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedToolConfigurationList
    """

    return (
        await asyncio_detailed(
            client=client,
            authentication_type=authentication_type,
            id=id,
            limit=limit,
            name=name,
            offset=offset,
            prefetch=prefetch,
            tool_type=tool_type,
            url_query=url_query,
        )
    ).parsed
