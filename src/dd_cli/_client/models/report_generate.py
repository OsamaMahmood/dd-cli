from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.endpoint import Endpoint
    from ..models.engagement import Engagement
    from ..models.executive_summary import ExecutiveSummary
    from ..models.finding import Finding
    from ..models.finding_to_notes import FindingToNotes
    from ..models.product import Product
    from ..models.product_type import ProductType
    from ..models.test import Test
    from ..models.user_stub import UserStub


T = TypeVar("T", bound="ReportGenerate")


@_attrs_define
class ReportGenerate:
    """
    Attributes:
        executive_summary (ExecutiveSummary | None):
        product_type (ProductType):
        product (Product):
        engagement (Engagement):
        report_name (str):
        report_info (str):
        test (Test):
        endpoint (Endpoint):
        endpoints (list[Endpoint]):
        findings (list[Finding]):
        user (UserStub):
        team_name (str):
        title (str):
        user_id (int):
        host (str):
        finding_notes (list[FindingToNotes] | None | Unset):
    """

    executive_summary: ExecutiveSummary | None
    product_type: ProductType
    product: Product
    engagement: Engagement
    report_name: str
    report_info: str
    test: Test
    endpoint: Endpoint
    endpoints: list[Endpoint]
    findings: list[Finding]
    user: UserStub
    team_name: str
    title: str
    user_id: int
    host: str
    finding_notes: list[FindingToNotes] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.executive_summary import ExecutiveSummary

        executive_summary: dict[str, Any] | None
        if isinstance(self.executive_summary, ExecutiveSummary):
            executive_summary = self.executive_summary.to_dict()
        else:
            executive_summary = self.executive_summary

        product_type = self.product_type.to_dict()

        product = self.product.to_dict()

        engagement = self.engagement.to_dict()

        report_name = self.report_name

        report_info = self.report_info

        test = self.test.to_dict()

        endpoint = self.endpoint.to_dict()

        endpoints = []
        for endpoints_item_data in self.endpoints:
            endpoints_item = endpoints_item_data.to_dict()
            endpoints.append(endpoints_item)

        findings = []
        for findings_item_data in self.findings:
            findings_item = findings_item_data.to_dict()
            findings.append(findings_item)

        user = self.user.to_dict()

        team_name = self.team_name

        title = self.title

        user_id = self.user_id

        host = self.host

        finding_notes: list[dict[str, Any]] | None | Unset
        if isinstance(self.finding_notes, Unset):
            finding_notes = UNSET
        elif isinstance(self.finding_notes, list):
            finding_notes = []
            for finding_notes_type_0_item_data in self.finding_notes:
                finding_notes_type_0_item = finding_notes_type_0_item_data.to_dict()
                finding_notes.append(finding_notes_type_0_item)

        else:
            finding_notes = self.finding_notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "executive_summary": executive_summary,
                "product_type": product_type,
                "product": product,
                "engagement": engagement,
                "report_name": report_name,
                "report_info": report_info,
                "test": test,
                "endpoint": endpoint,
                "endpoints": endpoints,
                "findings": findings,
                "user": user,
                "team_name": team_name,
                "title": title,
                "user_id": user_id,
                "host": host,
            }
        )
        if finding_notes is not UNSET:
            field_dict["finding_notes"] = finding_notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.endpoint import Endpoint
        from ..models.engagement import Engagement
        from ..models.executive_summary import ExecutiveSummary
        from ..models.finding import Finding
        from ..models.finding_to_notes import FindingToNotes
        from ..models.product import Product
        from ..models.product_type import ProductType
        from ..models.test import Test
        from ..models.user_stub import UserStub

        d = dict(src_dict)

        def _parse_executive_summary(data: object) -> ExecutiveSummary | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                executive_summary_type_1 = ExecutiveSummary.from_dict(data)

                return executive_summary_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExecutiveSummary | None, data)

        executive_summary = _parse_executive_summary(d.pop("executive_summary"))

        product_type = ProductType.from_dict(d.pop("product_type"))

        product = Product.from_dict(d.pop("product"))

        engagement = Engagement.from_dict(d.pop("engagement"))

        report_name = d.pop("report_name")

        report_info = d.pop("report_info")

        test = Test.from_dict(d.pop("test"))

        endpoint = Endpoint.from_dict(d.pop("endpoint"))

        endpoints = []
        _endpoints = d.pop("endpoints")
        for endpoints_item_data in _endpoints:
            endpoints_item = Endpoint.from_dict(endpoints_item_data)

            endpoints.append(endpoints_item)

        findings = []
        _findings = d.pop("findings")
        for findings_item_data in _findings:
            findings_item = Finding.from_dict(findings_item_data)

            findings.append(findings_item)

        user = UserStub.from_dict(d.pop("user"))

        team_name = d.pop("team_name")

        title = d.pop("title")

        user_id = d.pop("user_id")

        host = d.pop("host")

        def _parse_finding_notes(data: object) -> list[FindingToNotes] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                finding_notes_type_0 = []
                _finding_notes_type_0 = data
                for finding_notes_type_0_item_data in _finding_notes_type_0:
                    finding_notes_type_0_item = FindingToNotes.from_dict(
                        finding_notes_type_0_item_data
                    )

                    finding_notes_type_0.append(finding_notes_type_0_item)

                return finding_notes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FindingToNotes] | None | Unset, data)

        finding_notes = _parse_finding_notes(d.pop("finding_notes", UNSET))

        report_generate = cls(
            executive_summary=executive_summary,
            product_type=product_type,
            product=product,
            engagement=engagement,
            report_name=report_name,
            report_info=report_info,
            test=test,
            endpoint=endpoint,
            endpoints=endpoints,
            findings=findings,
            user=user,
            team_name=team_name,
            title=title,
            user_id=user_id,
            host=host,
            finding_notes=finding_notes,
        )

        report_generate.additional_properties = d
        return report_generate

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
