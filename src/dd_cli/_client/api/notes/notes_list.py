import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_note_list import PaginatedNoteList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    author: int | Unset = UNSET,
    date: datetime.datetime | Unset = UNSET,
    edit_time: datetime.datetime | Unset = UNSET,
    edited: bool | Unset = UNSET,
    editor: int | Unset = UNSET,
    entry: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    private: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["author"] = author

    json_date: str | Unset = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    json_edit_time: str | Unset = UNSET
    if not isinstance(edit_time, Unset):
        json_edit_time = edit_time.isoformat()
    params["edit_time"] = json_edit_time

    params["edited"] = edited

    params["editor"] = editor

    params["entry"] = entry

    params["id"] = id

    params["limit"] = limit

    params["offset"] = offset

    params["private"] = private

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/notes/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedNoteList | None:
    if response.status_code == 200:
        response_200 = PaginatedNoteList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedNoteList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    author: int | Unset = UNSET,
    date: datetime.datetime | Unset = UNSET,
    edit_time: datetime.datetime | Unset = UNSET,
    edited: bool | Unset = UNSET,
    editor: int | Unset = UNSET,
    entry: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    private: bool | Unset = UNSET,
) -> Response[PaginatedNoteList]:
    """
    Args:
        author (int | Unset):
        date (datetime.datetime | Unset):
        edit_time (datetime.datetime | Unset):
        edited (bool | Unset):
        editor (int | Unset):
        entry (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        private (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedNoteList]
    """

    kwargs = _get_kwargs(
        author=author,
        date=date,
        edit_time=edit_time,
        edited=edited,
        editor=editor,
        entry=entry,
        id=id,
        limit=limit,
        offset=offset,
        private=private,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    author: int | Unset = UNSET,
    date: datetime.datetime | Unset = UNSET,
    edit_time: datetime.datetime | Unset = UNSET,
    edited: bool | Unset = UNSET,
    editor: int | Unset = UNSET,
    entry: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    private: bool | Unset = UNSET,
) -> PaginatedNoteList | None:
    """
    Args:
        author (int | Unset):
        date (datetime.datetime | Unset):
        edit_time (datetime.datetime | Unset):
        edited (bool | Unset):
        editor (int | Unset):
        entry (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        private (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedNoteList
    """

    return sync_detailed(
        client=client,
        author=author,
        date=date,
        edit_time=edit_time,
        edited=edited,
        editor=editor,
        entry=entry,
        id=id,
        limit=limit,
        offset=offset,
        private=private,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    author: int | Unset = UNSET,
    date: datetime.datetime | Unset = UNSET,
    edit_time: datetime.datetime | Unset = UNSET,
    edited: bool | Unset = UNSET,
    editor: int | Unset = UNSET,
    entry: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    private: bool | Unset = UNSET,
) -> Response[PaginatedNoteList]:
    """
    Args:
        author (int | Unset):
        date (datetime.datetime | Unset):
        edit_time (datetime.datetime | Unset):
        edited (bool | Unset):
        editor (int | Unset):
        entry (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        private (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedNoteList]
    """

    kwargs = _get_kwargs(
        author=author,
        date=date,
        edit_time=edit_time,
        edited=edited,
        editor=editor,
        entry=entry,
        id=id,
        limit=limit,
        offset=offset,
        private=private,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    author: int | Unset = UNSET,
    date: datetime.datetime | Unset = UNSET,
    edit_time: datetime.datetime | Unset = UNSET,
    edited: bool | Unset = UNSET,
    editor: int | Unset = UNSET,
    entry: str | Unset = UNSET,
    id: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    private: bool | Unset = UNSET,
) -> PaginatedNoteList | None:
    """
    Args:
        author (int | Unset):
        date (datetime.datetime | Unset):
        edit_time (datetime.datetime | Unset):
        edited (bool | Unset):
        editor (int | Unset):
        entry (str | Unset):
        id (int | Unset):
        limit (int | Unset):
        offset (int | Unset):
        private (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedNoteList
    """

    return (
        await asyncio_detailed(
            client=client,
            author=author,
            date=date,
            edit_time=edit_time,
            edited=edited,
            editor=editor,
            entry=entry,
            id=id,
            limit=limit,
            offset=offset,
            private=private,
        )
    ).parsed
