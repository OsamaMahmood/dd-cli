import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_user_list import PaginatedUserList
from ...models.users_list_o_item import UsersListOItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date_joined_after: datetime.date | Unset = UNSET,
    date_joined_before: datetime.date | Unset = UNSET,
    email: str | Unset = UNSET,
    first_name: str | Unset = UNSET,
    id: int | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    is_superuser: bool | Unset = UNSET,
    last_login_after: datetime.date | Unset = UNSET,
    last_login_before: datetime.date | Unset = UNSET,
    last_name: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    o: list[UsersListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    username: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_date_joined_after: str | Unset = UNSET
    if not isinstance(date_joined_after, Unset):
        json_date_joined_after = date_joined_after.isoformat()
    params["date_joined_after"] = json_date_joined_after

    json_date_joined_before: str | Unset = UNSET
    if not isinstance(date_joined_before, Unset):
        json_date_joined_before = date_joined_before.isoformat()
    params["date_joined_before"] = json_date_joined_before

    params["email"] = email

    params["first_name"] = first_name

    params["id"] = id

    params["is_active"] = is_active

    params["is_superuser"] = is_superuser

    json_last_login_after: str | Unset = UNSET
    if not isinstance(last_login_after, Unset):
        json_last_login_after = last_login_after.isoformat()
    params["last_login_after"] = json_last_login_after

    json_last_login_before: str | Unset = UNSET
    if not isinstance(last_login_before, Unset):
        json_last_login_before = last_login_before.isoformat()
    params["last_login_before"] = json_last_login_before

    params["last_name"] = last_name

    params["limit"] = limit

    json_o: list[str] | Unset = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    params["offset"] = offset

    params["username"] = username

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/users/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedUserList | None:
    if response.status_code == 200:
        response_200 = PaginatedUserList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedUserList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    date_joined_after: datetime.date | Unset = UNSET,
    date_joined_before: datetime.date | Unset = UNSET,
    email: str | Unset = UNSET,
    first_name: str | Unset = UNSET,
    id: int | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    is_superuser: bool | Unset = UNSET,
    last_login_after: datetime.date | Unset = UNSET,
    last_login_before: datetime.date | Unset = UNSET,
    last_name: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    o: list[UsersListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    username: str | Unset = UNSET,
) -> Response[PaginatedUserList]:
    """
    Args:
        date_joined_after (datetime.date | Unset):
        date_joined_before (datetime.date | Unset):
        email (str | Unset):
        first_name (str | Unset):
        id (int | Unset):
        is_active (bool | Unset):
        is_superuser (bool | Unset):
        last_login_after (datetime.date | Unset):
        last_login_before (datetime.date | Unset):
        last_name (str | Unset):
        limit (int | Unset):
        o (list[UsersListOItem] | Unset):
        offset (int | Unset):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserList]
    """

    kwargs = _get_kwargs(
        date_joined_after=date_joined_after,
        date_joined_before=date_joined_before,
        email=email,
        first_name=first_name,
        id=id,
        is_active=is_active,
        is_superuser=is_superuser,
        last_login_after=last_login_after,
        last_login_before=last_login_before,
        last_name=last_name,
        limit=limit,
        o=o,
        offset=offset,
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    date_joined_after: datetime.date | Unset = UNSET,
    date_joined_before: datetime.date | Unset = UNSET,
    email: str | Unset = UNSET,
    first_name: str | Unset = UNSET,
    id: int | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    is_superuser: bool | Unset = UNSET,
    last_login_after: datetime.date | Unset = UNSET,
    last_login_before: datetime.date | Unset = UNSET,
    last_name: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    o: list[UsersListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    username: str | Unset = UNSET,
) -> PaginatedUserList | None:
    """
    Args:
        date_joined_after (datetime.date | Unset):
        date_joined_before (datetime.date | Unset):
        email (str | Unset):
        first_name (str | Unset):
        id (int | Unset):
        is_active (bool | Unset):
        is_superuser (bool | Unset):
        last_login_after (datetime.date | Unset):
        last_login_before (datetime.date | Unset):
        last_name (str | Unset):
        limit (int | Unset):
        o (list[UsersListOItem] | Unset):
        offset (int | Unset):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedUserList
    """

    return sync_detailed(
        client=client,
        date_joined_after=date_joined_after,
        date_joined_before=date_joined_before,
        email=email,
        first_name=first_name,
        id=id,
        is_active=is_active,
        is_superuser=is_superuser,
        last_login_after=last_login_after,
        last_login_before=last_login_before,
        last_name=last_name,
        limit=limit,
        o=o,
        offset=offset,
        username=username,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    date_joined_after: datetime.date | Unset = UNSET,
    date_joined_before: datetime.date | Unset = UNSET,
    email: str | Unset = UNSET,
    first_name: str | Unset = UNSET,
    id: int | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    is_superuser: bool | Unset = UNSET,
    last_login_after: datetime.date | Unset = UNSET,
    last_login_before: datetime.date | Unset = UNSET,
    last_name: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    o: list[UsersListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    username: str | Unset = UNSET,
) -> Response[PaginatedUserList]:
    """
    Args:
        date_joined_after (datetime.date | Unset):
        date_joined_before (datetime.date | Unset):
        email (str | Unset):
        first_name (str | Unset):
        id (int | Unset):
        is_active (bool | Unset):
        is_superuser (bool | Unset):
        last_login_after (datetime.date | Unset):
        last_login_before (datetime.date | Unset):
        last_name (str | Unset):
        limit (int | Unset):
        o (list[UsersListOItem] | Unset):
        offset (int | Unset):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserList]
    """

    kwargs = _get_kwargs(
        date_joined_after=date_joined_after,
        date_joined_before=date_joined_before,
        email=email,
        first_name=first_name,
        id=id,
        is_active=is_active,
        is_superuser=is_superuser,
        last_login_after=last_login_after,
        last_login_before=last_login_before,
        last_name=last_name,
        limit=limit,
        o=o,
        offset=offset,
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    date_joined_after: datetime.date | Unset = UNSET,
    date_joined_before: datetime.date | Unset = UNSET,
    email: str | Unset = UNSET,
    first_name: str | Unset = UNSET,
    id: int | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    is_superuser: bool | Unset = UNSET,
    last_login_after: datetime.date | Unset = UNSET,
    last_login_before: datetime.date | Unset = UNSET,
    last_name: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    o: list[UsersListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    username: str | Unset = UNSET,
) -> PaginatedUserList | None:
    """
    Args:
        date_joined_after (datetime.date | Unset):
        date_joined_before (datetime.date | Unset):
        email (str | Unset):
        first_name (str | Unset):
        id (int | Unset):
        is_active (bool | Unset):
        is_superuser (bool | Unset):
        last_login_after (datetime.date | Unset):
        last_login_before (datetime.date | Unset):
        last_name (str | Unset):
        limit (int | Unset):
        o (list[UsersListOItem] | Unset):
        offset (int | Unset):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedUserList
    """

    return (
        await asyncio_detailed(
            client=client,
            date_joined_after=date_joined_after,
            date_joined_before=date_joined_before,
            email=email,
            first_name=first_name,
            id=id,
            is_active=is_active,
            is_superuser=is_superuser,
            last_login_after=last_login_after,
            last_login_before=last_login_before,
            last_name=last_name,
            limit=limit,
            o=o,
            offset=offset,
            username=username,
        )
    ).parsed
