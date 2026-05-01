from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.risk_acceptance_decision import RiskAcceptanceDecision
from ..models.risk_acceptance_security_recommendation import RiskAcceptanceSecurityRecommendation
from ..types import UNSET, Unset

T = TypeVar("T", bound="RiskAcceptance")


@_attrs_define
class RiskAcceptance:
    """
    Attributes:
        id (int):
        path (str):
        name (str): Descriptive name which in the future may also be used to group risk acceptances together across
            engagements and products
        created (datetime.datetime):
        updated (datetime.datetime):
        owner (int): User in DefectDojo owning this acceptance. Only the owner and staff users can edit the risk
            acceptance.
        accepted_findings (list[int]):
        notes (list[int]):
        recommendation (RiskAcceptanceSecurityRecommendation | Unset): Recommendation from the security team.

            * `A` - Accept (The risk is acknowledged, yet remains)
            * `V` - Avoid (Do not engage with whatever creates the risk)
            * `M` - Mitigate (The risk still exists, yet compensating controls make it less of a threat)
            * `F` - Fix (The risk is eradicated)
            * `T` - Transfer (The risk is transferred to a 3rd party)
        recommendation_details (None | str | Unset): Explanation of security recommendation
        decision (RiskAcceptanceDecision | Unset): Risk treatment decision by risk owner

            * `A` - Accept (The risk is acknowledged, yet remains)
            * `V` - Avoid (Do not engage with whatever creates the risk)
            * `M` - Mitigate (The risk still exists, yet compensating controls make it less of a threat)
            * `F` - Fix (The risk is eradicated)
            * `T` - Transfer (The risk is transferred to a 3rd party)
        decision_details (None | str | Unset): If a compensating control exists to mitigate the finding or reduce risk,
            then list the compensating control(s).
        accepted_by (None | str | Unset): The person that accepts the risk, can be outside of DefectDojo.
        expiration_date (datetime.datetime | None | Unset): When the risk acceptance expires, the findings will be
            reactivated (unless disabled below).
        expiration_date_warned (datetime.datetime | None | Unset): (readonly) Date at which notice about the risk
            acceptance expiration was sent.
        expiration_date_handled (datetime.datetime | None | Unset): (readonly) When the risk acceptance expiration was
            handled (manually or by the daily job).
        reactivate_expired (bool | Unset): Reactivate findings when risk acceptance expires?
        restart_sla_expired (bool | Unset): When enabled, the SLA for findings is restarted when the risk acceptance
            expires.
    """

    id: int
    path: str
    name: str
    created: datetime.datetime
    updated: datetime.datetime
    owner: int
    accepted_findings: list[int]
    notes: list[int]
    recommendation: RiskAcceptanceSecurityRecommendation | Unset = UNSET
    recommendation_details: None | str | Unset = UNSET
    decision: RiskAcceptanceDecision | Unset = UNSET
    decision_details: None | str | Unset = UNSET
    accepted_by: None | str | Unset = UNSET
    expiration_date: datetime.datetime | None | Unset = UNSET
    expiration_date_warned: datetime.datetime | None | Unset = UNSET
    expiration_date_handled: datetime.datetime | None | Unset = UNSET
    reactivate_expired: bool | Unset = UNSET
    restart_sla_expired: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        path = self.path

        name = self.name

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        owner = self.owner

        accepted_findings = self.accepted_findings

        notes = self.notes

        recommendation: str | Unset = UNSET
        if not isinstance(self.recommendation, Unset):
            recommendation = self.recommendation.value

        recommendation_details: None | str | Unset
        if isinstance(self.recommendation_details, Unset):
            recommendation_details = UNSET
        else:
            recommendation_details = self.recommendation_details

        decision: str | Unset = UNSET
        if not isinstance(self.decision, Unset):
            decision = self.decision.value

        decision_details: None | str | Unset
        if isinstance(self.decision_details, Unset):
            decision_details = UNSET
        else:
            decision_details = self.decision_details

        accepted_by: None | str | Unset
        if isinstance(self.accepted_by, Unset):
            accepted_by = UNSET
        else:
            accepted_by = self.accepted_by

        expiration_date: None | str | Unset
        if isinstance(self.expiration_date, Unset):
            expiration_date = UNSET
        elif isinstance(self.expiration_date, datetime.datetime):
            expiration_date = self.expiration_date.isoformat()
        else:
            expiration_date = self.expiration_date

        expiration_date_warned: None | str | Unset
        if isinstance(self.expiration_date_warned, Unset):
            expiration_date_warned = UNSET
        elif isinstance(self.expiration_date_warned, datetime.datetime):
            expiration_date_warned = self.expiration_date_warned.isoformat()
        else:
            expiration_date_warned = self.expiration_date_warned

        expiration_date_handled: None | str | Unset
        if isinstance(self.expiration_date_handled, Unset):
            expiration_date_handled = UNSET
        elif isinstance(self.expiration_date_handled, datetime.datetime):
            expiration_date_handled = self.expiration_date_handled.isoformat()
        else:
            expiration_date_handled = self.expiration_date_handled

        reactivate_expired = self.reactivate_expired

        restart_sla_expired = self.restart_sla_expired

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "path": path,
                "name": name,
                "created": created,
                "updated": updated,
                "owner": owner,
                "accepted_findings": accepted_findings,
                "notes": notes,
            }
        )
        if recommendation is not UNSET:
            field_dict["recommendation"] = recommendation
        if recommendation_details is not UNSET:
            field_dict["recommendation_details"] = recommendation_details
        if decision is not UNSET:
            field_dict["decision"] = decision
        if decision_details is not UNSET:
            field_dict["decision_details"] = decision_details
        if accepted_by is not UNSET:
            field_dict["accepted_by"] = accepted_by
        if expiration_date is not UNSET:
            field_dict["expiration_date"] = expiration_date
        if expiration_date_warned is not UNSET:
            field_dict["expiration_date_warned"] = expiration_date_warned
        if expiration_date_handled is not UNSET:
            field_dict["expiration_date_handled"] = expiration_date_handled
        if reactivate_expired is not UNSET:
            field_dict["reactivate_expired"] = reactivate_expired
        if restart_sla_expired is not UNSET:
            field_dict["restart_sla_expired"] = restart_sla_expired

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        path = d.pop("path")

        name = d.pop("name")

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        owner = d.pop("owner")

        accepted_findings = cast(list[int], d.pop("accepted_findings"))

        notes = cast(list[int], d.pop("notes"))

        _recommendation = d.pop("recommendation", UNSET)
        recommendation: RiskAcceptanceSecurityRecommendation | Unset
        if isinstance(_recommendation, Unset):
            recommendation = UNSET
        else:
            recommendation = RiskAcceptanceSecurityRecommendation(_recommendation)

        def _parse_recommendation_details(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recommendation_details = _parse_recommendation_details(
            d.pop("recommendation_details", UNSET)
        )

        _decision = d.pop("decision", UNSET)
        decision: RiskAcceptanceDecision | Unset
        if isinstance(_decision, Unset):
            decision = UNSET
        else:
            decision = RiskAcceptanceDecision(_decision)

        def _parse_decision_details(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        decision_details = _parse_decision_details(d.pop("decision_details", UNSET))

        def _parse_accepted_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accepted_by = _parse_accepted_by(d.pop("accepted_by", UNSET))

        def _parse_expiration_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiration_date_type_0 = isoparse(data)

                return expiration_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expiration_date = _parse_expiration_date(d.pop("expiration_date", UNSET))

        def _parse_expiration_date_warned(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiration_date_warned_type_0 = isoparse(data)

                return expiration_date_warned_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expiration_date_warned = _parse_expiration_date_warned(
            d.pop("expiration_date_warned", UNSET)
        )

        def _parse_expiration_date_handled(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiration_date_handled_type_0 = isoparse(data)

                return expiration_date_handled_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expiration_date_handled = _parse_expiration_date_handled(
            d.pop("expiration_date_handled", UNSET)
        )

        reactivate_expired = d.pop("reactivate_expired", UNSET)

        restart_sla_expired = d.pop("restart_sla_expired", UNSET)

        risk_acceptance = cls(
            id=id,
            path=path,
            name=name,
            created=created,
            updated=updated,
            owner=owner,
            accepted_findings=accepted_findings,
            notes=notes,
            recommendation=recommendation,
            recommendation_details=recommendation_details,
            decision=decision,
            decision_details=decision_details,
            accepted_by=accepted_by,
            expiration_date=expiration_date,
            expiration_date_warned=expiration_date_warned,
            expiration_date_handled=expiration_date_handled,
            reactivate_expired=reactivate_expired,
            restart_sla_expired=restart_sla_expired,
        )

        risk_acceptance.additional_properties = d
        return risk_acceptance

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
