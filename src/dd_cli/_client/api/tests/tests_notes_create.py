from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_new_note_option_request import AddNewNoteOptionRequest
from ...models.note import Note
from ...types import UNSET, Response


def _get_kwargs(
    id: int,
    *,
    body: AddNewNoteOptionRequest
    | AddNewNoteOptionRequest
    | AddNewNoteOptionRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/tests/{id}/notes/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, AddNewNoteOptionRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, AddNewNoteOptionRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, AddNewNoteOptionRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Note | None:
    if response.status_code == 201:
        response_201 = Note.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Note]:
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
    body: AddNewNoteOptionRequest
    | AddNewNoteOptionRequest
    | AddNewNoteOptionRequest
    | Unset = UNSET,
) -> Response[Note]:
    """
    Args:
        id (int):
        body (AddNewNoteOptionRequest):
        body (AddNewNoteOptionRequest):
        body (AddNewNoteOptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Note]
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
    body: AddNewNoteOptionRequest
    | AddNewNoteOptionRequest
    | AddNewNoteOptionRequest
    | Unset = UNSET,
) -> Note | None:
    """
    Args:
        id (int):
        body (AddNewNoteOptionRequest):
        body (AddNewNoteOptionRequest):
        body (AddNewNoteOptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Note
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
    body: AddNewNoteOptionRequest
    | AddNewNoteOptionRequest
    | AddNewNoteOptionRequest
    | Unset = UNSET,
) -> Response[Note]:
    """
    Args:
        id (int):
        body (AddNewNoteOptionRequest):
        body (AddNewNoteOptionRequest):
        body (AddNewNoteOptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Note]
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
    body: AddNewNoteOptionRequest
    | AddNewNoteOptionRequest
    | AddNewNoteOptionRequest
    | Unset = UNSET,
) -> Note | None:
    """
    Args:
        id (int):
        body (AddNewNoteOptionRequest):
        body (AddNewNoteOptionRequest):
        body (AddNewNoteOptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Note
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
