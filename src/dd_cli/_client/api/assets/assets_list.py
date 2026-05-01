from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assets_list_business_criticality_item import AssetsListBusinessCriticalityItem
from ...models.assets_list_created_type_1 import AssetsListCreatedType1
from ...models.assets_list_created_type_2_type_1 import AssetsListCreatedType2Type1
from ...models.assets_list_created_type_3_type_1 import AssetsListCreatedType3Type1
from ...models.assets_list_lifecycle_item import AssetsListLifecycleItem
from ...models.assets_list_o_item import AssetsListOItem
from ...models.assets_list_origin_item import AssetsListOriginItem
from ...models.assets_list_platform_item import AssetsListPlatformItem
from ...models.assets_list_prefetch_item import AssetsListPrefetchItem
from ...models.assets_list_updated_type_1 import AssetsListUpdatedType1
from ...models.assets_list_updated_type_2_type_1 import AssetsListUpdatedType2Type1
from ...models.assets_list_updated_type_3_type_1 import AssetsListUpdatedType3Type1
from ...models.paginated_asset_list import PaginatedAssetList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    asset_manager: list[int] | Unset = UNSET,
    asset_numeric_grade: list[int] | Unset = UNSET,
    business_criticality: list[AssetsListBusinessCriticalityItem] | Unset = UNSET,
    created: AssetsListCreatedType1
    | AssetsListCreatedType2Type1
    | AssetsListCreatedType3Type1
    | None
    | Unset = UNSET,
    description: str | Unset = UNSET,
    external_audience: bool | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    id: list[int] | Unset = UNSET,
    internet_accessible: bool | Unset = UNSET,
    lifecycle: list[AssetsListLifecycleItem] | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    o: list[AssetsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    organization: list[int] | Unset = UNSET,
    origin: list[AssetsListOriginItem] | Unset = UNSET,
    outside_of_sla: float | Unset = UNSET,
    platform: list[AssetsListPlatformItem] | Unset = UNSET,
    prefetch: list[AssetsListPrefetchItem] | Unset = UNSET,
    regulations: list[int] | Unset = UNSET,
    revenue: float | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    team_manager: list[int] | Unset = UNSET,
    technical_contact: list[int] | Unset = UNSET,
    tid: list[int] | Unset = UNSET,
    updated: AssetsListUpdatedType1
    | AssetsListUpdatedType2Type1
    | AssetsListUpdatedType3Type1
    | None
    | Unset = UNSET,
    user_records: list[int] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_asset_manager: list[int] | Unset = UNSET
    if not isinstance(asset_manager, Unset):
        json_asset_manager = asset_manager

    params["asset_manager"] = json_asset_manager

    json_asset_numeric_grade: list[int] | Unset = UNSET
    if not isinstance(asset_numeric_grade, Unset):
        json_asset_numeric_grade = asset_numeric_grade

    params["asset_numeric_grade"] = json_asset_numeric_grade

    json_business_criticality: list[str] | Unset = UNSET
    if not isinstance(business_criticality, Unset):
        json_business_criticality = []
        for business_criticality_item_data in business_criticality:
            business_criticality_item = business_criticality_item_data.value
            json_business_criticality.append(business_criticality_item)

    params["business_criticality"] = json_business_criticality

    json_created: int | None | Unset
    if isinstance(created, Unset):
        json_created = UNSET
    elif (
        isinstance(created, AssetsListCreatedType1)
        or isinstance(created, AssetsListCreatedType2Type1)
        or isinstance(created, AssetsListCreatedType3Type1)
    ):
        json_created = created.value
    else:
        json_created = created
    params["created"] = json_created

    params["description"] = description

    params["external_audience"] = external_audience

    params["has_tags"] = has_tags

    json_id: list[int] | Unset = UNSET
    if not isinstance(id, Unset):
        json_id = id

    params["id"] = json_id

    params["internet_accessible"] = internet_accessible

    json_lifecycle: list[str] | Unset = UNSET
    if not isinstance(lifecycle, Unset):
        json_lifecycle = []
        for lifecycle_item_data in lifecycle:
            lifecycle_item = lifecycle_item_data.value
            json_lifecycle.append(lifecycle_item)

    params["lifecycle"] = json_lifecycle

    params["limit"] = limit

    params["name"] = name

    params["name_exact"] = name_exact

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

    json_organization: list[int] | Unset = UNSET
    if not isinstance(organization, Unset):
        json_organization = organization

    params["organization"] = json_organization

    json_origin: list[str] | Unset = UNSET
    if not isinstance(origin, Unset):
        json_origin = []
        for origin_item_data in origin:
            origin_item = origin_item_data.value
            json_origin.append(origin_item)

    params["origin"] = json_origin

    params["outside_of_sla"] = outside_of_sla

    json_platform: list[str] | Unset = UNSET
    if not isinstance(platform, Unset):
        json_platform = []
        for platform_item_data in platform:
            platform_item = platform_item_data.value
            json_platform.append(platform_item)

    params["platform"] = json_platform

    json_prefetch: list[str] | Unset = UNSET
    if not isinstance(prefetch, Unset):
        json_prefetch = []
        for prefetch_item_data in prefetch:
            prefetch_item = prefetch_item_data.value
            json_prefetch.append(prefetch_item)

    params["prefetch"] = json_prefetch

    json_regulations: list[int] | Unset = UNSET
    if not isinstance(regulations, Unset):
        json_regulations = regulations

    params["regulations"] = json_regulations

    params["revenue"] = revenue

    params["tag"] = tag

    json_tags: list[str] | Unset = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    json_tags_and: list[str] | Unset = UNSET
    if not isinstance(tags_and, Unset):
        json_tags_and = tags_and

    params["tags__and"] = json_tags_and

    json_team_manager: list[int] | Unset = UNSET
    if not isinstance(team_manager, Unset):
        json_team_manager = team_manager

    params["team_manager"] = json_team_manager

    json_technical_contact: list[int] | Unset = UNSET
    if not isinstance(technical_contact, Unset):
        json_technical_contact = technical_contact

    params["technical_contact"] = json_technical_contact

    json_tid: list[int] | Unset = UNSET
    if not isinstance(tid, Unset):
        json_tid = tid

    params["tid"] = json_tid

    json_updated: int | None | Unset
    if isinstance(updated, Unset):
        json_updated = UNSET
    elif (
        isinstance(updated, AssetsListUpdatedType1)
        or isinstance(updated, AssetsListUpdatedType2Type1)
        or isinstance(updated, AssetsListUpdatedType3Type1)
    ):
        json_updated = updated.value
    else:
        json_updated = updated
    params["updated"] = json_updated

    json_user_records: list[int] | Unset = UNSET
    if not isinstance(user_records, Unset):
        json_user_records = user_records

    params["user_records"] = json_user_records

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/assets/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedAssetList | None:
    if response.status_code == 200:
        response_200 = PaginatedAssetList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedAssetList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    asset_manager: list[int] | Unset = UNSET,
    asset_numeric_grade: list[int] | Unset = UNSET,
    business_criticality: list[AssetsListBusinessCriticalityItem] | Unset = UNSET,
    created: AssetsListCreatedType1
    | AssetsListCreatedType2Type1
    | AssetsListCreatedType3Type1
    | None
    | Unset = UNSET,
    description: str | Unset = UNSET,
    external_audience: bool | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    id: list[int] | Unset = UNSET,
    internet_accessible: bool | Unset = UNSET,
    lifecycle: list[AssetsListLifecycleItem] | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    o: list[AssetsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    organization: list[int] | Unset = UNSET,
    origin: list[AssetsListOriginItem] | Unset = UNSET,
    outside_of_sla: float | Unset = UNSET,
    platform: list[AssetsListPlatformItem] | Unset = UNSET,
    prefetch: list[AssetsListPrefetchItem] | Unset = UNSET,
    regulations: list[int] | Unset = UNSET,
    revenue: float | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    team_manager: list[int] | Unset = UNSET,
    technical_contact: list[int] | Unset = UNSET,
    tid: list[int] | Unset = UNSET,
    updated: AssetsListUpdatedType1
    | AssetsListUpdatedType2Type1
    | AssetsListUpdatedType3Type1
    | None
    | Unset = UNSET,
    user_records: list[int] | Unset = UNSET,
) -> Response[PaginatedAssetList]:
    """
    Args:
        asset_manager (list[int] | Unset):
        asset_numeric_grade (list[int] | Unset):
        business_criticality (list[AssetsListBusinessCriticalityItem] | Unset):
        created (AssetsListCreatedType1 | AssetsListCreatedType2Type1 |
            AssetsListCreatedType3Type1 | None | Unset):
        description (str | Unset):
        external_audience (bool | Unset):
        has_tags (bool | Unset):
        id (list[int] | Unset):
        internet_accessible (bool | Unset):
        lifecycle (list[AssetsListLifecycleItem] | Unset):
        limit (int | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        o (list[AssetsListOItem] | Unset):
        offset (int | Unset):
        organization (list[int] | Unset):
        origin (list[AssetsListOriginItem] | Unset):
        outside_of_sla (float | Unset):
        platform (list[AssetsListPlatformItem] | Unset):
        prefetch (list[AssetsListPrefetchItem] | Unset):
        regulations (list[int] | Unset):
        revenue (float | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        team_manager (list[int] | Unset):
        technical_contact (list[int] | Unset):
        tid (list[int] | Unset):
        updated (AssetsListUpdatedType1 | AssetsListUpdatedType2Type1 |
            AssetsListUpdatedType3Type1 | None | Unset):
        user_records (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAssetList]
    """

    kwargs = _get_kwargs(
        asset_manager=asset_manager,
        asset_numeric_grade=asset_numeric_grade,
        business_criticality=business_criticality,
        created=created,
        description=description,
        external_audience=external_audience,
        has_tags=has_tags,
        id=id,
        internet_accessible=internet_accessible,
        lifecycle=lifecycle,
        limit=limit,
        name=name,
        name_exact=name_exact,
        not_tag=not_tag,
        not_tags=not_tags,
        o=o,
        offset=offset,
        organization=organization,
        origin=origin,
        outside_of_sla=outside_of_sla,
        platform=platform,
        prefetch=prefetch,
        regulations=regulations,
        revenue=revenue,
        tag=tag,
        tags=tags,
        tags_and=tags_and,
        team_manager=team_manager,
        technical_contact=technical_contact,
        tid=tid,
        updated=updated,
        user_records=user_records,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    asset_manager: list[int] | Unset = UNSET,
    asset_numeric_grade: list[int] | Unset = UNSET,
    business_criticality: list[AssetsListBusinessCriticalityItem] | Unset = UNSET,
    created: AssetsListCreatedType1
    | AssetsListCreatedType2Type1
    | AssetsListCreatedType3Type1
    | None
    | Unset = UNSET,
    description: str | Unset = UNSET,
    external_audience: bool | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    id: list[int] | Unset = UNSET,
    internet_accessible: bool | Unset = UNSET,
    lifecycle: list[AssetsListLifecycleItem] | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    o: list[AssetsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    organization: list[int] | Unset = UNSET,
    origin: list[AssetsListOriginItem] | Unset = UNSET,
    outside_of_sla: float | Unset = UNSET,
    platform: list[AssetsListPlatformItem] | Unset = UNSET,
    prefetch: list[AssetsListPrefetchItem] | Unset = UNSET,
    regulations: list[int] | Unset = UNSET,
    revenue: float | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    team_manager: list[int] | Unset = UNSET,
    technical_contact: list[int] | Unset = UNSET,
    tid: list[int] | Unset = UNSET,
    updated: AssetsListUpdatedType1
    | AssetsListUpdatedType2Type1
    | AssetsListUpdatedType3Type1
    | None
    | Unset = UNSET,
    user_records: list[int] | Unset = UNSET,
) -> PaginatedAssetList | None:
    """
    Args:
        asset_manager (list[int] | Unset):
        asset_numeric_grade (list[int] | Unset):
        business_criticality (list[AssetsListBusinessCriticalityItem] | Unset):
        created (AssetsListCreatedType1 | AssetsListCreatedType2Type1 |
            AssetsListCreatedType3Type1 | None | Unset):
        description (str | Unset):
        external_audience (bool | Unset):
        has_tags (bool | Unset):
        id (list[int] | Unset):
        internet_accessible (bool | Unset):
        lifecycle (list[AssetsListLifecycleItem] | Unset):
        limit (int | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        o (list[AssetsListOItem] | Unset):
        offset (int | Unset):
        organization (list[int] | Unset):
        origin (list[AssetsListOriginItem] | Unset):
        outside_of_sla (float | Unset):
        platform (list[AssetsListPlatformItem] | Unset):
        prefetch (list[AssetsListPrefetchItem] | Unset):
        regulations (list[int] | Unset):
        revenue (float | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        team_manager (list[int] | Unset):
        technical_contact (list[int] | Unset):
        tid (list[int] | Unset):
        updated (AssetsListUpdatedType1 | AssetsListUpdatedType2Type1 |
            AssetsListUpdatedType3Type1 | None | Unset):
        user_records (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAssetList
    """

    return sync_detailed(
        client=client,
        asset_manager=asset_manager,
        asset_numeric_grade=asset_numeric_grade,
        business_criticality=business_criticality,
        created=created,
        description=description,
        external_audience=external_audience,
        has_tags=has_tags,
        id=id,
        internet_accessible=internet_accessible,
        lifecycle=lifecycle,
        limit=limit,
        name=name,
        name_exact=name_exact,
        not_tag=not_tag,
        not_tags=not_tags,
        o=o,
        offset=offset,
        organization=organization,
        origin=origin,
        outside_of_sla=outside_of_sla,
        platform=platform,
        prefetch=prefetch,
        regulations=regulations,
        revenue=revenue,
        tag=tag,
        tags=tags,
        tags_and=tags_and,
        team_manager=team_manager,
        technical_contact=technical_contact,
        tid=tid,
        updated=updated,
        user_records=user_records,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    asset_manager: list[int] | Unset = UNSET,
    asset_numeric_grade: list[int] | Unset = UNSET,
    business_criticality: list[AssetsListBusinessCriticalityItem] | Unset = UNSET,
    created: AssetsListCreatedType1
    | AssetsListCreatedType2Type1
    | AssetsListCreatedType3Type1
    | None
    | Unset = UNSET,
    description: str | Unset = UNSET,
    external_audience: bool | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    id: list[int] | Unset = UNSET,
    internet_accessible: bool | Unset = UNSET,
    lifecycle: list[AssetsListLifecycleItem] | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    o: list[AssetsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    organization: list[int] | Unset = UNSET,
    origin: list[AssetsListOriginItem] | Unset = UNSET,
    outside_of_sla: float | Unset = UNSET,
    platform: list[AssetsListPlatformItem] | Unset = UNSET,
    prefetch: list[AssetsListPrefetchItem] | Unset = UNSET,
    regulations: list[int] | Unset = UNSET,
    revenue: float | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    team_manager: list[int] | Unset = UNSET,
    technical_contact: list[int] | Unset = UNSET,
    tid: list[int] | Unset = UNSET,
    updated: AssetsListUpdatedType1
    | AssetsListUpdatedType2Type1
    | AssetsListUpdatedType3Type1
    | None
    | Unset = UNSET,
    user_records: list[int] | Unset = UNSET,
) -> Response[PaginatedAssetList]:
    """
    Args:
        asset_manager (list[int] | Unset):
        asset_numeric_grade (list[int] | Unset):
        business_criticality (list[AssetsListBusinessCriticalityItem] | Unset):
        created (AssetsListCreatedType1 | AssetsListCreatedType2Type1 |
            AssetsListCreatedType3Type1 | None | Unset):
        description (str | Unset):
        external_audience (bool | Unset):
        has_tags (bool | Unset):
        id (list[int] | Unset):
        internet_accessible (bool | Unset):
        lifecycle (list[AssetsListLifecycleItem] | Unset):
        limit (int | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        o (list[AssetsListOItem] | Unset):
        offset (int | Unset):
        organization (list[int] | Unset):
        origin (list[AssetsListOriginItem] | Unset):
        outside_of_sla (float | Unset):
        platform (list[AssetsListPlatformItem] | Unset):
        prefetch (list[AssetsListPrefetchItem] | Unset):
        regulations (list[int] | Unset):
        revenue (float | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        team_manager (list[int] | Unset):
        technical_contact (list[int] | Unset):
        tid (list[int] | Unset):
        updated (AssetsListUpdatedType1 | AssetsListUpdatedType2Type1 |
            AssetsListUpdatedType3Type1 | None | Unset):
        user_records (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAssetList]
    """

    kwargs = _get_kwargs(
        asset_manager=asset_manager,
        asset_numeric_grade=asset_numeric_grade,
        business_criticality=business_criticality,
        created=created,
        description=description,
        external_audience=external_audience,
        has_tags=has_tags,
        id=id,
        internet_accessible=internet_accessible,
        lifecycle=lifecycle,
        limit=limit,
        name=name,
        name_exact=name_exact,
        not_tag=not_tag,
        not_tags=not_tags,
        o=o,
        offset=offset,
        organization=organization,
        origin=origin,
        outside_of_sla=outside_of_sla,
        platform=platform,
        prefetch=prefetch,
        regulations=regulations,
        revenue=revenue,
        tag=tag,
        tags=tags,
        tags_and=tags_and,
        team_manager=team_manager,
        technical_contact=technical_contact,
        tid=tid,
        updated=updated,
        user_records=user_records,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    asset_manager: list[int] | Unset = UNSET,
    asset_numeric_grade: list[int] | Unset = UNSET,
    business_criticality: list[AssetsListBusinessCriticalityItem] | Unset = UNSET,
    created: AssetsListCreatedType1
    | AssetsListCreatedType2Type1
    | AssetsListCreatedType3Type1
    | None
    | Unset = UNSET,
    description: str | Unset = UNSET,
    external_audience: bool | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    id: list[int] | Unset = UNSET,
    internet_accessible: bool | Unset = UNSET,
    lifecycle: list[AssetsListLifecycleItem] | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    o: list[AssetsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    organization: list[int] | Unset = UNSET,
    origin: list[AssetsListOriginItem] | Unset = UNSET,
    outside_of_sla: float | Unset = UNSET,
    platform: list[AssetsListPlatformItem] | Unset = UNSET,
    prefetch: list[AssetsListPrefetchItem] | Unset = UNSET,
    regulations: list[int] | Unset = UNSET,
    revenue: float | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    team_manager: list[int] | Unset = UNSET,
    technical_contact: list[int] | Unset = UNSET,
    tid: list[int] | Unset = UNSET,
    updated: AssetsListUpdatedType1
    | AssetsListUpdatedType2Type1
    | AssetsListUpdatedType3Type1
    | None
    | Unset = UNSET,
    user_records: list[int] | Unset = UNSET,
) -> PaginatedAssetList | None:
    """
    Args:
        asset_manager (list[int] | Unset):
        asset_numeric_grade (list[int] | Unset):
        business_criticality (list[AssetsListBusinessCriticalityItem] | Unset):
        created (AssetsListCreatedType1 | AssetsListCreatedType2Type1 |
            AssetsListCreatedType3Type1 | None | Unset):
        description (str | Unset):
        external_audience (bool | Unset):
        has_tags (bool | Unset):
        id (list[int] | Unset):
        internet_accessible (bool | Unset):
        lifecycle (list[AssetsListLifecycleItem] | Unset):
        limit (int | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        o (list[AssetsListOItem] | Unset):
        offset (int | Unset):
        organization (list[int] | Unset):
        origin (list[AssetsListOriginItem] | Unset):
        outside_of_sla (float | Unset):
        platform (list[AssetsListPlatformItem] | Unset):
        prefetch (list[AssetsListPrefetchItem] | Unset):
        regulations (list[int] | Unset):
        revenue (float | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        team_manager (list[int] | Unset):
        technical_contact (list[int] | Unset):
        tid (list[int] | Unset):
        updated (AssetsListUpdatedType1 | AssetsListUpdatedType2Type1 |
            AssetsListUpdatedType3Type1 | None | Unset):
        user_records (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAssetList
    """

    return (
        await asyncio_detailed(
            client=client,
            asset_manager=asset_manager,
            asset_numeric_grade=asset_numeric_grade,
            business_criticality=business_criticality,
            created=created,
            description=description,
            external_audience=external_audience,
            has_tags=has_tags,
            id=id,
            internet_accessible=internet_accessible,
            lifecycle=lifecycle,
            limit=limit,
            name=name,
            name_exact=name_exact,
            not_tag=not_tag,
            not_tags=not_tags,
            o=o,
            offset=offset,
            organization=organization,
            origin=origin,
            outside_of_sla=outside_of_sla,
            platform=platform,
            prefetch=prefetch,
            regulations=regulations,
            revenue=revenue,
            tag=tag,
            tags=tags,
            tags_and=tags_and,
            team_manager=team_manager,
            technical_contact=technical_contact,
            tid=tid,
            updated=updated,
            user_records=user_records,
        )
    ).parsed
