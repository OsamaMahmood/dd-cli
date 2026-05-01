from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.jira_product_configurations_list_prefetch_item import (
    JiraProductConfigurationsListPrefetchItem,
)
from ...models.paginated_jira_project_list import PaginatedJIRAProjectList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    component: str | Unset = UNSET,
    enable_engagement_epic_mapping: bool | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    engagement: int | Unset = UNSET,
    id: int | Unset = UNSET,
    jira_instance: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[JiraProductConfigurationsListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
    project_key: str | Unset = UNSET,
    push_all_issues: bool | Unset = UNSET,
    push_notes: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["component"] = component

    params["enable_engagement_epic_mapping"] = enable_engagement_epic_mapping

    params["enabled"] = enabled

    params["engagement"] = engagement

    params["id"] = id

    params["jira_instance"] = jira_instance

    params["limit"] = limit

    params["offset"] = offset

    json_prefetch: list[str] | Unset = UNSET
    if not isinstance(prefetch, Unset):
        json_prefetch = []
        for prefetch_item_data in prefetch:
            prefetch_item = prefetch_item_data.value
            json_prefetch.append(prefetch_item)

    params["prefetch"] = json_prefetch

    params["product"] = product

    params["project_key"] = project_key

    params["push_all_issues"] = push_all_issues

    params["push_notes"] = push_notes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/jira_product_configurations/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedJIRAProjectList | None:
    if response.status_code == 200:
        response_200 = PaginatedJIRAProjectList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedJIRAProjectList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    component: str | Unset = UNSET,
    enable_engagement_epic_mapping: bool | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    engagement: int | Unset = UNSET,
    id: int | Unset = UNSET,
    jira_instance: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[JiraProductConfigurationsListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
    project_key: str | Unset = UNSET,
    push_all_issues: bool | Unset = UNSET,
    push_notes: bool | Unset = UNSET,
) -> Response[PaginatedJIRAProjectList]:
    """
    Args:
        component (str | Unset):
        enable_engagement_epic_mapping (bool | Unset):
        enabled (bool | Unset):
        engagement (int | Unset):
        id (int | Unset):
        jira_instance (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[JiraProductConfigurationsListPrefetchItem] | Unset):
        product (int | Unset):
        project_key (str | Unset):
        push_all_issues (bool | Unset):
        push_notes (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedJIRAProjectList]
    """

    kwargs = _get_kwargs(
        component=component,
        enable_engagement_epic_mapping=enable_engagement_epic_mapping,
        enabled=enabled,
        engagement=engagement,
        id=id,
        jira_instance=jira_instance,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        product=product,
        project_key=project_key,
        push_all_issues=push_all_issues,
        push_notes=push_notes,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    component: str | Unset = UNSET,
    enable_engagement_epic_mapping: bool | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    engagement: int | Unset = UNSET,
    id: int | Unset = UNSET,
    jira_instance: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[JiraProductConfigurationsListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
    project_key: str | Unset = UNSET,
    push_all_issues: bool | Unset = UNSET,
    push_notes: bool | Unset = UNSET,
) -> PaginatedJIRAProjectList | None:
    """
    Args:
        component (str | Unset):
        enable_engagement_epic_mapping (bool | Unset):
        enabled (bool | Unset):
        engagement (int | Unset):
        id (int | Unset):
        jira_instance (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[JiraProductConfigurationsListPrefetchItem] | Unset):
        product (int | Unset):
        project_key (str | Unset):
        push_all_issues (bool | Unset):
        push_notes (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedJIRAProjectList
    """

    return sync_detailed(
        client=client,
        component=component,
        enable_engagement_epic_mapping=enable_engagement_epic_mapping,
        enabled=enabled,
        engagement=engagement,
        id=id,
        jira_instance=jira_instance,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        product=product,
        project_key=project_key,
        push_all_issues=push_all_issues,
        push_notes=push_notes,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    component: str | Unset = UNSET,
    enable_engagement_epic_mapping: bool | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    engagement: int | Unset = UNSET,
    id: int | Unset = UNSET,
    jira_instance: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[JiraProductConfigurationsListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
    project_key: str | Unset = UNSET,
    push_all_issues: bool | Unset = UNSET,
    push_notes: bool | Unset = UNSET,
) -> Response[PaginatedJIRAProjectList]:
    """
    Args:
        component (str | Unset):
        enable_engagement_epic_mapping (bool | Unset):
        enabled (bool | Unset):
        engagement (int | Unset):
        id (int | Unset):
        jira_instance (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[JiraProductConfigurationsListPrefetchItem] | Unset):
        product (int | Unset):
        project_key (str | Unset):
        push_all_issues (bool | Unset):
        push_notes (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedJIRAProjectList]
    """

    kwargs = _get_kwargs(
        component=component,
        enable_engagement_epic_mapping=enable_engagement_epic_mapping,
        enabled=enabled,
        engagement=engagement,
        id=id,
        jira_instance=jira_instance,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        product=product,
        project_key=project_key,
        push_all_issues=push_all_issues,
        push_notes=push_notes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    component: str | Unset = UNSET,
    enable_engagement_epic_mapping: bool | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    engagement: int | Unset = UNSET,
    id: int | Unset = UNSET,
    jira_instance: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    prefetch: list[JiraProductConfigurationsListPrefetchItem] | Unset = UNSET,
    product: int | Unset = UNSET,
    project_key: str | Unset = UNSET,
    push_all_issues: bool | Unset = UNSET,
    push_notes: bool | Unset = UNSET,
) -> PaginatedJIRAProjectList | None:
    """
    Args:
        component (str | Unset):
        enable_engagement_epic_mapping (bool | Unset):
        enabled (bool | Unset):
        engagement (int | Unset):
        id (int | Unset):
        jira_instance (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        prefetch (list[JiraProductConfigurationsListPrefetchItem] | Unset):
        product (int | Unset):
        project_key (str | Unset):
        push_all_issues (bool | Unset):
        push_notes (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedJIRAProjectList
    """

    return (
        await asyncio_detailed(
            client=client,
            component=component,
            enable_engagement_epic_mapping=enable_engagement_epic_mapping,
            enabled=enabled,
            engagement=engagement,
            id=id,
            jira_instance=jira_instance,
            limit=limit,
            offset=offset,
            prefetch=prefetch,
            product=product,
            project_key=project_key,
            push_all_issues=push_all_issues,
            push_notes=push_notes,
        )
    ).parsed
