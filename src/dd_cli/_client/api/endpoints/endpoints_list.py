from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.endpoints_list_o_item import EndpointsListOItem
from ...models.paginated_endpoint_list import PaginatedEndpointList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fragment: str | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    host: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    o: list[EndpointsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    path: str | Unset = UNSET,
    port: int | Unset = UNSET,
    product: int | Unset = UNSET,
    protocol: str | Unset = UNSET,
    query: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    userinfo: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["fragment"] = fragment

    params["has_tags"] = has_tags

    params["host"] = host

    params["id"] = id

    params["limit"] = limit

    params["not_tag"] = not_tag

    json_not_tags: list[str] | Unset = UNSET
    if not isinstance(not_tags, Unset):
        json_not_tags = not_tags

    params["not_tags"] = json_not_tags

    json_o: list[str] | Unset = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    params["offset"] = offset

    params["path"] = path

    params["port"] = port

    params["product"] = product

    params["protocol"] = protocol

    params["query"] = query

    params["tag"] = tag

    json_tags: list[str] | Unset = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    json_tags_and: list[str] | Unset = UNSET
    if not isinstance(tags_and, Unset):
        json_tags_and = tags_and

    params["tags__and"] = json_tags_and

    params["userinfo"] = userinfo

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/endpoints/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedEndpointList | None:
    if response.status_code == 200:
        response_200 = PaginatedEndpointList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedEndpointList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    fragment: str | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    host: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    o: list[EndpointsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    path: str | Unset = UNSET,
    port: int | Unset = UNSET,
    product: int | Unset = UNSET,
    protocol: str | Unset = UNSET,
    query: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    userinfo: str | Unset = UNSET,
) -> Response[PaginatedEndpointList]:
    """
    Args:
        fragment (str | Unset):
        has_tags (bool | Unset):
        host (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        o (list[EndpointsListOItem] | Unset):
        offset (int | Unset):
        path (str | Unset):
        port (int | Unset):
        product (int | Unset):
        protocol (str | Unset):
        query (str | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        userinfo (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedEndpointList]
    """

    kwargs = _get_kwargs(
        fragment=fragment,
        has_tags=has_tags,
        host=host,
        id=id,
        limit=limit,
        not_tag=not_tag,
        not_tags=not_tags,
        o=o,
        offset=offset,
        path=path,
        port=port,
        product=product,
        protocol=protocol,
        query=query,
        tag=tag,
        tags=tags,
        tags_and=tags_and,
        userinfo=userinfo,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    fragment: str | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    host: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    o: list[EndpointsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    path: str | Unset = UNSET,
    port: int | Unset = UNSET,
    product: int | Unset = UNSET,
    protocol: str | Unset = UNSET,
    query: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    userinfo: str | Unset = UNSET,
) -> PaginatedEndpointList | None:
    """
    Args:
        fragment (str | Unset):
        has_tags (bool | Unset):
        host (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        o (list[EndpointsListOItem] | Unset):
        offset (int | Unset):
        path (str | Unset):
        port (int | Unset):
        product (int | Unset):
        protocol (str | Unset):
        query (str | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        userinfo (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedEndpointList
    """

    return sync_detailed(
        client=client,
        fragment=fragment,
        has_tags=has_tags,
        host=host,
        id=id,
        limit=limit,
        not_tag=not_tag,
        not_tags=not_tags,
        o=o,
        offset=offset,
        path=path,
        port=port,
        product=product,
        protocol=protocol,
        query=query,
        tag=tag,
        tags=tags,
        tags_and=tags_and,
        userinfo=userinfo,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    fragment: str | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    host: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    o: list[EndpointsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    path: str | Unset = UNSET,
    port: int | Unset = UNSET,
    product: int | Unset = UNSET,
    protocol: str | Unset = UNSET,
    query: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    userinfo: str | Unset = UNSET,
) -> Response[PaginatedEndpointList]:
    """
    Args:
        fragment (str | Unset):
        has_tags (bool | Unset):
        host (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        o (list[EndpointsListOItem] | Unset):
        offset (int | Unset):
        path (str | Unset):
        port (int | Unset):
        product (int | Unset):
        protocol (str | Unset):
        query (str | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        userinfo (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedEndpointList]
    """

    kwargs = _get_kwargs(
        fragment=fragment,
        has_tags=has_tags,
        host=host,
        id=id,
        limit=limit,
        not_tag=not_tag,
        not_tags=not_tags,
        o=o,
        offset=offset,
        path=path,
        port=port,
        product=product,
        protocol=protocol,
        query=query,
        tag=tag,
        tags=tags,
        tags_and=tags_and,
        userinfo=userinfo,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    fragment: str | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    host: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    o: list[EndpointsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    path: str | Unset = UNSET,
    port: int | Unset = UNSET,
    product: int | Unset = UNSET,
    protocol: str | Unset = UNSET,
    query: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    userinfo: str | Unset = UNSET,
) -> PaginatedEndpointList | None:
    """
    Args:
        fragment (str | Unset):
        has_tags (bool | Unset):
        host (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        o (list[EndpointsListOItem] | Unset):
        offset (int | Unset):
        path (str | Unset):
        port (int | Unset):
        product (int | Unset):
        protocol (str | Unset):
        query (str | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        userinfo (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedEndpointList
    """

    return (
        await asyncio_detailed(
            client=client,
            fragment=fragment,
            has_tags=has_tags,
            host=host,
            id=id,
            limit=limit,
            not_tag=not_tag,
            not_tags=not_tags,
            o=o,
            offset=offset,
            path=path,
            port=port,
            product=product,
            protocol=protocol,
            query=query,
            tag=tag,
            tags=tags,
            tags_and=tags_and,
            userinfo=userinfo,
        )
    ).parsed
