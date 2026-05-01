from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.burp_raw_request_response import BurpRawRequestResponse
    from ..models.finding_group import FindingGroup
    from ..models.finding_meta import FindingMeta
    from ..models.finding_prefetch import FindingPrefetch
    from ..models.finding_related_fields import FindingRelatedFields
    from ..models.note import Note
    from ..models.risk_acceptance import RiskAcceptance
    from ..models.vulnerability_id import VulnerabilityId


T = TypeVar("T", bound="Finding")


@_attrs_define
class Finding:
    """
    Attributes:
        id (int):
        request_response (BurpRawRequestResponse):
        accepted_risks (list[RiskAcceptance]):
        found_by (list[int]):
        age (int):
        sla_days_remaining (int | None):
        finding_meta (list[FindingMeta]):
        related_fields (FindingRelatedFields | None):
        jira_creation (datetime.datetime | None):
        jira_change (datetime.datetime | None):
        display_status (str):
        finding_groups (list[FindingGroup]):
        title (str): A short description of the flaw.
        url (None | str): External reference that provides more information about this flaw.
        severity (str): The severity level of this flaw (Critical, High, Medium, Low, Info).
        description (str): Longer more descriptive information about the flaw.
        last_status_update (datetime.datetime | None): Timestamp of latest status update (change in status related
            fields).
        thread_id (int):
        numerical_severity (str): The numerical representation of the severity (S0, S1, S2, S3, S4).
        last_reviewed (datetime.datetime | None): Provides the date the flaw was last 'touched' by a tester.
        param (None | str): Parameter used to trigger the issue (DAST).
        payload (None | str): Payload used to attack the service / application and trigger the bug / problem.
        hash_code (None | str): A hash over a configurable set of fields that is used for findings deduplication.
        created (datetime.datetime | None): The date the finding was created inside DefectDojo.
        scanner_confidence (int | None): Confidence level of vulnerability which is supplied by the scanner.
        test (int): The test that is associated with this flaw.
        duplicate_finding (int | None): Link to the original finding if this finding is a duplicate.
        last_reviewed_by (int | None): Provides the person who last reviewed the flaw.
        endpoints (list[int]): The hosts within the product that are susceptible to this flaw. + The status of the
            endpoint associated with this flaw (Vulnerable, Mitigated, ...).
        notes (list[Note]):
        files (list[int]): Files(s) related to the flaw.
        mitigated (datetime.datetime | None | Unset):
        mitigated_by (int | None | Unset):
        tags (list[str] | Unset):
        push_to_jira (bool | Unset):  Default: False.
        vulnerability_ids (list[VulnerabilityId] | Unset):
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
        active (bool | Unset): Denotes if this flaw is active or not.
        verified (bool | Unset): Denotes if this flaw has been manually verified by the tester.
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
        prefetch (FindingPrefetch | Unset):
    """

    id: int
    request_response: BurpRawRequestResponse
    accepted_risks: list[RiskAcceptance]
    found_by: list[int]
    age: int
    sla_days_remaining: int | None
    finding_meta: list[FindingMeta]
    related_fields: FindingRelatedFields | None
    jira_creation: datetime.datetime | None
    jira_change: datetime.datetime | None
    display_status: str
    finding_groups: list[FindingGroup]
    title: str
    url: None | str
    severity: str
    description: str
    last_status_update: datetime.datetime | None
    thread_id: int
    numerical_severity: str
    last_reviewed: datetime.datetime | None
    param: None | str
    payload: None | str
    hash_code: None | str
    created: datetime.datetime | None
    scanner_confidence: int | None
    test: int
    duplicate_finding: int | None
    last_reviewed_by: int | None
    endpoints: list[int]
    notes: list[Note]
    files: list[int]
    mitigated: datetime.datetime | None | Unset = UNSET
    mitigated_by: int | None | Unset = UNSET
    tags: list[str] | Unset = UNSET
    push_to_jira: bool | Unset = False
    vulnerability_ids: list[VulnerabilityId] | Unset = UNSET
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
    active: bool | Unset = UNSET
    verified: bool | Unset = UNSET
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
    prefetch: FindingPrefetch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.finding_related_fields import FindingRelatedFields

        id = self.id

        request_response = self.request_response.to_dict()

        accepted_risks = []
        for accepted_risks_item_data in self.accepted_risks:
            accepted_risks_item = accepted_risks_item_data.to_dict()
            accepted_risks.append(accepted_risks_item)

        found_by = self.found_by

        age = self.age

        sla_days_remaining: int | None
        sla_days_remaining = self.sla_days_remaining

        finding_meta = []
        for finding_meta_item_data in self.finding_meta:
            finding_meta_item = finding_meta_item_data.to_dict()
            finding_meta.append(finding_meta_item)

        related_fields: dict[str, Any] | None
        if isinstance(self.related_fields, FindingRelatedFields):
            related_fields = self.related_fields.to_dict()
        else:
            related_fields = self.related_fields

        jira_creation: None | str
        if isinstance(self.jira_creation, datetime.datetime):
            jira_creation = self.jira_creation.isoformat()
        else:
            jira_creation = self.jira_creation

        jira_change: None | str
        if isinstance(self.jira_change, datetime.datetime):
            jira_change = self.jira_change.isoformat()
        else:
            jira_change = self.jira_change

        display_status = self.display_status

        finding_groups = []
        for finding_groups_item_data in self.finding_groups:
            finding_groups_item = finding_groups_item_data.to_dict()
            finding_groups.append(finding_groups_item)

        title = self.title

        url: None | str
        url = self.url

        severity = self.severity

        description = self.description

        last_status_update: None | str
        if isinstance(self.last_status_update, datetime.datetime):
            last_status_update = self.last_status_update.isoformat()
        else:
            last_status_update = self.last_status_update

        thread_id = self.thread_id

        numerical_severity = self.numerical_severity

        last_reviewed: None | str
        if isinstance(self.last_reviewed, datetime.datetime):
            last_reviewed = self.last_reviewed.isoformat()
        else:
            last_reviewed = self.last_reviewed

        param: None | str
        param = self.param

        payload: None | str
        payload = self.payload

        hash_code: None | str
        hash_code = self.hash_code

        created: None | str
        if isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        scanner_confidence: int | None
        scanner_confidence = self.scanner_confidence

        test = self.test

        duplicate_finding: int | None
        duplicate_finding = self.duplicate_finding

        last_reviewed_by: int | None
        last_reviewed_by = self.last_reviewed_by

        endpoints = self.endpoints

        notes = []
        for notes_item_data in self.notes:
            notes_item = notes_item_data.to_dict()
            notes.append(notes_item)

        files = self.files

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

        active = self.active

        verified = self.verified

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

        prefetch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prefetch, Unset):
            prefetch = self.prefetch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "request_response": request_response,
                "accepted_risks": accepted_risks,
                "found_by": found_by,
                "age": age,
                "sla_days_remaining": sla_days_remaining,
                "finding_meta": finding_meta,
                "related_fields": related_fields,
                "jira_creation": jira_creation,
                "jira_change": jira_change,
                "display_status": display_status,
                "finding_groups": finding_groups,
                "title": title,
                "url": url,
                "severity": severity,
                "description": description,
                "last_status_update": last_status_update,
                "thread_id": thread_id,
                "numerical_severity": numerical_severity,
                "last_reviewed": last_reviewed,
                "param": param,
                "payload": payload,
                "hash_code": hash_code,
                "created": created,
                "scanner_confidence": scanner_confidence,
                "test": test,
                "duplicate_finding": duplicate_finding,
                "last_reviewed_by": last_reviewed_by,
                "endpoints": endpoints,
                "notes": notes,
                "files": files,
            }
        )
        if mitigated is not UNSET:
            field_dict["mitigated"] = mitigated
        if mitigated_by is not UNSET:
            field_dict["mitigated_by"] = mitigated_by
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
        if active is not UNSET:
            field_dict["active"] = active
        if verified is not UNSET:
            field_dict["verified"] = verified
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
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.burp_raw_request_response import BurpRawRequestResponse
        from ..models.finding_group import FindingGroup
        from ..models.finding_meta import FindingMeta
        from ..models.finding_prefetch import FindingPrefetch
        from ..models.finding_related_fields import FindingRelatedFields
        from ..models.note import Note
        from ..models.risk_acceptance import RiskAcceptance
        from ..models.vulnerability_id import VulnerabilityId

        d = dict(src_dict)
        id = d.pop("id")

        request_response = BurpRawRequestResponse.from_dict(d.pop("request_response"))

        accepted_risks = []
        _accepted_risks = d.pop("accepted_risks")
        for accepted_risks_item_data in _accepted_risks:
            accepted_risks_item = RiskAcceptance.from_dict(accepted_risks_item_data)

            accepted_risks.append(accepted_risks_item)

        found_by = cast(list[int], d.pop("found_by"))

        age = d.pop("age")

        def _parse_sla_days_remaining(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        sla_days_remaining = _parse_sla_days_remaining(d.pop("sla_days_remaining"))

        finding_meta = []
        _finding_meta = d.pop("finding_meta")
        for finding_meta_item_data in _finding_meta:
            finding_meta_item = FindingMeta.from_dict(finding_meta_item_data)

            finding_meta.append(finding_meta_item)

        def _parse_related_fields(data: object) -> FindingRelatedFields | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                related_fields_type_1 = FindingRelatedFields.from_dict(data)

                return related_fields_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FindingRelatedFields | None, data)

        related_fields = _parse_related_fields(d.pop("related_fields"))

        def _parse_jira_creation(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                jira_creation_type_0 = isoparse(data)

                return jira_creation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        jira_creation = _parse_jira_creation(d.pop("jira_creation"))

        def _parse_jira_change(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                jira_change_type_0 = isoparse(data)

                return jira_change_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        jira_change = _parse_jira_change(d.pop("jira_change"))

        display_status = d.pop("display_status")

        finding_groups = []
        _finding_groups = d.pop("finding_groups")
        for finding_groups_item_data in _finding_groups:
            finding_groups_item = FindingGroup.from_dict(finding_groups_item_data)

            finding_groups.append(finding_groups_item)

        title = d.pop("title")

        def _parse_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        url = _parse_url(d.pop("url"))

        severity = d.pop("severity")

        description = d.pop("description")

        def _parse_last_status_update(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_status_update_type_0 = isoparse(data)

                return last_status_update_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_status_update = _parse_last_status_update(d.pop("last_status_update"))

        thread_id = d.pop("thread_id")

        numerical_severity = d.pop("numerical_severity")

        def _parse_last_reviewed(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_reviewed_type_0 = isoparse(data)

                return last_reviewed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_reviewed = _parse_last_reviewed(d.pop("last_reviewed"))

        def _parse_param(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        param = _parse_param(d.pop("param"))

        def _parse_payload(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        payload = _parse_payload(d.pop("payload"))

        def _parse_hash_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        hash_code = _parse_hash_code(d.pop("hash_code"))

        def _parse_created(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_type_0 = isoparse(data)

                return created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        created = _parse_created(d.pop("created"))

        def _parse_scanner_confidence(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        scanner_confidence = _parse_scanner_confidence(d.pop("scanner_confidence"))

        test = d.pop("test")

        def _parse_duplicate_finding(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        duplicate_finding = _parse_duplicate_finding(d.pop("duplicate_finding"))

        def _parse_last_reviewed_by(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        last_reviewed_by = _parse_last_reviewed_by(d.pop("last_reviewed_by"))

        endpoints = cast(list[int], d.pop("endpoints"))

        notes = []
        _notes = d.pop("notes")
        for notes_item_data in _notes:
            notes_item = Note.from_dict(notes_item_data)

            notes.append(notes_item)

        files = cast(list[int], d.pop("files"))

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

        tags = cast(list[str], d.pop("tags", UNSET))

        push_to_jira = d.pop("push_to_jira", UNSET)

        _vulnerability_ids = d.pop("vulnerability_ids", UNSET)
        vulnerability_ids: list[VulnerabilityId] | Unset = UNSET
        if _vulnerability_ids is not UNSET:
            vulnerability_ids = []
            for vulnerability_ids_item_data in _vulnerability_ids:
                vulnerability_ids_item = VulnerabilityId.from_dict(vulnerability_ids_item_data)

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

        active = d.pop("active", UNSET)

        verified = d.pop("verified", UNSET)

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

        _prefetch = d.pop("prefetch", UNSET)
        prefetch: FindingPrefetch | Unset
        if isinstance(_prefetch, Unset):
            prefetch = UNSET
        else:
            prefetch = FindingPrefetch.from_dict(_prefetch)

        finding = cls(
            id=id,
            request_response=request_response,
            accepted_risks=accepted_risks,
            found_by=found_by,
            age=age,
            sla_days_remaining=sla_days_remaining,
            finding_meta=finding_meta,
            related_fields=related_fields,
            jira_creation=jira_creation,
            jira_change=jira_change,
            display_status=display_status,
            finding_groups=finding_groups,
            title=title,
            url=url,
            severity=severity,
            description=description,
            last_status_update=last_status_update,
            thread_id=thread_id,
            numerical_severity=numerical_severity,
            last_reviewed=last_reviewed,
            param=param,
            payload=payload,
            hash_code=hash_code,
            created=created,
            scanner_confidence=scanner_confidence,
            test=test,
            duplicate_finding=duplicate_finding,
            last_reviewed_by=last_reviewed_by,
            endpoints=endpoints,
            notes=notes,
            files=files,
            mitigated=mitigated,
            mitigated_by=mitigated_by,
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
            active=active,
            verified=verified,
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
            prefetch=prefetch,
        )

        finding.additional_properties = d
        return finding

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
