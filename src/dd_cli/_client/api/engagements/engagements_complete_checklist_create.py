from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.engagement_check_list import EngagementCheckList
from ...models.engagement_check_list_request import EngagementCheckListRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: EngagementCheckListRequest
    | EngagementCheckListRequest
    | EngagementCheckListRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/engagements/{id}/complete_checklist/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, EngagementCheckListRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, EngagementCheckListRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, EngagementCheckListRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EngagementCheckList | None:
    if response.status_code == 201:
        response_201 = EngagementCheckList.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EngagementCheckList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: EngagementCheckListRequest
    | EngagementCheckListRequest
    | EngagementCheckListRequest
    | Unset = UNSET,
) -> Response[EngagementCheckList]:
    """
    Args:
        id (int):
        body (EngagementCheckListRequest | Unset):
        body (EngagementCheckListRequest | Unset):
        body (EngagementCheckListRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EngagementCheckList]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: EngagementCheckListRequest
    | EngagementCheckListRequest
    | EngagementCheckListRequest
    | Unset = UNSET,
) -> EngagementCheckList | None:
    """
    Args:
        id (int):
        body (EngagementCheckListRequest | Unset):
        body (EngagementCheckListRequest | Unset):
        body (EngagementCheckListRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EngagementCheckList
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: EngagementCheckListRequest
    | EngagementCheckListRequest
    | EngagementCheckListRequest
    | Unset = UNSET,
) -> Response[EngagementCheckList]:
    """
    Args:
        id (int):
        body (EngagementCheckListRequest | Unset):
        body (EngagementCheckListRequest | Unset):
        body (EngagementCheckListRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EngagementCheckList]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: EngagementCheckListRequest
    | EngagementCheckListRequest
    | EngagementCheckListRequest
    | Unset = UNSET,
) -> EngagementCheckList | None:
    """
    Args:
        id (int):
        body (EngagementCheckListRequest | Unset):
        body (EngagementCheckListRequest | Unset):
        body (EngagementCheckListRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EngagementCheckList
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
