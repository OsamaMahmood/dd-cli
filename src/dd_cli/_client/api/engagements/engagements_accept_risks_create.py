from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.accepted_risk_request import AcceptedRiskRequest
from ...models.risk_acceptance import RiskAcceptance
from ...types import UNSET, Response


def _get_kwargs(
    id: int,
    *,
    body: list[AcceptedRiskRequest]
    | list[AcceptedRiskRequest]
    | list[AcceptedRiskRequest]
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/engagements/{id}/accept_risks/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, list[AcceptedRiskRequest]):
        _kwargs["json"] = []
        for body_item_data in body:
            body_item = body_item_data.to_dict()
            _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[AcceptedRiskRequest]):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, list[AcceptedRiskRequest]):
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[RiskAcceptance] | None:
    if response.status_code == 201:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:
            response_201_item = RiskAcceptance.from_dict(response_201_item_data)

            response_201.append(response_201_item)

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[RiskAcceptance]]:
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
    body: list[AcceptedRiskRequest]
    | list[AcceptedRiskRequest]
    | list[AcceptedRiskRequest]
    | Unset = UNSET,
) -> Response[list[RiskAcceptance]]:
    """
    Args:
        id (int):
        body (list[AcceptedRiskRequest]):
        body (list[AcceptedRiskRequest]):
        body (list[AcceptedRiskRequest]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[RiskAcceptance]]
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
    body: list[AcceptedRiskRequest]
    | list[AcceptedRiskRequest]
    | list[AcceptedRiskRequest]
    | Unset = UNSET,
) -> list[RiskAcceptance] | None:
    """
    Args:
        id (int):
        body (list[AcceptedRiskRequest]):
        body (list[AcceptedRiskRequest]):
        body (list[AcceptedRiskRequest]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[RiskAcceptance]
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
    body: list[AcceptedRiskRequest]
    | list[AcceptedRiskRequest]
    | list[AcceptedRiskRequest]
    | Unset = UNSET,
) -> Response[list[RiskAcceptance]]:
    """
    Args:
        id (int):
        body (list[AcceptedRiskRequest]):
        body (list[AcceptedRiskRequest]):
        body (list[AcceptedRiskRequest]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[RiskAcceptance]]
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
    body: list[AcceptedRiskRequest]
    | list[AcceptedRiskRequest]
    | list[AcceptedRiskRequest]
    | Unset = UNSET,
) -> list[RiskAcceptance] | None:
    """
    Args:
        id (int):
        body (list[AcceptedRiskRequest]):
        body (list[AcceptedRiskRequest]):
        body (list[AcceptedRiskRequest]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[RiskAcceptance]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
