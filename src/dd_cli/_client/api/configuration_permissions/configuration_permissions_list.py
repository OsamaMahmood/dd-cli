from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_configuration_permission_list import PaginatedConfigurationPermissionList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    codename: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["codename"] = codename

    params["id"] = id

    params["limit"] = limit

    params["name"] = name

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/configuration_permissions/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedConfigurationPermissionList | None:
    if response.status_code == 200:
        response_200 = PaginatedConfigurationPermissionList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedConfigurationPermissionList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    codename: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PaginatedConfigurationPermissionList]:
    """
    Args:
        codename (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedConfigurationPermissionList]
    """

    kwargs = _get_kwargs(
        codename=codename,
        id=id,
        limit=limit,
        name=name,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    codename: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PaginatedConfigurationPermissionList | None:
    """
    Args:
        codename (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedConfigurationPermissionList
    """

    return sync_detailed(
        client=client,
        codename=codename,
        id=id,
        limit=limit,
        name=name,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    codename: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PaginatedConfigurationPermissionList]:
    """
    Args:
        codename (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedConfigurationPermissionList]
    """

    kwargs = _get_kwargs(
        codename=codename,
        id=id,
        limit=limit,
        name=name,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    codename: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PaginatedConfigurationPermissionList | None:
    """
    Args:
        codename (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedConfigurationPermissionList
    """

    return (
        await asyncio_detailed(
            client=client,
            codename=codename,
            id=id,
            limit=limit,
            name=name,
            offset=offset,
        )
    ).parsed
