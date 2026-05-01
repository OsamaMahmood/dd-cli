from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_app_analysis_list import PaginatedAppAnalysisList
from ...models.technologies_list_prefetch_item import TechnologiesListPrefetchItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[TechnologiesListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    user: int | Unset = UNSET,
    version: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["name"] = name

    params["not_tag"] = not_tag

    json_not_tags: list[str] | Unset = UNSET
    if not isinstance(not_tags, Unset):
        json_not_tags = not_tags

    params["not_tags"] = json_not_tags

    params["offset"] = offset

    json_prefetch: list[str] | Unset = UNSET
    if not isinstance(prefetch, Unset):
        json_prefetch = []
        for prefetch_item_data in prefetch:
            prefetch_item = prefetch_item_data.value
            json_prefetch.append(prefetch_item)

    params["prefetch"] = json_prefetch

    params["product"] = product

    params["tag"] = tag

    json_tags: list[str] | Unset = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    json_tags_and: list[str] | Unset = UNSET
    if not isinstance(tags_and, Unset):
        json_tags_and = tags_and

    params["tags__and"] = json_tags_and

    params["user"] = user

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/technologies/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedAppAnalysisList | None:
    if response.status_code == 200:
        response_200 = PaginatedAppAnalysisList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedAppAnalysisList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[TechnologiesListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    user: int | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Response[PaginatedAppAnalysisList]:
    """
    Args:
        limit (int | Unset):
        name (str | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        offset (int | Unset):
        prefetch (list[TechnologiesListPrefetchItem] | Unset):
        product (int | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        user (int | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAppAnalysisList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        name=name,
        not_tag=not_tag,
        not_tags=not_tags,
        offset=offset,
        prefetch=prefetch,
        product=product,
        tag=tag,
        tags=tags,
        tags_and=tags_and,
        user=user,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[TechnologiesListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    user: int | Unset = UNSET,
    version: str | Unset = UNSET,
) -> PaginatedAppAnalysisList | None:
    """
    Args:
        limit (int | Unset):
        name (str | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        offset (int | Unset):
        prefetch (list[TechnologiesListPrefetchItem] | Unset):
        product (int | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        user (int | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAppAnalysisList
    """

    return sync_detailed(
        client=client,
        limit=limit,
        name=name,
        not_tag=not_tag,
        not_tags=not_tags,
        offset=offset,
        prefetch=prefetch,
        product=product,
        tag=tag,
        tags=tags,
        tags_and=tags_and,
        user=user,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[TechnologiesListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    user: int | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Response[PaginatedAppAnalysisList]:
    """
    Args:
        limit (int | Unset):
        name (str | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        offset (int | Unset):
        prefetch (list[TechnologiesListPrefetchItem] | Unset):
        product (int | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        user (int | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAppAnalysisList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        name=name,
        not_tag=not_tag,
        not_tags=not_tags,
        offset=offset,
        prefetch=prefetch,
        product=product,
        tag=tag,
        tags=tags,
        tags_and=tags_and,
        user=user,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[TechnologiesListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    user: int | Unset = UNSET,
    version: str | Unset = UNSET,
) -> PaginatedAppAnalysisList | None:
    """
    Args:
        limit (int | Unset):
        name (str | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        offset (int | Unset):
        prefetch (list[TechnologiesListPrefetchItem] | Unset):
        product (int | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        user (int | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAppAnalysisList
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            name=name,
            not_tag=not_tag,
            not_tags=not_tags,
            offset=offset,
            prefetch=prefetch,
            product=product,
            tag=tag,
            tags=tags,
            tags_and=tags_and,
            user=user,
            version=version,
        )
    ).parsed
