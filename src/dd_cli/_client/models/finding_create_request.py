from __future__ import annotations

import datetime
import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from .. import types
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vulnerability_id_request import VulnerabilityIdRequest


T = TypeVar("T", bound="FindingCreateRequest")


@_attrs_define
class FindingCreateRequest:
    """
    Attributes:
        test (int):
        found_by (list[int]):
        title (str): A short description of the flaw.
        severity (str): The severity level of this flaw (Critical, High, Medium, Low, Info).
        description (str): Longer more descriptive information about the flaw.
        active (bool): Denotes if this flaw is active or not.
        verified (bool): Denotes if this flaw has been manually verified by the tester.
        numerical_severity (str): The numerical representation of the severity (S0, S1, S2, S3, S4).
        mitigated (datetime.datetime | None | Unset):
        mitigated_by (int | None | Unset):
        thread_id (int | Unset):  Default: 0.
        url (None | str | Unset):
        tags (list[str] | Unset):
        push_to_jira (bool | Unset):  Default: False.
        vulnerability_ids (list[VulnerabilityIdRequest] | Unset):
        reporter (int | Unset):
        date (datetime.date | Unset): The date the flaw was discovered.
        sla_start_date (datetime.date | None | Unset): (readonly)The date used as start date for SLA calculation. Set by
            expiring risk acceptances. Empty by default, causing a fallback to 'date'.
        sla_expiration_date (datetime.date | None | Unset): (readonly)The date SLA expires for this finding. Empty by
            default, causing a fallback to 'date'.
        cwe (int | None | Unset): The CWE number associated with this flaw.
        epss_score (float | None | Unset): EPSS score for the CVE. Describes how likely it is the vulnerability will be
            exploited in the next 30 days.
        epss_percentile (float | None | Unset): EPSS percentile for the CVE. Describes how many CVEs are scored at or
            below this one.
        known_exploited (bool | Unset): Whether this vulnerability is known to have been exploited in the wild.
        ransomware_used (bool | Unset): Whether this vulnerability is known to have been leveraged as part of a
            ransomware campaign.
        kev_date (datetime.date | None | Unset): The date the vulnerability was added to the KEV catalog.
        cvssv3 (None | str | Unset): Common Vulnerability Scoring System version 3 (CVSS3) score associated with this
            finding.
        cvssv3_score (float | None | Unset): Numerical CVSSv3 score for the vulnerability. If the vector is given, the
            score is updated while saving the finding. The value must be between 0-10.
        cvssv4 (None | str | Unset): Common Vulnerability Scoring System version 4 (CVSS4) score associated with this
            finding.
        cvssv4_score (float | None | Unset): Numerical CVSSv4 score for the vulnerability. If the vector is given, the
            score is updated while saving the finding. The value must be between 0-10.
        mitigation (None | str | Unset): Text describing how to best fix the flaw.
        fix_available (bool | None | Unset): Denotes if there is a fix available for this flaw.
        fix_version (None | str | Unset): Version of the affected component in which the flaw is fixed.
        impact (None | str | Unset): Text describing the impact this flaw has on systems, products, enterprise, etc.
        steps_to_reproduce (None | str | Unset): Text describing the steps that must be followed in order to reproduce
            the flaw / bug.
        severity_justification (None | str | Unset): Text describing why a certain severity was associated with this
            flaw.
        references (None | str | Unset): The external documentation available for this flaw.
        false_p (bool | Unset): Denotes if this flaw has been deemed a false positive by the tester.
        duplicate (bool | Unset): Denotes if this flaw is a duplicate of other flaws reported.
        out_of_scope (bool | Unset): Denotes if this flaw falls outside the scope of the test and/or engagement.
        risk_accepted (bool | Unset): Denotes if this finding has been marked as an accepted risk.
        under_review (bool | Unset): Denotes is this flaw is currently being reviewed.
        under_defect_review (bool | Unset): Denotes if this finding is under defect review.
        is_mitigated (bool | Unset): Denotes if this flaw has been fixed.
        line (int | None | Unset): Source line number of the attack vector.
        file_path (None | str | Unset): Identified file(s) containing the flaw.
        component_name (None | str | Unset): Name of the affected component (library name, part of a system, ...).
        component_version (None | str | Unset): Version of the affected component.
        static_finding (bool | Unset): Flaw has been detected from a Static Application Security Testing tool (SAST).
        dynamic_finding (bool | Unset): Flaw has been detected from a Dynamic Application Security Testing tool (DAST).
        unique_id_from_tool (None | str | Unset): Vulnerability technical id from the source tool. Allows to track
            unique vulnerabilities over time across subsequent scans.
        vuln_id_from_tool (None | str | Unset): Non-unique technical id from the source tool associated with the
            vulnerability type.
        sast_source_object (None | str | Unset): Source object (variable, function...) of the attack vector.
        sast_sink_object (None | str | Unset): Sink object (variable, function...) of the attack vector.
        sast_source_line (int | None | Unset): Source line number of the attack vector.
        sast_source_file_path (None | str | Unset): Source file path of the attack vector.
        nb_occurences (int | None | Unset): Number of occurences in the source tool when several vulnerabilites were
            found and aggregated by the scanner.
        publish_date (datetime.date | None | Unset): Date when this vulnerability was made publicly available.
        service (None | str | Unset): A service is a self-contained piece of functionality within a Product. This is an
            optional field which is used in deduplication of findings when set.
        planned_remediation_date (datetime.date | None | Unset): The date the flaw is expected to be remediated.
        planned_remediation_version (None | str | Unset): The target version when the vulnerability should be fixed /
            remediated
        effort_for_fixing (None | str | Unset): Effort for fixing / remediating the vulnerability (Low, Medium, High)
        review_requested_by (int | None | Unset): Documents who requested a review for this finding.
        defect_review_requested_by (int | None | Unset): Documents who requested a defect review for this flaw.
        sonarqube_issue (int | None | Unset): The SonarQube issue associated with this finding.
        reviewers (list[int] | Unset): Documents who reviewed the flaw.
    """

    test: int
    found_by: list[int]
    title: str
    severity: str
    description: str
    active: bool
    verified: bool
    numerical_severity: str
    mitigated: datetime.datetime | None | Unset = UNSET
    mitigated_by: int | None | Unset = UNSET
    thread_id: int | Unset = 0
    url: None | str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    push_to_jira: bool | Unset = False
    vulnerability_ids: list[VulnerabilityIdRequest] | Unset = UNSET
    reporter: int | Unset = UNSET
    date: datetime.date | Unset = UNSET
    sla_start_date: datetime.date | None | Unset = UNSET
    sla_expiration_date: datetime.date | None | Unset = UNSET
    cwe: int | None | Unset = UNSET
    epss_score: float | None | Unset = UNSET
    epss_percentile: float | None | Unset = UNSET
    known_exploited: bool | Unset = UNSET
    ransomware_used: bool | Unset = UNSET
    kev_date: datetime.date | None | Unset = UNSET
    cvssv3: None | str | Unset = UNSET
    cvssv3_score: float | None | Unset = UNSET
    cvssv4: None | str | Unset = UNSET
    cvssv4_score: float | None | Unset = UNSET
    mitigation: None | str | Unset = UNSET
    fix_available: bool | None | Unset = UNSET
    fix_version: None | str | Unset = UNSET
    impact: None | str | Unset = UNSET
    steps_to_reproduce: None | str | Unset = UNSET
    severity_justification: None | str | Unset = UNSET
    references: None | str | Unset = UNSET
    false_p: bool | Unset = UNSET
    duplicate: bool | Unset = UNSET
    out_of_scope: bool | Unset = UNSET
    risk_accepted: bool | Unset = UNSET
    under_review: bool | Unset = UNSET
    under_defect_review: bool | Unset = UNSET
    is_mitigated: bool | Unset = UNSET
    line: int | None | Unset = UNSET
    file_path: None | str | Unset = UNSET
    component_name: None | str | Unset = UNSET
    component_version: None | str | Unset = UNSET
    static_finding: bool | Unset = UNSET
    dynamic_finding: bool | Unset = UNSET
    unique_id_from_tool: None | str | Unset = UNSET
    vuln_id_from_tool: None | str | Unset = UNSET
    sast_source_object: None | str | Unset = UNSET
    sast_sink_object: None | str | Unset = UNSET
    sast_source_line: int | None | Unset = UNSET
    sast_source_file_path: None | str | Unset = UNSET
    nb_occurences: int | None | Unset = UNSET
    publish_date: datetime.date | None | Unset = UNSET
    service: None | str | Unset = UNSET
    planned_remediation_date: datetime.date | None | Unset = UNSET
    planned_remediation_version: None | str | Unset = UNSET
    effort_for_fixing: None | str | Unset = UNSET
    review_requested_by: int | None | Unset = UNSET
    defect_review_requested_by: int | None | Unset = UNSET
    sonarqube_issue: int | None | Unset = UNSET
    reviewers: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        test = self.test

        found_by = self.found_by

        title = self.title

        severity = self.severity

        description = self.description

        active = self.active

        verified = self.verified

        numerical_severity = self.numerical_severity

        mitigated: None | str | Unset
        if isinstance(self.mitigated, Unset):
            mitigated = UNSET
        elif isinstance(self.mitigated, datetime.datetime):
            mitigated = self.mitigated.isoformat()
        else:
            mitigated = self.mitigated

        mitigated_by: int | None | Unset
        if isinstance(self.mitigated_by, Unset):
            mitigated_by = UNSET
        else:
            mitigated_by = self.mitigated_by

        thread_id = self.thread_id

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        push_to_jira = self.push_to_jira

        vulnerability_ids: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vulnerability_ids, Unset):
            vulnerability_ids = []
            for vulnerability_ids_item_data in self.vulnerability_ids:
                vulnerability_ids_item = vulnerability_ids_item_data.to_dict()
                vulnerability_ids.append(vulnerability_ids_item)

        reporter = self.reporter

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        sla_start_date: None | str | Unset
        if isinstance(self.sla_start_date, Unset):
            sla_start_date = UNSET
        elif isinstance(self.sla_start_date, datetime.date):
            sla_start_date = self.sla_start_date.isoformat()
        else:
            sla_start_date = self.sla_start_date

        sla_expiration_date: None | str | Unset
        if isinstance(self.sla_expiration_date, Unset):
            sla_expiration_date = UNSET
        elif isinstance(self.sla_expiration_date, datetime.date):
            sla_expiration_date = self.sla_expiration_date.isoformat()
        else:
            sla_expiration_date = self.sla_expiration_date

        cwe: int | None | Unset
        if isinstance(self.cwe, Unset):
            cwe = UNSET
        else:
            cwe = self.cwe

        epss_score: float | None | Unset
        if isinstance(self.epss_score, Unset):
            epss_score = UNSET
        else:
            epss_score = self.epss_score

        epss_percentile: float | None | Unset
        if isinstance(self.epss_percentile, Unset):
            epss_percentile = UNSET
        else:
            epss_percentile = self.epss_percentile

        known_exploited = self.known_exploited

        ransomware_used = self.ransomware_used

        kev_date: None | str | Unset
        if isinstance(self.kev_date, Unset):
            kev_date = UNSET
        elif isinstance(self.kev_date, datetime.date):
            kev_date = self.kev_date.isoformat()
        else:
            kev_date = self.kev_date

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

        mitigation: None | str | Unset
        if isinstance(self.mitigation, Unset):
            mitigation = UNSET
        else:
            mitigation = self.mitigation

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

        impact: None | str | Unset
        if isinstance(self.impact, Unset):
            impact = UNSET
        else:
            impact = self.impact

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

        references: None | str | Unset
        if isinstance(self.references, Unset):
            references = UNSET
        else:
            references = self.references

        false_p = self.false_p

        duplicate = self.duplicate

        out_of_scope = self.out_of_scope

        risk_accepted = self.risk_accepted

        under_review = self.under_review

        under_defect_review = self.under_defect_review

        is_mitigated = self.is_mitigated

        line: int | None | Unset
        if isinstance(self.line, Unset):
            line = UNSET
        else:
            line = self.line

        file_path: None | str | Unset
        if isinstance(self.file_path, Unset):
            file_path = UNSET
        else:
            file_path = self.file_path

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

        static_finding = self.static_finding

        dynamic_finding = self.dynamic_finding

        unique_id_from_tool: None | str | Unset
        if isinstance(self.unique_id_from_tool, Unset):
            unique_id_from_tool = UNSET
        else:
            unique_id_from_tool = self.unique_id_from_tool

        vuln_id_from_tool: None | str | Unset
        if isinstance(self.vuln_id_from_tool, Unset):
            vuln_id_from_tool = UNSET
        else:
            vuln_id_from_tool = self.vuln_id_from_tool

        sast_source_object: None | str | Unset
        if isinstance(self.sast_source_object, Unset):
            sast_source_object = UNSET
        else:
            sast_source_object = self.sast_source_object

        sast_sink_object: None | str | Unset
        if isinstance(self.sast_sink_object, Unset):
            sast_sink_object = UNSET
        else:
            sast_sink_object = self.sast_sink_object

        sast_source_line: int | None | Unset
        if isinstance(self.sast_source_line, Unset):
            sast_source_line = UNSET
        else:
            sast_source_line = self.sast_source_line

        sast_source_file_path: None | str | Unset
        if isinstance(self.sast_source_file_path, Unset):
            sast_source_file_path = UNSET
        else:
            sast_source_file_path = self.sast_source_file_path

        nb_occurences: int | None | Unset
        if isinstance(self.nb_occurences, Unset):
            nb_occurences = UNSET
        else:
            nb_occurences = self.nb_occurences

        publish_date: None | str | Unset
        if isinstance(self.publish_date, Unset):
            publish_date = UNSET
        elif isinstance(self.publish_date, datetime.date):
            publish_date = self.publish_date.isoformat()
        else:
            publish_date = self.publish_date

        service: None | str | Unset
        if isinstance(self.service, Unset):
            service = UNSET
        else:
            service = self.service

        planned_remediation_date: None | str | Unset
        if isinstance(self.planned_remediation_date, Unset):
            planned_remediation_date = UNSET
        elif isinstance(self.planned_remediation_date, datetime.date):
            planned_remediation_date = self.planned_remediation_date.isoformat()
        else:
            planned_remediation_date = self.planned_remediation_date

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

        review_requested_by: int | None | Unset
        if isinstance(self.review_requested_by, Unset):
            review_requested_by = UNSET
        else:
            review_requested_by = self.review_requested_by

        defect_review_requested_by: int | None | Unset
        if isinstance(self.defect_review_requested_by, Unset):
            defect_review_requested_by = UNSET
        else:
            defect_review_requested_by = self.defect_review_requested_by

        sonarqube_issue: int | None | Unset
        if isinstance(self.sonarqube_issue, Unset):
            sonarqube_issue = UNSET
        else:
            sonarqube_issue = self.sonarqube_issue

        reviewers: list[int] | Unset = UNSET
        if not isinstance(self.reviewers, Unset):
            reviewers = self.reviewers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "test": test,
                "found_by": found_by,
                "title": title,
                "severity": severity,
                "description": description,
                "active": active,
                "verified": verified,
                "numerical_severity": numerical_severity,
            }
        )
        if mitigated is not UNSET:
            field_dict["mitigated"] = mitigated
        if mitigated_by is not UNSET:
            field_dict["mitigated_by"] = mitigated_by
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id
        if url is not UNSET:
            field_dict["url"] = url
        if tags is not UNSET:
            field_dict["tags"] = tags
        if push_to_jira is not UNSET:
            field_dict["push_to_jira"] = push_to_jira
        if vulnerability_ids is not UNSET:
            field_dict["vulnerability_ids"] = vulnerability_ids
        if reporter is not UNSET:
            field_dict["reporter"] = reporter
        if date is not UNSET:
            field_dict["date"] = date
        if sla_start_date is not UNSET:
            field_dict["sla_start_date"] = sla_start_date
        if sla_expiration_date is not UNSET:
            field_dict["sla_expiration_date"] = sla_expiration_date
        if cwe is not UNSET:
            field_dict["cwe"] = cwe
        if epss_score is not UNSET:
            field_dict["epss_score"] = epss_score
        if epss_percentile is not UNSET:
            field_dict["epss_percentile"] = epss_percentile
        if known_exploited is not UNSET:
            field_dict["known_exploited"] = known_exploited
        if ransomware_used is not UNSET:
            field_dict["ransomware_used"] = ransomware_used
        if kev_date is not UNSET:
            field_dict["kev_date"] = kev_date
        if cvssv3 is not UNSET:
            field_dict["cvssv3"] = cvssv3
        if cvssv3_score is not UNSET:
            field_dict["cvssv3_score"] = cvssv3_score
        if cvssv4 is not UNSET:
            field_dict["cvssv4"] = cvssv4
        if cvssv4_score is not UNSET:
            field_dict["cvssv4_score"] = cvssv4_score
        if mitigation is not UNSET:
            field_dict["mitigation"] = mitigation
        if fix_available is not UNSET:
            field_dict["fix_available"] = fix_available
        if fix_version is not UNSET:
            field_dict["fix_version"] = fix_version
        if impact is not UNSET:
            field_dict["impact"] = impact
        if steps_to_reproduce is not UNSET:
            field_dict["steps_to_reproduce"] = steps_to_reproduce
        if severity_justification is not UNSET:
            field_dict["severity_justification"] = severity_justification
        if references is not UNSET:
            field_dict["references"] = references
        if false_p is not UNSET:
            field_dict["false_p"] = false_p
        if duplicate is not UNSET:
            field_dict["duplicate"] = duplicate
        if out_of_scope is not UNSET:
            field_dict["out_of_scope"] = out_of_scope
        if risk_accepted is not UNSET:
            field_dict["risk_accepted"] = risk_accepted
        if under_review is not UNSET:
            field_dict["under_review"] = under_review
        if under_defect_review is not UNSET:
            field_dict["under_defect_review"] = under_defect_review
        if is_mitigated is not UNSET:
            field_dict["is_mitigated"] = is_mitigated
        if line is not UNSET:
            field_dict["line"] = line
        if file_path is not UNSET:
            field_dict["file_path"] = file_path
        if component_name is not UNSET:
            field_dict["component_name"] = component_name
        if component_version is not UNSET:
            field_dict["component_version"] = component_version
        if static_finding is not UNSET:
            field_dict["static_finding"] = static_finding
        if dynamic_finding is not UNSET:
            field_dict["dynamic_finding"] = dynamic_finding
        if unique_id_from_tool is not UNSET:
            field_dict["unique_id_from_tool"] = unique_id_from_tool
        if vuln_id_from_tool is not UNSET:
            field_dict["vuln_id_from_tool"] = vuln_id_from_tool
        if sast_source_object is not UNSET:
            field_dict["sast_source_object"] = sast_source_object
        if sast_sink_object is not UNSET:
            field_dict["sast_sink_object"] = sast_sink_object
        if sast_source_line is not UNSET:
            field_dict["sast_source_line"] = sast_source_line
        if sast_source_file_path is not UNSET:
            field_dict["sast_source_file_path"] = sast_source_file_path
        if nb_occurences is not UNSET:
            field_dict["nb_occurences"] = nb_occurences
        if publish_date is not UNSET:
            field_dict["publish_date"] = publish_date
        if service is not UNSET:
            field_dict["service"] = service
        if planned_remediation_date is not UNSET:
            field_dict["planned_remediation_date"] = planned_remediation_date
        if planned_remediation_version is not UNSET:
            field_dict["planned_remediation_version"] = planned_remediation_version
        if effort_for_fixing is not UNSET:
            field_dict["effort_for_fixing"] = effort_for_fixing
        if review_requested_by is not UNSET:
            field_dict["review_requested_by"] = review_requested_by
        if defect_review_requested_by is not UNSET:
            field_dict["defect_review_requested_by"] = defect_review_requested_by
        if sonarqube_issue is not UNSET:
            field_dict["sonarqube_issue"] = sonarqube_issue
        if reviewers is not UNSET:
            field_dict["reviewers"] = reviewers

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("test", (None, str(self.test).encode(), "text/plain")))

        for found_by_item_element in self.found_by:
            files.append(("found_by", (None, str(found_by_item_element).encode(), "text/plain")))

        files.append(("title", (None, str(self.title).encode(), "text/plain")))

        files.append(("severity", (None, str(self.severity).encode(), "text/plain")))

        files.append(("description", (None, str(self.description).encode(), "text/plain")))

        files.append(("active", (None, str(self.active).encode(), "text/plain")))

        files.append(("verified", (None, str(self.verified).encode(), "text/plain")))

        files.append(
            ("numerical_severity", (None, str(self.numerical_severity).encode(), "text/plain"))
        )

        if not isinstance(self.mitigated, Unset):
            if isinstance(self.mitigated, datetime.datetime):
                files.append(
                    ("mitigated", (None, self.mitigated.isoformat().encode(), "text/plain"))
                )
            else:
                files.append(("mitigated", (None, str(self.mitigated).encode(), "text/plain")))

        if not isinstance(self.mitigated_by, Unset):
            if isinstance(self.mitigated_by, int):
                files.append(
                    ("mitigated_by", (None, str(self.mitigated_by).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("mitigated_by", (None, str(self.mitigated_by).encode(), "text/plain"))
                )

        if not isinstance(self.thread_id, Unset):
            files.append(("thread_id", (None, str(self.thread_id).encode(), "text/plain")))

        if not isinstance(self.url, Unset):
            if isinstance(self.url, str):
                files.append(("url", (None, str(self.url).encode(), "text/plain")))
            else:
                files.append(("url", (None, str(self.url).encode(), "text/plain")))

        if not isinstance(self.tags, Unset):
            for tags_item_element in self.tags:
                files.append(("tags", (None, str(tags_item_element).encode(), "text/plain")))

        if not isinstance(self.push_to_jira, Unset):
            files.append(("push_to_jira", (None, str(self.push_to_jira).encode(), "text/plain")))

        if not isinstance(self.vulnerability_ids, Unset):
            for vulnerability_ids_item_element in self.vulnerability_ids:
                files.append(
                    (
                        "vulnerability_ids",
                        (
                            None,
                            json.dumps(vulnerability_ids_item_element.to_dict()).encode(),
                            "application/json",
                        ),
                    )
                )

        if not isinstance(self.reporter, Unset):
            files.append(("reporter", (None, str(self.reporter).encode(), "text/plain")))

        if not isinstance(self.date, Unset):
            files.append(("date", (None, self.date.isoformat().encode(), "text/plain")))

        if not isinstance(self.sla_start_date, Unset):
            if isinstance(self.sla_start_date, datetime.date):
                files.append(
                    (
                        "sla_start_date",
                        (None, self.sla_start_date.isoformat().encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    ("sla_start_date", (None, str(self.sla_start_date).encode(), "text/plain"))
                )

        if not isinstance(self.sla_expiration_date, Unset):
            if isinstance(self.sla_expiration_date, datetime.date):
                files.append(
                    (
                        "sla_expiration_date",
                        (None, self.sla_expiration_date.isoformat().encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "sla_expiration_date",
                        (None, str(self.sla_expiration_date).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.cwe, Unset):
            if isinstance(self.cwe, int):
                files.append(("cwe", (None, str(self.cwe).encode(), "text/plain")))
            else:
                files.append(("cwe", (None, str(self.cwe).encode(), "text/plain")))

        if not isinstance(self.epss_score, Unset):
            if isinstance(self.epss_score, float):
                files.append(("epss_score", (None, str(self.epss_score).encode(), "text/plain")))
            else:
                files.append(("epss_score", (None, str(self.epss_score).encode(), "text/plain")))

        if not isinstance(self.epss_percentile, Unset):
            if isinstance(self.epss_percentile, float):
                files.append(
                    ("epss_percentile", (None, str(self.epss_percentile).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("epss_percentile", (None, str(self.epss_percentile).encode(), "text/plain"))
                )

        if not isinstance(self.known_exploited, Unset):
            files.append(
                ("known_exploited", (None, str(self.known_exploited).encode(), "text/plain"))
            )

        if not isinstance(self.ransomware_used, Unset):
            files.append(
                ("ransomware_used", (None, str(self.ransomware_used).encode(), "text/plain"))
            )

        if not isinstance(self.kev_date, Unset):
            if isinstance(self.kev_date, datetime.date):
                files.append(("kev_date", (None, self.kev_date.isoformat().encode(), "text/plain")))
            else:
                files.append(("kev_date", (None, str(self.kev_date).encode(), "text/plain")))

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

        if not isinstance(self.mitigation, Unset):
            if isinstance(self.mitigation, str):
                files.append(("mitigation", (None, str(self.mitigation).encode(), "text/plain")))
            else:
                files.append(("mitigation", (None, str(self.mitigation).encode(), "text/plain")))

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

        if not isinstance(self.impact, Unset):
            if isinstance(self.impact, str):
                files.append(("impact", (None, str(self.impact).encode(), "text/plain")))
            else:
                files.append(("impact", (None, str(self.impact).encode(), "text/plain")))

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

        if not isinstance(self.references, Unset):
            if isinstance(self.references, str):
                files.append(("references", (None, str(self.references).encode(), "text/plain")))
            else:
                files.append(("references", (None, str(self.references).encode(), "text/plain")))

        if not isinstance(self.false_p, Unset):
            files.append(("false_p", (None, str(self.false_p).encode(), "text/plain")))

        if not isinstance(self.duplicate, Unset):
            files.append(("duplicate", (None, str(self.duplicate).encode(), "text/plain")))

        if not isinstance(self.out_of_scope, Unset):
            files.append(("out_of_scope", (None, str(self.out_of_scope).encode(), "text/plain")))

        if not isinstance(self.risk_accepted, Unset):
            files.append(("risk_accepted", (None, str(self.risk_accepted).encode(), "text/plain")))

        if not isinstance(self.under_review, Unset):
            files.append(("under_review", (None, str(self.under_review).encode(), "text/plain")))

        if not isinstance(self.under_defect_review, Unset):
            files.append(
                (
                    "under_defect_review",
                    (None, str(self.under_defect_review).encode(), "text/plain"),
                )
            )

        if not isinstance(self.is_mitigated, Unset):
            files.append(("is_mitigated", (None, str(self.is_mitigated).encode(), "text/plain")))

        if not isinstance(self.line, Unset):
            if isinstance(self.line, int):
                files.append(("line", (None, str(self.line).encode(), "text/plain")))
            else:
                files.append(("line", (None, str(self.line).encode(), "text/plain")))

        if not isinstance(self.file_path, Unset):
            if isinstance(self.file_path, str):
                files.append(("file_path", (None, str(self.file_path).encode(), "text/plain")))
            else:
                files.append(("file_path", (None, str(self.file_path).encode(), "text/plain")))

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

        if not isinstance(self.static_finding, Unset):
            files.append(
                ("static_finding", (None, str(self.static_finding).encode(), "text/plain"))
            )

        if not isinstance(self.dynamic_finding, Unset):
            files.append(
                ("dynamic_finding", (None, str(self.dynamic_finding).encode(), "text/plain"))
            )

        if not isinstance(self.unique_id_from_tool, Unset):
            if isinstance(self.unique_id_from_tool, str):
                files.append(
                    (
                        "unique_id_from_tool",
                        (None, str(self.unique_id_from_tool).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "unique_id_from_tool",
                        (None, str(self.unique_id_from_tool).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.vuln_id_from_tool, Unset):
            if isinstance(self.vuln_id_from_tool, str):
                files.append(
                    (
                        "vuln_id_from_tool",
                        (None, str(self.vuln_id_from_tool).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "vuln_id_from_tool",
                        (None, str(self.vuln_id_from_tool).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.sast_source_object, Unset):
            if isinstance(self.sast_source_object, str):
                files.append(
                    (
                        "sast_source_object",
                        (None, str(self.sast_source_object).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "sast_source_object",
                        (None, str(self.sast_source_object).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.sast_sink_object, Unset):
            if isinstance(self.sast_sink_object, str):
                files.append(
                    ("sast_sink_object", (None, str(self.sast_sink_object).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("sast_sink_object", (None, str(self.sast_sink_object).encode(), "text/plain"))
                )

        if not isinstance(self.sast_source_line, Unset):
            if isinstance(self.sast_source_line, int):
                files.append(
                    ("sast_source_line", (None, str(self.sast_source_line).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("sast_source_line", (None, str(self.sast_source_line).encode(), "text/plain"))
                )

        if not isinstance(self.sast_source_file_path, Unset):
            if isinstance(self.sast_source_file_path, str):
                files.append(
                    (
                        "sast_source_file_path",
                        (None, str(self.sast_source_file_path).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "sast_source_file_path",
                        (None, str(self.sast_source_file_path).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.nb_occurences, Unset):
            if isinstance(self.nb_occurences, int):
                files.append(
                    ("nb_occurences", (None, str(self.nb_occurences).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("nb_occurences", (None, str(self.nb_occurences).encode(), "text/plain"))
                )

        if not isinstance(self.publish_date, Unset):
            if isinstance(self.publish_date, datetime.date):
                files.append(
                    ("publish_date", (None, self.publish_date.isoformat().encode(), "text/plain"))
                )
            else:
                files.append(
                    ("publish_date", (None, str(self.publish_date).encode(), "text/plain"))
                )

        if not isinstance(self.service, Unset):
            if isinstance(self.service, str):
                files.append(("service", (None, str(self.service).encode(), "text/plain")))
            else:
                files.append(("service", (None, str(self.service).encode(), "text/plain")))

        if not isinstance(self.planned_remediation_date, Unset):
            if isinstance(self.planned_remediation_date, datetime.date):
                files.append(
                    (
                        "planned_remediation_date",
                        (None, self.planned_remediation_date.isoformat().encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "planned_remediation_date",
                        (None, str(self.planned_remediation_date).encode(), "text/plain"),
                    )
                )

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

        if not isinstance(self.review_requested_by, Unset):
            if isinstance(self.review_requested_by, int):
                files.append(
                    (
                        "review_requested_by",
                        (None, str(self.review_requested_by).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "review_requested_by",
                        (None, str(self.review_requested_by).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.defect_review_requested_by, Unset):
            if isinstance(self.defect_review_requested_by, int):
                files.append(
                    (
                        "defect_review_requested_by",
                        (None, str(self.defect_review_requested_by).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "defect_review_requested_by",
                        (None, str(self.defect_review_requested_by).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.sonarqube_issue, Unset):
            if isinstance(self.sonarqube_issue, int):
                files.append(
                    ("sonarqube_issue", (None, str(self.sonarqube_issue).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("sonarqube_issue", (None, str(self.sonarqube_issue).encode(), "text/plain"))
                )

        if not isinstance(self.reviewers, Unset):
            for reviewers_item_element in self.reviewers:
                files.append(
                    ("reviewers", (None, str(reviewers_item_element).encode(), "text/plain"))
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vulnerability_id_request import VulnerabilityIdRequest

        d = dict(src_dict)
        test = d.pop("test")

        found_by = cast(list[int], d.pop("found_by"))

        title = d.pop("title")

        severity = d.pop("severity")

        description = d.pop("description")

        active = d.pop("active")

        verified = d.pop("verified")

        numerical_severity = d.pop("numerical_severity")

        def _parse_mitigated(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mitigated_type_0 = isoparse(data)

                return mitigated_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        mitigated = _parse_mitigated(d.pop("mitigated", UNSET))

        def _parse_mitigated_by(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        mitigated_by = _parse_mitigated_by(d.pop("mitigated_by", UNSET))

        thread_id = d.pop("thread_id", UNSET)

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        push_to_jira = d.pop("push_to_jira", UNSET)

        _vulnerability_ids = d.pop("vulnerability_ids", UNSET)
        vulnerability_ids: list[VulnerabilityIdRequest] | Unset = UNSET
        if _vulnerability_ids is not UNSET:
            vulnerability_ids = []
            for vulnerability_ids_item_data in _vulnerability_ids:
                vulnerability_ids_item = VulnerabilityIdRequest.from_dict(
                    vulnerability_ids_item_data
                )

                vulnerability_ids.append(vulnerability_ids_item)

        reporter = d.pop("reporter", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        def _parse_sla_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sla_start_date_type_0 = isoparse(data).date()

                return sla_start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        sla_start_date = _parse_sla_start_date(d.pop("sla_start_date", UNSET))

        def _parse_sla_expiration_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sla_expiration_date_type_0 = isoparse(data).date()

                return sla_expiration_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        sla_expiration_date = _parse_sla_expiration_date(d.pop("sla_expiration_date", UNSET))

        def _parse_cwe(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cwe = _parse_cwe(d.pop("cwe", UNSET))

        def _parse_epss_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        epss_score = _parse_epss_score(d.pop("epss_score", UNSET))

        def _parse_epss_percentile(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        epss_percentile = _parse_epss_percentile(d.pop("epss_percentile", UNSET))

        known_exploited = d.pop("known_exploited", UNSET)

        ransomware_used = d.pop("ransomware_used", UNSET)

        def _parse_kev_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kev_date_type_0 = isoparse(data).date()

                return kev_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        kev_date = _parse_kev_date(d.pop("kev_date", UNSET))

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

        def _parse_mitigation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mitigation = _parse_mitigation(d.pop("mitigation", UNSET))

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

        def _parse_impact(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        impact = _parse_impact(d.pop("impact", UNSET))

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

        def _parse_references(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        references = _parse_references(d.pop("references", UNSET))

        false_p = d.pop("false_p", UNSET)

        duplicate = d.pop("duplicate", UNSET)

        out_of_scope = d.pop("out_of_scope", UNSET)

        risk_accepted = d.pop("risk_accepted", UNSET)

        under_review = d.pop("under_review", UNSET)

        under_defect_review = d.pop("under_defect_review", UNSET)

        is_mitigated = d.pop("is_mitigated", UNSET)

        def _parse_line(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        line = _parse_line(d.pop("line", UNSET))

        def _parse_file_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_path = _parse_file_path(d.pop("file_path", UNSET))

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

        static_finding = d.pop("static_finding", UNSET)

        dynamic_finding = d.pop("dynamic_finding", UNSET)

        def _parse_unique_id_from_tool(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unique_id_from_tool = _parse_unique_id_from_tool(d.pop("unique_id_from_tool", UNSET))

        def _parse_vuln_id_from_tool(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vuln_id_from_tool = _parse_vuln_id_from_tool(d.pop("vuln_id_from_tool", UNSET))

        def _parse_sast_source_object(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sast_source_object = _parse_sast_source_object(d.pop("sast_source_object", UNSET))

        def _parse_sast_sink_object(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sast_sink_object = _parse_sast_sink_object(d.pop("sast_sink_object", UNSET))

        def _parse_sast_source_line(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sast_source_line = _parse_sast_source_line(d.pop("sast_source_line", UNSET))

        def _parse_sast_source_file_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sast_source_file_path = _parse_sast_source_file_path(d.pop("sast_source_file_path", UNSET))

        def _parse_nb_occurences(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        nb_occurences = _parse_nb_occurences(d.pop("nb_occurences", UNSET))

        def _parse_publish_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                publish_date_type_0 = isoparse(data).date()

                return publish_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        publish_date = _parse_publish_date(d.pop("publish_date", UNSET))

        def _parse_service(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service = _parse_service(d.pop("service", UNSET))

        def _parse_planned_remediation_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                planned_remediation_date_type_0 = isoparse(data).date()

                return planned_remediation_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        planned_remediation_date = _parse_planned_remediation_date(
            d.pop("planned_remediation_date", UNSET)
        )

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

        def _parse_review_requested_by(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        review_requested_by = _parse_review_requested_by(d.pop("review_requested_by", UNSET))

        def _parse_defect_review_requested_by(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        defect_review_requested_by = _parse_defect_review_requested_by(
            d.pop("defect_review_requested_by", UNSET)
        )

        def _parse_sonarqube_issue(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sonarqube_issue = _parse_sonarqube_issue(d.pop("sonarqube_issue", UNSET))

        reviewers = cast(list[int], d.pop("reviewers", UNSET))

        finding_create_request = cls(
            test=test,
            found_by=found_by,
            title=title,
            severity=severity,
            description=description,
            active=active,
            verified=verified,
            numerical_severity=numerical_severity,
            mitigated=mitigated,
            mitigated_by=mitigated_by,
            thread_id=thread_id,
            url=url,
            tags=tags,
            push_to_jira=push_to_jira,
            vulnerability_ids=vulnerability_ids,
            reporter=reporter,
            date=date,
            sla_start_date=sla_start_date,
            sla_expiration_date=sla_expiration_date,
            cwe=cwe,
            epss_score=epss_score,
            epss_percentile=epss_percentile,
            known_exploited=known_exploited,
            ransomware_used=ransomware_used,
            kev_date=kev_date,
            cvssv3=cvssv3,
            cvssv3_score=cvssv3_score,
            cvssv4=cvssv4,
            cvssv4_score=cvssv4_score,
            mitigation=mitigation,
            fix_available=fix_available,
            fix_version=fix_version,
            impact=impact,
            steps_to_reproduce=steps_to_reproduce,
            severity_justification=severity_justification,
            references=references,
            false_p=false_p,
            duplicate=duplicate,
            out_of_scope=out_of_scope,
            risk_accepted=risk_accepted,
            under_review=under_review,
            under_defect_review=under_defect_review,
            is_mitigated=is_mitigated,
            line=line,
            file_path=file_path,
            component_name=component_name,
            component_version=component_version,
            static_finding=static_finding,
            dynamic_finding=dynamic_finding,
            unique_id_from_tool=unique_id_from_tool,
            vuln_id_from_tool=vuln_id_from_tool,
            sast_source_object=sast_source_object,
            sast_sink_object=sast_sink_object,
            sast_source_line=sast_source_line,
            sast_source_file_path=sast_source_file_path,
            nb_occurences=nb_occurences,
            publish_date=publish_date,
            service=service,
            planned_remediation_date=planned_remediation_date,
            planned_remediation_version=planned_remediation_version,
            effort_for_fixing=effort_for_fixing,
            review_requested_by=review_requested_by,
            defect_review_requested_by=defect_review_requested_by,
            sonarqube_issue=sonarqube_issue,
            reviewers=reviewers,
        )

        finding_create_request.additional_properties = d
        return finding_create_request

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
