import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_test_list import PaginatedTestList
from ...models.tests_list_o_item import TestsListOItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    api_scan_configuration: int | Unset = UNSET,
    branch_tag: str | Unset = UNSET,
    build_id: str | Unset = UNSET,
    commit_hash: str | Unset = UNSET,
    engagement: int | Unset = UNSET,
    engagement_product_tags: list[str] | Unset = UNSET,
    engagement_product_tags_and: list[str] | Unset = UNSET,
    engagement_tags: list[str] | Unset = UNSET,
    engagement_tags_and: list[str] | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    not_engagement_product_tags: list[str] | Unset = UNSET,
    not_engagement_tags: list[str] | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    notes: list[int] | Unset = UNSET,
    o: list[TestsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    percent_complete: int | Unset = UNSET,
    scan_type: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    target_end: datetime.datetime | Unset = UNSET,
    target_start: datetime.datetime | Unset = UNSET,
    test_type: int | Unset = UNSET,
    title: str | Unset = UNSET,
    version: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["api_scan_configuration"] = api_scan_configuration

    params["branch_tag"] = branch_tag

    params["build_id"] = build_id

    params["commit_hash"] = commit_hash

    params["engagement"] = engagement

    json_engagement_product_tags: list[str] | Unset = UNSET
    if not isinstance(engagement_product_tags, Unset):
        json_engagement_product_tags = engagement_product_tags

    params["engagement__product__tags"] = json_engagement_product_tags

    json_engagement_product_tags_and: list[str] | Unset = UNSET
    if not isinstance(engagement_product_tags_and, Unset):
        json_engagement_product_tags_and = engagement_product_tags_and

    params["engagement__product__tags__and"] = json_engagement_product_tags_and

    json_engagement_tags: list[str] | Unset = UNSET
    if not isinstance(engagement_tags, Unset):
        json_engagement_tags = engagement_tags

    params["engagement__tags"] = json_engagement_tags

    json_engagement_tags_and: list[str] | Unset = UNSET
    if not isinstance(engagement_tags_and, Unset):
        json_engagement_tags_and = engagement_tags_and

    params["engagement__tags__and"] = json_engagement_tags_and

    params["has_tags"] = has_tags

    params["id"] = id

    params["limit"] = limit

    json_not_engagement_product_tags: list[str] | Unset = UNSET
    if not isinstance(not_engagement_product_tags, Unset):
        json_not_engagement_product_tags = not_engagement_product_tags

    params["not_engagement__product__tags"] = json_not_engagement_product_tags

    json_not_engagement_tags: list[str] | Unset = UNSET
    if not isinstance(not_engagement_tags, Unset):
        json_not_engagement_tags = not_engagement_tags

    params["not_engagement__tags"] = json_not_engagement_tags

    params["not_tag"] = not_tag

    json_not_tags: list[str] | Unset = UNSET
    if not isinstance(not_tags, Unset):
        json_not_tags = not_tags

    params["not_tags"] = json_not_tags

    json_notes: list[int] | Unset = UNSET
    if not isinstance(notes, Unset):
        json_notes = notes

    params["notes"] = json_notes

    json_o: list[str] | Unset = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    params["offset"] = offset

    params["percent_complete"] = percent_complete

    params["scan_type"] = scan_type

    params["tag"] = tag

    json_tags: list[str] | Unset = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    json_tags_and: list[str] | Unset = UNSET
    if not isinstance(tags_and, Unset):
        json_tags_and = tags_and

    params["tags__and"] = json_tags_and

    json_target_end: str | Unset = UNSET
    if not isinstance(target_end, Unset):
        json_target_end = target_end.isoformat()
    params["target_end"] = json_target_end

    json_target_start: str | Unset = UNSET
    if not isinstance(target_start, Unset):
        json_target_start = target_start.isoformat()
    params["target_start"] = json_target_start

    params["test_type"] = test_type

    params["title"] = title

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/tests/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedTestList | None:
    if response.status_code == 200:
        response_200 = PaginatedTestList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedTestList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    api_scan_configuration: int | Unset = UNSET,
    branch_tag: str | Unset = UNSET,
    build_id: str | Unset = UNSET,
    commit_hash: str | Unset = UNSET,
    engagement: int | Unset = UNSET,
    engagement_product_tags: list[str] | Unset = UNSET,
    engagement_product_tags_and: list[str] | Unset = UNSET,
    engagement_tags: list[str] | Unset = UNSET,
    engagement_tags_and: list[str] | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    not_engagement_product_tags: list[str] | Unset = UNSET,
    not_engagement_tags: list[str] | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    notes: list[int] | Unset = UNSET,
    o: list[TestsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    percent_complete: int | Unset = UNSET,
    scan_type: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    target_end: datetime.datetime | Unset = UNSET,
    target_start: datetime.datetime | Unset = UNSET,
    test_type: int | Unset = UNSET,
    title: str | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Response[PaginatedTestList]:
    """
    Args:
        api_scan_configuration (int | Unset):
        branch_tag (str | Unset):
        build_id (str | Unset):
        commit_hash (str | Unset):
        engagement (int | Unset):
        engagement_product_tags (list[str] | Unset):
        engagement_product_tags_and (list[str] | Unset):
        engagement_tags (list[str] | Unset):
        engagement_tags_and (list[str] | Unset):
        has_tags (bool | Unset):
        id (int | Unset):
        limit (int | Unset):
        not_engagement_product_tags (list[str] | Unset):
        not_engagement_tags (list[str] | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        notes (list[int] | Unset):
        o (list[TestsListOItem] | Unset):
        offset (int | Unset):
        percent_complete (int | Unset):
        scan_type (str | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        target_end (datetime.datetime | Unset):
        target_start (datetime.datetime | Unset):
        test_type (int | Unset):
        title (str | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTestList]
    """

    kwargs = _get_kwargs(
        api_scan_configuration=api_scan_configuration,
        branch_tag=branch_tag,
        build_id=build_id,
        commit_hash=commit_hash,
        engagement=engagement,
        engagement_product_tags=engagement_product_tags,
        engagement_product_tags_and=engagement_product_tags_and,
        engagement_tags=engagement_tags,
        engagement_tags_and=engagement_tags_and,
        has_tags=has_tags,
        id=id,
        limit=limit,
        not_engagement_product_tags=not_engagement_product_tags,
        not_engagement_tags=not_engagement_tags,
        not_tag=not_tag,
        not_tags=not_tags,
        notes=notes,
        o=o,
        offset=offset,
        percent_complete=percent_complete,
        scan_type=scan_type,
        tag=tag,
        tags=tags,
        tags_and=tags_and,
        target_end=target_end,
        target_start=target_start,
        test_type=test_type,
        title=title,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    api_scan_configuration: int | Unset = UNSET,
    branch_tag: str | Unset = UNSET,
    build_id: str | Unset = UNSET,
    commit_hash: str | Unset = UNSET,
    engagement: int | Unset = UNSET,
    engagement_product_tags: list[str] | Unset = UNSET,
    engagement_product_tags_and: list[str] | Unset = UNSET,
    engagement_tags: list[str] | Unset = UNSET,
    engagement_tags_and: list[str] | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    not_engagement_product_tags: list[str] | Unset = UNSET,
    not_engagement_tags: list[str] | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    notes: list[int] | Unset = UNSET,
    o: list[TestsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    percent_complete: int | Unset = UNSET,
    scan_type: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    target_end: datetime.datetime | Unset = UNSET,
    target_start: datetime.datetime | Unset = UNSET,
    test_type: int | Unset = UNSET,
    title: str | Unset = UNSET,
    version: str | Unset = UNSET,
) -> PaginatedTestList | None:
    """
    Args:
        api_scan_configuration (int | Unset):
        branch_tag (str | Unset):
        build_id (str | Unset):
        commit_hash (str | Unset):
        engagement (int | Unset):
        engagement_product_tags (list[str] | Unset):
        engagement_product_tags_and (list[str] | Unset):
        engagement_tags (list[str] | Unset):
        engagement_tags_and (list[str] | Unset):
        has_tags (bool | Unset):
        id (int | Unset):
        limit (int | Unset):
        not_engagement_product_tags (list[str] | Unset):
        not_engagement_tags (list[str] | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        notes (list[int] | Unset):
        o (list[TestsListOItem] | Unset):
        offset (int | Unset):
        percent_complete (int | Unset):
        scan_type (str | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        target_end (datetime.datetime | Unset):
        target_start (datetime.datetime | Unset):
        test_type (int | Unset):
        title (str | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedTestList
    """

    return sync_detailed(
        client=client,
        api_scan_configuration=api_scan_configuration,
        branch_tag=branch_tag,
        build_id=build_id,
        commit_hash=commit_hash,
        engagement=engagement,
        engagement_product_tags=engagement_product_tags,
        engagement_product_tags_and=engagement_product_tags_and,
        engagement_tags=engagement_tags,
        engagement_tags_and=engagement_tags_and,
        has_tags=has_tags,
        id=id,
        limit=limit,
        not_engagement_product_tags=not_engagement_product_tags,
        not_engagement_tags=not_engagement_tags,
        not_tag=not_tag,
        not_tags=not_tags,
        notes=notes,
        o=o,
        offset=offset,
        percent_complete=percent_complete,
        scan_type=scan_type,
        tag=tag,
        tags=tags,
        tags_and=tags_and,
        target_end=target_end,
        target_start=target_start,
        test_type=test_type,
        title=title,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    api_scan_configuration: int | Unset = UNSET,
    branch_tag: str | Unset = UNSET,
    build_id: str | Unset = UNSET,
    commit_hash: str | Unset = UNSET,
    engagement: int | Unset = UNSET,
    engagement_product_tags: list[str] | Unset = UNSET,
    engagement_product_tags_and: list[str] | Unset = UNSET,
    engagement_tags: list[str] | Unset = UNSET,
    engagement_tags_and: list[str] | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    not_engagement_product_tags: list[str] | Unset = UNSET,
    not_engagement_tags: list[str] | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    notes: list[int] | Unset = UNSET,
    o: list[TestsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    percent_complete: int | Unset = UNSET,
    scan_type: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    target_end: datetime.datetime | Unset = UNSET,
    target_start: datetime.datetime | Unset = UNSET,
    test_type: int | Unset = UNSET,
    title: str | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Response[PaginatedTestList]:
    """
    Args:
        api_scan_configuration (int | Unset):
        branch_tag (str | Unset):
        build_id (str | Unset):
        commit_hash (str | Unset):
        engagement (int | Unset):
        engagement_product_tags (list[str] | Unset):
        engagement_product_tags_and (list[str] | Unset):
        engagement_tags (list[str] | Unset):
        engagement_tags_and (list[str] | Unset):
        has_tags (bool | Unset):
        id (int | Unset):
        limit (int | Unset):
        not_engagement_product_tags (list[str] | Unset):
        not_engagement_tags (list[str] | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        notes (list[int] | Unset):
        o (list[TestsListOItem] | Unset):
        offset (int | Unset):
        percent_complete (int | Unset):
        scan_type (str | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        target_end (datetime.datetime | Unset):
        target_start (datetime.datetime | Unset):
        test_type (int | Unset):
        title (str | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTestList]
    """

    kwargs = _get_kwargs(
        api_scan_configuration=api_scan_configuration,
        branch_tag=branch_tag,
        build_id=build_id,
        commit_hash=commit_hash,
        engagement=engagement,
        engagement_product_tags=engagement_product_tags,
        engagement_product_tags_and=engagement_product_tags_and,
        engagement_tags=engagement_tags,
        engagement_tags_and=engagement_tags_and,
        has_tags=has_tags,
        id=id,
        limit=limit,
        not_engagement_product_tags=not_engagement_product_tags,
        not_engagement_tags=not_engagement_tags,
        not_tag=not_tag,
        not_tags=not_tags,
        notes=notes,
        o=o,
        offset=offset,
        percent_complete=percent_complete,
        scan_type=scan_type,
        tag=tag,
        tags=tags,
        tags_and=tags_and,
        target_end=target_end,
        target_start=target_start,
        test_type=test_type,
        title=title,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    api_scan_configuration: int | Unset = UNSET,
    branch_tag: str | Unset = UNSET,
    build_id: str | Unset = UNSET,
    commit_hash: str | Unset = UNSET,
    engagement: int | Unset = UNSET,
    engagement_product_tags: list[str] | Unset = UNSET,
    engagement_product_tags_and: list[str] | Unset = UNSET,
    engagement_tags: list[str] | Unset = UNSET,
    engagement_tags_and: list[str] | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    not_engagement_product_tags: list[str] | Unset = UNSET,
    not_engagement_tags: list[str] | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    notes: list[int] | Unset = UNSET,
    o: list[TestsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    percent_complete: int | Unset = UNSET,
    scan_type: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    target_end: datetime.datetime | Unset = UNSET,
    target_start: datetime.datetime | Unset = UNSET,
    test_type: int | Unset = UNSET,
    title: str | Unset = UNSET,
    version: str | Unset = UNSET,
) -> PaginatedTestList | None:
    """
    Args:
        api_scan_configuration (int | Unset):
        branch_tag (str | Unset):
        build_id (str | Unset):
        commit_hash (str | Unset):
        engagement (int | Unset):
        engagement_product_tags (list[str] | Unset):
        engagement_product_tags_and (list[str] | Unset):
        engagement_tags (list[str] | Unset):
        engagement_tags_and (list[str] | Unset):
        has_tags (bool | Unset):
        id (int | Unset):
        limit (int | Unset):
        not_engagement_product_tags (list[str] | Unset):
        not_engagement_tags (list[str] | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        notes (list[int] | Unset):
        o (list[TestsListOItem] | Unset):
        offset (int | Unset):
        percent_complete (int | Unset):
        scan_type (str | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        target_end (datetime.datetime | Unset):
        target_start (datetime.datetime | Unset):
        test_type (int | Unset):
        title (str | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedTestList
    """

    return (
        await asyncio_detailed(
            client=client,
            api_scan_configuration=api_scan_configuration,
            branch_tag=branch_tag,
            build_id=build_id,
            commit_hash=commit_hash,
            engagement=engagement,
            engagement_product_tags=engagement_product_tags,
            engagement_product_tags_and=engagement_product_tags_and,
            engagement_tags=engagement_tags,
            engagement_tags_and=engagement_tags_and,
            has_tags=has_tags,
            id=id,
            limit=limit,
            not_engagement_product_tags=not_engagement_product_tags,
            not_engagement_tags=not_engagement_tags,
            not_tag=not_tag,
            not_tags=not_tags,
            notes=notes,
            o=o,
            offset=offset,
            percent_complete=percent_complete,
            scan_type=scan_type,
            tag=tag,
            tags=tags,
            tags_and=tags_and,
            target_end=target_end,
            target_start=target_start,
            test_type=test_type,
            title=title,
            version=version,
        )
    ).parsed
