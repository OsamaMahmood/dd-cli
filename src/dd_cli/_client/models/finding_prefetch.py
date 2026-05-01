from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.finding_prefetch_auth_issues import FindingPrefetchAuthIssues
    from ..models.finding_prefetch_author_issues import FindingPrefetchAuthorIssues
    from ..models.finding_prefetch_config_issues import FindingPrefetchConfigIssues
    from ..models.finding_prefetch_crypto_issues import FindingPrefetchCryptoIssues
    from ..models.finding_prefetch_data_issues import FindingPrefetchDataIssues
    from ..models.finding_prefetch_defect_review_requested_by import (
        FindingPrefetchDefectReviewRequestedBy,
    )
    from ..models.finding_prefetch_duplicate_finding import FindingPrefetchDuplicateFinding
    from ..models.finding_prefetch_endpoint_set import FindingPrefetchEndpointSet
    from ..models.finding_prefetch_endpoints import FindingPrefetchEndpoints
    from ..models.finding_prefetch_files import FindingPrefetchFiles
    from ..models.finding_prefetch_finding_group_set import FindingPrefetchFindingGroupSet
    from ..models.finding_prefetch_found_by import FindingPrefetchFoundBy
    from ..models.finding_prefetch_last_reviewed_by import FindingPrefetchLastReviewedBy
    from ..models.finding_prefetch_mitigated_by import FindingPrefetchMitigatedBy
    from ..models.finding_prefetch_notes import FindingPrefetchNotes
    from ..models.finding_prefetch_other_issues import FindingPrefetchOtherIssues
    from ..models.finding_prefetch_reporter import FindingPrefetchReporter
    from ..models.finding_prefetch_review_requested_by import FindingPrefetchReviewRequestedBy
    from ..models.finding_prefetch_reviewers import FindingPrefetchReviewers
    from ..models.finding_prefetch_risk_acceptance_set import FindingPrefetchRiskAcceptanceSet
    from ..models.finding_prefetch_sensitive_issues import FindingPrefetchSensitiveIssues
    from ..models.finding_prefetch_session_issues import FindingPrefetchSessionIssues
    from ..models.finding_prefetch_sonarqube_issue import FindingPrefetchSonarqubeIssue
    from ..models.finding_prefetch_test import FindingPrefetchTest
    from ..models.finding_prefetch_test_import_set import FindingPrefetchTestImportSet


T = TypeVar("T", bound="FindingPrefetch")


