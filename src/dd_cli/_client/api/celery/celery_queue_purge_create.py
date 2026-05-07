from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.celery_queue_purge_create_response_200 import CeleryQueuePurgeCreateResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/celery/queue/purge/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CeleryQueuePurgeCreateResponse200 | None:
    if response.status_code == 200:
        response_200 = CeleryQueuePurgeCreateResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CeleryQueuePurgeCreateResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[CeleryQueuePurgeCreateResponse200]:
    """Purge all pending Celery tasks from the queue

     Removes all pending tasks from the default Celery queue. Tasks already being executed by workers are
    not affected. Note: if deduplication tasks were queued, you may need to re-run deduplication
    manually via `python manage.py dedupe`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CeleryQueuePurgeCreateResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> CeleryQueuePurgeCreateResponse200 | None:
    """Purge all pending Celery tasks from the queue

     Removes all pending tasks from the default Celery queue. Tasks already being executed by workers are
    not affected. Note: if deduplication tasks were queued, you may need to re-run deduplication
    manually via `python manage.py dedupe`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CeleryQueuePurgeCreateResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[CeleryQueuePurgeCreateResponse200]:
    """Purge all pending Celery tasks from the queue

     Removes all pending tasks from the default Celery queue. Tasks already being executed by workers are
    not affected. Note: if deduplication tasks were queued, you may need to re-run deduplication
    manually via `python manage.py dedupe`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CeleryQueuePurgeCreateResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> CeleryQueuePurgeCreateResponse200 | None:
    """Purge all pending Celery tasks from the queue

     Removes all pending tasks from the default Celery queue. Tasks already being executed by workers are
    not affected. Note: if deduplication tasks were queued, you may need to re-run deduplication
    manually via `python manage.py dedupe`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CeleryQueuePurgeCreateResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
