from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.finding_meta import FindingMeta
from ...models.finding_meta_request import FindingMetaRequest
from ...types import UNSET, Response


def _get_kwargs(
    id: int,
    *,
    body: FindingMetaRequest | FindingMetaRequest | FindingMetaRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/findings/{id}/metadata/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, FindingMetaRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, FindingMetaRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, FindingMetaRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FindingMeta | None:
    if response.status_code == 200:
        response_200 = FindingMeta.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | FindingMeta]:
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
    body: FindingMetaRequest | FindingMetaRequest | FindingMetaRequest | Unset = UNSET,
) -> Response[Any | FindingMeta]:
    """
    Args:
        id (int):
        body (FindingMetaRequest):
        body (FindingMetaRequest):
        body (FindingMetaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FindingMeta]
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
    body: FindingMetaRequest | FindingMetaRequest | FindingMetaRequest | Unset = UNSET,
) -> Any | FindingMeta | None:
    """
    Args:
        id (int):
        body (FindingMetaRequest):
        body (FindingMetaRequest):
        body (FindingMetaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FindingMeta
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
    body: FindingMetaRequest | FindingMetaRequest | FindingMetaRequest | Unset = UNSET,
) -> Response[Any | FindingMeta]:
    """
    Args:
        id (int):
        body (FindingMetaRequest):
        body (FindingMetaRequest):
        body (FindingMetaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FindingMeta]
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
    body: FindingMetaRequest | FindingMetaRequest | FindingMetaRequest | Unset = UNSET,
) -> Any | FindingMeta | None:
    """
    Args:
        id (int):
        body (FindingMetaRequest):
        body (FindingMetaRequest):
        body (FindingMetaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FindingMeta
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
