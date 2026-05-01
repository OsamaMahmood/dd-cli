from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedFindingTemplateRequest")


@_attrs_define
class PatchedFindingTemplateRequest:
    """
    Attributes:
        tags (list[str] | Unset):
        title (str | Unset):
        cwe (int | None | Unset):
        cvssv3 (None | str | Unset): Common Vulnerability Scoring System version 3 (CVSSv3) score associated with this
            finding.
        cvssv3_score (float | None | Unset): CVSSv3 score
        cvssv4 (None | str | Unset): Common Vulnerability Scoring System version 4 (CVSS4) score associated with this
            finding.
        cvssv4_score (float | None | Unset): CVSSv4 score
        severity (None | str | Unset):
        description (None | str | Unset):
        mitigation (None | str | Unset):
        impact (None | str | Unset):
        references (None | str | Unset):
        fix_available (bool | None | Unset): Indicates if a fix is available for this vulnerability type
        fix_version (None | str | Unset): Version where fix is available
        planned_remediation_version (None | str | Unset): Target version for remediation
        effort_for_fixing (None | str | Unset): Effort estimate for fixing (e.g., Low/Medium/High)
        steps_to_reproduce (None | str | Unset): Standard reproduction steps for this vulnerability type
        severity_justification (None | str | Unset): Explanation of why this severity level is appropriate
        component_name (None | str | Unset): Affected component name (e.g., library name)
        component_version (None | str | Unset): Affected component version
        notes (None | str | Unset): Note content to add when applying this template
        endpoints_text (None | str | Unset): Endpoint URLs (one per line)
    """

    tags: list[str] | Unset = UNSET
    title: str | Unset = UNSET
    cwe: int | None | Unset = UNSET
    cvssv3: None | str | Unset = UNSET
    cvssv3_score: float | None | Unset = UNSET
    cvssv4: None | str | Unset = UNSET
    cvssv4_score: float | None | Unset = UNSET
    severity: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    mitigation: None | str | Unset = UNSET
    impact: None | str | Unset = UNSET
    references: None | str | Unset = UNSET
    fix_available: bool | None | Unset = UNSET
    fix_version: None | str | Unset = UNSET
    planned_remediation_version: None | str | Unset = UNSET
    effort_for_fixing: None | str | Unset = UNSET
    steps_to_reproduce: None | str | Unset = UNSET
    severity_justification: None | str | Unset = UNSET
    component_name: None | str | Unset = UNSET
    component_version: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    endpoints_text: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        title = self.title

        cwe: int | None | Unset
        if isinstance(self.cwe, Unset):
            cwe = UNSET
        else:
            cwe = self.cwe

        cvssv3: None | str | Unset
        if isinstance(self.cvssv3, Unset):
            cvssv3 = UNSET
        else:
            cvssv3 = self.cvssv3

        cvssv3_score: float | None | Unset
        if isinstance(self.cvssv3_score, Unset):
            cvssv3_score = UNSET
        else:
            cvssv3_score = self.cvssv3_score

        cvssv4: None | str | Unset
        if isinstance(self.cvssv4, Unset):
            cvssv4 = UNSET
        else:
            cvssv4 = self.cvssv4

        cvssv4_score: float | None | Unset
        if isinstance(self.cvssv4_score, Unset):
            cvssv4_score = UNSET
        else:
            cvssv4_score = self.cvssv4_score

        severity: None | str | Unset
        if isinstance(self.severity, Unset):
            severity = UNSET
        else:
            severity = self.severity

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        mitigation: None | str | Unset
        if isinstance(self.mitigation, Unset):
            mitigation = UNSET
        else:
            mitigation = self.mitigation

        impact: None | str | Unset
        if isinstance(self.impact, Unset):
            impact = UNSET
        else:
            impact = self.impact

        references: None | str | Unset
        if isinstance(self.references, Unset):
            references = UNSET
        else:
            references = self.references

        fix_available: bool | None | Unset
        if isinstance(self.fix_available, Unset):
            fix_available = UNSET
        else:
            fix_available = self.fix_available

        fix_version: None | str | Unset
        if isinstance(self.fix_version, Unset):
            fix_version = UNSET
        else:
            fix_version = self.fix_version

        planned_remediation_version: None | str | Unset
        if isinstance(self.planned_remediation_version, Unset):
            planned_remediation_version = UNSET
        else:
            planned_remediation_version = self.planned_remediation_version

        effort_for_fixing: None | str | Unset
        if isinstance(self.effort_for_fixing, Unset):
            effort_for_fixing = UNSET
        else:
            effort_for_fixing = self.effort_for_fixing

        steps_to_reproduce: None | str | Unset
        if isinstance(self.steps_to_reproduce, Unset):
            steps_to_reproduce = UNSET
        else:
            steps_to_reproduce = self.steps_to_reproduce

        severity_justification: None | str | Unset
        if isinstance(self.severity_justification, Unset):
            severity_justification = UNSET
        else:
            severity_justification = self.severity_justification

        component_name: None | str | Unset
        if isinstance(self.component_name, Unset):
            component_name = UNSET
        else:
            component_name = self.component_name

        component_version: None | str | Unset
        if isinstance(self.component_version, Unset):
            component_version = UNSET
        else:
            component_version = self.component_version

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        endpoints_text: None | str | Unset
        if isinstance(self.endpoints_text, Unset):
            endpoints_text = UNSET
        else:
            endpoints_text = self.endpoints_text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tags is not UNSET:
            field_dict["tags"] = tags
        if title is not UNSET:
            field_dict["title"] = title
        if cwe is not UNSET:
            field_dict["cwe"] = cwe
        if cvssv3 is not UNSET:
            field_dict["cvssv3"] = cvssv3
        if cvssv3_score is not UNSET:
            field_dict["cvssv3_score"] = cvssv3_score
        if cvssv4 is not UNSET:
            field_dict["cvssv4"] = cvssv4
        if cvssv4_score is not UNSET:
            field_dict["cvssv4_score"] = cvssv4_score
        if severity is not UNSET:
            field_dict["severity"] = severity
        if description is not UNSET:
            field_dict["description"] = description
        if mitigation is not UNSET:
            field_dict["mitigation"] = mitigation
        if impact is not UNSET:
            field_dict["impact"] = impact
        if references is not UNSET:
            field_dict["references"] = references
        if fix_available is not UNSET:
            field_dict["fix_available"] = fix_available
        if fix_version is not UNSET:
            field_dict["fix_version"] = fix_version
        if planned_remediation_version is not UNSET:
            field_dict["planned_remediation_version"] = planned_remediation_version
        if effort_for_fixing is not UNSET:
            field_dict["effort_for_fixing"] = effort_for_fixing
        if steps_to_reproduce is not UNSET:
            field_dict["steps_to_reproduce"] = steps_to_reproduce
        if severity_justification is not UNSET:
            field_dict["severity_justification"] = severity_justification
        if component_name is not UNSET:
            field_dict["component_name"] = component_name
        if component_version is not UNSET:
            field_dict["component_version"] = component_version
        if notes is not UNSET:
            field_dict["notes"] = notes
        if endpoints_text is not UNSET:
            field_dict["endpoints_text"] = endpoints_text

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.tags, Unset):
            for tags_item_element in self.tags:
                files.append(("tags", (None, str(tags_item_element).encode(), "text/plain")))

        if not isinstance(self.title, Unset):
            files.append(("title", (None, str(self.title).encode(), "text/plain")))

        if not isinstance(self.cwe, Unset):
            if isinstance(self.cwe, int):
                files.append(("cwe", (None, str(self.cwe).encode(), "text/plain")))
            else:
                files.append(("cwe", (None, str(self.cwe).encode(), "text/plain")))

        if not isinstance(self.cvssv3, Unset):
            if isinstance(self.cvssv3, str):
                files.append(("cvssv3", (None, str(self.cvssv3).encode(), "text/plain")))
            else:
                files.append(("cvssv3", (None, str(self.cvssv3).encode(), "text/plain")))

        if not isinstance(self.cvssv3_score, Unset):
            if isinstance(self.cvssv3_score, float):
                files.append(
                    ("cvssv3_score", (None, str(self.cvssv3_score).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("cvssv3_score", (None, str(self.cvssv3_score).encode(), "text/plain"))
                )

        if not isinstance(self.cvssv4, Unset):
            if isinstance(self.cvssv4, str):
                files.append(("cvssv4", (None, str(self.cvssv4).encode(), "text/plain")))
            else:
                files.append(("cvssv4", (None, str(self.cvssv4).encode(), "text/plain")))

        if not isinstance(self.cvssv4_score, Unset):
            if isinstance(self.cvssv4_score, float):
                files.append(
                    ("cvssv4_score", (None, str(self.cvssv4_score).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("cvssv4_score", (None, str(self.cvssv4_score).encode(), "text/plain"))
                )

        if not isinstance(self.severity, Unset):
            if isinstance(self.severity, str):
                files.append(("severity", (None, str(self.severity).encode(), "text/plain")))
            else:
                files.append(("severity", (None, str(self.severity).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            if isinstance(self.description, str):
                files.append(("description", (None, str(self.description).encode(), "text/plain")))
            else:
                files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.mitigation, Unset):
            if isinstance(self.mitigation, str):
                files.append(("mitigation", (None, str(self.mitigation).encode(), "text/plain")))
            else:
                files.append(("mitigation", (None, str(self.mitigation).encode(), "text/plain")))

        if not isinstance(self.impact, Unset):
            if isinstance(self.impact, str):
                files.append(("impact", (None, str(self.impact).encode(), "text/plain")))
            else:
                files.append(("impact", (None, str(self.impact).encode(), "text/plain")))

        if not isinstance(self.references, Unset):
            if isinstance(self.references, str):
                files.append(("references", (None, str(self.references).encode(), "text/plain")))
            else:
                files.append(("references", (None, str(self.references).encode(), "text/plain")))

        if not isinstance(self.fix_available, Unset):
            if isinstance(self.fix_available, bool):
                files.append(
                    ("fix_available", (None, str(self.fix_available).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("fix_available", (None, str(self.fix_available).encode(), "text/plain"))
                )

        if not isinstance(self.fix_version, Unset):
            if isinstance(self.fix_version, str):
                files.append(("fix_version", (None, str(self.fix_version).encode(), "text/plain")))
            else:
                files.append(("fix_version", (None, str(self.fix_version).encode(), "text/plain")))

        if not isinstance(self.planned_remediation_version, Unset):
            if isinstance(self.planned_remediation_version, str):
                files.append(
                    (
                        "planned_remediation_version",
                        (None, str(self.planned_remediation_version).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "planned_remediation_version",
                        (None, str(self.planned_remediation_version).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.effort_for_fixing, Unset):
            if isinstance(self.effort_for_fixing, str):
                files.append(
                    (
                        "effort_for_fixing",
                        (None, str(self.effort_for_fixing).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "effort_for_fixing",
                        (None, str(self.effort_for_fixing).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.steps_to_reproduce, Unset):
            if isinstance(self.steps_to_reproduce, str):
                files.append(
                    (
                        "steps_to_reproduce",
                        (None, str(self.steps_to_reproduce).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "steps_to_reproduce",
                        (None, str(self.steps_to_reproduce).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.severity_justification, Unset):
            if isinstance(self.severity_justification, str):
                files.append(
                    (
                        "severity_justification",
                        (None, str(self.severity_justification).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "severity_justification",
                        (None, str(self.severity_justification).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.component_name, Unset):
            if isinstance(self.component_name, str):
                files.append(
                    ("component_name", (None, str(self.component_name).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("component_name", (None, str(self.component_name).encode(), "text/plain"))
                )

        if not isinstance(self.component_version, Unset):
            if isinstance(self.component_version, str):
                files.append(
                    (
                        "component_version",
                        (None, str(self.component_version).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "component_version",
                        (None, str(self.component_version).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.notes, Unset):
            if isinstance(self.notes, str):
                files.append(("notes", (None, str(self.notes).encode(), "text/plain")))
            else:
                files.append(("notes", (None, str(self.notes).encode(), "text/plain")))

        if not isinstance(self.endpoints_text, Unset):
            if isinstance(self.endpoints_text, str):
                files.append(
                    ("endpoints_text", (None, str(self.endpoints_text).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("endpoints_text", (None, str(self.endpoints_text).encode(), "text/plain"))
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tags = cast(list[str], d.pop("tags", UNSET))

        title = d.pop("title", UNSET)

        def _parse_cwe(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cwe = _parse_cwe(d.pop("cwe", UNSET))

        def _parse_cvssv3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cvssv3 = _parse_cvssv3(d.pop("cvssv3", UNSET))

        def _parse_cvssv3_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cvssv3_score = _parse_cvssv3_score(d.pop("cvssv3_score", UNSET))

        def _parse_cvssv4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cvssv4 = _parse_cvssv4(d.pop("cvssv4", UNSET))

        def _parse_cvssv4_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cvssv4_score = _parse_cvssv4_score(d.pop("cvssv4_score", UNSET))

        def _parse_severity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        severity = _parse_severity(d.pop("severity", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_mitigation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mitigation = _parse_mitigation(d.pop("mitigation", UNSET))

        def _parse_impact(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        impact = _parse_impact(d.pop("impact", UNSET))

        def _parse_references(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        references = _parse_references(d.pop("references", UNSET))

        def _parse_fix_available(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        fix_available = _parse_fix_available(d.pop("fix_available", UNSET))

        def _parse_fix_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fix_version = _parse_fix_version(d.pop("fix_version", UNSET))

        def _parse_planned_remediation_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        planned_remediation_version = _parse_planned_remediation_version(
            d.pop("planned_remediation_version", UNSET)
        )

        def _parse_effort_for_fixing(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        effort_for_fixing = _parse_effort_for_fixing(d.pop("effort_for_fixing", UNSET))

        def _parse_steps_to_reproduce(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        steps_to_reproduce = _parse_steps_to_reproduce(d.pop("steps_to_reproduce", UNSET))

        def _parse_severity_justification(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        severity_justification = _parse_severity_justification(
            d.pop("severity_justification", UNSET)
        )

        def _parse_component_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        component_name = _parse_component_name(d.pop("component_name", UNSET))

        def _parse_component_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        component_version = _parse_component_version(d.pop("component_version", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_endpoints_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        endpoints_text = _parse_endpoints_text(d.pop("endpoints_text", UNSET))

        patched_finding_template_request = cls(
            tags=tags,
            title=title,
            cwe=cwe,
            cvssv3=cvssv3,
            cvssv3_score=cvssv3_score,
            cvssv4=cvssv4,
            cvssv4_score=cvssv4_score,
            severity=severity,
            description=description,
            mitigation=mitigation,
            impact=impact,
            references=references,
            fix_available=fix_available,
            fix_version=fix_version,
            planned_remediation_version=planned_remediation_version,
            effort_for_fixing=effort_for_fixing,
            steps_to_reproduce=steps_to_reproduce,
            severity_justification=severity_justification,
            component_name=component_name,
            component_version=component_version,
            notes=notes,
            endpoints_text=endpoints_text,
        )

        patched_finding_template_request.additional_properties = d
        return patched_finding_template_request

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