@_attrs_define
class FindingPrefetch:
    """
    Attributes:
        auth_issues (FindingPrefetchAuthIssues | Unset):
        author_issues (FindingPrefetchAuthorIssues | Unset):
        config_issues (FindingPrefetchConfigIssues | Unset):
        crypto_issues (FindingPrefetchCryptoIssues | Unset):
        data_issues (FindingPrefetchDataIssues | Unset):
        defect_review_requested_by (FindingPrefetchDefectReviewRequestedBy | Unset):
        duplicate_finding (FindingPrefetchDuplicateFinding | Unset):
        endpoint_set (FindingPrefetchEndpointSet | Unset):
        endpoints (FindingPrefetchEndpoints | Unset):
        files (FindingPrefetchFiles | Unset):
        finding_group_set (FindingPrefetchFindingGroupSet | Unset):
        found_by (FindingPrefetchFoundBy | Unset):
        last_reviewed_by (FindingPrefetchLastReviewedBy | Unset):
        mitigated_by (FindingPrefetchMitigatedBy | Unset):
        notes (FindingPrefetchNotes | Unset):
        other_issues (FindingPrefetchOtherIssues | Unset):
        reporter (FindingPrefetchReporter | Unset):
        review_requested_by (FindingPrefetchReviewRequestedBy | Unset):
        reviewers (FindingPrefetchReviewers | Unset):
        risk_acceptance_set (FindingPrefetchRiskAcceptanceSet | Unset):
        sensitive_issues (FindingPrefetchSensitiveIssues | Unset):
        session_issues (FindingPrefetchSessionIssues | Unset):
        sonarqube_issue (FindingPrefetchSonarqubeIssue | Unset):
        test (FindingPrefetchTest | Unset):
        test_import_set (FindingPrefetchTestImportSet | Unset):
    """

    auth_issues: FindingPrefetchAuthIssues | Unset = UNSET
    author_issues: FindingPrefetchAuthorIssues | Unset = UNSET
    config_issues: FindingPrefetchConfigIssues | Unset = UNSET
    crypto_issues: FindingPrefetchCryptoIssues | Unset = UNSET
    data_issues: FindingPrefetchDataIssues | Unset = UNSET
    defect_review_requested_by: FindingPrefetchDefectReviewRequestedBy | Unset = UNSET
    duplicate_finding: FindingPrefetchDuplicateFinding | Unset = UNSET
    endpoint_set: FindingPrefetchEndpointSet | Unset = UNSET
    endpoints: FindingPrefetchEndpoints | Unset = UNSET
    files: FindingPrefetchFiles | Unset = UNSET
    finding_group_set: FindingPrefetchFindingGroupSet | Unset = UNSET
    found_by: FindingPrefetchFoundBy | Unset = UNSET
    last_reviewed_by: FindingPrefetchLastReviewedBy | Unset = UNSET
    mitigated_by: FindingPrefetchMitigatedBy | Unset = UNSET
    notes: FindingPrefetchNotes | Unset = UNSET
    other_issues: FindingPrefetchOtherIssues | Unset = UNSET
    reporter: FindingPrefetchReporter | Unset = UNSET
    review_requested_by: FindingPrefetchReviewRequestedBy | Unset = UNSET
    reviewers: FindingPrefetchReviewers | Unset = UNSET
    risk_acceptance_set: FindingPrefetchRiskAcceptanceSet | Unset = UNSET
    sensitive_issues: FindingPrefetchSensitiveIssues | Unset = UNSET
    session_issues: FindingPrefetchSessionIssues | Unset = UNSET
    sonarqube_issue: FindingPrefetchSonarqubeIssue | Unset = UNSET
    test: FindingPrefetchTest | Unset = UNSET
    test_import_set: FindingPrefetchTestImportSet | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_issues: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth_issues, Unset):
            auth_issues = self.auth_issues.to_dict()

        author_issues: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author_issues, Unset):
            author_issues = self.author_issues.to_dict()

        config_issues: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config_issues, Unset):
            config_issues = self.config_issues.to_dict()

        crypto_issues: dict[str, Any] | Unset = UNSET
        if not isinstance(self.crypto_issues, Unset):
            crypto_issues = self.crypto_issues.to_dict()

        data_issues: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_issues, Unset):
            data_issues = self.data_issues.to_dict()

        defect_review_requested_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.defect_review_requested_by, Unset):
            defect_review_requested_by = self.defect_review_requested_by.to_dict()

        duplicate_finding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.duplicate_finding, Unset):
            duplicate_finding = self.duplicate_finding.to_dict()

        endpoint_set: dict[str, Any] | Unset = UNSET
        if not isinstance(self.endpoint_set, Unset):
            endpoint_set = self.endpoint_set.to_dict()

        endpoints: dict[str, Any] | Unset = UNSET
        if not isinstance(self.endpoints, Unset):
            endpoints = self.endpoints.to_dict()

        files: dict[str, Any] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_dict()

        finding_group_set: dict[str, Any] | Unset = UNSET
        if not isinstance(self.finding_group_set, Unset):
            finding_group_set = self.finding_group_set.to_dict()

        found_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.found_by, Unset):
            found_by = self.found_by.to_dict()

        last_reviewed_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_reviewed_by, Unset):
            last_reviewed_by = self.last_reviewed_by.to_dict()

        mitigated_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mitigated_by, Unset):
            mitigated_by = self.mitigated_by.to_dict()

        notes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notes, Unset):
            notes = self.notes.to_dict()

        other_issues: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other_issues, Unset):
            other_issues = self.other_issues.to_dict()

        reporter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reporter, Unset):
            reporter = self.reporter.to_dict()

        review_requested_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.review_requested_by, Unset):
            review_requested_by = self.review_requested_by.to_dict()

        reviewers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reviewers, Unset):
            reviewers = self.reviewers.to_dict()

        risk_acceptance_set: dict[str, Any] | Unset = UNSET
        if not isinstance(self.risk_acceptance_set, Unset):
            risk_acceptance_set = self.risk_acceptance_set.to_dict()

        sensitive_issues: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sensitive_issues, Unset):
            sensitive_issues = self.sensitive_issues.to_dict()

        session_issues: dict[str, Any] | Unset = UNSET
        if not isinstance(self.session_issues, Unset):
            session_issues = self.session_issues.to_dict()

        sonarqube_issue: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sonarqube_issue, Unset):
            sonarqube_issue = self.sonarqube_issue.to_dict()

        test: dict[str, Any] | Unset = UNSET
        if not isinstance(self.test, Unset):
            test = self.test.to_dict()

        test_import_set: dict[str, Any] | Unset = UNSET
        if not isinstance(self.test_import_set, Unset):
            test_import_set = self.test_import_set.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_issues is not UNSET:
            field_dict["auth_issues"] = auth_issues
        if author_issues is not UNSET:
            field_dict["author_issues"] = author_issues
        if config_issues is not UNSET:
            field_dict["config_issues"] = config_issues
        if crypto_issues is not UNSET:
            field_dict["crypto_issues"] = crypto_issues
        if data_issues is not UNSET:
            field_dict["data_issues"] = data_issues
        if defect_review_requested_by is not UNSET:
            field_dict["defect_review_requested_by"] = defect_review_requested_by
        if duplicate_finding is not UNSET:
            field_dict["duplicate_finding"] = duplicate_finding
        if endpoint_set is not UNSET:
            field_dict["endpoint_set"] = endpoint_set
        if endpoints is not UNSET:
            field_dict["endpoints"] = endpoints
        if files is not UNSET:
            field_dict["files"] = files
        if finding_group_set is not UNSET:
            field_dict["finding_group_set"] = finding_group_set
        if found_by is not UNSET:
            field_dict["found_by"] = found_by
        if last_reviewed_by is not UNSET:
            field_dict["last_reviewed_by"] = last_reviewed_by
        if mitigated_by is not UNSET:
            field_dict["mitigated_by"] = mitigated_by
        if notes is not UNSET:
            field_dict["notes"] = notes
        if other_issues is not UNSET:
            field_dict["other_issues"] = other_issues
        if reporter is not UNSET:
            field_dict["reporter"] = reporter
        if review_requested_by is not UNSET:
            field_dict["review_requested_by"] = review_requested_by
        if reviewers is not UNSET:
            field_dict["reviewers"] = reviewers
        if risk_acceptance_set is not UNSET:
            field_dict["risk_acceptance_set"] = risk_acceptance_set
        if sensitive_issues is not UNSET:
            field_dict["sensitive_issues"] = sensitive_issues
        if session_issues is not UNSET:
            field_dict["session_issues"] = session_issues
        if sonarqube_issue is not UNSET:
            field_dict["sonarqube_issue"] = sonarqube_issue
        if test is not UNSET:
            field_dict["test"] = test
        if test_import_set is not UNSET:
            field_dict["test_import_set"] = test_import_set

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.finding_prefetch_auth_issues import FindingPrefetchAuthIssues
        from ..models.finding_prefetch_author_issues import FindingPrefetchAuthorIssues
        from ..models.finding_prefetch_config_issues import FindingPrefetchConfigIssues
        from ..models.finding_prefetch_crypto_issues import FindingPrefetchCryptoIssues
        from ..models.finding_prefetch_data_issues import FindingPrefetchDataIssues
        from ..models.finding_prefetch_defect_review_requested_by import (
            FindingPrefetchDefectReviewRequestedBy,
        )
        from ..models.finding_prefetch_duplicate_finding import FindingPrefetchDuplicateFinding
        from ..models.finding_prefetch_endpoint_set import FindingPrefetchEndpointSet
        from ..models.finding_prefetch_endpoints import FindingPrefetchEndpoints
        from ..models.finding_prefetch_files import FindingPrefetchFiles
        from ..models.finding_prefetch_finding_group_set import FindingPrefetchFindingGroupSet
        from ..models.finding_prefetch_found_by import FindingPrefetchFoundBy
        from ..models.finding_prefetch_last_reviewed_by import FindingPrefetchLastReviewedBy
        from ..models.finding_prefetch_mitigated_by import FindingPrefetchMitigatedBy
        from ..models.finding_prefetch_notes import FindingPrefetchNotes
        from ..models.finding_prefetch_other_issues import FindingPrefetchOtherIssues
        from ..models.finding_prefetch_reporter import FindingPrefetchReporter
        from ..models.finding_prefetch_review_requested_by import FindingPrefetchReviewRequestedBy
        from ..models.finding_prefetch_reviewers import FindingPrefetchReviewers
        from ..models.finding_prefetch_risk_acceptance_set import FindingPrefetchRiskAcceptanceSet
        from ..models.finding_prefetch_sensitive_issues import FindingPrefetchSensitiveIssues
        from ..models.finding_prefetch_session_issues import FindingPrefetchSessionIssues
        from ..models.finding_prefetch_sonarqube_issue import FindingPrefetchSonarqubeIssue
        from ..models.finding_prefetch_test import FindingPrefetchTest
        from ..models.finding_prefetch_test_import_set import FindingPrefetchTestImportSet

        d = dict(src_dict)
        _auth_issues = d.pop("auth_issues", UNSET)
        auth_issues: FindingPrefetchAuthIssues | Unset
        if isinstance(_auth_issues, Unset):
            auth_issues = UNSET
        else:
            auth_issues = FindingPrefetchAuthIssues.from_dict(_auth_issues)

        _author_issues = d.pop("author_issues", UNSET)
        author_issues: FindingPrefetchAuthorIssues | Unset
        if isinstance(_author_issues, Unset):
            author_issues = UNSET
        else:
            author_issues = FindingPrefetchAuthorIssues.from_dict(_author_issues)

        _config_issues = d.pop("config_issues", UNSET)
        config_issues: FindingPrefetchConfigIssues | Unset
        if isinstance(_config_issues, Unset):
            config_issues = UNSET
        else:
            config_issues = FindingPrefetchConfigIssues.from_dict(_config_issues)

        _crypto_issues = d.pop("crypto_issues", UNSET)
        crypto_issues: FindingPrefetchCryptoIssues | Unset
        if isinstance(_crypto_issues, Unset):
            crypto_issues = UNSET
        else:
            crypto_issues = FindingPrefetchCryptoIssues.from_dict(_crypto_issues)

        _data_issues = d.pop("data_issues", UNSET)
        data_issues: FindingPrefetchDataIssues | Unset
        if isinstance(_data_issues, Unset):
            data_issues = UNSET
        else:
            data_issues = FindingPrefetchDataIssues.from_dict(_data_issues)

        _defect_review_requested_by = d.pop("defect_review_requested_by", UNSET)
        defect_review_requested_by: FindingPrefetchDefectReviewRequestedBy | Unset
        if isinstance(_defect_review_requested_by, Unset):
            defect_review_requested_by = UNSET
        else:
            defect_review_requested_by = FindingPrefetchDefectReviewRequestedBy.from_dict(
                _defect_review_requested_by
            )

        _duplicate_finding = d.pop("duplicate_finding", UNSET)
        duplicate_finding: FindingPrefetchDuplicateFinding | Unset
        if isinstance(_duplicate_finding, Unset):
            duplicate_finding = UNSET
        else:
            duplicate_finding = FindingPrefetchDuplicateFinding.from_dict(_duplicate_finding)

        _endpoint_set = d.pop("endpoint_set", UNSET)
        endpoint_set: FindingPrefetchEndpointSet | Unset
        if isinstance(_endpoint_set, Unset):
            endpoint_set = UNSET
        else:
            endpoint_set = FindingPrefetchEndpointSet.from_dict(_endpoint_set)

        _endpoints = d.pop("endpoints", UNSET)
        endpoints: FindingPrefetchEndpoints | Unset
        if isinstance(_endpoints, Unset):
            endpoints = UNSET
        else:
            endpoints = FindingPrefetchEndpoints.from_dict(_endpoints)

        _files = d.pop("files", UNSET)
        files: FindingPrefetchFiles | Unset
        if isinstance(_files, Unset):
            files = UNSET
        else:
            files = FindingPrefetchFiles.from_dict(_files)

        _finding_group_set = d.pop("finding_group_set", UNSET)
        finding_group_set: FindingPrefetchFindingGroupSet | Unset
        if isinstance(_finding_group_set, Unset):
            finding_group_set = UNSET
        else:
            finding_group_set = FindingPrefetchFindingGroupSet.from_dict(_finding_group_set)

        _found_by = d.pop("found_by", UNSET)
        found_by: FindingPrefetchFoundBy | Unset
        if isinstance(_found_by, Unset):
            found_by = UNSET
        else:
            found_by = FindingPrefetchFoundBy.from_dict(_found_by)

        _last_reviewed_by = d.pop("last_reviewed_by", UNSET)
        last_reviewed_by: FindingPrefetchLastReviewedBy | Unset
        if isinstance(_last_reviewed_by, Unset):
            last_reviewed_by = UNSET
        else:
            last_reviewed_by = FindingPrefetchLastReviewedBy.from_dict(_last_reviewed_by)

        _mitigated_by = d.pop("mitigated_by", UNSET)
        mitigated_by: FindingPrefetchMitigatedBy | Unset
        if isinstance(_mitigated_by, Unset):
            mitigated_by = UNSET
        else:
            mitigated_by = FindingPrefetchMitigatedBy.from_dict(_mitigated_by)

        _notes = d.pop("notes", UNSET)
        notes: FindingPrefetchNotes | Unset
        if isinstance(_notes, Unset):
            notes = UNSET
        else:
            notes = FindingPrefetchNotes.from_dict(_notes)

        _other_issues = d.pop("other_issues", UNSET)
        other_issues: FindingPrefetchOtherIssues | Unset
        if isinstance(_other_issues, Unset):
            other_issues = UNSET
        else:
            other_issues = FindingPrefetchOtherIssues.from_dict(_other_issues)

        _reporter = d.pop("reporter", UNSET)
        reporter: FindingPrefetchReporter | Unset
        if isinstance(_reporter, Unset):
            reporter = UNSET
        else:
            reporter = FindingPrefetchReporter.from_dict(_reporter)

        _review_requested_by = d.pop("review_requested_by", UNSET)
        review_requested_by: FindingPrefetchReviewRequestedBy | Unset
        if isinstance(_review_requested_by, Unset):
            review_requested_by = UNSET
        else:
            review_requested_by = FindingPrefetchReviewRequestedBy.from_dict(_review_requested_by)

        _reviewers = d.pop("reviewers", UNSET)
        reviewers: FindingPrefetchReviewers | Unset
        if isinstance(_reviewers, Unset):
            reviewers = UNSET
        else:
            reviewers = FindingPrefetchReviewers.from_dict(_reviewers)

        _risk_acceptance_set = d.pop("risk_acceptance_set", UNSET)
        risk_acceptance_set: FindingPrefetchRiskAcceptanceSet | Unset
        if isinstance(_risk_acceptance_set, Unset):
            risk_acceptance_set = UNSET
        else:
            risk_acceptance_set = FindingPrefetchRiskAcceptanceSet.from_dict(_risk_acceptance_set)

        _sensitive_issues = d.pop("sensitive_issues", UNSET)
        sensitive_issues: FindingPrefetchSensitiveIssues | Unset
        if isinstance(_sensitive_issues, Unset):
            sensitive_issues = UNSET
        else:
            sensitive_issues = FindingPrefetchSensitiveIssues.from_dict(_sensitive_issues)

        _session_issues = d.pop("session_issues", UNSET)
        session_issues: FindingPrefetchSessionIssues | Unset
        if isinstance(_session_issues, Unset):
            session_issues = UNSET
        else:
            session_issues = FindingPrefetchSessionIssues.from_dict(_session_issues)

        _sonarqube_issue = d.pop("sonarqube_issue", UNSET)
        sonarqube_issue: FindingPrefetchSonarqubeIssue | Unset
        if isinstance(_sonarqube_issue, Unset):
            sonarqube_issue = UNSET
        else:
            sonarqube_issue = FindingPrefetchSonarqubeIssue.from_dict(_sonarqube_issue)

        _test = d.pop("test", UNSET)
        test: FindingPrefetchTest | Unset
        if isinstance(_test, Unset):
            test = UNSET
        else:
            test = FindingPrefetchTest.from_dict(_test)

        _test_import_set = d.pop("test_import_set", UNSET)
        test_import_set: FindingPrefetchTestImportSet | Unset
        if isinstance(_test_import_set, Unset):
            test_import_set = UNSET
        else:
            test_import_set = FindingPrefetchTestImportSet.from_dict(_test_import_set)

        finding_prefetch = cls(
            auth_issues=auth_issues,
            author_issues=author_issues,
            config_issues=config_issues,
            crypto_issues=crypto_issues,
            data_issues=data_issues,
            defect_review_requested_by=defect_review_requested_by,
            duplicate_finding=duplicate_finding,
            endpoint_set=endpoint_set,
            endpoints=endpoints,
            files=files,
            finding_group_set=finding_group_set,
            found_by=found_by,
            last_reviewed_by=last_reviewed_by,
            mitigated_by=mitigated_by,
            notes=notes,
            other_issues=other_issues,
            reporter=reporter,
            review_requested_by=review_requested_by,
            reviewers=reviewers,
            risk_acceptance_set=risk_acceptance_set,
            sensitive_issues=sensitive_issues,
            session_issues=session_issues,
            sonarqube_issue=sonarqube_issue,
            test=test,
            test_import_set=test_import_set,
        )

        finding_prefetch.additional_properties = d
        return finding_prefetch

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
