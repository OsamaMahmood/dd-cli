import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_stub_finding_list import PaginatedStubFindingList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date: datetime.date | Unset = UNSET,
    description: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    severity: str | Unset = UNSET,
    title: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_date: str | Unset = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    params["description"] = description

    params["id"] = id

    params["limit"] = limit

    params["offset"] = offset

    params["severity"] = severity

    params["title"] = title

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/stub_findings/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedStubFindingList | None:
    if response.status_code == 200:
        response_200 = PaginatedStubFindingList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedStubFindingList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    date: datetime.date | Unset = UNSET,
    description: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    severity: str | Unset = UNSET,
    title: str | Unset = UNSET,
) -> Response[PaginatedStubFindingList]:
    """
    Args:
        date (datetime.date | Unset):
        description (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        severity (str | Unset):
        title (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedStubFindingList]
    """

    kwargs = _get_kwargs(
        date=date,
        description=description,
        id=id,
        limit=limit,
        offset=offset,
        severity=severity,
        title=title,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    date: datetime.date | Unset = UNSET,
    description: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    severity: str | Unset = UNSET,
    title: str | Unset = UNSET,
) -> PaginatedStubFindingList | None:
    """
    Args:
        date (datetime.date | Unset):
        description (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        severity (str | Unset):
        title (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedStubFindingList
    """

    return sync_detailed(
        client=client,
        date=date,
        description=description,
        id=id,
        limit=limit,
        offset=offset,
        severity=severity,
        title=title,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    date: datetime.date | Unset = UNSET,
    description: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    severity: str | Unset = UNSET,
    title: str | Unset = UNSET,
) -> Response[PaginatedStubFindingList]:
    """
    Args:
        date (datetime.date | Unset):
        description (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        severity (str | Unset):
        title (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedStubFindingList]
    """

    kwargs = _get_kwargs(
        date=date,
        description=description,
        id=id,
        limit=limit,
        offset=offset,
        severity=severity,
        title=title,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    date: datetime.date | Unset = UNSET,
    description: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    severity: str | Unset = UNSET,
    title: str | Unset = UNSET,
) -> PaginatedStubFindingList | None:
    """
    Args:
        date (datetime.date | Unset):
        description (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        severity (str | Unset):
        title (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedStubFindingList
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
            description=description,
            id=id,
            limit=limit,
            offset=offset,
            severity=severity,
            title=title,
        )
    ).parsed
