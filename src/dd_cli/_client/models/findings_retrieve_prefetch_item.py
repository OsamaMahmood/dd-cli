from enum import Enum


class FindingsRetrievePrefetchItem(str, Enum):
    AUTHOR_ISSUES = "author_issues"
    AUTH_ISSUES = "auth_issues"
    CONFIG_ISSUES = "config_issues"
    CRYPTO_ISSUES = "crypto_issues"
    DATA_ISSUES = "data_issues"
    DEFECT_REVIEW_REQUESTED_BY = "defect_review_requested_by"
    DUPLICATE_FINDING = "duplicate_finding"
    ENDPOINTS = "endpoints"
    ENDPOINT_SET = "endpoint_set"
    FILES = "files"
    FINDING_GROUP_SET = "finding_group_set"
    FOUND_BY = "found_by"
    LAST_REVIEWED_BY = "last_reviewed_by"
    MITIGATED_BY = "mitigated_by"
    NOTES = "notes"
    OTHER_ISSUES = "other_issues"
    REPORTER = "reporter"
    REVIEWERS = "reviewers"
    REVIEW_REQUESTED_BY = "review_requested_by"
    RISK_ACCEPTANCE_SET = "risk_acceptance_set"
    SENSITIVE_ISSUES = "sensitive_issues"
    SESSION_ISSUES = "session_issues"
    SONARQUBE_ISSUE = "sonarqube_issue"
    TEST = "test"
    TEST_IMPORT_SET = "test_import_set"

    def __str__(self) -> str:
        return str(self.value)
