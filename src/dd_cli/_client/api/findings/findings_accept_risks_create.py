import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.accepted_risk_request import AcceptedRiskRequest
from ...models.findings_accept_risks_create_created_type_1 import (
    FindingsAcceptRisksCreateCreatedType1,
)
from ...models.findings_accept_risks_create_created_type_2_type_1 import (
    FindingsAcceptRisksCreateCreatedType2Type1,
)
from ...models.findings_accept_risks_create_created_type_3_type_1 import (
    FindingsAcceptRisksCreateCreatedType3Type1,
)
from ...models.findings_accept_risks_create_date_type_1 import FindingsAcceptRisksCreateDateType1
from ...models.findings_accept_risks_create_jira_creation_type_1 import (
    FindingsAcceptRisksCreateJiraCreationType1,
)
from ...models.findings_accept_risks_create_jira_creation_type_2_type_1 import (
    FindingsAcceptRisksCreateJiraCreationType2Type1,
)
from ...models.findings_accept_risks_create_jira_creation_type_3_type_1 import (
    FindingsAcceptRisksCreateJiraCreationType3Type1,
)
from ...models.findings_accept_risks_create_jira_last_update import (
    FindingsAcceptRisksCreateJiraLastUpdate,
)
from ...models.findings_accept_risks_create_last_reviewed_type_1 import (
    FindingsAcceptRisksCreateLastReviewedType1,
)
from ...models.findings_accept_risks_create_last_reviewed_type_2_type_1 import (
    FindingsAcceptRisksCreateLastReviewedType2Type1,
)
from ...models.findings_accept_risks_create_last_reviewed_type_3_type_1 import (
    FindingsAcceptRisksCreateLastReviewedType3Type1,
)
from ...models.findings_accept_risks_create_mitigated_type_1 import (
    FindingsAcceptRisksCreateMitigatedType1,
)
from ...models.findings_accept_risks_create_mitigated_type_2_type_1 import (
    FindingsAcceptRisksCreateMitigatedType2Type1,
)
from ...models.findings_accept_risks_create_mitigated_type_3_type_1 import (
    FindingsAcceptRisksCreateMitigatedType3Type1,
)
from ...models.findings_accept_risks_create_o_item import FindingsAcceptRisksCreateOItem
from ...models.paginated_risk_acceptance_list import PaginatedRiskAcceptanceList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[AcceptedRiskRequest]
    | list[AcceptedRiskRequest]
    | list[AcceptedRiskRequest]
    | Unset = UNSET,
    active: bool | Unset = UNSET,
    component_name: str | Unset = UNSET,
    component_version: str | Unset = UNSET,
    created: FindingsAcceptRisksCreateCreatedType1
    | FindingsAcceptRisksCreateCreatedType2Type1
    | FindingsAcceptRisksCreateCreatedType3Type1
    | None
    | Unset = UNSET,
    cvssv3: str | Unset = UNSET,
    cvssv3_score: float | Unset = UNSET,
    cvssv4: str | Unset = UNSET,
    cvssv4_score: float | Unset = UNSET,
    cwe: list[int] | Unset = UNSET,
    date: FindingsAcceptRisksCreateDateType1 | None | Unset = UNSET,
    defect_review_requested_by: list[int] | Unset = UNSET,
    description: str | Unset = UNSET,
    discovered_after: datetime.date | Unset = UNSET,
    discovered_before: datetime.date | Unset = UNSET,
    discovered_on: datetime.date | Unset = UNSET,
    duplicate: bool | Unset = UNSET,
    duplicate_finding: int | Unset = UNSET,
    dynamic_finding: bool | Unset = UNSET,
    effort_for_fixing: str | Unset = UNSET,
    endpoints: list[int] | Unset = UNSET,
    epss_percentile_max: float | None | Unset = UNSET,
    epss_percentile_min: float | None | Unset = UNSET,
    epss_score_max: float | None | Unset = UNSET,
    epss_score_min: float | None | Unset = UNSET,
    false_p: bool | Unset = UNSET,
    file_path: str | Unset = UNSET,
    finding_group: list[float] | Unset = UNSET,
    fix_available: bool | Unset = UNSET,
    fix_version: str | Unset = UNSET,
    found_by: list[int] | Unset = UNSET,
    has_jira: bool | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    hash_code: str | Unset = UNSET,
    id: list[int] | Unset = UNSET,
    impact: str | Unset = UNSET,
    inherited_tags: list[list[int]] | Unset = UNSET,
    is_mitigated: bool | Unset = UNSET,
    jira_change: FindingsAcceptRisksCreateJiraLastUpdate | None | Unset = UNSET,
    jira_creation: FindingsAcceptRisksCreateJiraCreationType1
    | FindingsAcceptRisksCreateJiraCreationType2Type1
    | FindingsAcceptRisksCreateJiraCreationType3Type1
    | None
    | Unset = UNSET,
    kev_date: datetime.date | Unset = UNSET,
    known_exploited: bool | Unset = UNSET,
    last_reviewed: FindingsAcceptRisksCreateLastReviewedType1
    | FindingsAcceptRisksCreateLastReviewedType2Type1
    | FindingsAcceptRisksCreateLastReviewedType3Type1
    | None
    | Unset = UNSET,
    last_reviewed_by: list[int] | Unset = UNSET,
    last_status_update: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    mitigated: FindingsAcceptRisksCreateMitigatedType1
    | FindingsAcceptRisksCreateMitigatedType2Type1
    | FindingsAcceptRisksCreateMitigatedType3Type1
    | None
    | Unset = UNSET,
    mitigated_after: datetime.datetime | Unset = UNSET,
    mitigated_before: datetime.datetime | Unset = UNSET,
    mitigated_by: list[int] | Unset = UNSET,
    mitigated_on: datetime.datetime | Unset = UNSET,
    mitigation: str | Unset = UNSET,
    nb_occurences: list[int] | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    not_test_engagement_product_tags: list[str] | Unset = UNSET,
    not_test_engagement_tags: list[str] | Unset = UNSET,
    not_test_tags: list[str] | Unset = UNSET,
    numerical_severity: str | Unset = UNSET,
    o: list[FindingsAcceptRisksCreateOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    out_of_scope: bool | Unset = UNSET,
    outside_of_sla: float | Unset = UNSET,
    param: str | Unset = UNSET,
    payload: str | Unset = UNSET,
    planned_remediation_date: datetime.date | Unset = UNSET,
    planned_remediation_version: str | Unset = UNSET,
    product_lifecycle: str | Unset = UNSET,
    product_name: str | Unset = UNSET,
    product_name_contains: str | Unset = UNSET,
    publish_date: datetime.date | Unset = UNSET,
    ransomware_used: bool | Unset = UNSET,
    references: str | Unset = UNSET,
    reporter: list[int] | Unset = UNSET,
    review_requested_by: list[int] | Unset = UNSET,
    reviewers: list[int] | Unset = UNSET,
    risk_acceptance: float | Unset = UNSET,
    risk_accepted: bool | Unset = UNSET,
    sast_sink_object: str | Unset = UNSET,
    sast_source_file_path: str | Unset = UNSET,
    sast_source_line: list[int] | Unset = UNSET,
    sast_source_object: str | Unset = UNSET,
    scanner_confidence: list[int] | Unset = UNSET,
    service: str | Unset = UNSET,
    severity: str | Unset = UNSET,
    severity_justification: str | Unset = UNSET,
    sla_expiration_date: datetime.date | Unset = UNSET,
    sla_start_date: datetime.date | Unset = UNSET,
    sonarqube_issue: list[int] | Unset = UNSET,
    static_finding: bool | Unset = UNSET,
    steps_to_reproduce: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    test: int | Unset = UNSET,
    test_engagement: list[int] | Unset = UNSET,
    test_engagement_product: list[int] | Unset = UNSET,
    test_engagement_product_prod_type: list[int] | Unset = UNSET,
    test_engagement_product_tags: list[str] | Unset = UNSET,
    test_engagement_product_tags_and: list[str] | Unset = UNSET,
    test_engagement_tags: list[str] | Unset = UNSET,
    test_engagement_tags_and: list[str] | Unset = UNSET,
    test_tags: list[str] | Unset = UNSET,
    test_tags_and: list[str] | Unset = UNSET,
    test_test_type: list[int] | Unset = UNSET,
    title: str | Unset = UNSET,
    under_defect_review: bool | Unset = UNSET,
    under_review: bool | Unset = UNSET,
    unique_id_from_tool: str | Unset = UNSET,
    verified: bool | Unset = UNSET,
    vuln_id_from_tool: str | Unset = UNSET,
    vulnerability_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["active"] = active

    params["component_name"] = component_name

    params["component_version"] = component_version

    json_created: int | None | Unset
    if isinstance(created, Unset):
        json_created = UNSET
    elif (
        isinstance(created, FindingsAcceptRisksCreateCreatedType1)
        or isinstance(created, FindingsAcceptRisksCreateCreatedType2Type1)
        or isinstance(created, FindingsAcceptRisksCreateCreatedType3Type1)
    ):
        json_created = created.value
    else:
        json_created = created
    params["created"] = json_created

    params["cvssv3"] = cvssv3

    params["cvssv3_score"] = cvssv3_score

    params["cvssv4"] = cvssv4

    params["cvssv4_score"] = cvssv4_score

    json_cwe: list[int] | Unset = UNSET
    if not isinstance(cwe, Unset):
        json_cwe = cwe

    params["cwe"] = json_cwe

    json_date: int | None | Unset
    if isinstance(date, Unset):
        json_date = UNSET
    elif isinstance(date, FindingsAcceptRisksCreateDateType1):
        json_date = date.value
    else:
        json_date = date
    params["date"] = json_date

    json_defect_review_requested_by: list[int] | Unset = UNSET
    if not isinstance(defect_review_requested_by, Unset):
        json_defect_review_requested_by = defect_review_requested_by

    params["defect_review_requested_by"] = json_defect_review_requested_by

    params["description"] = description

    json_discovered_after: str | Unset = UNSET
    if not isinstance(discovered_after, Unset):
        json_discovered_after = discovered_after.isoformat()
    params["discovered_after"] = json_discovered_after

    json_discovered_before: str | Unset = UNSET
    if not isinstance(discovered_before, Unset):
        json_discovered_before = discovered_before.isoformat()
    params["discovered_before"] = json_discovered_before

    json_discovered_on: str | Unset = UNSET
    if not isinstance(discovered_on, Unset):
        json_discovered_on = discovered_on.isoformat()
    params["discovered_on"] = json_discovered_on

    params["duplicate"] = duplicate

    params["duplicate_finding"] = duplicate_finding

    params["dynamic_finding"] = dynamic_finding

    params["effort_for_fixing"] = effort_for_fixing

    json_endpoints: list[int] | Unset = UNSET
    if not isinstance(endpoints, Unset):
        json_endpoints = endpoints

    params["endpoints"] = json_endpoints

    json_epss_percentile_max: float | None | Unset
    if isinstance(epss_percentile_max, Unset):
        json_epss_percentile_max = UNSET
    else:
        json_epss_percentile_max = epss_percentile_max
    params["epss_percentile_max"] = json_epss_percentile_max

    json_epss_percentile_min: float | None | Unset
    if isinstance(epss_percentile_min, Unset):
        json_epss_percentile_min = UNSET
    else:
        json_epss_percentile_min = epss_percentile_min
    params["epss_percentile_min"] = json_epss_percentile_min

    json_epss_score_max: float | None | Unset
    if isinstance(epss_score_max, Unset):
        json_epss_score_max = UNSET
    else:
        json_epss_score_max = epss_score_max
    params["epss_score_max"] = json_epss_score_max

    json_epss_score_min: float | None | Unset
    if isinstance(epss_score_min, Unset):
        json_epss_score_min = UNSET
    else:
        json_epss_score_min = epss_score_min
    params["epss_score_min"] = json_epss_score_min

    params["false_p"] = false_p

    params["file_path"] = file_path

    json_finding_group: list[float] | Unset = UNSET
    if not isinstance(finding_group, Unset):
        json_finding_group = finding_group

    params["finding_group"] = json_finding_group

    params["fix_available"] = fix_available

    params["fix_version"] = fix_version

    json_found_by: list[int] | Unset = UNSET
    if not isinstance(found_by, Unset):
        json_found_by = found_by

    params["found_by"] = json_found_by

    params["has_jira"] = has_jira

    params["has_tags"] = has_tags

    params["hash_code"] = hash_code

    json_id: list[int] | Unset = UNSET
    if not isinstance(id, Unset):
        json_id = id

    params["id"] = json_id

    params["impact"] = impact

    json_inherited_tags: list[list[int]] | Unset = UNSET
    if not isinstance(inherited_tags, Unset):
        json_inherited_tags = []
        for inherited_tags_item_data in inherited_tags:
            inherited_tags_item = inherited_tags_item_data

            json_inherited_tags.append(inherited_tags_item)

    params["inherited_tags"] = json_inherited_tags

    params["is_mitigated"] = is_mitigated

    json_jira_change: int | None | Unset
    if isinstance(jira_change, Unset):
        json_jira_change = UNSET
    elif isinstance(jira_change, FindingsAcceptRisksCreateJiraLastUpdate):
        json_jira_change = jira_change.value
    else:
        json_jira_change = jira_change
    params["jira_change"] = json_jira_change

    json_jira_creation: int | None | Unset
    if isinstance(jira_creation, Unset):
        json_jira_creation = UNSET
    elif (
        isinstance(jira_creation, FindingsAcceptRisksCreateJiraCreationType1)
        or isinstance(jira_creation, FindingsAcceptRisksCreateJiraCreationType2Type1)
        or isinstance(jira_creation, FindingsAcceptRisksCreateJiraCreationType3Type1)
    ):
        json_jira_creation = jira_creation.value
    else:
        json_jira_creation = jira_creation
    params["jira_creation"] = json_jira_creation

    json_kev_date: str | Unset = UNSET
    if not isinstance(kev_date, Unset):
        json_kev_date = kev_date.isoformat()
    params["kev_date"] = json_kev_date

    params["known_exploited"] = known_exploited

    json_last_reviewed: int | None | Unset
    if isinstance(last_reviewed, Unset):
        json_last_reviewed = UNSET
    elif (
        isinstance(last_reviewed, FindingsAcceptRisksCreateLastReviewedType1)
        or isinstance(last_reviewed, FindingsAcceptRisksCreateLastReviewedType2Type1)
        or isinstance(last_reviewed, FindingsAcceptRisksCreateLastReviewedType3Type1)
    ):
        json_last_reviewed = last_reviewed.value
    else:
        json_last_reviewed = last_reviewed
    params["last_reviewed"] = json_last_reviewed

    json_last_reviewed_by: list[int] | Unset = UNSET
    if not isinstance(last_reviewed_by, Unset):
        json_last_reviewed_by = last_reviewed_by

    params["last_reviewed_by"] = json_last_reviewed_by

    json_last_status_update: str | Unset = UNSET
    if not isinstance(last_status_update, Unset):
        json_last_status_update = last_status_update.isoformat()
    params["last_status_update"] = json_last_status_update

    params["limit"] = limit

    json_mitigated: int | None | Unset
    if isinstance(mitigated, Unset):
        json_mitigated = UNSET
    elif (
        isinstance(mitigated, FindingsAcceptRisksCreateMitigatedType1)
        or isinstance(mitigated, FindingsAcceptRisksCreateMitigatedType2Type1)
        or isinstance(mitigated, FindingsAcceptRisksCreateMitigatedType3Type1)
    ):
        json_mitigated = mitigated.value
    else:
        json_mitigated = mitigated
    params["mitigated"] = json_mitigated

    json_mitigated_after: str | Unset = UNSET
    if not isinstance(mitigated_after, Unset):
        json_mitigated_after = mitigated_after.isoformat()
    params["mitigated_after"] = json_mitigated_after

    json_mitigated_before: str | Unset = UNSET
    if not isinstance(mitigated_before, Unset):
        json_mitigated_before = mitigated_before.isoformat()
    params["mitigated_before"] = json_mitigated_before

    json_mitigated_by: list[int] | Unset = UNSET
    if not isinstance(mitigated_by, Unset):
        json_mitigated_by = mitigated_by

    params["mitigated_by"] = json_mitigated_by

    json_mitigated_on: str | Unset = UNSET
    if not isinstance(mitigated_on, Unset):
        json_mitigated_on = mitigated_on.isoformat()
    params["mitigated_on"] = json_mitigated_on

    params["mitigation"] = mitigation

    json_nb_occurences: list[int] | Unset = UNSET
    if not isinstance(nb_occurences, Unset):
        json_nb_occurences = nb_occurences

    params["nb_occurences"] = json_nb_occurences

    params["not_tag"] = not_tag

    json_not_tags: list[str] | Unset = UNSET
    if not isinstance(not_tags, Unset):
        json_not_tags = not_tags

    params["not_tags"] = json_not_tags

    json_not_test_engagement_product_tags: list[str] | Unset = UNSET
    if not isinstance(not_test_engagement_product_tags, Unset):
        json_not_test_engagement_product_tags = not_test_engagement_product_tags

    params["not_test__engagement__product__tags"] = json_not_test_engagement_product_tags

    json_not_test_engagement_tags: list[str] | Unset = UNSET
    if not isinstance(not_test_engagement_tags, Unset):
        json_not_test_engagement_tags = not_test_engagement_tags

    params["not_test__engagement__tags"] = json_not_test_engagement_tags

    json_not_test_tags: list[str] | Unset = UNSET
    if not isinstance(not_test_tags, Unset):
        json_not_test_tags = not_test_tags

    params["not_test__tags"] = json_not_test_tags

    params["numerical_severity"] = numerical_severity

    json_o: list[str] | Unset = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    params["offset"] = offset

    params["out_of_scope"] = out_of_scope

    params["outside_of_sla"] = outside_of_sla

    params["param"] = param

    params["payload"] = payload

    json_planned_remediation_date: str | Unset = UNSET
    if not isinstance(planned_remediation_date, Unset):
        json_planned_remediation_date = planned_remediation_date.isoformat()
    params["planned_remediation_date"] = json_planned_remediation_date

    params["planned_remediation_version"] = planned_remediation_version

    params["product_lifecycle"] = product_lifecycle

    params["product_name"] = product_name

    params["product_name_contains"] = product_name_contains

    json_publish_date: str | Unset = UNSET
    if not isinstance(publish_date, Unset):
        json_publish_date = publish_date.isoformat()
    params["publish_date"] = json_publish_date

    params["ransomware_used"] = ransomware_used

    params["references"] = references

    json_reporter: list[int] | Unset = UNSET
    if not isinstance(reporter, Unset):
        json_reporter = reporter

    params["reporter"] = json_reporter

    json_review_requested_by: list[int] | Unset = UNSET
    if not isinstance(review_requested_by, Unset):
        json_review_requested_by = review_requested_by

    params["review_requested_by"] = json_review_requested_by

    json_reviewers: list[int] | Unset = UNSET
    if not isinstance(reviewers, Unset):
        json_reviewers = reviewers

    params["reviewers"] = json_reviewers

    params["risk_acceptance"] = risk_acceptance

    params["risk_accepted"] = risk_accepted

    params["sast_sink_object"] = sast_sink_object

    params["sast_source_file_path"] = sast_source_file_path

    json_sast_source_line: list[int] | Unset = UNSET
    if not isinstance(sast_source_line, Unset):
        json_sast_source_line = sast_source_line

    params["sast_source_line"] = json_sast_source_line

    params["sast_source_object"] = sast_source_object

    json_scanner_confidence: list[int] | Unset = UNSET
    if not isinstance(scanner_confidence, Unset):
        json_scanner_confidence = scanner_confidence

    params["scanner_confidence"] = json_scanner_confidence

    params["service"] = service

    params["severity"] = severity

    params["severity_justification"] = severity_justification

    json_sla_expiration_date: str | Unset = UNSET
    if not isinstance(sla_expiration_date, Unset):
        json_sla_expiration_date = sla_expiration_date.isoformat()
    params["sla_expiration_date"] = json_sla_expiration_date

    json_sla_start_date: str | Unset = UNSET
    if not isinstance(sla_start_date, Unset):
        json_sla_start_date = sla_start_date.isoformat()
    params["sla_start_date"] = json_sla_start_date

    json_sonarqube_issue: list[int] | Unset = UNSET
    if not isinstance(sonarqube_issue, Unset):
        json_sonarqube_issue = sonarqube_issue

    params["sonarqube_issue"] = json_sonarqube_issue

    params["static_finding"] = static_finding

    params["steps_to_reproduce"] = steps_to_reproduce

    params["tag"] = tag

    json_tags: list[str] | Unset = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    json_tags_and: list[str] | Unset = UNSET
    if not isinstance(tags_and, Unset):
        json_tags_and = tags_and

    params["tags__and"] = json_tags_and

    params["test"] = test

    json_test_engagement: list[int] | Unset = UNSET
    if not isinstance(test_engagement, Unset):
        json_test_engagement = test_engagement

    params["test__engagement"] = json_test_engagement

    json_test_engagement_product: list[int] | Unset = UNSET
    if not isinstance(test_engagement_product, Unset):
        json_test_engagement_product = test_engagement_product

    params["test__engagement__product"] = json_test_engagement_product

    json_test_engagement_product_prod_type: list[int] | Unset = UNSET
    if not isinstance(test_engagement_product_prod_type, Unset):
        json_test_engagement_product_prod_type = test_engagement_product_prod_type

    params["test__engagement__product__prod_type"] = json_test_engagement_product_prod_type

    json_test_engagement_product_tags: list[str] | Unset = UNSET
    if not isinstance(test_engagement_product_tags, Unset):
        json_test_engagement_product_tags = test_engagement_product_tags

    params["test__engagement__product__tags"] = json_test_engagement_product_tags

    json_test_engagement_product_tags_and: list[str] | Unset = UNSET
    if not isinstance(test_engagement_product_tags_and, Unset):
        json_test_engagement_product_tags_and = test_engagement_product_tags_and

    params["test__engagement__product__tags__and"] = json_test_engagement_product_tags_and

    json_test_engagement_tags: list[str] | Unset = UNSET
    if not isinstance(test_engagement_tags, Unset):
        json_test_engagement_tags = test_engagement_tags

    params["test__engagement__tags"] = json_test_engagement_tags

    json_test_engagement_tags_and: list[str] | Unset = UNSET
    if not isinstance(test_engagement_tags_and, Unset):
        json_test_engagement_tags_and = test_engagement_tags_and

    params["test__engagement__tags__and"] = json_test_engagement_tags_and

    json_test_tags: list[str] | Unset = UNSET
    if not isinstance(test_tags, Unset):
        json_test_tags = test_tags

    params["test__tags"] = json_test_tags

    json_test_tags_and: list[str] | Unset = UNSET
    if not isinstance(test_tags_and, Unset):
        json_test_tags_and = test_tags_and

    params["test__tags__and"] = json_test_tags_and

    json_test_test_type: list[int] | Unset = UNSET
    if not isinstance(test_test_type, Unset):
        json_test_test_type = test_test_type

    params["test__test_type"] = json_test_test_type

    params["title"] = title

    params["under_defect_review"] = under_defect_review

    params["under_review"] = under_review

    params["unique_id_from_tool"] = unique_id_from_tool

    params["verified"] = verified

    params["vuln_id_from_tool"] = vuln_id_from_tool

    params["vulnerability_id"] = vulnerability_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/findings/accept_risks/",
        "params": params,
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
) -> PaginatedRiskAcceptanceList | None:
    if response.status_code == 201:
        response_201 = PaginatedRiskAcceptanceList.from_dict(response.json())

        return response_201

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
    body: list[AcceptedRiskRequest]
    | list[AcceptedRiskRequest]
    | list[AcceptedRiskRequest]
    | Unset = UNSET,
    active: bool | Unset = UNSET,
    component_name: str | Unset = UNSET,
    component_version: str | Unset = UNSET,
    created: FindingsAcceptRisksCreateCreatedType1
    | FindingsAcceptRisksCreateCreatedType2Type1
    | FindingsAcceptRisksCreateCreatedType3Type1
    | None
    | Unset = UNSET,
    cvssv3: str | Unset = UNSET,
    cvssv3_score: float | Unset = UNSET,
    cvssv4: str | Unset = UNSET,
    cvssv4_score: float | Unset = UNSET,
    cwe: list[int] | Unset = UNSET,
    date: FindingsAcceptRisksCreateDateType1 | None | Unset = UNSET,
    defect_review_requested_by: list[int] | Unset = UNSET,
    description: str | Unset = UNSET,
    discovered_after: datetime.date | Unset = UNSET,
    discovered_before: datetime.date | Unset = UNSET,
    discovered_on: datetime.date | Unset = UNSET,
    duplicate: bool | Unset = UNSET,
    duplicate_finding: int | Unset = UNSET,
    dynamic_finding: bool | Unset = UNSET,
    effort_for_fixing: str | Unset = UNSET,
    endpoints: list[int] | Unset = UNSET,
    epss_percentile_max: float | None | Unset = UNSET,
    epss_percentile_min: float | None | Unset = UNSET,
    epss_score_max: float | None | Unset = UNSET,
    epss_score_min: float | None | Unset = UNSET,
    false_p: bool | Unset = UNSET,
    file_path: str | Unset = UNSET,
    finding_group: list[float] | Unset = UNSET,
    fix_available: bool | Unset = UNSET,
    fix_version: str | Unset = UNSET,
    found_by: list[int] | Unset = UNSET,
    has_jira: bool | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    hash_code: str | Unset = UNSET,
    id: list[int] | Unset = UNSET,
    impact: str | Unset = UNSET,
    inherited_tags: list[list[int]] | Unset = UNSET,
    is_mitigated: bool | Unset = UNSET,
    jira_change: FindingsAcceptRisksCreateJiraLastUpdate | None | Unset = UNSET,
    jira_creation: FindingsAcceptRisksCreateJiraCreationType1
    | FindingsAcceptRisksCreateJiraCreationType2Type1
    | FindingsAcceptRisksCreateJiraCreationType3Type1
    | None
    | Unset = UNSET,
    kev_date: datetime.date | Unset = UNSET,
    known_exploited: bool | Unset = UNSET,
    last_reviewed: FindingsAcceptRisksCreateLastReviewedType1
    | FindingsAcceptRisksCreateLastReviewedType2Type1
    | FindingsAcceptRisksCreateLastReviewedType3Type1
    | None
    | Unset = UNSET,
    last_reviewed_by: list[int] | Unset = UNSET,
    last_status_update: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    mitigated: FindingsAcceptRisksCreateMitigatedType1
    | FindingsAcceptRisksCreateMitigatedType2Type1
    | FindingsAcceptRisksCreateMitigatedType3Type1
    | None
    | Unset = UNSET,
    mitigated_after: datetime.datetime | Unset = UNSET,
    mitigated_before: datetime.datetime | Unset = UNSET,
    mitigated_by: list[int] | Unset = UNSET,
    mitigated_on: datetime.datetime | Unset = UNSET,
    mitigation: str | Unset = UNSET,
    nb_occurences: list[int] | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    not_test_engagement_product_tags: list[str] | Unset = UNSET,
    not_test_engagement_tags: list[str] | Unset = UNSET,
    not_test_tags: list[str] | Unset = UNSET,
    numerical_severity: str | Unset = UNSET,
    o: list[FindingsAcceptRisksCreateOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    out_of_scope: bool | Unset = UNSET,
    outside_of_sla: float | Unset = UNSET,
    param: str | Unset = UNSET,
    payload: str | Unset = UNSET,
    planned_remediation_date: datetime.date | Unset = UNSET,
    planned_remediation_version: str | Unset = UNSET,
    product_lifecycle: str | Unset = UNSET,
    product_name: str | Unset = UNSET,
    product_name_contains: str | Unset = UNSET,
    publish_date: datetime.date | Unset = UNSET,
    ransomware_used: bool | Unset = UNSET,
    references: str | Unset = UNSET,
    reporter: list[int] | Unset = UNSET,
    review_requested_by: list[int] | Unset = UNSET,
    reviewers: list[int] | Unset = UNSET,
    risk_acceptance: float | Unset = UNSET,
    risk_accepted: bool | Unset = UNSET,
    sast_sink_object: str | Unset = UNSET,
    sast_source_file_path: str | Unset = UNSET,
    sast_source_line: list[int] | Unset = UNSET,
    sast_source_object: str | Unset = UNSET,
    scanner_confidence: list[int] | Unset = UNSET,
    service: str | Unset = UNSET,
    severity: str | Unset = UNSET,
    severity_justification: str | Unset = UNSET,
    sla_expiration_date: datetime.date | Unset = UNSET,
    sla_start_date: datetime.date | Unset = UNSET,
    sonarqube_issue: list[int] | Unset = UNSET,
    static_finding: bool | Unset = UNSET,
    steps_to_reproduce: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    test: int | Unset = UNSET,
    test_engagement: list[int] | Unset = UNSET,
    test_engagement_product: list[int] | Unset = UNSET,
    test_engagement_product_prod_type: list[int] | Unset = UNSET,
    test_engagement_product_tags: list[str] | Unset = UNSET,
    test_engagement_product_tags_and: list[str] | Unset = UNSET,
    test_engagement_tags: list[str] | Unset = UNSET,
    test_engagement_tags_and: list[str] | Unset = UNSET,
    test_tags: list[str] | Unset = UNSET,
    test_tags_and: list[str] | Unset = UNSET,
    test_test_type: list[int] | Unset = UNSET,
    title: str | Unset = UNSET,
    under_defect_review: bool | Unset = UNSET,
    under_review: bool | Unset = UNSET,
    unique_id_from_tool: str | Unset = UNSET,
    verified: bool | Unset = UNSET,
    vuln_id_from_tool: str | Unset = UNSET,
    vulnerability_id: str | Unset = UNSET,
) -> Response[PaginatedRiskAcceptanceList]:
    """
    Args:
        active (bool | Unset):
        component_name (str | Unset):
        component_version (str | Unset):
        created (FindingsAcceptRisksCreateCreatedType1 |
            FindingsAcceptRisksCreateCreatedType2Type1 | FindingsAcceptRisksCreateCreatedType3Type1 |
            None | Unset):
        cvssv3 (str | Unset):
        cvssv3_score (float | Unset):
        cvssv4 (str | Unset):
        cvssv4_score (float | Unset):
        cwe (list[int] | Unset):
        date (FindingsAcceptRisksCreateDateType1 | None | Unset):
        defect_review_requested_by (list[int] | Unset):
        description (str | Unset):
        discovered_after (datetime.date | Unset):
        discovered_before (datetime.date | Unset):
        discovered_on (datetime.date | Unset):
        duplicate (bool | Unset):
        duplicate_finding (int | Unset):
        dynamic_finding (bool | Unset):
        effort_for_fixing (str | Unset):
        endpoints (list[int] | Unset):
        epss_percentile_max (float | None | Unset):
        epss_percentile_min (float | None | Unset):
        epss_score_max (float | None | Unset):
        epss_score_min (float | None | Unset):
        false_p (bool | Unset):
        file_path (str | Unset):
        finding_group (list[float] | Unset):
        fix_available (bool | Unset):
        fix_version (str | Unset):
        found_by (list[int] | Unset):
        has_jira (bool | Unset):
        has_tags (bool | Unset):
        hash_code (str | Unset):
        id (list[int] | Unset):
        impact (str | Unset):
        inherited_tags (list[list[int]] | Unset):
        is_mitigated (bool | Unset):
        jira_change (FindingsAcceptRisksCreateJiraLastUpdate | None | Unset):
        jira_creation (FindingsAcceptRisksCreateJiraCreationType1 |
            FindingsAcceptRisksCreateJiraCreationType2Type1 |
            FindingsAcceptRisksCreateJiraCreationType3Type1 | None | Unset):
        kev_date (datetime.date | Unset):
        known_exploited (bool | Unset):
        last_reviewed (FindingsAcceptRisksCreateLastReviewedType1 |
            FindingsAcceptRisksCreateLastReviewedType2Type1 |
            FindingsAcceptRisksCreateLastReviewedType3Type1 | None | Unset):
        last_reviewed_by (list[int] | Unset):
        last_status_update (datetime.datetime | Unset):
        limit (int | Unset):
        mitigated (FindingsAcceptRisksCreateMitigatedType1 |
            FindingsAcceptRisksCreateMitigatedType2Type1 |
            FindingsAcceptRisksCreateMitigatedType3Type1 | None | Unset):
        mitigated_after (datetime.datetime | Unset):
        mitigated_before (datetime.datetime | Unset):
        mitigated_by (list[int] | Unset):
        mitigated_on (datetime.datetime | Unset):
        mitigation (str | Unset):
        nb_occurences (list[int] | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        not_test_engagement_product_tags (list[str] | Unset):
        not_test_engagement_tags (list[str] | Unset):
        not_test_tags (list[str] | Unset):
        numerical_severity (str | Unset):
        o (list[FindingsAcceptRisksCreateOItem] | Unset):
        offset (int | Unset):
        out_of_scope (bool | Unset):
        outside_of_sla (float | Unset):
        param (str | Unset):
        payload (str | Unset):
        planned_remediation_date (datetime.date | Unset):
        planned_remediation_version (str | Unset):
        product_lifecycle (str | Unset):
        product_name (str | Unset):
        product_name_contains (str | Unset):
        publish_date (datetime.date | Unset):
        ransomware_used (bool | Unset):
        references (str | Unset):
        reporter (list[int] | Unset):
        review_requested_by (list[int] | Unset):
        reviewers (list[int] | Unset):
        risk_acceptance (float | Unset):
        risk_accepted (bool | Unset):
        sast_sink_object (str | Unset):
        sast_source_file_path (str | Unset):
        sast_source_line (list[int] | Unset):
        sast_source_object (str | Unset):
        scanner_confidence (list[int] | Unset):
        service (str | Unset):
        severity (str | Unset):
        severity_justification (str | Unset):
        sla_expiration_date (datetime.date | Unset):
        sla_start_date (datetime.date | Unset):
        sonarqube_issue (list[int] | Unset):
        static_finding (bool | Unset):
        steps_to_reproduce (str | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        test (int | Unset):
        test_engagement (list[int] | Unset):
        test_engagement_product (list[int] | Unset):
        test_engagement_product_prod_type (list[int] | Unset):
        test_engagement_product_tags (list[str] | Unset):
        test_engagement_product_tags_and (list[str] | Unset):
        test_engagement_tags (list[str] | Unset):
        test_engagement_tags_and (list[str] | Unset):
        test_tags (list[str] | Unset):
        test_tags_and (list[str] | Unset):
        test_test_type (list[int] | Unset):
        title (str | Unset):
        under_defect_review (bool | Unset):
        under_review (bool | Unset):
        unique_id_from_tool (str | Unset):
        verified (bool | Unset):
        vuln_id_from_tool (str | Unset):
        vulnerability_id (str | Unset):
        body (list[AcceptedRiskRequest]):
        body (list[AcceptedRiskRequest]):
        body (list[AcceptedRiskRequest]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRiskAcceptanceList]
    """

    kwargs = _get_kwargs(
        body=body,
        active=active,
        component_name=component_name,
        component_version=component_version,
        created=created,
        cvssv3=cvssv3,
        cvssv3_score=cvssv3_score,
        cvssv4=cvssv4,
        cvssv4_score=cvssv4_score,
        cwe=cwe,
        date=date,
        defect_review_requested_by=defect_review_requested_by,
        description=description,
        discovered_after=discovered_after,
        discovered_before=discovered_before,
        discovered_on=discovered_on,
        duplicate=duplicate,
        duplicate_finding=duplicate_finding,
        dynamic_finding=dynamic_finding,
        effort_for_fixing=effort_for_fixing,
        endpoints=endpoints,
        epss_percentile_max=epss_percentile_max,
        epss_percentile_min=epss_percentile_min,
        epss_score_max=epss_score_max,
        epss_score_min=epss_score_min,
        false_p=false_p,
        file_path=file_path,
        finding_group=finding_group,
        fix_available=fix_available,
        fix_version=fix_version,
        found_by=found_by,
        has_jira=has_jira,
        has_tags=has_tags,
        hash_code=hash_code,
        id=id,
        impact=impact,
        inherited_tags=inherited_tags,
        is_mitigated=is_mitigated,
        jira_change=jira_change,
        jira_creation=jira_creation,
        kev_date=kev_date,
        known_exploited=known_exploited,
        last_reviewed=last_reviewed,
        last_reviewed_by=last_reviewed_by,
        last_status_update=last_status_update,
        limit=limit,
        mitigated=mitigated,
        mitigated_after=mitigated_after,
        mitigated_before=mitigated_before,
        mitigated_by=mitigated_by,
        mitigated_on=mitigated_on,
        mitigation=mitigation,
        nb_occurences=nb_occurences,
        not_tag=not_tag,
        not_tags=not_tags,
        not_test_engagement_product_tags=not_test_engagement_product_tags,
        not_test_engagement_tags=not_test_engagement_tags,
        not_test_tags=not_test_tags,
        numerical_severity=numerical_severity,
        o=o,
        offset=offset,
        out_of_scope=out_of_scope,
        outside_of_sla=outside_of_sla,
        param=param,
        payload=payload,
        planned_remediation_date=planned_remediation_date,
        planned_remediation_version=planned_remediation_version,
        product_lifecycle=product_lifecycle,
        product_name=product_name,
        product_name_contains=product_name_contains,
        publish_date=publish_date,
        ransomware_used=ransomware_used,
        references=references,
        reporter=reporter,
        review_requested_by=review_requested_by,
        reviewers=reviewers,
        risk_acceptance=risk_acceptance,
        risk_accepted=risk_accepted,
        sast_sink_object=sast_sink_object,
        sast_source_file_path=sast_source_file_path,
        sast_source_line=sast_source_line,
        sast_source_object=sast_source_object,
        scanner_confidence=scanner_confidence,
        service=service,
        severity=severity,
        severity_justification=severity_justification,
        sla_expiration_date=sla_expiration_date,
        sla_start_date=sla_start_date,
        sonarqube_issue=sonarqube_issue,
        static_finding=static_finding,
        steps_to_reproduce=steps_to_reproduce,
        tag=tag,
        tags=tags,
        tags_and=tags_and,
        test=test,
        test_engagement=test_engagement,
        test_engagement_product=test_engagement_product,
        test_engagement_product_prod_type=test_engagement_product_prod_type,
        test_engagement_product_tags=test_engagement_product_tags,
        test_engagement_product_tags_and=test_engagement_product_tags_and,
        test_engagement_tags=test_engagement_tags,
        test_engagement_tags_and=test_engagement_tags_and,
        test_tags=test_tags,
        test_tags_and=test_tags_and,
        test_test_type=test_test_type,
        title=title,
        under_defect_review=under_defect_review,
        under_review=under_review,
        unique_id_from_tool=unique_id_from_tool,
        verified=verified,
        vuln_id_from_tool=vuln_id_from_tool,
        vulnerability_id=vulnerability_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: list[AcceptedRiskRequest]
    | list[AcceptedRiskRequest]
    | list[AcceptedRiskRequest]
    | Unset = UNSET,
    active: bool | Unset = UNSET,
    component_name: str | Unset = UNSET,
    component_version: str | Unset = UNSET,
    created: FindingsAcceptRisksCreateCreatedType1
    | FindingsAcceptRisksCreateCreatedType2Type1
    | FindingsAcceptRisksCreateCreatedType3Type1
    | None
    | Unset = UNSET,
    cvssv3: str | Unset = UNSET,
    cvssv3_score: float | Unset = UNSET,
    cvssv4: str | Unset = UNSET,
    cvssv4_score: float | Unset = UNSET,
    cwe: list[int] | Unset = UNSET,
    date: FindingsAcceptRisksCreateDateType1 | None | Unset = UNSET,
    defect_review_requested_by: list[int] | Unset = UNSET,
    description: str | Unset = UNSET,
    discovered_after: datetime.date | Unset = UNSET,
    discovered_before: datetime.date | Unset = UNSET,
    discovered_on: datetime.date | Unset = UNSET,
    duplicate: bool | Unset = UNSET,
    duplicate_finding: int | Unset = UNSET,
    dynamic_finding: bool | Unset = UNSET,
    effort_for_fixing: str | Unset = UNSET,
    endpoints: list[int] | Unset = UNSET,
    epss_percentile_max: float | None | Unset = UNSET,
    epss_percentile_min: float | None | Unset = UNSET,
    epss_score_max: float | None | Unset = UNSET,
    epss_score_min: float | None | Unset = UNSET,
    false_p: bool | Unset = UNSET,
    file_path: str | Unset = UNSET,
    finding_group: list[float] | Unset = UNSET,
    fix_available: bool | Unset = UNSET,
    fix_version: str | Unset = UNSET,
    found_by: list[int] | Unset = UNSET,
    has_jira: bool | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    hash_code: str | Unset = UNSET,
    id: list[int] | Unset = UNSET,
    impact: str | Unset = UNSET,
    inherited_tags: list[list[int]] | Unset = UNSET,
    is_mitigated: bool | Unset = UNSET,
    jira_change: FindingsAcceptRisksCreateJiraLastUpdate | None | Unset = UNSET,
    jira_creation: FindingsAcceptRisksCreateJiraCreationType1
    | FindingsAcceptRisksCreateJiraCreationType2Type1
    | FindingsAcceptRisksCreateJiraCreationType3Type1
    | None
    | Unset = UNSET,
    kev_date: datetime.date | Unset = UNSET,
    known_exploited: bool | Unset = UNSET,
    last_reviewed: FindingsAcceptRisksCreateLastReviewedType1
    | FindingsAcceptRisksCreateLastReviewedType2Type1
    | FindingsAcceptRisksCreateLastReviewedType3Type1
    | None
    | Unset = UNSET,
    last_reviewed_by: list[int] | Unset = UNSET,
    last_status_update: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    mitigated: FindingsAcceptRisksCreateMitigatedType1
    | FindingsAcceptRisksCreateMitigatedType2Type1
    | FindingsAcceptRisksCreateMitigatedType3Type1
    | None
    | Unset = UNSET,
    mitigated_after: datetime.datetime | Unset = UNSET,
    mitigated_before: datetime.datetime | Unset = UNSET,
    mitigated_by: list[int] | Unset = UNSET,
    mitigated_on: datetime.datetime | Unset = UNSET,
    mitigation: str | Unset = UNSET,
    nb_occurences: list[int] | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    not_test_engagement_product_tags: list[str] | Unset = UNSET,
    not_test_engagement_tags: list[str] | Unset = UNSET,
    not_test_tags: list[str] | Unset = UNSET,
    numerical_severity: str | Unset = UNSET,
    o: list[FindingsAcceptRisksCreateOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    out_of_scope: bool | Unset = UNSET,
    outside_of_sla: float | Unset = UNSET,
    param: str | Unset = UNSET,
    payload: str | Unset = UNSET,
    planned_remediation_date: datetime.date | Unset = UNSET,
    planned_remediation_version: str | Unset = UNSET,
    product_lifecycle: str | Unset = UNSET,
    product_name: str | Unset = UNSET,
    product_name_contains: str | Unset = UNSET,
    publish_date: datetime.date | Unset = UNSET,
    ransomware_used: bool | Unset = UNSET,
    references: str | Unset = UNSET,
    reporter: list[int] | Unset = UNSET,
    review_requested_by: list[int] | Unset = UNSET,
    reviewers: list[int] | Unset = UNSET,
    risk_acceptance: float | Unset = UNSET,
    risk_accepted: bool | Unset = UNSET,
    sast_sink_object: str | Unset = UNSET,
    sast_source_file_path: str | Unset = UNSET,
    sast_source_line: list[int] | Unset = UNSET,
    sast_source_object: str | Unset = UNSET,
    scanner_confidence: list[int] | Unset = UNSET,
    service: str | Unset = UNSET,
    severity: str | Unset = UNSET,
    severity_justification: str | Unset = UNSET,
    sla_expiration_date: datetime.date | Unset = UNSET,
    sla_start_date: datetime.date | Unset = UNSET,
    sonarqube_issue: list[int] | Unset = UNSET,
    static_finding: bool | Unset = UNSET,
    steps_to_reproduce: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    test: int | Unset = UNSET,
    test_engagement: list[int] | Unset = UNSET,
    test_engagement_product: list[int] | Unset = UNSET,
    test_engagement_product_prod_type: list[int] | Unset = UNSET,
    test_engagement_product_tags: list[str] | Unset = UNSET,
    test_engagement_product_tags_and: list[str] | Unset = UNSET,
    test_engagement_tags: list[str] | Unset = UNSET,
    test_engagement_tags_and: list[str] | Unset = UNSET,
    test_tags: list[str] | Unset = UNSET,
    test_tags_and: list[str] | Unset = UNSET,
    test_test_type: list[int] | Unset = UNSET,
    title: str | Unset = UNSET,
    under_defect_review: bool | Unset = UNSET,
    under_review: bool | Unset = UNSET,
    unique_id_from_tool: str | Unset = UNSET,
    verified: bool | Unset = UNSET,
    vuln_id_from_tool: str | Unset = UNSET,
    vulnerability_id: str | Unset = UNSET,
) -> PaginatedRiskAcceptanceList | None:
    """
    Args:
        active (bool | Unset):
        component_name (str | Unset):
        component_version (str | Unset):
        created (FindingsAcceptRisksCreateCreatedType1 |
            FindingsAcceptRisksCreateCreatedType2Type1 | FindingsAcceptRisksCreateCreatedType3Type1 |
            None | Unset):
        cvssv3 (str | Unset):
        cvssv3_score (float | Unset):
        cvssv4 (str | Unset):
        cvssv4_score (float | Unset):
        cwe (list[int] | Unset):
        date (FindingsAcceptRisksCreateDateType1 | None | Unset):
        defect_review_requested_by (list[int] | Unset):
        description (str | Unset):
        discovered_after (datetime.date | Unset):
        discovered_before (datetime.date | Unset):
        discovered_on (datetime.date | Unset):
        duplicate (bool | Unset):
        duplicate_finding (int | Unset):
        dynamic_finding (bool | Unset):
        effort_for_fixing (str | Unset):
        endpoints (list[int] | Unset):
        epss_percentile_max (float | None | Unset):
        epss_percentile_min (float | None | Unset):
        epss_score_max (float | None | Unset):
        epss_score_min (float | None | Unset):
        false_p (bool | Unset):
        file_path (str | Unset):
        finding_group (list[float] | Unset):
        fix_available (bool | Unset):
        fix_version (str | Unset):
        found_by (list[int] | Unset):
        has_jira (bool | Unset):
        has_tags (bool | Unset):
        hash_code (str | Unset):
        id (list[int] | Unset):
        impact (str | Unset):
        inherited_tags (list[list[int]] | Unset):
        is_mitigated (bool | Unset):
        jira_change (FindingsAcceptRisksCreateJiraLastUpdate | None | Unset):
        jira_creation (FindingsAcceptRisksCreateJiraCreationType1 |
            FindingsAcceptRisksCreateJiraCreationType2Type1 |
            FindingsAcceptRisksCreateJiraCreationType3Type1 | None | Unset):
        kev_date (datetime.date | Unset):
        known_exploited (bool | Unset):
        last_reviewed (FindingsAcceptRisksCreateLastReviewedType1 |
            FindingsAcceptRisksCreateLastReviewedType2Type1 |
            FindingsAcceptRisksCreateLastReviewedType3Type1 | None | Unset):
        last_reviewed_by (list[int] | Unset):
        last_status_update (datetime.datetime | Unset):
        limit (int | Unset):
        mitigated (FindingsAcceptRisksCreateMitigatedType1 |
            FindingsAcceptRisksCreateMitigatedType2Type1 |
            FindingsAcceptRisksCreateMitigatedType3Type1 | None | Unset):
        mitigated_after (datetime.datetime | Unset):
        mitigated_before (datetime.datetime | Unset):
        mitigated_by (list[int] | Unset):
        mitigated_on (datetime.datetime | Unset):
        mitigation (str | Unset):
        nb_occurences (list[int] | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        not_test_engagement_product_tags (list[str] | Unset):
        not_test_engagement_tags (list[str] | Unset):
        not_test_tags (list[str] | Unset):
        numerical_severity (str | Unset):
        o (list[FindingsAcceptRisksCreateOItem] | Unset):
        offset (int | Unset):
        out_of_scope (bool | Unset):
        outside_of_sla (float | Unset):
        param (str | Unset):
        payload (str | Unset):
        planned_remediation_date (datetime.date | Unset):
        planned_remediation_version (str | Unset):
        product_lifecycle (str | Unset):
        product_name (str | Unset):
        product_name_contains (str | Unset):
        publish_date (datetime.date | Unset):
        ransomware_used (bool | Unset):
        references (str | Unset):
        reporter (list[int] | Unset):
        review_requested_by (list[int] | Unset):
        reviewers (list[int] | Unset):
        risk_acceptance (float | Unset):
        risk_accepted (bool | Unset):
        sast_sink_object (str | Unset):
        sast_source_file_path (str | Unset):
        sast_source_line (list[int] | Unset):
        sast_source_object (str | Unset):
        scanner_confidence (list[int] | Unset):
        service (str | Unset):
        severity (str | Unset):
        severity_justification (str | Unset):
        sla_expiration_date (datetime.date | Unset):
        sla_start_date (datetime.date | Unset):
        sonarqube_issue (list[int] | Unset):
        static_finding (bool | Unset):
        steps_to_reproduce (str | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        test (int | Unset):
        test_engagement (list[int] | Unset):
        test_engagement_product (list[int] | Unset):
        test_engagement_product_prod_type (list[int] | Unset):
        test_engagement_product_tags (list[str] | Unset):
        test_engagement_product_tags_and (list[str] | Unset):
        test_engagement_tags (list[str] | Unset):
        test_engagement_tags_and (list[str] | Unset):
        test_tags (list[str] | Unset):
        test_tags_and (list[str] | Unset):
        test_test_type (list[int] | Unset):
        title (str | Unset):
        under_defect_review (bool | Unset):
        under_review (bool | Unset):
        unique_id_from_tool (str | Unset):
        verified (bool | Unset):
        vuln_id_from_tool (str | Unset):
        vulnerability_id (str | Unset):
        body (list[AcceptedRiskRequest]):
        body (list[AcceptedRiskRequest]):
        body (list[AcceptedRiskRequest]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRiskAcceptanceList
    """

    return sync_detailed(
        client=client,
        body=body,
        active=active,
        component_name=component_name,
        component_version=component_version,
        created=created,
        cvssv3=cvssv3,
        cvssv3_score=cvssv3_score,
        cvssv4=cvssv4,
        cvssv4_score=cvssv4_score,
        cwe=cwe,
        date=date,
        defect_review_requested_by=defect_review_requested_by,
        description=description,
        discovered_after=discovered_after,
        discovered_before=discovered_before,
        discovered_on=discovered_on,
        duplicate=duplicate,
        duplicate_finding=duplicate_finding,
        dynamic_finding=dynamic_finding,
        effort_for_fixing=effort_for_fixing,
        endpoints=endpoints,
        epss_percentile_max=epss_percentile_max,
        epss_percentile_min=epss_percentile_min,
        epss_score_max=epss_score_max,
        epss_score_min=epss_score_min,
        false_p=false_p,
        file_path=file_path,
        finding_group=finding_group,
        fix_available=fix_available,
        fix_version=fix_version,
        found_by=found_by,
        has_jira=has_jira,
        has_tags=has_tags,
        hash_code=hash_code,
        id=id,
        impact=impact,
        inherited_tags=inherited_tags,
        is_mitigated=is_mitigated,
        jira_change=jira_change,
        jira_creation=jira_creation,
        kev_date=kev_date,
        known_exploited=known_exploited,
        last_reviewed=last_reviewed,
        last_reviewed_by=last_reviewed_by,
        last_status_update=last_status_update,
        limit=limit,
        mitigated=mitigated,
        mitigated_after=mitigated_after,
        mitigated_before=mitigated_before,
        mitigated_by=mitigated_by,
        mitigated_on=mitigated_on,
        mitigation=mitigation,
        nb_occurences=nb_occurences,
        not_tag=not_tag,
        not_tags=not_tags,
        not_test_engagement_product_tags=not_test_engagement_product_tags,
        not_test_engagement_tags=not_test_engagement_tags,
        not_test_tags=not_test_tags,
        numerical_severity=numerical_severity,
        o=o,
        offset=offset,
        out_of_scope=out_of_scope,
        outside_of_sla=outside_of_sla,
        param=param,
        payload=payload,
        planned_remediation_date=planned_remediation_date,
        planned_remediation_version=planned_remediation_version,
        product_lifecycle=product_lifecycle,
        product_name=product_name,
        product_name_contains=product_name_contains,
        publish_date=publish_date,
        ransomware_used=ransomware_used,
        references=references,
        reporter=reporter,
        review_requested_by=review_requested_by,
        reviewers=reviewers,
        risk_acceptance=risk_acceptance,
        risk_accepted=risk_accepted,
        sast_sink_object=sast_sink_object,
        sast_source_file_path=sast_source_file_path,
        sast_source_line=sast_source_line,
        sast_source_object=sast_source_object,
        scanner_confidence=scanner_confidence,
        service=service,
        severity=severity,
        severity_justification=severity_justification,
        sla_expiration_date=sla_expiration_date,
        sla_start_date=sla_start_date,
        sonarqube_issue=sonarqube_issue,
        static_finding=static_finding,
        steps_to_reproduce=steps_to_reproduce,
        tag=tag,
        tags=tags,
        tags_and=tags_and,
        test=test,
        test_engagement=test_engagement,
        test_engagement_product=test_engagement_product,
        test_engagement_product_prod_type=test_engagement_product_prod_type,
        test_engagement_product_tags=test_engagement_product_tags,
        test_engagement_product_tags_and=test_engagement_product_tags_and,
        test_engagement_tags=test_engagement_tags,
        test_engagement_tags_and=test_engagement_tags_and,
        test_tags=test_tags,
        test_tags_and=test_tags_and,
        test_test_type=test_test_type,
        title=title,
        under_defect_review=under_defect_review,
        under_review=under_review,
        unique_id_from_tool=unique_id_from_tool,
        verified=verified,
        vuln_id_from_tool=vuln_id_from_tool,
        vulnerability_id=vulnerability_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: list[AcceptedRiskRequest]
    | list[AcceptedRiskRequest]
    | list[AcceptedRiskRequest]
    | Unset = UNSET,
    active: bool | Unset = UNSET,
    component_name: str | Unset = UNSET,
    component_version: str | Unset = UNSET,
    created: FindingsAcceptRisksCreateCreatedType1
    | FindingsAcceptRisksCreateCreatedType2Type1
    | FindingsAcceptRisksCreateCreatedType3Type1
    | None
    | Unset = UNSET,
    cvssv3: str | Unset = UNSET,
    cvssv3_score: float | Unset = UNSET,
    cvssv4: str | Unset = UNSET,
    cvssv4_score: float | Unset = UNSET,
    cwe: list[int] | Unset = UNSET,
    date: FindingsAcceptRisksCreateDateType1 | None | Unset = UNSET,
    defect_review_requested_by: list[int] | Unset = UNSET,
    description: str | Unset = UNSET,
    discovered_after: datetime.date | Unset = UNSET,
    discovered_before: datetime.date | Unset = UNSET,
    discovered_on: datetime.date | Unset = UNSET,
    duplicate: bool | Unset = UNSET,
    duplicate_finding: int | Unset = UNSET,
    dynamic_finding: bool | Unset = UNSET,
    effort_for_fixing: str | Unset = UNSET,
    endpoints: list[int] | Unset = UNSET,
    epss_percentile_max: float | None | Unset = UNSET,
    epss_percentile_min: float | None | Unset = UNSET,
    epss_score_max: float | None | Unset = UNSET,
    epss_score_min: float | None | Unset = UNSET,
    false_p: bool | Unset = UNSET,
    file_path: str | Unset = UNSET,
    finding_group: list[float] | Unset = UNSET,
    fix_available: bool | Unset = UNSET,
    fix_version: str | Unset = UNSET,
    found_by: list[int] | Unset = UNSET,
    has_jira: bool | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    hash_code: str | Unset = UNSET,
    id: list[int] | Unset = UNSET,
    impact: str | Unset = UNSET,
    inherited_tags: list[list[int]] | Unset = UNSET,
    is_mitigated: bool | Unset = UNSET,
    jira_change: FindingsAcceptRisksCreateJiraLastUpdate | None | Unset = UNSET,
    jira_creation: FindingsAcceptRisksCreateJiraCreationType1
    | FindingsAcceptRisksCreateJiraCreationType2Type1
    | FindingsAcceptRisksCreateJiraCreationType3Type1
    | None
    | Unset = UNSET,
    kev_date: datetime.date | Unset = UNSET,
    known_exploited: bool | Unset = UNSET,
    last_reviewed: FindingsAcceptRisksCreateLastReviewedType1
    | FindingsAcceptRisksCreateLastReviewedType2Type1
    | FindingsAcceptRisksCreateLastReviewedType3Type1
    | None
    | Unset = UNSET,
    last_reviewed_by: list[int] | Unset = UNSET,
    last_status_update: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    mitigated: FindingsAcceptRisksCreateMitigatedType1
    | FindingsAcceptRisksCreateMitigatedType2Type1
    | FindingsAcceptRisksCreateMitigatedType3Type1
    | None
    | Unset = UNSET,
    mitigated_after: datetime.datetime | Unset = UNSET,
    mitigated_before: datetime.datetime | Unset = UNSET,
    mitigated_by: list[int] | Unset = UNSET,
    mitigated_on: datetime.datetime | Unset = UNSET,
    mitigation: str | Unset = UNSET,
    nb_occurences: list[int] | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    not_test_engagement_product_tags: list[str] | Unset = UNSET,
    not_test_engagement_tags: list[str] | Unset = UNSET,
    not_test_tags: list[str] | Unset = UNSET,
    numerical_severity: str | Unset = UNSET,
    o: list[FindingsAcceptRisksCreateOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    out_of_scope: bool | Unset = UNSET,
    outside_of_sla: float | Unset = UNSET,
    param: str | Unset = UNSET,
    payload: str | Unset = UNSET,
    planned_remediation_date: datetime.date | Unset = UNSET,
    planned_remediation_version: str | Unset = UNSET,
    product_lifecycle: str | Unset = UNSET,
    product_name: str | Unset = UNSET,
    product_name_contains: str | Unset = UNSET,
    publish_date: datetime.date | Unset = UNSET,
    ransomware_used: bool | Unset = UNSET,
    references: str | Unset = UNSET,
    reporter: list[int] | Unset = UNSET,
    review_requested_by: list[int] | Unset = UNSET,
    reviewers: list[int] | Unset = UNSET,
    risk_acceptance: float | Unset = UNSET,
    risk_accepted: bool | Unset = UNSET,
    sast_sink_object: str | Unset = UNSET,
    sast_source_file_path: str | Unset = UNSET,
    sast_source_line: list[int] | Unset = UNSET,
    sast_source_object: str | Unset = UNSET,
    scanner_confidence: list[int] | Unset = UNSET,
    service: str | Unset = UNSET,
    severity: str | Unset = UNSET,
    severity_justification: str | Unset = UNSET,
    sla_expiration_date: datetime.date | Unset = UNSET,
    sla_start_date: datetime.date | Unset = UNSET,
    sonarqube_issue: list[int] | Unset = UNSET,
    static_finding: bool | Unset = UNSET,
    steps_to_reproduce: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    test: int | Unset = UNSET,
    test_engagement: list[int] | Unset = UNSET,
    test_engagement_product: list[int] | Unset = UNSET,
    test_engagement_product_prod_type: list[int] | Unset = UNSET,
    test_engagement_product_tags: list[str] | Unset = UNSET,
    test_engagement_product_tags_and: list[str] | Unset = UNSET,
    test_engagement_tags: list[str] | Unset = UNSET,
    test_engagement_tags_and: list[str] | Unset = UNSET,
    test_tags: list[str] | Unset = UNSET,
    test_tags_and: list[str] | Unset = UNSET,
    test_test_type: list[int] | Unset = UNSET,
    title: str | Unset = UNSET,
    under_defect_review: bool | Unset = UNSET,
    under_review: bool | Unset = UNSET,
    unique_id_from_tool: str | Unset = UNSET,
    verified: bool | Unset = UNSET,
    vuln_id_from_tool: str | Unset = UNSET,
    vulnerability_id: str | Unset = UNSET,
) -> Response[PaginatedRiskAcceptanceList]:
    """
    Args:
        active (bool | Unset):
        component_name (str | Unset):
        component_version (str | Unset):
        created (FindingsAcceptRisksCreateCreatedType1 |
            FindingsAcceptRisksCreateCreatedType2Type1 | FindingsAcceptRisksCreateCreatedType3Type1 |
            None | Unset):
        cvssv3 (str | Unset):
        cvssv3_score (float | Unset):
        cvssv4 (str | Unset):
        cvssv4_score (float | Unset):
        cwe (list[int] | Unset):
        date (FindingsAcceptRisksCreateDateType1 | None | Unset):
        defect_review_requested_by (list[int] | Unset):
        description (str | Unset):
        discovered_after (datetime.date | Unset):
        discovered_before (datetime.date | Unset):
        discovered_on (datetime.date | Unset):
        duplicate (bool | Unset):
        duplicate_finding (int | Unset):
        dynamic_finding (bool | Unset):
        effort_for_fixing (str | Unset):
        endpoints (list[int] | Unset):
        epss_percentile_max (float | None | Unset):
        epss_percentile_min (float | None | Unset):
        epss_score_max (float | None | Unset):
        epss_score_min (float | None | Unset):
        false_p (bool | Unset):
        file_path (str | Unset):
        finding_group (list[float] | Unset):
        fix_available (bool | Unset):
        fix_version (str | Unset):
        found_by (list[int] | Unset):
        has_jira (bool | Unset):
        has_tags (bool | Unset):
        hash_code (str | Unset):
        id (list[int] | Unset):
        impact (str | Unset):
        inherited_tags (list[list[int]] | Unset):
        is_mitigated (bool | Unset):
        jira_change (FindingsAcceptRisksCreateJiraLastUpdate | None | Unset):
        jira_creation (FindingsAcceptRisksCreateJiraCreationType1 |
            FindingsAcceptRisksCreateJiraCreationType2Type1 |
            FindingsAcceptRisksCreateJiraCreationType3Type1 | None | Unset):
        kev_date (datetime.date | Unset):
        known_exploited (bool | Unset):
        last_reviewed (FindingsAcceptRisksCreateLastReviewedType1 |
            FindingsAcceptRisksCreateLastReviewedType2Type1 |
            FindingsAcceptRisksCreateLastReviewedType3Type1 | None | Unset):
        last_reviewed_by (list[int] | Unset):
        last_status_update (datetime.datetime | Unset):
        limit (int | Unset):
        mitigated (FindingsAcceptRisksCreateMitigatedType1 |
            FindingsAcceptRisksCreateMitigatedType2Type1 |
            FindingsAcceptRisksCreateMitigatedType3Type1 | None | Unset):
        mitigated_after (datetime.datetime | Unset):
        mitigated_before (datetime.datetime | Unset):
        mitigated_by (list[int] | Unset):
        mitigated_on (datetime.datetime | Unset):
        mitigation (str | Unset):
        nb_occurences (list[int] | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        not_test_engagement_product_tags (list[str] | Unset):
        not_test_engagement_tags (list[str] | Unset):
        not_test_tags (list[str] | Unset):
        numerical_severity (str | Unset):
        o (list[FindingsAcceptRisksCreateOItem] | Unset):
        offset (int | Unset):
        out_of_scope (bool | Unset):
        outside_of_sla (float | Unset):
        param (str | Unset):
        payload (str | Unset):
        planned_remediation_date (datetime.date | Unset):
        planned_remediation_version (str | Unset):
        product_lifecycle (str | Unset):
        product_name (str | Unset):
        product_name_contains (str | Unset):
        publish_date (datetime.date | Unset):
        ransomware_used (bool | Unset):
        references (str | Unset):
        reporter (list[int] | Unset):
        review_requested_by (list[int] | Unset):
        reviewers (list[int] | Unset):
        risk_acceptance (float | Unset):
        risk_accepted (bool | Unset):
        sast_sink_object (str | Unset):
        sast_source_file_path (str | Unset):
        sast_source_line (list[int] | Unset):
        sast_source_object (str | Unset):
        scanner_confidence (list[int] | Unset):
        service (str | Unset):
        severity (str | Unset):
        severity_justification (str | Unset):
        sla_expiration_date (datetime.date | Unset):
        sla_start_date (datetime.date | Unset):
        sonarqube_issue (list[int] | Unset):
        static_finding (bool | Unset):
        steps_to_reproduce (str | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        test (int | Unset):
        test_engagement (list[int] | Unset):
        test_engagement_product (list[int] | Unset):
        test_engagement_product_prod_type (list[int] | Unset):
        test_engagement_product_tags (list[str] | Unset):
        test_engagement_product_tags_and (list[str] | Unset):
        test_engagement_tags (list[str] | Unset):
        test_engagement_tags_and (list[str] | Unset):
        test_tags (list[str] | Unset):
        test_tags_and (list[str] | Unset):
        test_test_type (list[int] | Unset):
        title (str | Unset):
        under_defect_review (bool | Unset):
        under_review (bool | Unset):
        unique_id_from_tool (str | Unset):
        verified (bool | Unset):
        vuln_id_from_tool (str | Unset):
        vulnerability_id (str | Unset):
        body (list[AcceptedRiskRequest]):
        body (list[AcceptedRiskRequest]):
        body (list[AcceptedRiskRequest]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRiskAcceptanceList]
    """

    kwargs = _get_kwargs(
        body=body,
        active=active,
        component_name=component_name,
        component_version=component_version,
        created=created,
        cvssv3=cvssv3,
        cvssv3_score=cvssv3_score,
        cvssv4=cvssv4,
        cvssv4_score=cvssv4_score,
        cwe=cwe,
        date=date,
        defect_review_requested_by=defect_review_requested_by,
        description=description,
        discovered_after=discovered_after,
        discovered_before=discovered_before,
        discovered_on=discovered_on,
        duplicate=duplicate,
        duplicate_finding=duplicate_finding,
        dynamic_finding=dynamic_finding,
        effort_for_fixing=effort_for_fixing,
        endpoints=endpoints,
        epss_percentile_max=epss_percentile_max,
        epss_percentile_min=epss_percentile_min,
        epss_score_max=epss_score_max,
        epss_score_min=epss_score_min,
        false_p=false_p,
        file_path=file_path,
        finding_group=finding_group,
        fix_available=fix_available,
        fix_version=fix_version,
        found_by=found_by,
        has_jira=has_jira,
        has_tags=has_tags,
        hash_code=hash_code,
        id=id,
        impact=impact,
        inherited_tags=inherited_tags,
        is_mitigated=is_mitigated,
        jira_change=jira_change,
        jira_creation=jira_creation,
        kev_date=kev_date,
        known_exploited=known_exploited,
        last_reviewed=last_reviewed,
        last_reviewed_by=last_reviewed_by,
        last_status_update=last_status_update,
        limit=limit,
        mitigated=mitigated,
        mitigated_after=mitigated_after,
        mitigated_before=mitigated_before,
        mitigated_by=mitigated_by,
        mitigated_on=mitigated_on,
        mitigation=mitigation,
        nb_occurences=nb_occurences,
        not_tag=not_tag,
        not_tags=not_tags,
        not_test_engagement_product_tags=not_test_engagement_product_tags,
        not_test_engagement_tags=not_test_engagement_tags,
        not_test_tags=not_test_tags,
        numerical_severity=numerical_severity,
        o=o,
        offset=offset,
        out_of_scope=out_of_scope,
        outside_of_sla=outside_of_sla,
        param=param,
        payload=payload,
        planned_remediation_date=planned_remediation_date,
        planned_remediation_version=planned_remediation_version,
        product_lifecycle=product_lifecycle,
        product_name=product_name,
        product_name_contains=product_name_contains,
        publish_date=publish_date,
        ransomware_used=ransomware_used,
        references=references,
        reporter=reporter,
        review_requested_by=review_requested_by,
        reviewers=reviewers,
        risk_acceptance=risk_acceptance,
        risk_accepted=risk_accepted,
        sast_sink_object=sast_sink_object,
        sast_source_file_path=sast_source_file_path,
        sast_source_line=sast_source_line,
        sast_source_object=sast_source_object,
        scanner_confidence=scanner_confidence,
        service=service,
        severity=severity,
        severity_justification=severity_justification,
        sla_expiration_date=sla_expiration_date,
        sla_start_date=sla_start_date,
        sonarqube_issue=sonarqube_issue,
        static_finding=static_finding,
        steps_to_reproduce=steps_to_reproduce,
        tag=tag,
        tags=tags,
        tags_and=tags_and,
        test=test,
        test_engagement=test_engagement,
        test_engagement_product=test_engagement_product,
        test_engagement_product_prod_type=test_engagement_product_prod_type,
        test_engagement_product_tags=test_engagement_product_tags,
        test_engagement_product_tags_and=test_engagement_product_tags_and,
        test_engagement_tags=test_engagement_tags,
        test_engagement_tags_and=test_engagement_tags_and,
        test_tags=test_tags,
        test_tags_and=test_tags_and,
        test_test_type=test_test_type,
        title=title,
        under_defect_review=under_defect_review,
        under_review=under_review,
        unique_id_from_tool=unique_id_from_tool,
        verified=verified,
        vuln_id_from_tool=vuln_id_from_tool,
        vulnerability_id=vulnerability_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: list[AcceptedRiskRequest]
    | list[AcceptedRiskRequest]
    | list[AcceptedRiskRequest]
    | Unset = UNSET,
    active: bool | Unset = UNSET,
    component_name: str | Unset = UNSET,
    component_version: str | Unset = UNSET,
    created: FindingsAcceptRisksCreateCreatedType1
    | FindingsAcceptRisksCreateCreatedType2Type1
    | FindingsAcceptRisksCreateCreatedType3Type1
    | None
    | Unset = UNSET,
    cvssv3: str | Unset = UNSET,
    cvssv3_score: float | Unset = UNSET,
    cvssv4: str | Unset = UNSET,
    cvssv4_score: float | Unset = UNSET,
    cwe: list[int] | Unset = UNSET,
    date: FindingsAcceptRisksCreateDateType1 | None | Unset = UNSET,
    defect_review_requested_by: list[int] | Unset = UNSET,
    description: str | Unset = UNSET,
    discovered_after: datetime.date | Unset = UNSET,
    discovered_before: datetime.date | Unset = UNSET,
    discovered_on: datetime.date | Unset = UNSET,
    duplicate: bool | Unset = UNSET,
    duplicate_finding: int | Unset = UNSET,
    dynamic_finding: bool | Unset = UNSET,
    effort_for_fixing: str | Unset = UNSET,
    endpoints: list[int] | Unset = UNSET,
    epss_percentile_max: float | None | Unset = UNSET,
    epss_percentile_min: float | None | Unset = UNSET,
    epss_score_max: float | None | Unset = UNSET,
    epss_score_min: float | None | Unset = UNSET,
    false_p: bool | Unset = UNSET,
    file_path: str | Unset = UNSET,
    finding_group: list[float] | Unset = UNSET,
    fix_available: bool | Unset = UNSET,
    fix_version: str | Unset = UNSET,
    found_by: list[int] | Unset = UNSET,
    has_jira: bool | Unset = UNSET,
    has_tags: bool | Unset = UNSET,
    hash_code: str | Unset = UNSET,
    id: list[int] | Unset = UNSET,
    impact: str | Unset = UNSET,
    inherited_tags: list[list[int]] | Unset = UNSET,
    is_mitigated: bool | Unset = UNSET,
    jira_change: FindingsAcceptRisksCreateJiraLastUpdate | None | Unset = UNSET,
    jira_creation: FindingsAcceptRisksCreateJiraCreationType1
    | FindingsAcceptRisksCreateJiraCreationType2Type1
    | FindingsAcceptRisksCreateJiraCreationType3Type1
    | None
    | Unset = UNSET,
    kev_date: datetime.date | Unset = UNSET,
    known_exploited: bool | Unset = UNSET,
    last_reviewed: FindingsAcceptRisksCreateLastReviewedType1
    | FindingsAcceptRisksCreateLastReviewedType2Type1
    | FindingsAcceptRisksCreateLastReviewedType3Type1
    | None
    | Unset = UNSET,
    last_reviewed_by: list[int] | Unset = UNSET,
    last_status_update: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    mitigated: FindingsAcceptRisksCreateMitigatedType1
    | FindingsAcceptRisksCreateMitigatedType2Type1
    | FindingsAcceptRisksCreateMitigatedType3Type1
    | None
    | Unset = UNSET,
    mitigated_after: datetime.datetime | Unset = UNSET,
    mitigated_before: datetime.datetime | Unset = UNSET,
    mitigated_by: list[int] | Unset = UNSET,
    mitigated_on: datetime.datetime | Unset = UNSET,
    mitigation: str | Unset = UNSET,
    nb_occurences: list[int] | Unset = UNSET,
    not_tag: str | Unset = UNSET,
    not_tags: list[str] | Unset = UNSET,
    not_test_engagement_product_tags: list[str] | Unset = UNSET,
    not_test_engagement_tags: list[str] | Unset = UNSET,
    not_test_tags: list[str] | Unset = UNSET,
    numerical_severity: str | Unset = UNSET,
    o: list[FindingsAcceptRisksCreateOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    out_of_scope: bool | Unset = UNSET,
    outside_of_sla: float | Unset = UNSET,
    param: str | Unset = UNSET,
    payload: str | Unset = UNSET,
    planned_remediation_date: datetime.date | Unset = UNSET,
    planned_remediation_version: str | Unset = UNSET,
    product_lifecycle: str | Unset = UNSET,
    product_name: str | Unset = UNSET,
    product_name_contains: str | Unset = UNSET,
    publish_date: datetime.date | Unset = UNSET,
    ransomware_used: bool | Unset = UNSET,
    references: str | Unset = UNSET,
    reporter: list[int] | Unset = UNSET,
    review_requested_by: list[int] | Unset = UNSET,
    reviewers: list[int] | Unset = UNSET,
    risk_acceptance: float | Unset = UNSET,
    risk_accepted: bool | Unset = UNSET,
    sast_sink_object: str | Unset = UNSET,
    sast_source_file_path: str | Unset = UNSET,
    sast_source_line: list[int] | Unset = UNSET,
    sast_source_object: str | Unset = UNSET,
    scanner_confidence: list[int] | Unset = UNSET,
    service: str | Unset = UNSET,
    severity: str | Unset = UNSET,
    severity_justification: str | Unset = UNSET,
    sla_expiration_date: datetime.date | Unset = UNSET,
    sla_start_date: datetime.date | Unset = UNSET,
    sonarqube_issue: list[int] | Unset = UNSET,
    static_finding: bool | Unset = UNSET,
    steps_to_reproduce: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    tags_and: list[str] | Unset = UNSET,
    test: int | Unset = UNSET,
    test_engagement: list[int] | Unset = UNSET,
    test_engagement_product: list[int] | Unset = UNSET,
    test_engagement_product_prod_type: list[int] | Unset = UNSET,
    test_engagement_product_tags: list[str] | Unset = UNSET,
    test_engagement_product_tags_and: list[str] | Unset = UNSET,
    test_engagement_tags: list[str] | Unset = UNSET,
    test_engagement_tags_and: list[str] | Unset = UNSET,
    test_tags: list[str] | Unset = UNSET,
    test_tags_and: list[str] | Unset = UNSET,
    test_test_type: list[int] | Unset = UNSET,
    title: str | Unset = UNSET,
    under_defect_review: bool | Unset = UNSET,
    under_review: bool | Unset = UNSET,
    unique_id_from_tool: str | Unset = UNSET,
    verified: bool | Unset = UNSET,
    vuln_id_from_tool: str | Unset = UNSET,
    vulnerability_id: str | Unset = UNSET,
) -> PaginatedRiskAcceptanceList | None:
    """
    Args:
        active (bool | Unset):
        component_name (str | Unset):
        component_version (str | Unset):
        created (FindingsAcceptRisksCreateCreatedType1 |
            FindingsAcceptRisksCreateCreatedType2Type1 | FindingsAcceptRisksCreateCreatedType3Type1 |
            None | Unset):
        cvssv3 (str | Unset):
        cvssv3_score (float | Unset):
        cvssv4 (str | Unset):
        cvssv4_score (float | Unset):
        cwe (list[int] | Unset):
        date (FindingsAcceptRisksCreateDateType1 | None | Unset):
        defect_review_requested_by (list[int] | Unset):
        description (str | Unset):
        discovered_after (datetime.date | Unset):
        discovered_before (datetime.date | Unset):
        discovered_on (datetime.date | Unset):
        duplicate (bool | Unset):
        duplicate_finding (int | Unset):
        dynamic_finding (bool | Unset):
        effort_for_fixing (str | Unset):
        endpoints (list[int] | Unset):
        epss_percentile_max (float | None | Unset):
        epss_percentile_min (float | None | Unset):
        epss_score_max (float | None | Unset):
        epss_score_min (float | None | Unset):
        false_p (bool | Unset):
        file_path (str | Unset):
        finding_group (list[float] | Unset):
        fix_available (bool | Unset):
        fix_version (str | Unset):
        found_by (list[int] | Unset):
        has_jira (bool | Unset):
        has_tags (bool | Unset):
        hash_code (str | Unset):
        id (list[int] | Unset):
        impact (str | Unset):
        inherited_tags (list[list[int]] | Unset):
        is_mitigated (bool | Unset):
        jira_change (FindingsAcceptRisksCreateJiraLastUpdate | None | Unset):
        jira_creation (FindingsAcceptRisksCreateJiraCreationType1 |
            FindingsAcceptRisksCreateJiraCreationType2Type1 |
            FindingsAcceptRisksCreateJiraCreationType3Type1 | None | Unset):
        kev_date (datetime.date | Unset):
        known_exploited (bool | Unset):
        last_reviewed (FindingsAcceptRisksCreateLastReviewedType1 |
            FindingsAcceptRisksCreateLastReviewedType2Type1 |
            FindingsAcceptRisksCreateLastReviewedType3Type1 | None | Unset):
        last_reviewed_by (list[int] | Unset):
        last_status_update (datetime.datetime | Unset):
        limit (int | Unset):
        mitigated (FindingsAcceptRisksCreateMitigatedType1 |
            FindingsAcceptRisksCreateMitigatedType2Type1 |
            FindingsAcceptRisksCreateMitigatedType3Type1 | None | Unset):
        mitigated_after (datetime.datetime | Unset):
        mitigated_before (datetime.datetime | Unset):
        mitigated_by (list[int] | Unset):
        mitigated_on (datetime.datetime | Unset):
        mitigation (str | Unset):
        nb_occurences (list[int] | Unset):
        not_tag (str | Unset):
        not_tags (list[str] | Unset):
        not_test_engagement_product_tags (list[str] | Unset):
        not_test_engagement_tags (list[str] | Unset):
        not_test_tags (list[str] | Unset):
        numerical_severity (str | Unset):
        o (list[FindingsAcceptRisksCreateOItem] | Unset):
        offset (int | Unset):
        out_of_scope (bool | Unset):
        outside_of_sla (float | Unset):
        param (str | Unset):
        payload (str | Unset):
        planned_remediation_date (datetime.date | Unset):
        planned_remediation_version (str | Unset):
        product_lifecycle (str | Unset):
        product_name (str | Unset):
        product_name_contains (str | Unset):
        publish_date (datetime.date | Unset):
        ransomware_used (bool | Unset):
        references (str | Unset):
        reporter (list[int] | Unset):
        review_requested_by (list[int] | Unset):
        reviewers (list[int] | Unset):
        risk_acceptance (float | Unset):
        risk_accepted (bool | Unset):
        sast_sink_object (str | Unset):
        sast_source_file_path (str | Unset):
        sast_source_line (list[int] | Unset):
        sast_source_object (str | Unset):
        scanner_confidence (list[int] | Unset):
        service (str | Unset):
        severity (str | Unset):
        severity_justification (str | Unset):
        sla_expiration_date (datetime.date | Unset):
        sla_start_date (datetime.date | Unset):
        sonarqube_issue (list[int] | Unset):
        static_finding (bool | Unset):
        steps_to_reproduce (str | Unset):
        tag (str | Unset):
        tags (list[str] | Unset):
        tags_and (list[str] | Unset):
        test (int | Unset):
        test_engagement (list[int] | Unset):
        test_engagement_product (list[int] | Unset):
        test_engagement_product_prod_type (list[int] | Unset):
        test_engagement_product_tags (list[str] | Unset):
        test_engagement_product_tags_and (list[str] | Unset):
        test_engagement_tags (list[str] | Unset):
        test_engagement_tags_and (list[str] | Unset):
        test_tags (list[str] | Unset):
        test_tags_and (list[str] | Unset):
        test_test_type (list[int] | Unset):
        title (str | Unset):
        under_defect_review (bool | Unset):
        under_review (bool | Unset):
        unique_id_from_tool (str | Unset):
        verified (bool | Unset):
        vuln_id_from_tool (str | Unset):
        vulnerability_id (str | Unset):
        body (list[AcceptedRiskRequest]):
        body (list[AcceptedRiskRequest]):
        body (list[AcceptedRiskRequest]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRiskAcceptanceList
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            active=active,
            component_name=component_name,
            component_version=component_version,
            created=created,
            cvssv3=cvssv3,
            cvssv3_score=cvssv3_score,
            cvssv4=cvssv4,
            cvssv4_score=cvssv4_score,
            cwe=cwe,
            date=date,
            defect_review_requested_by=defect_review_requested_by,
            description=description,
            discovered_after=discovered_after,
            discovered_before=discovered_before,
            discovered_on=discovered_on,
            duplicate=duplicate,
            duplicate_finding=duplicate_finding,
            dynamic_finding=dynamic_finding,
            effort_for_fixing=effort_for_fixing,
            endpoints=endpoints,
            epss_percentile_max=epss_percentile_max,
            epss_percentile_min=epss_percentile_min,
            epss_score_max=epss_score_max,
            epss_score_min=epss_score_min,
            false_p=false_p,
            file_path=file_path,
            finding_group=finding_group,
            fix_available=fix_available,
            fix_version=fix_version,
            found_by=found_by,
            has_jira=has_jira,
            has_tags=has_tags,
            hash_code=hash_code,
            id=id,
            impact=impact,
            inherited_tags=inherited_tags,
            is_mitigated=is_mitigated,
            jira_change=jira_change,
            jira_creation=jira_creation,
            kev_date=kev_date,
            known_exploited=known_exploited,
            last_reviewed=last_reviewed,
            last_reviewed_by=last_reviewed_by,
            last_status_update=last_status_update,
            limit=limit,
            mitigated=mitigated,
            mitigated_after=mitigated_after,
            mitigated_before=mitigated_before,
            mitigated_by=mitigated_by,
            mitigated_on=mitigated_on,
            mitigation=mitigation,
            nb_occurences=nb_occurences,
            not_tag=not_tag,
            not_tags=not_tags,
            not_test_engagement_product_tags=not_test_engagement_product_tags,
            not_test_engagement_tags=not_test_engagement_tags,
            not_test_tags=not_test_tags,
            numerical_severity=numerical_severity,
            o=o,
            offset=offset,
            out_of_scope=out_of_scope,
            outside_of_sla=outside_of_sla,
            param=param,
            payload=payload,
            planned_remediation_date=planned_remediation_date,
            planned_remediation_version=planned_remediation_version,
            product_lifecycle=product_lifecycle,
            product_name=product_name,
            product_name_contains=product_name_contains,
            publish_date=publish_date,
            ransomware_used=ransomware_used,
            references=references,
            reporter=reporter,
            review_requested_by=review_requested_by,
            reviewers=reviewers,
            risk_acceptance=risk_acceptance,
            risk_accepted=risk_accepted,
            sast_sink_object=sast_sink_object,
            sast_source_file_path=sast_source_file_path,
            sast_source_line=sast_source_line,
            sast_source_object=sast_source_object,
            scanner_confidence=scanner_confidence,
            service=service,
            severity=severity,
            severity_justification=severity_justification,
            sla_expiration_date=sla_expiration_date,
            sla_start_date=sla_start_date,
            sonarqube_issue=sonarqube_issue,
            static_finding=static_finding,
            steps_to_reproduce=steps_to_reproduce,
            tag=tag,
            tags=tags,
            tags_and=tags_and,
            test=test,
            test_engagement=test_engagement,
            test_engagement_product=test_engagement_product,
            test_engagement_product_prod_type=test_engagement_product_prod_type,
            test_engagement_product_tags=test_engagement_product_tags,
            test_engagement_product_tags_and=test_engagement_product_tags_and,
            test_engagement_tags=test_engagement_tags,
            test_engagement_tags_and=test_engagement_tags_and,
            test_tags=test_tags,
            test_tags_and=test_tags_and,
            test_test_type=test_test_type,
            title=title,
            under_defect_review=under_defect_review,
            under_review=under_review,
            unique_id_from_tool=unique_id_from_tool,
            verified=verified,
            vuln_id_from_tool=vuln_id_from_tool,
            vulnerability_id=vulnerability_id,
        )
    ).parsed
