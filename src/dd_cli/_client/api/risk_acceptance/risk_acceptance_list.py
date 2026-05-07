import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_risk_acceptance_list import PaginatedRiskAcceptanceList
from ...models.risk_acceptance_list_created_type_1 import RiskAcceptanceListCreatedType1
from ...models.risk_acceptance_list_decision import RiskAcceptanceListDecision
from ...models.risk_acceptance_list_o_item import RiskAcceptanceListOItem
from ...models.risk_acceptance_list_security_recommendation import (
    RiskAcceptanceListSecurityRecommendation,
)
from ...models.risk_acceptance_list_updated_type_1 import RiskAcceptanceListUpdatedType1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    accepted_by: str | Unset = UNSET,
    accepted_by_icontains: str | Unset = UNSET,
    accepted_findings: list[int] | Unset = UNSET,
    created: None | RiskAcceptanceListCreatedType1 | Unset = UNSET,
    created_gt: datetime.datetime | Unset = UNSET,
    created_gte: datetime.datetime | Unset = UNSET,
    created_lt: datetime.datetime | Unset = UNSET,
    created_lte: datetime.datetime | Unset = UNSET,
    decision: RiskAcceptanceListDecision | Unset = UNSET,
    decision_details: str | Unset = UNSET,
    decision_details_icontains: str | Unset = UNSET,
    expiration_date: datetime.datetime | Unset = UNSET,
    expiration_date_gt: datetime.datetime | Unset = UNSET,
    expiration_date_gte: datetime.datetime | Unset = UNSET,
    expiration_date_lt: datetime.datetime | Unset = UNSET,
    expiration_date_lte: datetime.datetime | Unset = UNSET,
    expiration_date_handled: datetime.datetime | Unset = UNSET,
    expiration_date_handled_gt: datetime.datetime | Unset = UNSET,
    expiration_date_handled_gte: datetime.datetime | Unset = UNSET,
    expiration_date_handled_lt: datetime.datetime | Unset = UNSET,
    expiration_date_handled_lte: datetime.datetime | Unset = UNSET,
    expiration_date_warned: datetime.datetime | Unset = UNSET,
    expiration_date_warned_gt: datetime.datetime | Unset = UNSET,
    expiration_date_warned_gte: datetime.datetime | Unset = UNSET,
    expiration_date_warned_lt: datetime.datetime | Unset = UNSET,
    expiration_date_warned_lte: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_icontains: str | Unset = UNSET,
    notes: list[int] | Unset = UNSET,
    o: list[RiskAcceptanceListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    owner: int | Unset = UNSET,
    reactivate_expired: bool | Unset = UNSET,
    recommendation: RiskAcceptanceListSecurityRecommendation | Unset = UNSET,
    recommendation_details: str | Unset = UNSET,
    recommendation_details_icontains: str | Unset = UNSET,
    restart_sla_expired: bool | Unset = UNSET,
    updated: None | RiskAcceptanceListUpdatedType1 | Unset = UNSET,
    updated_gt: datetime.datetime | Unset = UNSET,
    updated_gte: datetime.datetime | Unset = UNSET,
    updated_lt: datetime.datetime | Unset = UNSET,
    updated_lte: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accepted_by"] = accepted_by

    params["accepted_by__icontains"] = accepted_by_icontains

    json_accepted_findings: list[int] | Unset = UNSET
    if not isinstance(accepted_findings, Unset):
        json_accepted_findings = accepted_findings

    params["accepted_findings"] = json_accepted_findings

    json_created: int | None | Unset
    if isinstance(created, Unset):
        json_created = UNSET
    elif isinstance(created, RiskAcceptanceListCreatedType1):
        json_created = created.value
    else:
        json_created = created
    params["created"] = json_created

    json_created_gt: str | Unset = UNSET
    if not isinstance(created_gt, Unset):
        json_created_gt = created_gt.isoformat()
    params["created__gt"] = json_created_gt

    json_created_gte: str | Unset = UNSET
    if not isinstance(created_gte, Unset):
        json_created_gte = created_gte.isoformat()
    params["created__gte"] = json_created_gte

    json_created_lt: str | Unset = UNSET
    if not isinstance(created_lt, Unset):
        json_created_lt = created_lt.isoformat()
    params["created__lt"] = json_created_lt

    json_created_lte: str | Unset = UNSET
    if not isinstance(created_lte, Unset):
        json_created_lte = created_lte.isoformat()
    params["created__lte"] = json_created_lte

    json_decision: str | Unset = UNSET
    if not isinstance(decision, Unset):
        json_decision = decision.value

    params["decision"] = json_decision

    params["decision_details"] = decision_details

    params["decision_details__icontains"] = decision_details_icontains

    json_expiration_date: str | Unset = UNSET
    if not isinstance(expiration_date, Unset):
        json_expiration_date = expiration_date.isoformat()
    params["expiration_date"] = json_expiration_date

    json_expiration_date_gt: str | Unset = UNSET
    if not isinstance(expiration_date_gt, Unset):
        json_expiration_date_gt = expiration_date_gt.isoformat()
    params["expiration_date__gt"] = json_expiration_date_gt

    json_expiration_date_gte: str | Unset = UNSET
    if not isinstance(expiration_date_gte, Unset):
        json_expiration_date_gte = expiration_date_gte.isoformat()
    params["expiration_date__gte"] = json_expiration_date_gte

    json_expiration_date_lt: str | Unset = UNSET
    if not isinstance(expiration_date_lt, Unset):
        json_expiration_date_lt = expiration_date_lt.isoformat()
    params["expiration_date__lt"] = json_expiration_date_lt

    json_expiration_date_lte: str | Unset = UNSET
    if not isinstance(expiration_date_lte, Unset):
        json_expiration_date_lte = expiration_date_lte.isoformat()
    params["expiration_date__lte"] = json_expiration_date_lte

    json_expiration_date_handled: str | Unset = UNSET
    if not isinstance(expiration_date_handled, Unset):
        json_expiration_date_handled = expiration_date_handled.isoformat()
    params["expiration_date_handled"] = json_expiration_date_handled

    json_expiration_date_handled_gt: str | Unset = UNSET
    if not isinstance(expiration_date_handled_gt, Unset):
        json_expiration_date_handled_gt = expiration_date_handled_gt.isoformat()
    params["expiration_date_handled__gt"] = json_expiration_date_handled_gt

    json_expiration_date_handled_gte: str | Unset = UNSET
    if not isinstance(expiration_date_handled_gte, Unset):
        json_expiration_date_handled_gte = expiration_date_handled_gte.isoformat()
    params["expiration_date_handled__gte"] = json_expiration_date_handled_gte

    json_expiration_date_handled_lt: str | Unset = UNSET
    if not isinstance(expiration_date_handled_lt, Unset):
        json_expiration_date_handled_lt = expiration_date_handled_lt.isoformat()
    params["expiration_date_handled__lt"] = json_expiration_date_handled_lt

    json_expiration_date_handled_lte: str | Unset = UNSET
    if not isinstance(expiration_date_handled_lte, Unset):
        json_expiration_date_handled_lte = expiration_date_handled_lte.isoformat()
    params["expiration_date_handled__lte"] = json_expiration_date_handled_lte

    json_expiration_date_warned: str | Unset = UNSET
    if not isinstance(expiration_date_warned, Unset):
        json_expiration_date_warned = expiration_date_warned.isoformat()
    params["expiration_date_warned"] = json_expiration_date_warned

    json_expiration_date_warned_gt: str | Unset = UNSET
    if not isinstance(expiration_date_warned_gt, Unset):
        json_expiration_date_warned_gt = expiration_date_warned_gt.isoformat()
    params["expiration_date_warned__gt"] = json_expiration_date_warned_gt

    json_expiration_date_warned_gte: str | Unset = UNSET
    if not isinstance(expiration_date_warned_gte, Unset):
        json_expiration_date_warned_gte = expiration_date_warned_gte.isoformat()
    params["expiration_date_warned__gte"] = json_expiration_date_warned_gte

    json_expiration_date_warned_lt: str | Unset = UNSET
    if not isinstance(expiration_date_warned_lt, Unset):
        json_expiration_date_warned_lt = expiration_date_warned_lt.isoformat()
    params["expiration_date_warned__lt"] = json_expiration_date_warned_lt

    json_expiration_date_warned_lte: str | Unset = UNSET
    if not isinstance(expiration_date_warned_lte, Unset):
        json_expiration_date_warned_lte = expiration_date_warned_lte.isoformat()
    params["expiration_date_warned__lte"] = json_expiration_date_warned_lte

    params["limit"] = limit

    params["name"] = name

    params["name__icontains"] = name_icontains

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

    params["recommendation_details__icontains"] = recommendation_details_icontains

    params["restart_sla_expired"] = restart_sla_expired

    json_updated: int | None | Unset
    if isinstance(updated, Unset):
        json_updated = UNSET
    elif isinstance(updated, RiskAcceptanceListUpdatedType1):
        json_updated = updated.value
    else:
        json_updated = updated
    params["updated"] = json_updated

    json_updated_gt: str | Unset = UNSET
    if not isinstance(updated_gt, Unset):
        json_updated_gt = updated_gt.isoformat()
    params["updated__gt"] = json_updated_gt

    json_updated_gte: str | Unset = UNSET
    if not isinstance(updated_gte, Unset):
        json_updated_gte = updated_gte.isoformat()
    params["updated__gte"] = json_updated_gte

    json_updated_lt: str | Unset = UNSET
    if not isinstance(updated_lt, Unset):
        json_updated_lt = updated_lt.isoformat()
    params["updated__lt"] = json_updated_lt

    json_updated_lte: str | Unset = UNSET
    if not isinstance(updated_lte, Unset):
        json_updated_lte = updated_lte.isoformat()
    params["updated__lte"] = json_updated_lte

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
    accepted_by_icontains: str | Unset = UNSET,
    accepted_findings: list[int] | Unset = UNSET,
    created: None | RiskAcceptanceListCreatedType1 | Unset = UNSET,
    created_gt: datetime.datetime | Unset = UNSET,
    created_gte: datetime.datetime | Unset = UNSET,
    created_lt: datetime.datetime | Unset = UNSET,
    created_lte: datetime.datetime | Unset = UNSET,
    decision: RiskAcceptanceListDecision | Unset = UNSET,
    decision_details: str | Unset = UNSET,
    decision_details_icontains: str | Unset = UNSET,
    expiration_date: datetime.datetime | Unset = UNSET,
    expiration_date_gt: datetime.datetime | Unset = UNSET,
    expiration_date_gte: datetime.datetime | Unset = UNSET,
    expiration_date_lt: datetime.datetime | Unset = UNSET,
    expiration_date_lte: datetime.datetime | Unset = UNSET,
    expiration_date_handled: datetime.datetime | Unset = UNSET,
    expiration_date_handled_gt: datetime.datetime | Unset = UNSET,
    expiration_date_handled_gte: datetime.datetime | Unset = UNSET,
    expiration_date_handled_lt: datetime.datetime | Unset = UNSET,
    expiration_date_handled_lte: datetime.datetime | Unset = UNSET,
    expiration_date_warned: datetime.datetime | Unset = UNSET,
    expiration_date_warned_gt: datetime.datetime | Unset = UNSET,
    expiration_date_warned_gte: datetime.datetime | Unset = UNSET,
    expiration_date_warned_lt: datetime.datetime | Unset = UNSET,
    expiration_date_warned_lte: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_icontains: str | Unset = UNSET,
    notes: list[int] | Unset = UNSET,
    o: list[RiskAcceptanceListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    owner: int | Unset = UNSET,
    reactivate_expired: bool | Unset = UNSET,
    recommendation: RiskAcceptanceListSecurityRecommendation | Unset = UNSET,
    recommendation_details: str | Unset = UNSET,
    recommendation_details_icontains: str | Unset = UNSET,
    restart_sla_expired: bool | Unset = UNSET,
    updated: None | RiskAcceptanceListUpdatedType1 | Unset = UNSET,
    updated_gt: datetime.datetime | Unset = UNSET,
    updated_gte: datetime.datetime | Unset = UNSET,
    updated_lt: datetime.datetime | Unset = UNSET,
    updated_lte: datetime.datetime | Unset = UNSET,
) -> Response[PaginatedRiskAcceptanceList]:
    """
    Args:
        accepted_by (str | Unset):
        accepted_by_icontains (str | Unset):
        accepted_findings (list[int] | Unset):
        created (None | RiskAcceptanceListCreatedType1 | Unset):
        created_gt (datetime.datetime | Unset):
        created_gte (datetime.datetime | Unset):
        created_lt (datetime.datetime | Unset):
        created_lte (datetime.datetime | Unset):
        decision (RiskAcceptanceListDecision | Unset):
        decision_details (str | Unset):
        decision_details_icontains (str | Unset):
        expiration_date (datetime.datetime | Unset):
        expiration_date_gt (datetime.datetime | Unset):
        expiration_date_gte (datetime.datetime | Unset):
        expiration_date_lt (datetime.datetime | Unset):
        expiration_date_lte (datetime.datetime | Unset):
        expiration_date_handled (datetime.datetime | Unset):
        expiration_date_handled_gt (datetime.datetime | Unset):
        expiration_date_handled_gte (datetime.datetime | Unset):
        expiration_date_handled_lt (datetime.datetime | Unset):
        expiration_date_handled_lte (datetime.datetime | Unset):
        expiration_date_warned (datetime.datetime | Unset):
        expiration_date_warned_gt (datetime.datetime | Unset):
        expiration_date_warned_gte (datetime.datetime | Unset):
        expiration_date_warned_lt (datetime.datetime | Unset):
        expiration_date_warned_lte (datetime.datetime | Unset):
        limit (int | Unset):
        name (str | Unset):
        name_icontains (str | Unset):
        notes (list[int] | Unset):
        o (list[RiskAcceptanceListOItem] | Unset):
        offset (int | Unset):
        owner (int | Unset):
        reactivate_expired (bool | Unset):
        recommendation (RiskAcceptanceListSecurityRecommendation | Unset):
        recommendation_details (str | Unset):
        recommendation_details_icontains (str | Unset):
        restart_sla_expired (bool | Unset):
        updated (None | RiskAcceptanceListUpdatedType1 | Unset):
        updated_gt (datetime.datetime | Unset):
        updated_gte (datetime.datetime | Unset):
        updated_lt (datetime.datetime | Unset):
        updated_lte (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRiskAcceptanceList]
    """

    kwargs = _get_kwargs(
        accepted_by=accepted_by,
        accepted_by_icontains=accepted_by_icontains,
        accepted_findings=accepted_findings,
        created=created,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        decision=decision,
        decision_details=decision_details,
        decision_details_icontains=decision_details_icontains,
        expiration_date=expiration_date,
        expiration_date_gt=expiration_date_gt,
        expiration_date_gte=expiration_date_gte,
        expiration_date_lt=expiration_date_lt,
        expiration_date_lte=expiration_date_lte,
        expiration_date_handled=expiration_date_handled,
        expiration_date_handled_gt=expiration_date_handled_gt,
        expiration_date_handled_gte=expiration_date_handled_gte,
        expiration_date_handled_lt=expiration_date_handled_lt,
        expiration_date_handled_lte=expiration_date_handled_lte,
        expiration_date_warned=expiration_date_warned,
        expiration_date_warned_gt=expiration_date_warned_gt,
        expiration_date_warned_gte=expiration_date_warned_gte,
        expiration_date_warned_lt=expiration_date_warned_lt,
        expiration_date_warned_lte=expiration_date_warned_lte,
        limit=limit,
        name=name,
        name_icontains=name_icontains,
        notes=notes,
        o=o,
        offset=offset,
        owner=owner,
        reactivate_expired=reactivate_expired,
        recommendation=recommendation,
        recommendation_details=recommendation_details,
        recommendation_details_icontains=recommendation_details_icontains,
        restart_sla_expired=restart_sla_expired,
        updated=updated,
        updated_gt=updated_gt,
        updated_gte=updated_gte,
        updated_lt=updated_lt,
        updated_lte=updated_lte,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    accepted_by: str | Unset = UNSET,
    accepted_by_icontains: str | Unset = UNSET,
    accepted_findings: list[int] | Unset = UNSET,
    created: None | RiskAcceptanceListCreatedType1 | Unset = UNSET,
    created_gt: datetime.datetime | Unset = UNSET,
    created_gte: datetime.datetime | Unset = UNSET,
    created_lt: datetime.datetime | Unset = UNSET,
    created_lte: datetime.datetime | Unset = UNSET,
    decision: RiskAcceptanceListDecision | Unset = UNSET,
    decision_details: str | Unset = UNSET,
    decision_details_icontains: str | Unset = UNSET,
    expiration_date: datetime.datetime | Unset = UNSET,
    expiration_date_gt: datetime.datetime | Unset = UNSET,
    expiration_date_gte: datetime.datetime | Unset = UNSET,
    expiration_date_lt: datetime.datetime | Unset = UNSET,
    expiration_date_lte: datetime.datetime | Unset = UNSET,
    expiration_date_handled: datetime.datetime | Unset = UNSET,
    expiration_date_handled_gt: datetime.datetime | Unset = UNSET,
    expiration_date_handled_gte: datetime.datetime | Unset = UNSET,
    expiration_date_handled_lt: datetime.datetime | Unset = UNSET,
    expiration_date_handled_lte: datetime.datetime | Unset = UNSET,
    expiration_date_warned: datetime.datetime | Unset = UNSET,
    expiration_date_warned_gt: datetime.datetime | Unset = UNSET,
    expiration_date_warned_gte: datetime.datetime | Unset = UNSET,
    expiration_date_warned_lt: datetime.datetime | Unset = UNSET,
    expiration_date_warned_lte: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_icontains: str | Unset = UNSET,
    notes: list[int] | Unset = UNSET,
    o: list[RiskAcceptanceListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    owner: int | Unset = UNSET,
    reactivate_expired: bool | Unset = UNSET,
    recommendation: RiskAcceptanceListSecurityRecommendation | Unset = UNSET,
    recommendation_details: str | Unset = UNSET,
    recommendation_details_icontains: str | Unset = UNSET,
    restart_sla_expired: bool | Unset = UNSET,
    updated: None | RiskAcceptanceListUpdatedType1 | Unset = UNSET,
    updated_gt: datetime.datetime | Unset = UNSET,
    updated_gte: datetime.datetime | Unset = UNSET,
    updated_lt: datetime.datetime | Unset = UNSET,
    updated_lte: datetime.datetime | Unset = UNSET,
) -> PaginatedRiskAcceptanceList | None:
    """
    Args:
        accepted_by (str | Unset):
        accepted_by_icontains (str | Unset):
        accepted_findings (list[int] | Unset):
        created (None | RiskAcceptanceListCreatedType1 | Unset):
        created_gt (datetime.datetime | Unset):
        created_gte (datetime.datetime | Unset):
        created_lt (datetime.datetime | Unset):
        created_lte (datetime.datetime | Unset):
        decision (RiskAcceptanceListDecision | Unset):
        decision_details (str | Unset):
        decision_details_icontains (str | Unset):
        expiration_date (datetime.datetime | Unset):
        expiration_date_gt (datetime.datetime | Unset):
        expiration_date_gte (datetime.datetime | Unset):
        expiration_date_lt (datetime.datetime | Unset):
        expiration_date_lte (datetime.datetime | Unset):
        expiration_date_handled (datetime.datetime | Unset):
        expiration_date_handled_gt (datetime.datetime | Unset):
        expiration_date_handled_gte (datetime.datetime | Unset):
        expiration_date_handled_lt (datetime.datetime | Unset):
        expiration_date_handled_lte (datetime.datetime | Unset):
        expiration_date_warned (datetime.datetime | Unset):
        expiration_date_warned_gt (datetime.datetime | Unset):
        expiration_date_warned_gte (datetime.datetime | Unset):
        expiration_date_warned_lt (datetime.datetime | Unset):
        expiration_date_warned_lte (datetime.datetime | Unset):
        limit (int | Unset):
        name (str | Unset):
        name_icontains (str | Unset):
        notes (list[int] | Unset):
        o (list[RiskAcceptanceListOItem] | Unset):
        offset (int | Unset):
        owner (int | Unset):
        reactivate_expired (bool | Unset):
        recommendation (RiskAcceptanceListSecurityRecommendation | Unset):
        recommendation_details (str | Unset):
        recommendation_details_icontains (str | Unset):
        restart_sla_expired (bool | Unset):
        updated (None | RiskAcceptanceListUpdatedType1 | Unset):
        updated_gt (datetime.datetime | Unset):
        updated_gte (datetime.datetime | Unset):
        updated_lt (datetime.datetime | Unset):
        updated_lte (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRiskAcceptanceList
    """

    return sync_detailed(
        client=client,
        accepted_by=accepted_by,
        accepted_by_icontains=accepted_by_icontains,
        accepted_findings=accepted_findings,
        created=created,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        decision=decision,
        decision_details=decision_details,
        decision_details_icontains=decision_details_icontains,
        expiration_date=expiration_date,
        expiration_date_gt=expiration_date_gt,
        expiration_date_gte=expiration_date_gte,
        expiration_date_lt=expiration_date_lt,
        expiration_date_lte=expiration_date_lte,
        expiration_date_handled=expiration_date_handled,
        expiration_date_handled_gt=expiration_date_handled_gt,
        expiration_date_handled_gte=expiration_date_handled_gte,
        expiration_date_handled_lt=expiration_date_handled_lt,
        expiration_date_handled_lte=expiration_date_handled_lte,
        expiration_date_warned=expiration_date_warned,
        expiration_date_warned_gt=expiration_date_warned_gt,
        expiration_date_warned_gte=expiration_date_warned_gte,
        expiration_date_warned_lt=expiration_date_warned_lt,
        expiration_date_warned_lte=expiration_date_warned_lte,
        limit=limit,
        name=name,
        name_icontains=name_icontains,
        notes=notes,
        o=o,
        offset=offset,
        owner=owner,
        reactivate_expired=reactivate_expired,
        recommendation=recommendation,
        recommendation_details=recommendation_details,
        recommendation_details_icontains=recommendation_details_icontains,
        restart_sla_expired=restart_sla_expired,
        updated=updated,
        updated_gt=updated_gt,
        updated_gte=updated_gte,
        updated_lt=updated_lt,
        updated_lte=updated_lte,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    accepted_by: str | Unset = UNSET,
    accepted_by_icontains: str | Unset = UNSET,
    accepted_findings: list[int] | Unset = UNSET,
    created: None | RiskAcceptanceListCreatedType1 | Unset = UNSET,
    created_gt: datetime.datetime | Unset = UNSET,
    created_gte: datetime.datetime | Unset = UNSET,
    created_lt: datetime.datetime | Unset = UNSET,
    created_lte: datetime.datetime | Unset = UNSET,
    decision: RiskAcceptanceListDecision | Unset = UNSET,
    decision_details: str | Unset = UNSET,
    decision_details_icontains: str | Unset = UNSET,
    expiration_date: datetime.datetime | Unset = UNSET,
    expiration_date_gt: datetime.datetime | Unset = UNSET,
    expiration_date_gte: datetime.datetime | Unset = UNSET,
    expiration_date_lt: datetime.datetime | Unset = UNSET,
    expiration_date_lte: datetime.datetime | Unset = UNSET,
    expiration_date_handled: datetime.datetime | Unset = UNSET,
    expiration_date_handled_gt: datetime.datetime | Unset = UNSET,
    expiration_date_handled_gte: datetime.datetime | Unset = UNSET,
    expiration_date_handled_lt: datetime.datetime | Unset = UNSET,
    expiration_date_handled_lte: datetime.datetime | Unset = UNSET,
    expiration_date_warned: datetime.datetime | Unset = UNSET,
    expiration_date_warned_gt: datetime.datetime | Unset = UNSET,
    expiration_date_warned_gte: datetime.datetime | Unset = UNSET,
    expiration_date_warned_lt: datetime.datetime | Unset = UNSET,
    expiration_date_warned_lte: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_icontains: str | Unset = UNSET,
    notes: list[int] | Unset = UNSET,
    o: list[RiskAcceptanceListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    owner: int | Unset = UNSET,
    reactivate_expired: bool | Unset = UNSET,
    recommendation: RiskAcceptanceListSecurityRecommendation | Unset = UNSET,
    recommendation_details: str | Unset = UNSET,
    recommendation_details_icontains: str | Unset = UNSET,
    restart_sla_expired: bool | Unset = UNSET,
    updated: None | RiskAcceptanceListUpdatedType1 | Unset = UNSET,
    updated_gt: datetime.datetime | Unset = UNSET,
    updated_gte: datetime.datetime | Unset = UNSET,
    updated_lt: datetime.datetime | Unset = UNSET,
    updated_lte: datetime.datetime | Unset = UNSET,
) -> Response[PaginatedRiskAcceptanceList]:
    """
    Args:
        accepted_by (str | Unset):
        accepted_by_icontains (str | Unset):
        accepted_findings (list[int] | Unset):
        created (None | RiskAcceptanceListCreatedType1 | Unset):
        created_gt (datetime.datetime | Unset):
        created_gte (datetime.datetime | Unset):
        created_lt (datetime.datetime | Unset):
        created_lte (datetime.datetime | Unset):
        decision (RiskAcceptanceListDecision | Unset):
        decision_details (str | Unset):
        decision_details_icontains (str | Unset):
        expiration_date (datetime.datetime | Unset):
        expiration_date_gt (datetime.datetime | Unset):
        expiration_date_gte (datetime.datetime | Unset):
        expiration_date_lt (datetime.datetime | Unset):
        expiration_date_lte (datetime.datetime | Unset):
        expiration_date_handled (datetime.datetime | Unset):
        expiration_date_handled_gt (datetime.datetime | Unset):
        expiration_date_handled_gte (datetime.datetime | Unset):
        expiration_date_handled_lt (datetime.datetime | Unset):
        expiration_date_handled_lte (datetime.datetime | Unset):
        expiration_date_warned (datetime.datetime | Unset):
        expiration_date_warned_gt (datetime.datetime | Unset):
        expiration_date_warned_gte (datetime.datetime | Unset):
        expiration_date_warned_lt (datetime.datetime | Unset):
        expiration_date_warned_lte (datetime.datetime | Unset):
        limit (int | Unset):
        name (str | Unset):
        name_icontains (str | Unset):
        notes (list[int] | Unset):
        o (list[RiskAcceptanceListOItem] | Unset):
        offset (int | Unset):
        owner (int | Unset):
        reactivate_expired (bool | Unset):
        recommendation (RiskAcceptanceListSecurityRecommendation | Unset):
        recommendation_details (str | Unset):
        recommendation_details_icontains (str | Unset):
        restart_sla_expired (bool | Unset):
        updated (None | RiskAcceptanceListUpdatedType1 | Unset):
        updated_gt (datetime.datetime | Unset):
        updated_gte (datetime.datetime | Unset):
        updated_lt (datetime.datetime | Unset):
        updated_lte (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRiskAcceptanceList]
    """

    kwargs = _get_kwargs(
        accepted_by=accepted_by,
        accepted_by_icontains=accepted_by_icontains,
        accepted_findings=accepted_findings,
        created=created,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        decision=decision,
        decision_details=decision_details,
        decision_details_icontains=decision_details_icontains,
        expiration_date=expiration_date,
        expiration_date_gt=expiration_date_gt,
        expiration_date_gte=expiration_date_gte,
        expiration_date_lt=expiration_date_lt,
        expiration_date_lte=expiration_date_lte,
        expiration_date_handled=expiration_date_handled,
        expiration_date_handled_gt=expiration_date_handled_gt,
        expiration_date_handled_gte=expiration_date_handled_gte,
        expiration_date_handled_lt=expiration_date_handled_lt,
        expiration_date_handled_lte=expiration_date_handled_lte,
        expiration_date_warned=expiration_date_warned,
        expiration_date_warned_gt=expiration_date_warned_gt,
        expiration_date_warned_gte=expiration_date_warned_gte,
        expiration_date_warned_lt=expiration_date_warned_lt,
        expiration_date_warned_lte=expiration_date_warned_lte,
        limit=limit,
        name=name,
        name_icontains=name_icontains,
        notes=notes,
        o=o,
        offset=offset,
        owner=owner,
        reactivate_expired=reactivate_expired,
        recommendation=recommendation,
        recommendation_details=recommendation_details,
        recommendation_details_icontains=recommendation_details_icontains,
        restart_sla_expired=restart_sla_expired,
        updated=updated,
        updated_gt=updated_gt,
        updated_gte=updated_gte,
        updated_lt=updated_lt,
        updated_lte=updated_lte,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    accepted_by: str | Unset = UNSET,
    accepted_by_icontains: str | Unset = UNSET,
    accepted_findings: list[int] | Unset = UNSET,
    created: None | RiskAcceptanceListCreatedType1 | Unset = UNSET,
    created_gt: datetime.datetime | Unset = UNSET,
    created_gte: datetime.datetime | Unset = UNSET,
    created_lt: datetime.datetime | Unset = UNSET,
    created_lte: datetime.datetime | Unset = UNSET,
    decision: RiskAcceptanceListDecision | Unset = UNSET,
    decision_details: str | Unset = UNSET,
    decision_details_icontains: str | Unset = UNSET,
    expiration_date: datetime.datetime | Unset = UNSET,
    expiration_date_gt: datetime.datetime | Unset = UNSET,
    expiration_date_gte: datetime.datetime | Unset = UNSET,
    expiration_date_lt: datetime.datetime | Unset = UNSET,
    expiration_date_lte: datetime.datetime | Unset = UNSET,
    expiration_date_handled: datetime.datetime | Unset = UNSET,
    expiration_date_handled_gt: datetime.datetime | Unset = UNSET,
    expiration_date_handled_gte: datetime.datetime | Unset = UNSET,
    expiration_date_handled_lt: datetime.datetime | Unset = UNSET,
    expiration_date_handled_lte: datetime.datetime | Unset = UNSET,
    expiration_date_warned: datetime.datetime | Unset = UNSET,
    expiration_date_warned_gt: datetime.datetime | Unset = UNSET,
    expiration_date_warned_gte: datetime.datetime | Unset = UNSET,
    expiration_date_warned_lt: datetime.datetime | Unset = UNSET,
    expiration_date_warned_lte: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_icontains: str | Unset = UNSET,
    notes: list[int] | Unset = UNSET,
    o: list[RiskAcceptanceListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    owner: int | Unset = UNSET,
    reactivate_expired: bool | Unset = UNSET,
    recommendation: RiskAcceptanceListSecurityRecommendation | Unset = UNSET,
    recommendation_details: str | Unset = UNSET,
    recommendation_details_icontains: str | Unset = UNSET,
    restart_sla_expired: bool | Unset = UNSET,
    updated: None | RiskAcceptanceListUpdatedType1 | Unset = UNSET,
    updated_gt: datetime.datetime | Unset = UNSET,
    updated_gte: datetime.datetime | Unset = UNSET,
    updated_lt: datetime.datetime | Unset = UNSET,
    updated_lte: datetime.datetime | Unset = UNSET,
) -> PaginatedRiskAcceptanceList | None:
    """
    Args:
        accepted_by (str | Unset):
        accepted_by_icontains (str | Unset):
        accepted_findings (list[int] | Unset):
        created (None | RiskAcceptanceListCreatedType1 | Unset):
        created_gt (datetime.datetime | Unset):
        created_gte (datetime.datetime | Unset):
        created_lt (datetime.datetime | Unset):
        created_lte (datetime.datetime | Unset):
        decision (RiskAcceptanceListDecision | Unset):
        decision_details (str | Unset):
        decision_details_icontains (str | Unset):
        expiration_date (datetime.datetime | Unset):
        expiration_date_gt (datetime.datetime | Unset):
        expiration_date_gte (datetime.datetime | Unset):
        expiration_date_lt (datetime.datetime | Unset):
        expiration_date_lte (datetime.datetime | Unset):
        expiration_date_handled (datetime.datetime | Unset):
        expiration_date_handled_gt (datetime.datetime | Unset):
        expiration_date_handled_gte (datetime.datetime | Unset):
        expiration_date_handled_lt (datetime.datetime | Unset):
        expiration_date_handled_lte (datetime.datetime | Unset):
        expiration_date_warned (datetime.datetime | Unset):
        expiration_date_warned_gt (datetime.datetime | Unset):
        expiration_date_warned_gte (datetime.datetime | Unset):
        expiration_date_warned_lt (datetime.datetime | Unset):
        expiration_date_warned_lte (datetime.datetime | Unset):
        limit (int | Unset):
        name (str | Unset):
        name_icontains (str | Unset):
        notes (list[int] | Unset):
        o (list[RiskAcceptanceListOItem] | Unset):
        offset (int | Unset):
        owner (int | Unset):
        reactivate_expired (bool | Unset):
        recommendation (RiskAcceptanceListSecurityRecommendation | Unset):
        recommendation_details (str | Unset):
        recommendation_details_icontains (str | Unset):
        restart_sla_expired (bool | Unset):
        updated (None | RiskAcceptanceListUpdatedType1 | Unset):
        updated_gt (datetime.datetime | Unset):
        updated_gte (datetime.datetime | Unset):
        updated_lt (datetime.datetime | Unset):
        updated_lte (datetime.datetime | Unset):

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
            accepted_by_icontains=accepted_by_icontains,
            accepted_findings=accepted_findings,
            created=created,
            created_gt=created_gt,
            created_gte=created_gte,
            created_lt=created_lt,
            created_lte=created_lte,
            decision=decision,
            decision_details=decision_details,
            decision_details_icontains=decision_details_icontains,
            expiration_date=expiration_date,
            expiration_date_gt=expiration_date_gt,
            expiration_date_gte=expiration_date_gte,
            expiration_date_lt=expiration_date_lt,
            expiration_date_lte=expiration_date_lte,
            expiration_date_handled=expiration_date_handled,
            expiration_date_handled_gt=expiration_date_handled_gt,
            expiration_date_handled_gte=expiration_date_handled_gte,
            expiration_date_handled_lt=expiration_date_handled_lt,
            expiration_date_handled_lte=expiration_date_handled_lte,
            expiration_date_warned=expiration_date_warned,
            expiration_date_warned_gt=expiration_date_warned_gt,
            expiration_date_warned_gte=expiration_date_warned_gte,
            expiration_date_warned_lt=expiration_date_warned_lt,
            expiration_date_warned_lte=expiration_date_warned_lte,
            limit=limit,
            name=name,
            name_icontains=name_icontains,
            notes=notes,
            o=o,
            offset=offset,
            owner=owner,
            reactivate_expired=reactivate_expired,
            recommendation=recommendation,
            recommendation_details=recommendation_details,
            recommendation_details_icontains=recommendation_details_icontains,
            restart_sla_expired=restart_sla_expired,
            updated=updated,
            updated_gt=updated_gt,
            updated_gte=updated_gte,
            updated_lt=updated_lt,
            updated_lte=updated_lte,
        )
    ).parsed
