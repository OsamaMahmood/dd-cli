from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.finding_templates_list_o_item import FindingTemplatesListOItem
from ...models.paginated_finding_template_list import PaginatedFindingTemplateList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cwe: int | Unset = UNSET,
    description: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    mitigation: str | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    o: list[FindingTemplatesListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    severity: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    title: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cwe"] = cwe

    params["description"] = description

    params["id"] = id

    params["limit"] = limit

    params["mitigation"] = mitigation

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

    params["severity"] = severity

    params["tag"] = tag

    json_tags: list[str] | Unset = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    json_tags_and: list[str] | Unset = UNSET
    if not isinstance(tags_and, Unset):
        json_tags_and = tags_and

    params["tags__and"] = json_tags_and

    params["title"] = title

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/finding_templates/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedFindingTemplateList | None:
    if response.status_code == 200:
        response_200 = PaginatedFindingTemplateList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedFindingTemplateList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cwe: int | Unset = UNSET,
    description: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    mitigation: str | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    o: list[FindingTemplatesListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    severity: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    title: str | Unset = UNSET,
) -> Response[PaginatedFindingTemplateList]:
    """
    Args:
        cwe (int | Unset):
        description (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        mitigation (str | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        o (list[FindingTemplatesListOItem] | Unset):
        offset (int | Unset):
        severity (str | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        title (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedFindingTemplateList]
    """

    kwargs = _get_kwargs(
        cwe=cwe,
        description=description,
        id=id,
        limit=limit,
        mitigation=mitigation,
        not_tag=not_tag,
        not_tags=not_tags,
        o=o,
        offset=offset,
        severity=severity,
        tag=tag,
        tags=tags,
        tags_and=tags_and,
        title=title,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cwe: int | Unset = UNSET,
    description: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    mitigation: str | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    o: list[FindingTemplatesListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    severity: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    title: str | Unset = UNSET,
) -> PaginatedFindingTemplateList | None:
    """
    Args:
        cwe (int | Unset):
        description (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        mitigation (str | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        o (list[FindingTemplatesListOItem] | Unset):
        offset (int | Unset):
        severity (str | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        title (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedFindingTemplateList
    """

    return sync_detailed(
        client=client,
        cwe=cwe,
        description=description,
        id=id,
        limit=limit,
        mitigation=mitigation,
        not_tag=not_tag,
        not_tags=not_tags,
        o=o,
        offset=offset,
        severity=severity,
        tag=tag,
        tags=tags,
        tags_and=tags_and,
        title=title,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cwe: int | Unset = UNSET,
    description: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    mitigation: str | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    o: list[FindingTemplatesListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    severity: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    title: str | Unset = UNSET,
) -> Response[PaginatedFindingTemplateList]:
    """
    Args:
        cwe (int | Unset):
        description (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        mitigation (str | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        o (list[FindingTemplatesListOItem] | Unset):
        offset (int | Unset):
        severity (str | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        title (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedFindingTemplateList]
    """

    kwargs = _get_kwargs(
        cwe=cwe,
        description=description,
        id=id,
        limit=limit,
        mitigation=mitigation,
        not_tag=not_tag,
        not_tags=not_tags,
        o=o,
        offset=offset,
        severity=severity,
        tag=tag,
        tags=tags,
        tags_and=tags_and,
        title=title,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cwe: int | Unset = UNSET,
    description: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    mitigation: str | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    o: list[FindingTemplatesListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    severity: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    title: str | Unset = UNSET,
) -> PaginatedFindingTemplateList | None:
    """
    Args:
        cwe (int | Unset):
        description (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        mitigation (str | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        o (list[FindingTemplatesListOItem] | Unset):
        offset (int | Unset):
        severity (str | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        title (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedFindingTemplateList
    """

    return (
        await asyncio_detailed(
            client=client,
            cwe=cwe,
            description=description,
            id=id,
            limit=limit,
            mitigation=mitigation,
            not_tag=not_tag,
            not_tags=not_tags,
            o=o,
            offset=offset,
            severity=severity,
            tag=tag,
            tags=tags,
            tags_and=tags_and,
            title=title,
        )
    ).parsed
