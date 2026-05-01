from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_credential_mapping_list import PaginatedCredentialMappingList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cred_id: int | Unset = UNSET,
    engagement: int | Unset = UNSET,
    finding: int | Unset = UNSET,
    is_authn_provider: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    product: int | Unset = UNSET,
    test: int | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cred_id"] = cred_id

    params["engagement"] = engagement

    params["finding"] = finding

    params["is_authn_provider"] = is_authn_provider

    params["limit"] = limit

    params["offset"] = offset

    params["product"] = product

    params["test"] = test

    params["url"] = url_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/credential_mappings/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedCredentialMappingList | None:
    if response.status_code == 200:
        response_200 = PaginatedCredentialMappingList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedCredentialMappingList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cred_id: int | Unset = UNSET,
    engagement: int | Unset = UNSET,
    finding: int | Unset = UNSET,
    is_authn_provider: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    product: int | Unset = UNSET,
    test: int | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> Response[PaginatedCredentialMappingList]:
    """
    Args:
        cred_id (int | Unset):
        engagement (int | Unset):
        finding (int | Unset):
        is_authn_provider (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):
        product (int | Unset):
        test (int | Unset):
        url_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCredentialMappingList]
    """

    kwargs = _get_kwargs(
        cred_id=cred_id,
        engagement=engagement,
        finding=finding,
        is_authn_provider=is_authn_provider,
        limit=limit,
        offset=offset,
        product=product,
        test=test,
        url_query=url_query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cred_id: int | Unset = UNSET,
    engagement: int | Unset = UNSET,
    finding: int | Unset = UNSET,
    is_authn_provider: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    product: int | Unset = UNSET,
    test: int | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> PaginatedCredentialMappingList | None:
    """
    Args:
        cred_id (int | Unset):
        engagement (int | Unset):
        finding (int | Unset):
        is_authn_provider (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):
        product (int | Unset):
        test (int | Unset):
        url_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedCredentialMappingList
    """

    return sync_detailed(
        client=client,
        cred_id=cred_id,
        engagement=engagement,
        finding=finding,
        is_authn_provider=is_authn_provider,
        limit=limit,
        offset=offset,
        product=product,
        test=test,
        url_query=url_query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cred_id: int | Unset = UNSET,
    engagement: int | Unset = UNSET,
    finding: int | Unset = UNSET,
    is_authn_provider: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    product: int | Unset = UNSET,
    test: int | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> Response[PaginatedCredentialMappingList]:
    """
    Args:
        cred_id (int | Unset):
        engagement (int | Unset):
        finding (int | Unset):
        is_authn_provider (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):
        product (int | Unset):
        test (int | Unset):
        url_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCredentialMappingList]
    """

    kwargs = _get_kwargs(
        cred_id=cred_id,
        engagement=engagement,
        finding=finding,
        is_authn_provider=is_authn_provider,
        limit=limit,
        offset=offset,
        product=product,
        test=test,
        url_query=url_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cred_id: int | Unset = UNSET,
    engagement: int | Unset = UNSET,
    finding: int | Unset = UNSET,
    is_authn_provider: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    product: int | Unset = UNSET,
    test: int | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> PaginatedCredentialMappingList | None:
    """
    Args:
        cred_id (int | Unset):
        engagement (int | Unset):
        finding (int | Unset):
        is_authn_provider (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):
        product (int | Unset):
        test (int | Unset):
        url_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedCredentialMappingList
    """

    return (
        await asyncio_detailed(
            client=client,
            cred_id=cred_id,
            engagement=engagement,
            finding=finding,
            is_authn_provider=is_authn_provider,
            limit=limit,
            offset=offset,
            product=product,
            test=test,
            url_query=url_query,
        )
    ).parsed
