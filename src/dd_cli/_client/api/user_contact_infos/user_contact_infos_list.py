import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_user_contact_info_list import PaginatedUserContactInfoList
from ...models.user_contact_infos_list_prefetch_item import UserContactInfosListPrefetchItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    block_execution: bool | Unset = UNSET,
    cell_number: str | Unset = UNSET,
    force_password_reset: bool | Unset = UNSET,
    github_username: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    password_last_reset: datetime.datetime | Unset = UNSET,
    phone_number: str | Unset = UNSET,
    prefetch: list[UserContactInfosListPrefetchItem] | Unset = UNSET,
    slack_user_id: str | Unset = UNSET,
    slack_username: str | Unset = UNSET,
    title: str | Unset = UNSET,
    token_last_reset: datetime.datetime | Unset = UNSET,
    twitter_username: str | Unset = UNSET,
    user: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["block_execution"] = block_execution

    params["cell_number"] = cell_number

    params["force_password_reset"] = force_password_reset

    params["github_username"] = github_username

    params["limit"] = limit

    params["offset"] = offset

    json_password_last_reset: str | Unset = UNSET
    if not isinstance(password_last_reset, Unset):
        json_password_last_reset = password_last_reset.isoformat()
    params["password_last_reset"] = json_password_last_reset

    params["phone_number"] = phone_number

    json_prefetch: list[str] | Unset = UNSET
    if not isinstance(prefetch, Unset):
        json_prefetch = []
        for prefetch_item_data in prefetch:
            prefetch_item = prefetch_item_data.value
            json_prefetch.append(prefetch_item)

    params["prefetch"] = json_prefetch

    params["slack_user_id"] = slack_user_id

    params["slack_username"] = slack_username

    params["title"] = title

    json_token_last_reset: str | Unset = UNSET
    if not isinstance(token_last_reset, Unset):
        json_token_last_reset = token_last_reset.isoformat()
    params["token_last_reset"] = json_token_last_reset

    params["twitter_username"] = twitter_username

    params["user"] = user

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/user_contact_infos/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedUserContactInfoList | None:
    if response.status_code == 200:
        response_200 = PaginatedUserContactInfoList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedUserContactInfoList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    block_execution: bool | Unset = UNSET,
    cell_number: str | Unset = UNSET,
    force_password_reset: bool | Unset = UNSET,
    github_username: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    password_last_reset: datetime.datetime | Unset = UNSET,
    phone_number: str | Unset = UNSET,
    prefetch: list[UserContactInfosListPrefetchItem] | Unset = UNSET,
    slack_user_id: str | Unset = UNSET,
    slack_username: str | Unset = UNSET,
    title: str | Unset = UNSET,
    token_last_reset: datetime.datetime | Unset = UNSET,
    twitter_username: str | Unset = UNSET,
    user: int | Unset = UNSET,
) -> Response[PaginatedUserContactInfoList]:
    """
    Args:
        block_execution (bool | Unset):
        cell_number (str | Unset):
        force_password_reset (bool | Unset):
        github_username (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        password_last_reset (datetime.datetime | Unset):
        phone_number (str | Unset):
        prefetch (list[UserContactInfosListPrefetchItem] | Unset):
        slack_user_id (str | Unset):
        slack_username (str | Unset):
        title (str | Unset):
        token_last_reset (datetime.datetime | Unset):
        twitter_username (str | Unset):
        user (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserContactInfoList]
    """

    kwargs = _get_kwargs(
        block_execution=block_execution,
        cell_number=cell_number,
        force_password_reset=force_password_reset,
        github_username=github_username,
        limit=limit,
        offset=offset,
        password_last_reset=password_last_reset,
        phone_number=phone_number,
        prefetch=prefetch,
        slack_user_id=slack_user_id,
        slack_username=slack_username,
        title=title,
        token_last_reset=token_last_reset,
        twitter_username=twitter_username,
        user=user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    block_execution: bool | Unset = UNSET,
    cell_number: str | Unset = UNSET,
    force_password_reset: bool | Unset = UNSET,
    github_username: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    password_last_reset: datetime.datetime | Unset = UNSET,
    phone_number: str | Unset = UNSET,
    prefetch: list[UserContactInfosListPrefetchItem] | Unset = UNSET,
    slack_user_id: str | Unset = UNSET,
    slack_username: str | Unset = UNSET,
    title: str | Unset = UNSET,
    token_last_reset: datetime.datetime | Unset = UNSET,
    twitter_username: str | Unset = UNSET,
    user: int | Unset = UNSET,
) -> PaginatedUserContactInfoList | None:
    """
    Args:
        block_execution (bool | Unset):
        cell_number (str | Unset):
        force_password_reset (bool | Unset):
        github_username (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        password_last_reset (datetime.datetime | Unset):
        phone_number (str | Unset):
        prefetch (list[UserContactInfosListPrefetchItem] | Unset):
        slack_user_id (str | Unset):
        slack_username (str | Unset):
        title (str | Unset):
        token_last_reset (datetime.datetime | Unset):
        twitter_username (str | Unset):
        user (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedUserContactInfoList
    """

    return sync_detailed(
        client=client,
        block_execution=block_execution,
        cell_number=cell_number,
        force_password_reset=force_password_reset,
        github_username=github_username,
        limit=limit,
        offset=offset,
        password_last_reset=password_last_reset,
        phone_number=phone_number,
        prefetch=prefetch,
        slack_user_id=slack_user_id,
        slack_username=slack_username,
        title=title,
        token_last_reset=token_last_reset,
        twitter_username=twitter_username,
        user=user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    block_execution: bool | Unset = UNSET,
    cell_number: str | Unset = UNSET,
    force_password_reset: bool | Unset = UNSET,
    github_username: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    password_last_reset: datetime.datetime | Unset = UNSET,
    phone_number: str | Unset = UNSET,
    prefetch: list[UserContactInfosListPrefetchItem] | Unset = UNSET,
    slack_user_id: str | Unset = UNSET,
    slack_username: str | Unset = UNSET,
    title: str | Unset = UNSET,
    token_last_reset: datetime.datetime | Unset = UNSET,
    twitter_username: str | Unset = UNSET,
    user: int | Unset = UNSET,
) -> Response[PaginatedUserContactInfoList]:
    """
    Args:
        block_execution (bool | Unset):
        cell_number (str | Unset):
        force_password_reset (bool | Unset):
        github_username (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        password_last_reset (datetime.datetime | Unset):
        phone_number (str | Unset):
        prefetch (list[UserContactInfosListPrefetchItem] | Unset):
        slack_user_id (str | Unset):
        slack_username (str | Unset):
        title (str | Unset):
        token_last_reset (datetime.datetime | Unset):
        twitter_username (str | Unset):
        user (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserContactInfoList]
    """

    kwargs = _get_kwargs(
        block_execution=block_execution,
        cell_number=cell_number,
        force_password_reset=force_password_reset,
        github_username=github_username,
        limit=limit,
        offset=offset,
        password_last_reset=password_last_reset,
        phone_number=phone_number,
        prefetch=prefetch,
        slack_user_id=slack_user_id,
        slack_username=slack_username,
        title=title,
        token_last_reset=token_last_reset,
        twitter_username=twitter_username,
        user=user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    block_execution: bool | Unset = UNSET,
    cell_number: str | Unset = UNSET,
    force_password_reset: bool | Unset = UNSET,
    github_username: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    password_last_reset: datetime.datetime | Unset = UNSET,
    phone_number: str | Unset = UNSET,
    prefetch: list[UserContactInfosListPrefetchItem] | Unset = UNSET,
    slack_user_id: str | Unset = UNSET,
    slack_username: str | Unset = UNSET,
    title: str | Unset = UNSET,
    token_last_reset: datetime.datetime | Unset = UNSET,
    twitter_username: str | Unset = UNSET,
    user: int | Unset = UNSET,
) -> PaginatedUserContactInfoList | None:
    """
    Args:
        block_execution (bool | Unset):
        cell_number (str | Unset):
        force_password_reset (bool | Unset):
        github_username (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        password_last_reset (datetime.datetime | Unset):
        phone_number (str | Unset):
        prefetch (list[UserContactInfosListPrefetchItem] | Unset):
        slack_user_id (str | Unset):
        slack_username (str | Unset):
        title (str | Unset):
        token_last_reset (datetime.datetime | Unset):
        twitter_username (str | Unset):
        user (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedUserContactInfoList
    """

    return (
        await asyncio_detailed(
            client=client,
            block_execution=block_execution,
            cell_number=cell_number,
            force_password_reset=force_password_reset,
            github_username=github_username,
            limit=limit,
            offset=offset,
            password_last_reset=password_last_reset,
            phone_number=phone_number,
            prefetch=prefetch,
            slack_user_id=slack_user_id,
            slack_username=slack_username,
            title=title,
            token_last_reset=token_last_reset,
            twitter_username=twitter_username,
            user=user,
        )
    ).parsed
