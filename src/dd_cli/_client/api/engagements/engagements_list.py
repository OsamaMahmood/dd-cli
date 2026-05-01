import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.engagements_list_o_item import EngagementsListOItem
from ...models.engagements_list_status import EngagementsListStatus
from ...models.paginated_engagement_list import PaginatedEngagementList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    active: bool | Unset = UNSET,
    api_test: bool | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    not_product_tags: list[str] | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    o: list[EngagementsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    pen_test: bool | Unset = UNSET,
    product: int | Unset = UNSET,
    product_prod_type: list[int] | Unset = UNSET,
    product_tags: list[str] | Unset = UNSET,
    product_tags_and: list[str] | Unset = UNSET,
    report_type: int | Unset = UNSET,
    requester: int | Unset = UNSET,
    status: EngagementsListStatus | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    target_end: datetime.date | Unset = UNSET,
    target_start: datetime.date | Unset = UNSET,
    threat_model: bool | Unset = UNSET,
    updated: datetime.datetime | Unset = UNSET,
    version: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["active"] = active

    params["api_test"] = api_test

    params["has_tags"] = has_tags

    params["id"] = id

    params["limit"] = limit

    params["name"] = name

    json_not_product_tags: list[str] | Unset = UNSET
    if not isinstance(not_product_tags, Unset):
        json_not_product_tags = not_product_tags

    params["not_product__tags"] = json_not_product_tags

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

    params["pen_test"] = pen_test

    params["product"] = product

    json_product_prod_type: list[int] | Unset = UNSET
    if not isinstance(product_prod_type, Unset):
        json_product_prod_type = product_prod_type

    params["product__prod_type"] = json_product_prod_type

    json_product_tags: list[str] | Unset = UNSET
    if not isinstance(product_tags, Unset):
        json_product_tags = product_tags

    params["product__tags"] = json_product_tags

    json_product_tags_and: list[str] | Unset = UNSET
    if not isinstance(product_tags_and, Unset):
        json_product_tags_and = product_tags_and

    params["product__tags__and"] = json_product_tags_and

    params["report_type"] = report_type

    params["requester"] = requester

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

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

    params["threat_model"] = threat_model

    json_updated: str | Unset = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/engagements/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedEngagementList | None:
    if response.status_code == 200:
        response_200 = PaginatedEngagementList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedEngagementList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    api_test: bool | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    not_product_tags: list[str] | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    o: list[EngagementsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    pen_test: bool | Unset = UNSET,
    product: int | Unset = UNSET,
    product_prod_type: list[int] | Unset = UNSET,
    product_tags: list[str] | Unset = UNSET,
    product_tags_and: list[str] | Unset = UNSET,
    report_type: int | Unset = UNSET,
    requester: int | Unset = UNSET,
    status: EngagementsListStatus | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    target_end: datetime.date | Unset = UNSET,
    target_start: datetime.date | Unset = UNSET,
    threat_model: bool | Unset = UNSET,
    updated: datetime.datetime | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Response[PaginatedEngagementList]:
    """
    Args:
        active (bool | Unset):
        api_test (bool | Unset):
        has_tags (bool | Unset):
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        not_product_tags (list[str] | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        o (list[EngagementsListOItem] | Unset):
        offset (int | Unset):
        pen_test (bool | Unset):
        product (int | Unset):
        product_prod_type (list[int] | Unset):
        product_tags (list[str] | Unset):
        product_tags_and (list[str] | Unset):
        report_type (int | Unset):
        requester (int | Unset):
        status (EngagementsListStatus | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        target_end (datetime.date | Unset):
        target_start (datetime.date | Unset):
        threat_model (bool | Unset):
        updated (datetime.datetime | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedEngagementList]
    """

    kwargs = _get_kwargs(
        active=active,
        api_test=api_test,
        has_tags=has_tags,
        id=id,
        limit=limit,
        name=name,
        not_product_tags=not_product_tags,
        not_tag=not_tag,
        not_tags=not_tags,
        o=o,
        offset=offset,
        pen_test=pen_test,
        product=product,
        product_prod_type=product_prod_type,
        product_tags=product_tags,
        product_tags_and=product_tags_and,
        report_type=report_type,
        requester=requester,
        status=status,
        tag=tag,
        tags=tags,
        tags_and=tags_and,
        target_end=target_end,
        target_start=target_start,
        threat_model=threat_model,
        updated=updated,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    api_test: bool | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    not_product_tags: list[str] | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    o: list[EngagementsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    pen_test: bool | Unset = UNSET,
    product: int | Unset = UNSET,
    product_prod_type: list[int] | Unset = UNSET,
    product_tags: list[str] | Unset = UNSET,
    product_tags_and: list[str] | Unset = UNSET,
    report_type: int | Unset = UNSET,
    requester: int | Unset = UNSET,
    status: EngagementsListStatus | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    target_end: datetime.date | Unset = UNSET,
    target_start: datetime.date | Unset = UNSET,
    threat_model: bool | Unset = UNSET,
    updated: datetime.datetime | Unset = UNSET,
    version: str | Unset = UNSET,
) -> PaginatedEngagementList | None:
    """
    Args:
        active (bool | Unset):
        api_test (bool | Unset):
        has_tags (bool | Unset):
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        not_product_tags (list[str] | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        o (list[EngagementsListOItem] | Unset):
        offset (int | Unset):
        pen_test (bool | Unset):
        product (int | Unset):
        product_prod_type (list[int] | Unset):
        product_tags (list[str] | Unset):
        product_tags_and (list[str] | Unset):
        report_type (int | Unset):
        requester (int | Unset):
        status (EngagementsListStatus | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        target_end (datetime.date | Unset):
        target_start (datetime.date | Unset):
        threat_model (bool | Unset):
        updated (datetime.datetime | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedEngagementList
    """

    return sync_detailed(
        client=client,
        active=active,
        api_test=api_test,
        has_tags=has_tags,
        id=id,
        limit=limit,
        name=name,
        not_product_tags=not_product_tags,
        not_tag=not_tag,
        not_tags=not_tags,
        o=o,
        offset=offset,
        pen_test=pen_test,
        product=product,
        product_prod_type=product_prod_type,
        product_tags=product_tags,
        product_tags_and=product_tags_and,
        report_type=report_type,
        requester=requester,
        status=status,
        tag=tag,
        tags=tags,
        tags_and=tags_and,
        target_end=target_end,
        target_start=target_start,
        threat_model=threat_model,
        updated=updated,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    api_test: bool | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    not_product_tags: list[str] | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    o: list[EngagementsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    pen_test: bool | Unset = UNSET,
    product: int | Unset = UNSET,
    product_prod_type: list[int] | Unset = UNSET,
    product_tags: list[str] | Unset = UNSET,
    product_tags_and: list[str] | Unset = UNSET,
    report_type: int | Unset = UNSET,
    requester: int | Unset = UNSET,
    status: EngagementsListStatus | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    target_end: datetime.date | Unset = UNSET,
    target_start: datetime.date | Unset = UNSET,
    threat_model: bool | Unset = UNSET,
    updated: datetime.datetime | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Response[PaginatedEngagementList]:
    """
    Args:
        active (bool | Unset):
        api_test (bool | Unset):
        has_tags (bool | Unset):
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        not_product_tags (list[str] | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        o (list[EngagementsListOItem] | Unset):
        offset (int | Unset):
        pen_test (bool | Unset):
        product (int | Unset):
        product_prod_type (list[int] | Unset):
        product_tags (list[str] | Unset):
        product_tags_and (list[str] | Unset):
        report_type (int | Unset):
        requester (int | Unset):
        status (EngagementsListStatus | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        target_end (datetime.date | Unset):
        target_start (datetime.date | Unset):
        threat_model (bool | Unset):
        updated (datetime.datetime | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedEngagementList]
    """

    kwargs = _get_kwargs(
        active=active,
        api_test=api_test,
        has_tags=has_tags,
        id=id,
        limit=limit,
        name=name,
        not_product_tags=not_product_tags,
        not_tag=not_tag,
        not_tags=not_tags,
        o=o,
        offset=offset,
        pen_test=pen_test,
        product=product,
        product_prod_type=product_prod_type,
        product_tags=product_tags,
        product_tags_and=product_tags_and,
        report_type=report_type,
        requester=requester,
        status=status,
        tag=tag,
        tags=tags,
        tags_and=tags_and,
        target_end=target_end,
        target_start=target_start,
        threat_model=threat_model,
        updated=updated,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    api_test: bool | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    not_product_tags: list[str] | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    o: list[EngagementsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    pen_test: bool | Unset = UNSET,
    product: int | Unset = UNSET,
    product_prod_type: list[int] | Unset = UNSET,
    product_tags: list[str] | Unset = UNSET,
    product_tags_and: list[str] | Unset = UNSET,
    report_type: int | Unset = UNSET,
    requester: int | Unset = UNSET,
    status: EngagementsListStatus | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    target_end: datetime.date | Unset = UNSET,
    target_start: datetime.date | Unset = UNSET,
    threat_model: bool | Unset = UNSET,
    updated: datetime.datetime | Unset = UNSET,
    version: str | Unset = UNSET,
) -> PaginatedEngagementList | None:
    """
    Args:
        active (bool | Unset):
        api_test (bool | Unset):
        has_tags (bool | Unset):
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        not_product_tags (list[str] | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        o (list[EngagementsListOItem] | Unset):
        offset (int | Unset):
        pen_test (bool | Unset):
        product (int | Unset):
        product_prod_type (list[int] | Unset):
        product_tags (list[str] | Unset):
        product_tags_and (list[str] | Unset):
        report_type (int | Unset):
        requester (int | Unset):
        status (EngagementsListStatus | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        target_end (datetime.date | Unset):
        target_start (datetime.date | Unset):
        threat_model (bool | Unset):
        updated (datetime.datetime | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedEngagementList
    """

    return (
        await asyncio_detailed(
            client=client,
            active=active,
            api_test=api_test,
            has_tags=has_tags,
            id=id,
            limit=limit,
            name=name,
            not_product_tags=not_product_tags,
            not_tag=not_tag,
            not_tags=not_tags,
            o=o,
            offset=offset,
            pen_test=pen_test,
            product=product,
            product_prod_type=product_prod_type,
            product_tags=product_tags,
            product_tags_and=product_tags_and,
            report_type=report_type,
            requester=requester,
            status=status,
            tag=tag,
            tags=tags,
            tags_and=tags_and,
            target_end=target_end,
            target_start=target_start,
            threat_model=threat_model,
            updated=updated,
            version=version,
        )
    ).parsed
