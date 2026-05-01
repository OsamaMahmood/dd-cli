import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_risk_acceptance_list import PaginatedRiskAcceptanceList
from ...models.risk_acceptance_list_decision import RiskAcceptanceListDecision
from ...models.risk_acceptance_list_o_item import RiskAcceptanceListOItem
from ...models.risk_acceptance_list_security_recommendation import (
    RiskAcceptanceListSecurityRecommendation,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    accepted_by: str | Unset = UNSET,
    accepted_findings: list[int] | Unset = UNSET,
    decision: RiskAcceptanceListDecision | Unset = UNSET,
    decision_details: str | Unset = UNSET,
    expiration_date: datetime.datetime | Unset = UNSET,
    expiration_date_handled: datetime.datetime | Unset = UNSET,
    expiration_date_warned: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    notes: list[int] | Unset = UNSET,
    o: list[RiskAcceptanceListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    owner: int | Unset = UNSET,
    reactivate_expired: bool | Unset = UNSET,
    recommendation: RiskAcceptanceListSecurityRecommendation | Unset = UNSET,
    recommendation_details: str | Unset = UNSET,
    restart_sla_expired: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accepted_by"] = accepted_by

    json_accepted_findings: list[int] | Unset = UNSET
    if not isinstance(accepted_findings, Unset):
        json_accepted_findings = accepted_findings

    params["accepted_findings"] = json_accepted_findings

    json_decision: str | Unset = UNSET
    if not isinstance(decision, Unset):
        json_decision = decision.value

    params["decision"] = json_decision

    params["decision_details"] = decision_details

    json_expiration_date: str | Unset = UNSET
    if not isinstance(expiration_date, Unset):
        json_expiration_date = expiration_date.isoformat()
    params["expiration_date"] = json_expiration_date

    json_expiration_date_handled: str | Unset = UNSET
    if not isinstance(expiration_date_handled, Unset):
        json_expiration_date_handled = expiration_date_handled.isoformat()
    params["expiration_date_handled"] = json_expiration_date_handled

    json_expiration_date_warned: str | Unset = UNSET
    if not isinstance(expiration_date_warned, Unset):
        json_expiration_date_warned = expiration_date_warned.isoformat()
    params["expiration_date_warned"] = json_expiration_date_warned

    params["limit"] = limit

    params["name"] = name

    json_notes: list[int] | Unset = UNSET
    if not isinstance(notes, Unset):
        json_notes = notes

    params["notes"] = json_notes

    json_o: list[str] | Unset = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    params["offset"] = offset

    params["owner"] = owner

    params["reactivate_expired"] = reactivate_expired

    json_recommendation: str | Unset = UNSET
    if not isinstance(recommendation, Unset):
        json_recommendation = recommendation.value

    params["recommendation"] = json_recommendation

    params["recommendation_details"] = recommendation_details

    params["restart_sla_expired"] = restart_sla_expired

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/risk_acceptance/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedRiskAcceptanceList | None:
    if response.status_code == 200:
        response_200 = PaginatedRiskAcceptanceList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedRiskAcceptanceList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    accepted_by: str | Unset = UNSET,
    accepted_findings: list[int] | Unset = UNSET,
    decision: RiskAcceptanceListDecision | Unset = UNSET,
    decision_details: str | Unset = UNSET,
    expiration_date: datetime.datetime | Unset = UNSET,
    expiration_date_handled: datetime.datetime | Unset = UNSET,
    expiration_date_warned: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    notes: list[int] | Unset = UNSET,
    o: list[RiskAcceptanceListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    owner: int | Unset = UNSET,
    reactivate_expired: bool | Unset = UNSET,
    recommendation: RiskAcceptanceListSecurityRecommendation | Unset = UNSET,
    recommendation_details: str | Unset = UNSET,
    restart_sla_expired: bool | Unset = UNSET,
) -> Response[PaginatedRiskAcceptanceList]:
    """
    Args:
        accepted_by (str | Unset):
        accepted_findings (list[int] | Unset):
        decision (RiskAcceptanceListDecision | Unset):
        decision_details (str | Unset):
        expiration_date (datetime.datetime | Unset):
        expiration_date_handled (datetime.datetime | Unset):
        expiration_date_warned (datetime.datetime | Unset):
        limit (int | Unset):
        name (str | Unset):
        notes (list[int] | Unset):
        o (list[RiskAcceptanceListOItem] | Unset):
        offset (int | Unset):
        owner (int | Unset):
        reactivate_expired (bool | Unset):
        recommendation (RiskAcceptanceListSecurityRecommendation | Unset):
        recommendation_details (str | Unset):
        restart_sla_expired (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRiskAcceptanceList]
    """

    kwargs = _get_kwargs(
        accepted_by=accepted_by,
        accepted_findings=accepted_findings,
        decision=decision,
        decision_details=decision_details,
        expiration_date=expiration_date,
        expiration_date_handled=expiration_date_handled,
        expiration_date_warned=expiration_date_warned,
        limit=limit,
        name=name,
        notes=notes,
        o=o,
        offset=offset,
        owner=owner,
        reactivate_expired=reactivate_expired,
        recommendation=recommendation,
        recommendation_details=recommendation_details,
        restart_sla_expired=restart_sla_expired,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    accepted_by: str | Unset = UNSET,
    accepted_findings: list[int] | Unset = UNSET,
    decision: RiskAcceptanceListDecision | Unset = UNSET,
    decision_details: str | Unset = UNSET,
    expiration_date: datetime.datetime | Unset = UNSET,
    expiration_date_handled: datetime.datetime | Unset = UNSET,
    expiration_date_warned: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    notes: list[int] | Unset = UNSET,
    o: list[RiskAcceptanceListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    owner: int | Unset = UNSET,
    reactivate_expired: bool | Unset = UNSET,
    recommendation: RiskAcceptanceListSecurityRecommendation | Unset = UNSET,
    recommendation_details: str | Unset = UNSET,
    restart_sla_expired: bool | Unset = UNSET,
) -> PaginatedRiskAcceptanceList | None:
    """
    Args:
        accepted_by (str | Unset):
        accepted_findings (list[int] | Unset):
        decision (RiskAcceptanceListDecision | Unset):
        decision_details (str | Unset):
        expiration_date (datetime.datetime | Unset):
        expiration_date_handled (datetime.datetime | Unset):
        expiration_date_warned (datetime.datetime | Unset):
        limit (int | Unset):
        name (str | Unset):
        notes (list[int] | Unset):
        o (list[RiskAcceptanceListOItem] | Unset):
        offset (int | Unset):
        owner (int | Unset):
        reactivate_expired (bool | Unset):
        recommendation (RiskAcceptanceListSecurityRecommendation | Unset):
        recommendation_details (str | Unset):
        restart_sla_expired (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRiskAcceptanceList
    """

    return sync_detailed(
        client=client,
        accepted_by=accepted_by,
        accepted_findings=accepted_findings,
        decision=decision,
        decision_details=decision_details,
        expiration_date=expiration_date,
        expiration_date_handled=expiration_date_handled,
        expiration_date_warned=expiration_date_warned,
        limit=limit,
        name=name,
        notes=notes,
        o=o,
        offset=offset,
        owner=owner,
        reactivate_expired=reactivate_expired,
        recommendation=recommendation,
        recommendation_details=recommendation_details,
        restart_sla_expired=restart_sla_expired,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    accepted_by: str | Unset = UNSET,
    accepted_findings: list[int] | Unset = UNSET,
    decision: RiskAcceptanceListDecision | Unset = UNSET,
    decision_details: str | Unset = UNSET,
    expiration_date: datetime.datetime | Unset = UNSET,
    expiration_date_handled: datetime.datetime | Unset = UNSET,
    expiration_date_warned: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    notes: list[int] | Unset = UNSET,
    o: list[RiskAcceptanceListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    owner: int | Unset = UNSET,
    reactivate_expired: bool | Unset = UNSET,
    recommendation: RiskAcceptanceListSecurityRecommendation | Unset = UNSET,
    recommendation_details: str | Unset = UNSET,
    restart_sla_expired: bool | Unset = UNSET,
) -> Response[PaginatedRiskAcceptanceList]:
    """
    Args:
        accepted_by (str | Unset):
        accepted_findings (list[int] | Unset):
        decision (RiskAcceptanceListDecision | Unset):
        decision_details (str | Unset):
        expiration_date (datetime.datetime | Unset):
        expiration_date_handled (datetime.datetime | Unset):
        expiration_date_warned (datetime.datetime | Unset):
        limit (int | Unset):
        name (str | Unset):
        notes (list[int] | Unset):
        o (list[RiskAcceptanceListOItem] | Unset):
        offset (int | Unset):
        owner (int | Unset):
        reactivate_expired (bool | Unset):
        recommendation (RiskAcceptanceListSecurityRecommendation | Unset):
        recommendation_details (str | Unset):
        restart_sla_expired (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRiskAcceptanceList]
    """

    kwargs = _get_kwargs(
        accepted_by=accepted_by,
        accepted_findings=accepted_findings,
        decision=decision,
        decision_details=decision_details,
        expiration_date=expiration_date,
        expiration_date_handled=expiration_date_handled,
        expiration_date_warned=expiration_date_warned,
        limit=limit,
        name=name,
        notes=notes,
        o=o,
        offset=offset,
        owner=owner,
        reactivate_expired=reactivate_expired,
        recommendation=recommendation,
        recommendation_details=recommendation_details,
        restart_sla_expired=restart_sla_expired,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    accepted_by: str | Unset = UNSET,
    accepted_findings: list[int] | Unset = UNSET,
    decision: RiskAcceptanceListDecision | Unset = UNSET,
    decision_details: str | Unset = UNSET,
    expiration_date: datetime.datetime | Unset = UNSET,
    expiration_date_handled: datetime.datetime | Unset = UNSET,
    expiration_date_warned: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    notes: list[int] | Unset = UNSET,
    o: list[RiskAcceptanceListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    owner: int | Unset = UNSET,
    reactivate_expired: bool | Unset = UNSET,
    recommendation: RiskAcceptanceListSecurityRecommendation | Unset = UNSET,
    recommendation_details: str | Unset = UNSET,
    restart_sla_expired: bool | Unset = UNSET,
) -> PaginatedRiskAcceptanceList | None:
    """
    Args:
        accepted_by (str | Unset):
        accepted_findings (list[int] | Unset):
        decision (RiskAcceptanceListDecision | Unset):
        decision_details (str | Unset):
        expiration_date (datetime.datetime | Unset):
        expiration_date_handled (datetime.datetime | Unset):
        expiration_date_warned (datetime.datetime | Unset):
        limit (int | Unset):
        name (str | Unset):
        notes (list[int] | Unset):
        o (list[RiskAcceptanceListOItem] | Unset):
        offset (int | Unset):
        owner (int | Unset):
        reactivate_expired (bool | Unset):
        recommendation (RiskAcceptanceListSecurityRecommendation | Unset):
        recommendation_details (str | Unset):
        restart_sla_expired (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRiskAcceptanceList
    """

    return (
        await asyncio_detailed(
            client=client,
            accepted_by=accepted_by,
            accepted_findings=accepted_findings,
            decision=decision,
            decision_details=decision_details,
            expiration_date=expiration_date,
            expiration_date_handled=expiration_date_handled,
            expiration_date_warned=expiration_date_warned,
            limit=limit,
            name=name,
            notes=notes,
            o=o,
            offset=offset,
            owner=owner,
            reactivate_expired=reactivate_expired,
            recommendation=recommendation,
            recommendation_details=recommendation_details,
            restart_sla_expired=restart_sla_expired,
        )
    ).parsed
