from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_meta_list import PaginatedMetaList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    endpoint: int | Unset = UNSET,
    finding: int | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_case_insensitive: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    product: int | Unset = UNSET,
    value: str | Unset = UNSET,
    value_case_insensitive: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["endpoint"] = endpoint

    params["finding"] = finding

    params["id"] = id

    params["limit"] = limit

    params["name"] = name

    params["name_case_insensitive"] = name_case_insensitive

    params["offset"] = offset

    params["product"] = product

    params["value"] = value

    params["value_case_insensitive"] = value_case_insensitive

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/metadata/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedMetaList | None:
    if response.status_code == 200:
        response_200 = PaginatedMetaList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedMetaList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    endpoint: int | Unset = UNSET,
    finding: int | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_case_insensitive: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    product: int | Unset = UNSET,
    value: str | Unset = UNSET,
    value_case_insensitive: str | Unset = UNSET,
) -> Response[PaginatedMetaList]:
    """
    Args:
        endpoint (int | Unset):
        finding (int | Unset):
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        name_case_insensitive (str | Unset):
        offset (int | Unset):
        product (int | Unset):
        value (str | Unset):
        value_case_insensitive (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedMetaList]
    """

    kwargs = _get_kwargs(
        endpoint=endpoint,
        finding=finding,
        id=id,
        limit=limit,
        name=name,
        name_case_insensitive=name_case_insensitive,
        offset=offset,
        product=product,
        value=value,
        value_case_insensitive=value_case_insensitive,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    endpoint: int | Unset = UNSET,
    finding: int | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_case_insensitive: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    product: int | Unset = UNSET,
    value: str | Unset = UNSET,
    value_case_insensitive: str | Unset = UNSET,
) -> PaginatedMetaList | None:
    """
    Args:
        endpoint (int | Unset):
        finding (int | Unset):
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        name_case_insensitive (str | Unset):
        offset (int | Unset):
        product (int | Unset):
        value (str | Unset):
        value_case_insensitive (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedMetaList
    """

    return sync_detailed(
        client=client,
        endpoint=endpoint,
        finding=finding,
        id=id,
        limit=limit,
        name=name,
        name_case_insensitive=name_case_insensitive,
        offset=offset,
        product=product,
        value=value,
        value_case_insensitive=value_case_insensitive,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    endpoint: int | Unset = UNSET,
    finding: int | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_case_insensitive: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    product: int | Unset = UNSET,
    value: str | Unset = UNSET,
    value_case_insensitive: str | Unset = UNSET,
) -> Response[PaginatedMetaList]:
    """
    Args:
        endpoint (int | Unset):
        finding (int | Unset):
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        name_case_insensitive (str | Unset):
        offset (int | Unset):
        product (int | Unset):
        value (str | Unset):
        value_case_insensitive (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedMetaList]
    """

    kwargs = _get_kwargs(
        endpoint=endpoint,
        finding=finding,
        id=id,
        limit=limit,
        name=name,
        name_case_insensitive=name_case_insensitive,
        offset=offset,
        product=product,
        value=value,
        value_case_insensitive=value_case_insensitive,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    endpoint: int | Unset = UNSET,
    finding: int | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_case_insensitive: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    product: int | Unset = UNSET,
    value: str | Unset = UNSET,
    value_case_insensitive: str | Unset = UNSET,
) -> PaginatedMetaList | None:
    """
    Args:
        endpoint (int | Unset):
        finding (int | Unset):
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        name_case_insensitive (str | Unset):
        offset (int | Unset):
        product (int | Unset):
        value (str | Unset):
        value_case_insensitive (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedMetaList
    """

    return (
        await asyncio_detailed(
            client=client,
            endpoint=endpoint,
            finding=finding,
            id=id,
            limit=limit,
            name=name,
            name_case_insensitive=name_case_insensitive,
            offset=offset,
            product=product,
            value=value,
            value_case_insensitive=value_case_insensitive,
        )
    ).parsed
