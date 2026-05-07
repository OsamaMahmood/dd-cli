from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.celery_queue_task_detail import CeleryQueueTaskDetail
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/celery/queue/details/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[CeleryQueueTaskDetail] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CeleryQueueTaskDetail.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[CeleryQueueTaskDetail]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[list[CeleryQueueTaskDetail]]:
    """Get per-task breakdown of the Celery queue

     Scans every message in the queue (O(N)) and returns task name, count, and oldest/newest queue
    positions. May be slow for large queues.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[CeleryQueueTaskDetail]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> list[CeleryQueueTaskDetail] | None:
    """Get per-task breakdown of the Celery queue

     Scans every message in the queue (O(N)) and returns task name, count, and oldest/newest queue
    positions. May be slow for large queues.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[CeleryQueueTaskDetail]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[list[CeleryQueueTaskDetail]]:
    """Get per-task breakdown of the Celery queue

     Scans every message in the queue (O(N)) and returns task name, count, and oldest/newest queue
    positions. May be slow for large queues.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[CeleryQueueTaskDetail]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> list[CeleryQueueTaskDetail] | None:
    """Get per-task breakdown of the Celery queue

     Scans every message in the queue (O(N)) and returns task name, count, and oldest/newest queue
    positions. May be slow for large queues.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[CeleryQueueTaskDetail]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
