from __future__ import annotations

import datetime
from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from .. import types
from ..models.import_scan_request_group_by import ImportScanRequestGroupBy
from ..models.import_scan_request_minimum_severity import ImportScanRequestMinimumSeverity
from ..models.import_scan_request_scan_type import ImportScanRequestScanType
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="ImportScanRequest")


@_attrs_define
class ImportScanRequest:
    """
    Attributes:
        scan_type (ImportScanRequestScanType): * `Acunetix Scan` - Acunetix Scanner
            * `Anchore Engine Scan` - Anchore Engine Scan
            * `Anchore Enterprise Policy Check` - Anchore Enterprise Policy Check
            * `Anchore Grype` - Anchore Grype
            * `AnchoreCTL Policies Report` - AnchoreCTL Policies Report
            * `AnchoreCTL Vuln Report` - AnchoreCTL Vuln Report
            * `AppCheck Web Application Scanner` - AppCheck Web Application Scanner
            * `AppSpider Scan` - AppSpider Scan
            * `Aqua Scan` - Aqua Scan
            * `Arachni Scan` - Arachni Scan
            * `AuditJS Scan` - AuditJS Scan
            * `AWS Inspector2 Scan` - AWS Inspector2 Scan
            * `AWS Prowler Scan` - AWS Prowler Scan
            * `AWS Prowler V3` - AWS Prowler V3
            * `AWS Security Finding Format (ASFF) Scan` - AWS Security Finding Format (ASFF)
            * `AWS Security Hub Scan` - AWS Security Hub Scan
            * `Azure Security Center Recommendations Scan` - Azure Security Center Recommendations Scan
            * `Bandit Scan` - Bandit Scan
            * `Bearer CLI` - Bearer CLI
            * `BlackDuck API` - BlackDuck API
            * `Blackduck Binary Analysis` - Blackduck Binary Analysis
            * `Blackduck Component Risk` - Blackduck Component Risk
            * `Blackduck Hub Scan` - Blackduck Hub Scan
            * `Brakeman Scan` - Brakeman Scan
            * `Bugcrowd API Import` - Bugcrowd API Import
            * `BugCrowd Scan` - BugCrowd Scan
            * `Bundler-Audit Scan` - Bundler-Audit Scan
            * `Burp Dastardly Scan` - Burp Dastardly Scan
            * `Burp Enterprise Scan` - Burp Enterprise Scan (RENAMED to Burp Suite DAST Scan)
            * `Burp REST API` - Burp REST API
            * `Burp Scan` - Burp Scan
            * `Burp GraphQL API` - Burp Suite DAST GraphQL API
            * `Burp Suite DAST Scan` - Burp Suite DAST Scan
            * `CargoAudit Scan` - CargoAudit Scan
            * `Checkmarx CxFlow SAST` - Checkmarx CxFlow SAST
            * `Checkmarx One Scan` - Checkmarx One Scan
            * `Checkmarx OSA` - Checkmarx OSA
            * `Checkmarx Scan` - Checkmarx Scan
            * `Checkmarx Scan detailed` - Checkmarx Scan detailed
            * `Checkov Scan` - Checkov Scan
            * `Chef Inspect Log` - Chef Inspect Log
            * `Choctaw Hog Scan` - Choctaw Hog Scan
            * `Clair Scan` - Clair Scan
            * `Cloudflare Insights` - Cloudflare Insights
            * `Cloudsploit Scan` - Cloudsploit Scan
            * `Cobalt.io API Import` - Cobalt.io API Import
            * `Cobalt.io Scan` - Cobalt.io Scan
            * `Codechecker Report native` - Codechecker Report native
            * `Contrast Scan` - Contrast Scan
            * `Coverity API` - Coverity API
            * `Coverity Scan JSON Report` - Coverity Scan JSON Report
            * `Crashtest Security JSON File` - Crashtest Security JSON File
            * `Crashtest Security XML File` - Crashtest Security XML File
            * `CredScan Scan` - CredScan Scan
            * `Crunch42 Scan` - Crunch42 Scan
            * `Cyberwatch scan (Galeax)` - Cyberwatch scan (Galeax)
            * `CycloneDX Scan` - CycloneDX Scan
            * `Cycognito Scan` - Cycognito Scan
            * `DawnScanner Scan` - DawnScanner Scan
            * `Deepfence Threatmapper Report` - Deepfence Threatmapper Report
            * `Dependency Check Scan` - Dependency Check Scan
            * `Dependency Track Finding Packaging Format (FPF) Export` - Dependency Track Finding Packaging Format (FPF)
            Export
            * `Detect-secrets Scan` - Detect-secrets Scan
            * `docker-bench-security Scan` - docker-bench-security Scan
            * `Dockle Scan` - Dockle Scan
            * `DrHeader JSON Importer` - DrHeader JSON Importer
            * `DSOP Scan` - DSOP Scan
            * `Duroc Hog Scan` - Duroc Hog Scan
            * `Edgescan Scan` - Edgescan Scan
            * `ESLint Scan` - ESLint Scan
            * `Essex Hog Scan` - Essex Hog Scan
            * `Fortify Scan` - Fortify Scan
            * `Generic Findings Import` - Generic Findings Import
            * `Ggshield Scan` - Ggshield Scan
            * `Github SAST Scan` - Github SAST Scan
            * `Github Secrets Detection Report Scan` - Github Secrets Detection Report Scan
            * `Github Vulnerability Scan` - Github Vulnerability Scan
            * `GitLab API Fuzzing Report Scan` - GitLab API Fuzzing Report Scan
            * `GitLab Container Scan` - GitLab Container Scan Scan
            * `GitLab DAST Report` - GitLab DAST Report
            * `GitLab Dependency Scanning Report` - GitLab Dependency Scanning Report
            * `GitLab SAST Report` - GitLab SAST Report
            * `GitLab Secret Detection Report` - GitLab Secret Detection Report
            * `Gitleaks Scan` - Gitleaks Scan
            * `Google Cloud Artifact Vulnerability Scan` - Google Cloud Artifact Vulnerability Scan
            * `Gosec Scanner` - Gosec Scanner
            * `Gottingen Hog Scan` - Gottingen Hog Scan
            * `Govulncheck Scanner` - Govulncheck Scanner
            * `HackerOne Cases` - HackerOne Cases
            * `Hadolint Dockerfile check` - Hadolint Dockerfile check
            * `Harbor Vulnerability Scan` - Harbor Vulnerability Scan
            * `HCL AppScan on Cloud SAST XML` - HCL AppScan on Cloud SAST XML
            * `HCLAppScan XML` - HCLAppScan XML
            * `Horusec Scan` - Horusec Scan
            * `Humble Json Importer` - Humble Json Importer
            * `HuskyCI Report` - HuskyCI Report
            * `Hydra Scan` - Hydra Scan
            * `IBM AppScan DAST` - IBM AppScan DAST
            * `Immuniweb Scan` - Immuniweb Scan
            * `IntSights Report` - IntSights Report
            * `Invicti Scan` - Invicti Scan
            * `JFrog Xray API Summary Artifact Scan` - JFrog Xray API Summary Artifact Scan
            * `JFrog Xray On Demand Binary Scan` - JFrog Xray On Demand Binary Scan
            * `JFrog Xray Scan` - JFrog Xray Scan
            * `JFrog Xray Unified Scan` - JFrog Xray Unified Scan
            * `KICS Scan` - KICS Scan
            * `Kiuwan SCA Scan` - Kiuwan SCA Scan
            * `Kiuwan Scan` - Kiuwan Scan
            * `KrakenD Audit Scan` - KrakenD Audit Scan
            * `kube-bench Scan` - kube-bench Scan
            * `Kubeaudit Scan` - Kubeaudit Scan
            * `KubeHunter Scan` - KubeHunter Scan
            * `Kubescape JSON Importer` - Kubescape JSON Importer
            * `Legitify Scan` - Legitify Scan
            * `Mayhem SARIF Report` - Mayhem SARIF Report
            * `Mend Scan` - Mend Scan
            * `Meterian Scan` - Meterian Scan
            * `Microfocus Webinspect Scan` - Microfocus Webinspect Scan
            * `MobSF Scan` - MobSF Scan
            * `Mobsfscan Scan` - MobSF Scan
            * `MobSF Scorecard Scan` - MobSF Scorecard Scan
            * `Mozilla Observatory Scan` - Mozilla Observatory Scan
            * `MSDefender Parser` - MSDefender Parser
            * `n0s1 Scanner` - n0s1 Scanner
            * `Nancy Scan` - Nancy Scan
            * `Netsparker Scan` - Netsparker Scan
            * `NeuVector (compliance)` - NeuVector (compliance)
            * `NeuVector (REST)` - NeuVector (REST)
            * `Nexpose Scan` - Nexpose Scan
            * `Nikto Scan` - Nikto Scan
            * `Nmap Scan` - Nmap Scan
            * `Node Security Platform Scan` - Node Security Platform Scan
            * `Nosey Parker Scan` - Nosey Parker Scan
            * `NPM Audit Scan` - NPM Audit Scan
            * `NPM Audit v7+ Scan` - NPM Audit v7+ Scan
            * `Nuclei Scan` - Nuclei Scan
            * `OpenReports` - OpenReports
            * `Openscap Vulnerability Scan` - Openscap Vulnerability Scan
            * `OpenVAS Parser` - OpenVAS Parser
            * `OpenVAS Parser v2` - OpenVAS Parser v2
            * `ORT evaluated model Importer` - ORT evaluated model Importer
            * `OssIndex Devaudit SCA Scan Importer` - OssIndex Devaudit SCA Scan Importer
            * `OSV Scan` - OSV Scan
            * `Outpost24 Scan` - Outpost24 Scan
            * `PHP Security Audit v2` - PHP Security Audit v2
            * `PHP Symfony Security Check` - PHP Symfony Security Check
            * `PingCastle` - PingCastle
            * `pip-audit Scan` - pip-audit Scan
            * `PMD Scan` - PMD Scan
            * `Popeye Scan` - Popeye Scan
            * `Progpilot Scan` - Progpilot Scan
            * `Prowler Scan` - Prowler Scan
            * `PTART Report` - PTART Report
            * `PWN SAST` - PWN SAST
            * `Qualys Hacker Guardian Scan` - Qualys Hacker Guardian Scan
            * `Qualys Infrastructure Scan (WebGUI XML)` - Qualys Infrastructure Scan (WebGUI XML)
            * `Qualys Scan` - Qualys Scan
            * `Qualys Webapp Scan` - Qualys Webapp Scan
            * `Rapplex Scan` - Rapplex Scan
            * `Red Hat Satellite` - Red Hat Satellite
            * `Retire.js Scan` - Retire.js Scan
            * `ReversingLabs Spectra Assure` - ReversingLabs Spectra Assure
            * `Risk Recon API Importer` - Risk Recon API Importer
            * `Rubocop Scan` - Rubocop Scan
            * `Rusty Hog Scan` - Rusty Hog Scan
            * `SARIF` - SARIF
            * `Scantist Scan` - Scantist Scan
            * `Scout Suite Scan` - Scout Suite Scan
            * `Semgrep JSON Report` - Semgrep JSON Report
            * `Semgrep Pro JSON Report` - Semgrep Pro JSON Report
            * `SKF Scan` - SKF Scan
            * `Snyk Code Scan` - Snyk Code Scan
            * `Snyk Issue API Scan` - Snyk Issue API Scan
            * `Snyk Scan` - Snyk Scan
            * `Solar Appscreener Scan` - Solar Appscreener Scan Detailed_Results.csv
            * `SonarQube API Import` - SonarQube API Import
            * `SonarQube Scan` - SonarQube Scan
            * `SonarQube Scan detailed` - SonarQube Scan detailed
            * `Sonatype Application Scan` - Sonatype Application Scan
            * `SpotBugs Scan` - SpotBugs Scan
            * `SSH Audit Importer` - SSH Audit Importer
            * `SSL Labs Scan` - SSL Labs Scan
            * `Sslscan` - Sslscan
            * `Sslyze Scan` - Sslyze Scan
            * `SSLyze Scan (JSON)` - SSLyze Scan (JSON)
            * `StackHawk HawkScan` - StackHawk HawkScan
            * `Sysdig CLI Report` - Sysdig CLI Report Scan
            * `Sysdig Vulnerability Report` - Sysdig Vulnerability Report Scan
            * `Talisman Scan` - Talisman Scan
            * `Tenable Scan` - Tenable Scan
            * `Terrascan Scan` - Terrascan Scan
            * `Testssl Scan` - Testssl Scan
            * `TFSec Scan` - TFSec Scan
            * `Threagile risks report` - Threagile risks report
            * `ThreatComposer Scan` - ThreatComposer Scan
            * `Trivy Operator Scan` - Trivy Operator Scan
            * `Trivy Scan` - Trivy Scan
            * `Trufflehog Scan` - Trufflehog Scan
            * `Trufflehog3 Scan` - Trufflehog3 Scan
            * `Trustwave Fusion API Scan` - Trustwave Fusion API Scan
            * `Trustwave Scan (CSV)` - Trustwave Scan (CSV)
            * `Twistlock Image Scan` - Twistlock Image Scan
            * `VCG Scan` - VCG Scan
            * `Veracode Scan` - Veracode Scan
            * `Veracode SourceClear Scan` - Veracode SourceClear Scan
            * `Vulners` - Vulners
            * `Wapiti Scan` - Wapiti Scan
            * `Wazuh` - Wazuh
            * `WFuzz JSON report` - WFuzz JSON report
            * `Whispers Scan` - Whispers Scan
            * `WhiteHat Sentinel` - WhiteHat Sentinel
            * `Wizcli Dir Scan` - Wiz CLI Scan (Directory)
            * `Wizcli IaC Scan` - Wiz CLI Scan (IaC)
            * `Wizcli Img Scan` - Wiz CLI Scan (Image)
            * `Wiz Scan` - Wiz Scan
            * `Wpscan` - Wpscan
            * `Xanitizer Scan` - Xanitizer Scan
            * `Xeol Parser` - Xeol Parser
            * `Yarn Audit Scan` - Yarn Audit Scan
            * `ZAP Scan` - ZAP Scan
            * `Zora Parser` - Zora Parser
        scan_date (datetime.date | Unset): Scan completion date will be used on all findings.
        minimum_severity (ImportScanRequestMinimumSeverity | Unset): Minimum severity level to be imported

            * `Info` - Info
            * `Low` - Low
            * `Medium` - Medium
            * `High` - High
            * `Critical` - Critical Default: ImportScanRequestMinimumSeverity.INFO.
        active (bool | Unset): Force findings to be active/inactive or default to the original tool (None)
        verified (bool | Unset): Force findings to be verified/not verified or default to the original tool (None)
        endpoint_to_add (int | Unset): Enter the ID of an Endpoint that is associated with the target Product. New
            Findings will be added to that Endpoint.
        file (File | Unset):
        product_type_name (str | Unset): Also referred to as 'Organization' name.
        product_name (str | Unset): Also referred to as 'Asset' name.
        engagement_name (str | Unset):
        engagement_end_date (datetime.date | Unset): End Date for Engagement. Default is current time + 365 days.
            Required format year-month-day
        source_code_management_uri (str | Unset): Resource link to source code
        test_title (str | Unset):
        auto_create_context (bool | Unset):
        deduplication_on_engagement (bool | Unset):
        lead (int | None | Unset):
        push_to_jira (bool | Unset):  Default: False.
        environment (str | Unset):
        build_id (str | Unset): ID of the build that was scanned.
        branch_tag (str | Unset): Branch or Tag that was scanned.
        commit_hash (str | Unset): Commit that was scanned.
        api_scan_configuration (int | None | Unset):
        service (str | Unset): A service is a self-contained piece of functionality within a Product. This is an
            optional field which is used in deduplication and closing of old findings when set. This affects the whole
            engagement/product depending on your deduplication scope.
        group_by (ImportScanRequestGroupBy | Unset): Choose an option to automatically group new findings by the chosen
            option.

            * `component_name` - Component Name
            * `component_name+component_version` - Component Name + Version
            * `component_name+component_version+file_path` - Component Name + Version + File path
            * `file_path` - File path
            * `finding_title` - Finding Title
            * `vuln_id_from_tool` - Vulnerability ID from Tool
        create_finding_groups_for_all_findings (bool | Unset): If set to false, finding groups will only be created when
            there is more than one grouped finding Default: True.
        apply_tags_to_findings (bool | Unset): If set to True, the tags will be applied to the findings
        apply_tags_to_endpoints (bool | Unset): If set to True, the tags will be applied to the endpoints
        engagement (int | Unset):
        tags (list[str] | Unset): Add tags that help describe this scan.
        close_old_findings (bool | Unset): Old findings no longer present in the new report get closed as mitigated when
            importing. If service has been set, only the findings for this service will be closed; if no service is set,
            only findings without a service will be closed. This only affects findings within the same engagement. Default:
            False.
        close_old_findings_product_scope (bool | Unset): Old findings no longer present in the new report get closed as
            mitigated when importing. If service has been set, only the findings for this service will be closed; if no
            service is set, only findings without a service will be closed. This only affects findings within the same
            product.By default, it is false meaning that only old findings of the same type in the engagement are in scope.
            Default: False.
        version (str | Unset): Version that was scanned.
    """

    scan_type: ImportScanRequestScanType
    scan_date: datetime.date | Unset = UNSET
    minimum_severity: ImportScanRequestMinimumSeverity | Unset = (
        ImportScanRequestMinimumSeverity.INFO
    )
    active: bool | Unset = UNSET
    verified: bool | Unset = UNSET
    endpoint_to_add: int | Unset = UNSET
    file: File | Unset = UNSET
    product_type_name: str | Unset = UNSET
    product_name: str | Unset = UNSET
    engagement_name: str | Unset = UNSET
    engagement_end_date: datetime.date | Unset = UNSET
    source_code_management_uri: str | Unset = UNSET
    test_title: str | Unset = UNSET
    auto_create_context: bool | Unset = UNSET
    deduplication_on_engagement: bool | Unset = UNSET
    lead: int | None | Unset = UNSET
    push_to_jira: bool | Unset = False
    environment: str | Unset = UNSET
    build_id: str | Unset = UNSET
    branch_tag: str | Unset = UNSET
    commit_hash: str | Unset = UNSET
    api_scan_configuration: int | None | Unset = UNSET
    service: str | Unset = UNSET
    group_by: ImportScanRequestGroupBy | Unset = UNSET
    create_finding_groups_for_all_findings: bool | Unset = True
    apply_tags_to_findings: bool | Unset = UNSET
    apply_tags_to_endpoints: bool | Unset = UNSET
    engagement: int | Unset = UNSET
    tags: list[str] | Unset = UNSET
    close_old_findings: bool | Unset = False
    close_old_findings_product_scope: bool | Unset = False
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scan_type = self.scan_type.value

        scan_date: str | Unset = UNSET
        if not isinstance(self.scan_date, Unset):
            scan_date = self.scan_date.isoformat()

        minimum_severity: str | Unset = UNSET
        if not isinstance(self.minimum_severity, Unset):
            minimum_severity = self.minimum_severity.value

        active = self.active

        verified = self.verified

        endpoint_to_add = self.endpoint_to_add

        file: FileTypes | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        product_type_name = self.product_type_name

        product_name = self.product_name

        engagement_name = self.engagement_name

        engagement_end_date: str | Unset = UNSET
        if not isinstance(self.engagement_end_date, Unset):
            engagement_end_date = self.engagement_end_date.isoformat()

        source_code_management_uri = self.source_code_management_uri

        test_title = self.test_title

        auto_create_context = self.auto_create_context

        deduplication_on_engagement = self.deduplication_on_engagement

        lead: int | None | Unset
        if isinstance(self.lead, Unset):
            lead = UNSET
        else:
            lead = self.lead

        push_to_jira = self.push_to_jira

        environment = self.environment

        build_id = self.build_id

        branch_tag = self.branch_tag

        commit_hash = self.commit_hash

        api_scan_configuration: int | None | Unset
        if isinstance(self.api_scan_configuration, Unset):
            api_scan_configuration = UNSET
        else:
            api_scan_configuration = self.api_scan_configuration

        service = self.service

        group_by: str | Unset = UNSET
        if not isinstance(self.group_by, Unset):
            group_by = self.group_by.value

        create_finding_groups_for_all_findings = self.create_finding_groups_for_all_findings

        apply_tags_to_findings = self.apply_tags_to_findings

        apply_tags_to_endpoints = self.apply_tags_to_endpoints

        engagement = self.engagement

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        close_old_findings = self.close_old_findings

        close_old_findings_product_scope = self.close_old_findings_product_scope

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scan_type": scan_type,
            }
        )
        if scan_date is not UNSET:
            field_dict["scan_date"] = scan_date
        if minimum_severity is not UNSET:
            field_dict["minimum_severity"] = minimum_severity
        if active is not UNSET:
            field_dict["active"] = active
        if verified is not UNSET:
            field_dict["verified"] = verified
        if endpoint_to_add is not UNSET:
            field_dict["endpoint_to_add"] = endpoint_to_add
        if file is not UNSET:
            field_dict["file"] = file
        if product_type_name is not UNSET:
            field_dict["product_type_name"] = product_type_name
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if engagement_name is not UNSET:
            field_dict["engagement_name"] = engagement_name
        if engagement_end_date is not UNSET:
            field_dict["engagement_end_date"] = engagement_end_date
        if source_code_management_uri is not UNSET:
            field_dict["source_code_management_uri"] = source_code_management_uri
        if test_title is not UNSET:
            field_dict["test_title"] = test_title
        if auto_create_context is not UNSET:
            field_dict["auto_create_context"] = auto_create_context
        if deduplication_on_engagement is not UNSET:
            field_dict["deduplication_on_engagement"] = deduplication_on_engagement
        if lead is not UNSET:
            field_dict["lead"] = lead
        if push_to_jira is not UNSET:
            field_dict["push_to_jira"] = push_to_jira
        if environment is not UNSET:
            field_dict["environment"] = environment
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if branch_tag is not UNSET:
            field_dict["branch_tag"] = branch_tag
        if commit_hash is not UNSET:
            field_dict["commit_hash"] = commit_hash
        if api_scan_configuration is not UNSET:
            field_dict["api_scan_configuration"] = api_scan_configuration
        if service is not UNSET:
            field_dict["service"] = service
        if group_by is not UNSET:
            field_dict["group_by"] = group_by
        if create_finding_groups_for_all_findings is not UNSET:
            field_dict["create_finding_groups_for_all_findings"] = (
                create_finding_groups_for_all_findings
            )
        if apply_tags_to_findings is not UNSET:
            field_dict["apply_tags_to_findings"] = apply_tags_to_findings
        if apply_tags_to_endpoints is not UNSET:
            field_dict["apply_tags_to_endpoints"] = apply_tags_to_endpoints
        if engagement is not UNSET:
            field_dict["engagement"] = engagement
        if tags is not UNSET:
            field_dict["tags"] = tags
        if close_old_findings is not UNSET:
            field_dict["close_old_findings"] = close_old_findings
        if close_old_findings_product_scope is not UNSET:
            field_dict["close_old_findings_product_scope"] = close_old_findings_product_scope
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("scan_type", (None, str(self.scan_type.value).encode(), "text/plain")))

        if not isinstance(self.scan_date, Unset):
            files.append(("scan_date", (None, self.scan_date.isoformat().encode(), "text/plain")))

        if not isinstance(self.minimum_severity, Unset):
            files.append(
                (
                    "minimum_severity",
                    (None, str(self.minimum_severity.value).encode(), "text/plain"),
                )
            )

        if not isinstance(self.active, Unset):
            files.append(("active", (None, str(self.active).encode(), "text/plain")))

        if not isinstance(self.verified, Unset):
            files.append(("verified", (None, str(self.verified).encode(), "text/plain")))

        if not isinstance(self.endpoint_to_add, Unset):
            files.append(
                ("endpoint_to_add", (None, str(self.endpoint_to_add).encode(), "text/plain"))
            )

        if not isinstance(self.file, Unset):
            files.append(("file", self.file.to_tuple()))

        if not isinstance(self.product_type_name, Unset):
            files.append(
                ("product_type_name", (None, str(self.product_type_name).encode(), "text/plain"))
            )

        if not isinstance(self.product_name, Unset):
            files.append(("product_name", (None, str(self.product_name).encode(), "text/plain")))

        if not isinstance(self.engagement_name, Unset):
            files.append(
                ("engagement_name", (None, str(self.engagement_name).encode(), "text/plain"))
            )

        if not isinstance(self.engagement_end_date, Unset):
            files.append(
                (
                    "engagement_end_date",
                    (None, self.engagement_end_date.isoformat().encode(), "text/plain"),
                )
            )

        if not isinstance(self.source_code_management_uri, Unset):
            files.append(
                (
                    "source_code_management_uri",
                    (None, str(self.source_code_management_uri).encode(), "text/plain"),
                )
            )

        if not isinstance(self.test_title, Unset):
            files.append(("test_title", (None, str(self.test_title).encode(), "text/plain")))

        if not isinstance(self.auto_create_context, Unset):
            files.append(
                (
                    "auto_create_context",
                    (None, str(self.auto_create_context).encode(), "text/plain"),
                )
            )

        if not isinstance(self.deduplication_on_engagement, Unset):
            files.append(
                (
                    "deduplication_on_engagement",
                    (None, str(self.deduplication_on_engagement).encode(), "text/plain"),
                )
            )

        if not isinstance(self.lead, Unset):
            if isinstance(self.lead, int):
                files.append(("lead", (None, str(self.lead).encode(), "text/plain")))
            else:
                files.append(("lead", (None, str(self.lead).encode(), "text/plain")))

        if not isinstance(self.push_to_jira, Unset):
            files.append(("push_to_jira", (None, str(self.push_to_jira).encode(), "text/plain")))

        if not isinstance(self.environment, Unset):
            files.append(("environment", (None, str(self.environment).encode(), "text/plain")))

        if not isinstance(self.build_id, Unset):
            files.append(("build_id", (None, str(self.build_id).encode(), "text/plain")))

        if not isinstance(self.branch_tag, Unset):
            files.append(("branch_tag", (None, str(self.branch_tag).encode(), "text/plain")))

        if not isinstance(self.commit_hash, Unset):
            files.append(("commit_hash", (None, str(self.commit_hash).encode(), "text/plain")))

        if not isinstance(self.api_scan_configuration, Unset):
            if isinstance(self.api_scan_configuration, int):
                files.append(
                    (
                        "api_scan_configuration",
                        (None, str(self.api_scan_configuration).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "api_scan_configuration",
                        (None, str(self.api_scan_configuration).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.service, Unset):
            files.append(("service", (None, str(self.service).encode(), "text/plain")))

        if not isinstance(self.group_by, Unset):
            files.append(("group_by", (None, str(self.group_by.value).encode(), "text/plain")))

        if not isinstance(self.create_finding_groups_for_all_findings, Unset):
            files.append(
                (
                    "create_finding_groups_for_all_findings",
                    (None, str(self.create_finding_groups_for_all_findings).encode(), "text/plain"),
                )
            )

        if not isinstance(self.apply_tags_to_findings, Unset):
            files.append(
                (
                    "apply_tags_to_findings",
                    (None, str(self.apply_tags_to_findings).encode(), "text/plain"),
                )
            )

        if not isinstance(self.apply_tags_to_endpoints, Unset):
            files.append(
                (
                    "apply_tags_to_endpoints",
                    (None, str(self.apply_tags_to_endpoints).encode(), "text/plain"),
                )
            )

        if not isinstance(self.engagement, Unset):
            files.append(("engagement", (None, str(self.engagement).encode(), "text/plain")))

        if not isinstance(self.tags, Unset):
            for tags_item_element in self.tags:
                files.append(("tags", (None, str(tags_item_element).encode(), "text/plain")))

        if not isinstance(self.close_old_findings, Unset):
            files.append(
                ("close_old_findings", (None, str(self.close_old_findings).encode(), "text/plain"))
            )

        if not isinstance(self.close_old_findings_product_scope, Unset):
            files.append(
                (
                    "close_old_findings_product_scope",
                    (None, str(self.close_old_findings_product_scope).encode(), "text/plain"),
                )
            )

        if not isinstance(self.version, Unset):
            files.append(("version", (None, str(self.version).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scan_type = ImportScanRequestScanType(d.pop("scan_type"))

        _scan_date = d.pop("scan_date", UNSET)
        scan_date: datetime.date | Unset
        if isinstance(_scan_date, Unset):
            scan_date = UNSET
        else:
            scan_date = isoparse(_scan_date).date()

        _minimum_severity = d.pop("minimum_severity", UNSET)
        minimum_severity: ImportScanRequestMinimumSeverity | Unset
        if isinstance(_minimum_severity, Unset):
            minimum_severity = UNSET
        else:
            minimum_severity = ImportScanRequestMinimumSeverity(_minimum_severity)

        active = d.pop("active", UNSET)

        verified = d.pop("verified", UNSET)

        endpoint_to_add = d.pop("endpoint_to_add", UNSET)

        _file = d.pop("file", UNSET)
        file: File | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = File(payload=BytesIO(_file))

        product_type_name = d.pop("product_type_name", UNSET)

        product_name = d.pop("product_name", UNSET)

        engagement_name = d.pop("engagement_name", UNSET)

        _engagement_end_date = d.pop("engagement_end_date", UNSET)
        engagement_end_date: datetime.date | Unset
        if isinstance(_engagement_end_date, Unset):
            engagement_end_date = UNSET
        else:
            engagement_end_date = isoparse(_engagement_end_date).date()

        source_code_management_uri = d.pop("source_code_management_uri", UNSET)

        test_title = d.pop("test_title", UNSET)

        auto_create_context = d.pop("auto_create_context", UNSET)

        deduplication_on_engagement = d.pop("deduplication_on_engagement", UNSET)

        def _parse_lead(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lead = _parse_lead(d.pop("lead", UNSET))

        push_to_jira = d.pop("push_to_jira", UNSET)

        environment = d.pop("environment", UNSET)

        build_id = d.pop("build_id", UNSET)

        branch_tag = d.pop("branch_tag", UNSET)

        commit_hash = d.pop("commit_hash", UNSET)

        def _parse_api_scan_configuration(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        api_scan_configuration = _parse_api_scan_configuration(
            d.pop("api_scan_configuration", UNSET)
        )

        service = d.pop("service", UNSET)

        _group_by = d.pop("group_by", UNSET)
        group_by: ImportScanRequestGroupBy | Unset
        if isinstance(_group_by, Unset):
            group_by = UNSET
        else:
            group_by = ImportScanRequestGroupBy(_group_by)

        create_finding_groups_for_all_findings = d.pop(
            "create_finding_groups_for_all_findings", UNSET
        )

        apply_tags_to_findings = d.pop("apply_tags_to_findings", UNSET)

        apply_tags_to_endpoints = d.pop("apply_tags_to_endpoints", UNSET)

        engagement = d.pop("engagement", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        close_old_findings = d.pop("close_old_findings", UNSET)

        close_old_findings_product_scope = d.pop("close_old_findings_product_scope", UNSET)

        version = d.pop("version", UNSET)

        import_scan_request = cls(
            scan_type=scan_type,
            scan_date=scan_date,
            minimum_severity=minimum_severity,
            active=active,
            verified=verified,
            endpoint_to_add=endpoint_to_add,
            file=file,
            product_type_name=product_type_name,
            product_name=product_name,
            engagement_name=engagement_name,
            engagement_end_date=engagement_end_date,
            source_code_management_uri=source_code_management_uri,
            test_title=test_title,
            auto_create_context=auto_create_context,
            deduplication_on_engagement=deduplication_on_engagement,
            lead=lead,
            push_to_jira=push_to_jira,
            environment=environment,
            build_id=build_id,
            branch_tag=branch_tag,
            commit_hash=commit_hash,
            api_scan_configuration=api_scan_configuration,
            service=service,
            group_by=group_by,
            create_finding_groups_for_all_findings=create_finding_groups_for_all_findings,
            apply_tags_to_findings=apply_tags_to_findings,
            apply_tags_to_endpoints=apply_tags_to_endpoints,
            engagement=engagement,
            tags=tags,
            close_old_findings=close_old_findings,
            close_old_findings_product_scope=close_old_findings_product_scope,
            version=version,
        )

        import_scan_request.additional_properties = d
        return import_scan_request

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
