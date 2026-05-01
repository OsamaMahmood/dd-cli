from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_endpoint_status_list import PaginatedEndpointStatusList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    endpoint: int | Unset = UNSET,
    false_positive: bool | Unset = UNSET,
    finding: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    mitigated: bool | Unset = UNSET,
    mitigated_by: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    out_of_scope: bool | Unset = UNSET,
    risk_accepted: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["endpoint"] = endpoint

    params["false_positive"] = false_positive

    params["finding"] = finding

    params["limit"] = limit

    params["mitigated"] = mitigated

    params["mitigated_by"] = mitigated_by

    params["offset"] = offset

    params["out_of_scope"] = out_of_scope

    params["risk_accepted"] = risk_accepted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/endpoint_status/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedEndpointStatusList | None:
    if response.status_code == 200:
        response_200 = PaginatedEndpointStatusList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedEndpointStatusList]:
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
    false_positive: bool | Unset = UNSET,
    finding: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    mitigated: bool | Unset = UNSET,
    mitigated_by: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    out_of_scope: bool | Unset = UNSET,
    risk_accepted: bool | Unset = UNSET,
) -> Response[PaginatedEndpointStatusList]:
    """
    Args:
        endpoint (int | Unset):
        false_positive (bool | Unset):
        finding (int | Unset):
        limit (int | Unset):
        mitigated (bool | Unset):
        mitigated_by (int | Unset):
        offset (int | Unset):
        out_of_scope (bool | Unset):
        risk_accepted (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedEndpointStatusList]
    """

    kwargs = _get_kwargs(
        endpoint=endpoint,
        false_positive=false_positive,
        finding=finding,
        limit=limit,
        mitigated=mitigated,
        mitigated_by=mitigated_by,
        offset=offset,
        out_of_scope=out_of_scope,
        risk_accepted=risk_accepted,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    endpoint: int | Unset = UNSET,
    false_positive: bool | Unset = UNSET,
    finding: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    mitigated: bool | Unset = UNSET,
    mitigated_by: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    out_of_scope: bool | Unset = UNSET,
    risk_accepted: bool | Unset = UNSET,
) -> PaginatedEndpointStatusList | None:
    """
    Args:
        endpoint (int | Unset):
        false_positive (bool | Unset):
        finding (int | Unset):
        limit (int | Unset):
        mitigated (bool | Unset):
        mitigated_by (int | Unset):
        offset (int | Unset):
        out_of_scope (bool | Unset):
        risk_accepted (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedEndpointStatusList
    """

    return sync_detailed(
        client=client,
        endpoint=endpoint,
        false_positive=false_positive,
        finding=finding,
        limit=limit,
        mitigated=mitigated,
        mitigated_by=mitigated_by,
        offset=offset,
        out_of_scope=out_of_scope,
        risk_accepted=risk_accepted,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    endpoint: int | Unset = UNSET,
    false_positive: bool | Unset = UNSET,
    finding: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    mitigated: bool | Unset = UNSET,
    mitigated_by: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    out_of_scope: bool | Unset = UNSET,
    risk_accepted: bool | Unset = UNSET,
) -> Response[PaginatedEndpointStatusList]:
    """
    Args:
        endpoint (int | Unset):
        false_positive (bool | Unset):
        finding (int | Unset):
        limit (int | Unset):
        mitigated (bool | Unset):
        mitigated_by (int | Unset):
        offset (int | Unset):
        out_of_scope (bool | Unset):
        risk_accepted (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedEndpointStatusList]
    """

    kwargs = _get_kwargs(
        endpoint=endpoint,
        false_positive=false_positive,
        finding=finding,
        limit=limit,
        mitigated=mitigated,
        mitigated_by=mitigated_by,
        offset=offset,
        out_of_scope=out_of_scope,
        risk_accepted=risk_accepted,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    endpoint: int | Unset = UNSET,
    false_positive: bool | Unset = UNSET,
    finding: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    mitigated: bool | Unset = UNSET,
    mitigated_by: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    out_of_scope: bool | Unset = UNSET,
    risk_accepted: bool | Unset = UNSET,
) -> PaginatedEndpointStatusList | None:
    """
    Args:
        endpoint (int | Unset):
        false_positive (bool | Unset):
        finding (int | Unset):
        limit (int | Unset):
        mitigated (bool | Unset):
        mitigated_by (int | Unset):
        offset (int | Unset):
        out_of_scope (bool | Unset):
        risk_accepted (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedEndpointStatusList
    """

    return (
        await asyncio_detailed(
            client=client,
            endpoint=endpoint,
            false_positive=false_positive,
            finding=finding,
            limit=limit,
            mitigated=mitigated,
            mitigated_by=mitigated_by,
            offset=offset,
            out_of_scope=out_of_scope,
            risk_accepted=risk_accepted,
        )
    ).parsed
