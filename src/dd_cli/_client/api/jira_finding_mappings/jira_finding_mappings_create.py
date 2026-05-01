from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.jira_issue import JIRAIssue
from ...models.jira_issue_request import JIRAIssueRequest
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: JIRAIssueRequest | JIRAIssueRequest | JIRAIssueRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/jira_finding_mappings/",
    }

    if isinstance(body, JIRAIssueRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, JIRAIssueRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, JIRAIssueRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> JIRAIssue | None:
    if response.status_code == 201:
        response_201 = JIRAIssue.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[JIRAIssue]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: JIRAIssueRequest | JIRAIssueRequest | JIRAIssueRequest | Unset = UNSET,
) -> Response[JIRAIssue]:
    """
    Args:
        body (JIRAIssueRequest):
        body (JIRAIssueRequest):
        body (JIRAIssueRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JIRAIssue]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: JIRAIssueRequest | JIRAIssueRequest | JIRAIssueRequest | Unset = UNSET,
) -> JIRAIssue | None:
    """
    Args:
        body (JIRAIssueRequest):
        body (JIRAIssueRequest):
        body (JIRAIssueRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JIRAIssue
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: JIRAIssueRequest | JIRAIssueRequest | JIRAIssueRequest | Unset = UNSET,
) -> Response[JIRAIssue]:
    """
    Args:
        body (JIRAIssueRequest):
        body (JIRAIssueRequest):
        body (JIRAIssueRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JIRAIssue]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: JIRAIssueRequest | JIRAIssueRequest | JIRAIssueRequest | Unset = UNSET,
) -> JIRAIssue | None:
    """
    Args:
        body (JIRAIssueRequest):
        body (JIRAIssueRequest):
        body (JIRAIssueRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JIRAIssue
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
