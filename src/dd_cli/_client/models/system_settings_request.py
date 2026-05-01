from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.system_settings_request_jira_minimum_severity_type_1 import (
    SystemSettingsRequestJiraMinimumSeverityType1,
)
from ..models.system_settings_request_jira_minimum_severity_type_2_type_1 import (
    SystemSettingsRequestJiraMinimumSeverityType2Type1,
)
from ..models.system_settings_request_jira_minimum_severity_type_3_type_1 import (
    SystemSettingsRequestJiraMinimumSeverityType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemSettingsRequest")


@_attrs_define
class SystemSettingsRequest:
    r"""
    Attributes:
        enable_deduplication (bool | Unset): With this setting turned on, DefectDojo deduplicates findings by comparing
            endpoints, cwe fields, and titles. If two findings share a URL and have the same CWE or title, DefectDojo marks
            the recent finding as a duplicate. When deduplication is enabled, a list of deduplicated findings is added to
            the engagement view.
        delete_duplicates (bool | Unset): Requires next setting: maximum number of duplicates to retain.
        max_dupes (int | None | Unset): When enabled, if a single issue reaches the maximum number of duplicates, the
            oldest will be deleted. Duplicate will not be deleted when left empty. A value of 0 will remove all duplicates.
        email_from (str | Unset):
        enable_jira (bool | Unset):
        enable_jira_web_hook (bool | Unset): Please note: It is strongly recommended to use a secret below and / or IP
            whitelist the JIRA server using a proxy such as Nginx.
        disable_jira_webhook_secret (bool | Unset): Allows incoming requests without a secret (discouraged legacy
            behaviour)
        jira_webhook_secret (None | str | Unset): Secret needed in URL for incoming JIRA Webhook
        jira_minimum_severity (None | SystemSettingsRequestJiraMinimumSeverityType1 |
            SystemSettingsRequestJiraMinimumSeverityType2Type1 | SystemSettingsRequestJiraMinimumSeverityType3Type1 |
            Unset): * `Critical` - Critical
            * `High` - High
            * `Medium` - Medium
            * `Low` - Low
            * `Info` - Info
        jira_labels (None | str | Unset): JIRA issue labels space seperated
        add_vulnerability_id_to_jira_label (bool | Unset):
        enable_github (bool | Unset):
        enable_slack_notifications (bool | Unset):
        slack_channel (str | Unset): Optional. Needed if you want to send global notifications.
        slack_token (str | Unset): Token required for interacting with Slack. Get one at https://api.slack.com/tokens
        slack_username (str | Unset): Optional. Will take your bot name otherwise.
        enable_msteams_notifications (bool | Unset):
        msteams_url (str | Unset): The full URL of the incoming webhook
        enable_mail_notifications (bool | Unset):
        mail_notifications_to (str | Unset):
        enable_webhooks_notifications (bool | Unset):
        webhooks_notifications_timeout (int | Unset): How many seconds will DefectDojo waits for response from webhook
            endpoint
        enforce_verified_status (bool | Unset): When enabled, features such as product grading, jira integration,
            metrics, and reports will only interact with verified findings. This setting will override individually scoped
            verified toggles.
        enforce_verified_status_jira (bool | Unset): When enabled, findings must have a verified status to be pushed to
            jira.
        enforce_verified_status_product_grading (bool | Unset): When enabled, findings must have a verified status to be
            considered as part of a product's grading.
        enforce_verified_status_metrics (bool | Unset): When enabled, findings must have a verified status to be counted
            in metric calculations, be included in reports, and filters.
        false_positive_history (bool | Unset): (EXPERIMENTAL) DefectDojo will automatically mark the finding as a false
            positive if an equal finding (according to its dedupe algorithm) has been previously marked as a false positive
            on the same product. ATTENTION: Although the deduplication algorithm is used to determine if a finding should be
            marked as a false positive, this feature will not work if deduplication is enabled since it doesn't make sense
            to use both.
        retroactive_false_positive_history (bool | Unset): (EXPERIMENTAL) FP History will also retroactively mark/unmark
            all existing equal findings in the same product as a false positives. Only works if the False Positive History
            feature is also enabled.
        url_prefix (str | Unset): URL prefix if DefectDojo is installed in it's own virtual subdirectory.
        team_name (str | Unset):
        enable_product_grade (bool | Unset): Displays a grade letter next to a product to show the overall health.
        product_grade_a (int | Unset): Percentage score for an 'A' >=
        product_grade_b (int | Unset): Percentage score for a 'B' >=
        product_grade_c (int | Unset): Percentage score for a 'C' >=
        product_grade_d (int | Unset): Percentage score for a 'D' >=
        product_grade_f (int | Unset): Percentage score for an 'F' <=
        enable_product_tag_inheritance (bool | Unset): Enables product tag inheritance globally for all products. Any
            tags added on a product will automatically be added to all Engagements, Tests, and Findings
        enable_benchmark (bool | Unset): Enables Benchmarks such as the OWASP ASVS (Application Security Verification
            Standard)
        enable_similar_findings (bool | Unset): Enable the query of similar findings on the view finding page. This
            feature can involve potentially large queries and negatively impact performance
        engagement_auto_close (bool | Unset): Closes an engagement after 3 days (default) past due date including last
            update.
        engagement_auto_close_days (int | Unset): Closes an engagement after the specified number of days past due date
            including last update.
        enable_finding_sla (bool | Unset): Enables Finding SLA's for time to remediate.
        enable_notify_sla_active (bool | Unset): Enables Notify when time to remediate according to Finding SLA's is
            breached for active Findings.
        enable_notify_sla_active_verified (bool | Unset): Enables Notify when time to remediate according to Finding
            SLA's is breached for active, verified Findings.
        enable_notify_sla_jira_only (bool | Unset): Enables Notify when time to remediate according to Finding SLA's is
            breached for Findings that are linked to JIRA issues. Notification is disabled for Findings not linked to JIRA
            issues
        enable_notify_sla_exponential_backoff (bool | Unset): Enable an exponential backoff strategy for SLA breach
            notifications, e.g. 1, 2, 4, 8, etc. Otherwise it alerts every day
        allow_anonymous_survey_repsonse (bool | Unset): Enable anyone with a link to the survey to answer a survey
        credentials (str | Unset):
        disclaimer_notifications (str | Unset): Include this custom disclaimer on all notifications
        disclaimer_reports (str | Unset): Include this custom disclaimer on generated reports
        disclaimer_reports_forced (bool | Unset): Disclaimer will be added to all reports even if user didn't selected
            'Include disclaimer'.
        disclaimer_notes (str | Unset): Include this custom disclaimer next to input form for notes
        risk_acceptance_form_default_days (int | None | Unset): Default expiry period for risk acceptance form.
        risk_acceptance_notify_before_expiration (int | None | Unset): Notify X days before risk acceptance expires.
            Leave empty to disable.
        enable_credentials (bool | Unset): With this setting turned off, credentials will be disabled in the user
            interface.
        enable_questionnaires (bool | Unset): With this setting turned off, questionnaires will be disabled in the user
            interface.
        enable_checklists (bool | Unset): With this setting turned off, checklists will be disabled in the user
            interface.
        enable_endpoint_metadata_import (bool | Unset): With this setting turned off, endpoint metadata import will be
            disabled in the user interface.
        enable_user_profile_editable (bool | Unset): When turned on users can edit their profiles
        enable_product_tracking_files (bool | Unset): With this setting turned off, the product tracking files will be
            disabled in the user interface.
        enable_finding_groups (bool | Unset): With this setting turned off, the Finding Groups will be disabled.
        enable_ui_table_based_searching (bool | Unset): With this setting enabled, table headings will contain sort
            buttons for the current page of data in addition to sorting buttons that consider data from all pages.
        enable_calendar (bool | Unset): With this setting turned off, the Calendar will be disabled in the user
            interface.
        enable_cvss3_display (bool | Unset): With this setting turned off, CVSS3 fields will be hidden in the user
            interface.
        enable_cvss4_display (bool | Unset): With this setting turned off, CVSS4 fields will be hidden in the user
            interface.
        default_group_email_pattern (str | Unset): New users will only be assigned to the default group, when their
            email address matches this regex pattern. This is optional condition.
        minimum_password_length (int | Unset): Requires user to set passwords greater than minimum length.
        maximum_password_length (int | Unset): Requires user to set passwords less than maximum length.
        number_character_required (bool | Unset): Requires user passwords to contain at least one digit (0-9).
        special_character_required (bool | Unset): Requires user passwords to contain at least one special character
            (()[]{}|\`~!@#$%^&*_-+=;:'",<>./?).
        lowercase_character_required (bool | Unset): Requires user passwords to contain at least one lowercase letter
            (a-z).
        uppercase_character_required (bool | Unset): Requires user passwords to contain at least one uppercase letter
            (A-Z).
        non_common_password_required (bool | Unset): Requires user passwords to not be part of list of common passwords.
        api_expose_error_details (bool | Unset): When turned on, the API will expose error details in the response.
        filter_string_matching (bool | Unset): When turned on, all filter operations in the UI will require string
            matches rather than ID. This is a performance enhancement to avoid fetching objects unnecessarily.
        default_group (int | None | Unset): New users will be assigned to this group.
        default_group_role (int | None | Unset): New users will be assigned to their default group with this role.
    """

    enable_deduplication: bool | Unset = UNSET
    delete_duplicates: bool | Unset = UNSET
    max_dupes: int | None | Unset = UNSET
    email_from: str | Unset = UNSET
    enable_jira: bool | Unset = UNSET
    enable_jira_web_hook: bool | Unset = UNSET
    disable_jira_webhook_secret: bool | Unset = UNSET
    jira_webhook_secret: None | str | Unset = UNSET
    jira_minimum_severity: (
        None
        | SystemSettingsRequestJiraMinimumSeverityType1
        | SystemSettingsRequestJiraMinimumSeverityType2Type1
        | SystemSettingsRequestJiraMinimumSeverityType3Type1
        | Unset
    ) = UNSET
    jira_labels: None | str | Unset = UNSET
    add_vulnerability_id_to_jira_label: bool | Unset = UNSET
    enable_github: bool | Unset = UNSET
    enable_slack_notifications: bool | Unset = UNSET
    slack_channel: str | Unset = UNSET
    slack_token: str | Unset = UNSET
    slack_username: str | Unset = UNSET
    enable_msteams_notifications: bool | Unset = UNSET
    msteams_url: str | Unset = UNSET
    enable_mail_notifications: bool | Unset = UNSET
    mail_notifications_to: str | Unset = UNSET
    enable_webhooks_notifications: bool | Unset = UNSET
    webhooks_notifications_timeout: int | Unset = UNSET
    enforce_verified_status: bool | Unset = UNSET
    enforce_verified_status_jira: bool | Unset = UNSET
    enforce_verified_status_product_grading: bool | Unset = UNSET
    enforce_verified_status_metrics: bool | Unset = UNSET
    false_positive_history: bool | Unset = UNSET
    retroactive_false_positive_history: bool | Unset = UNSET
    url_prefix: str | Unset = UNSET
    team_name: str | Unset = UNSET
    enable_product_grade: bool | Unset = UNSET
    product_grade_a: int | Unset = UNSET
    product_grade_b: int | Unset = UNSET
    product_grade_c: int | Unset = UNSET
    product_grade_d: int | Unset = UNSET
    product_grade_f: int | Unset = UNSET
    enable_product_tag_inheritance: bool | Unset = UNSET
    enable_benchmark: bool | Unset = UNSET
    enable_similar_findings: bool | Unset = UNSET
    engagement_auto_close: bool | Unset = UNSET
    engagement_auto_close_days: int | Unset = UNSET
    enable_finding_sla: bool | Unset = UNSET
    enable_notify_sla_active: bool | Unset = UNSET
    enable_notify_sla_active_verified: bool | Unset = UNSET
    enable_notify_sla_jira_only: bool | Unset = UNSET
    enable_notify_sla_exponential_backoff: bool | Unset = UNSET
    allow_anonymous_survey_repsonse: bool | Unset = UNSET
    credentials: str | Unset = UNSET
    disclaimer_notifications: str | Unset = UNSET
    disclaimer_reports: str | Unset = UNSET
    disclaimer_reports_forced: bool | Unset = UNSET
    disclaimer_notes: str | Unset = UNSET
    risk_acceptance_form_default_days: int | None | Unset = UNSET
    risk_acceptance_notify_before_expiration: int | None | Unset = UNSET
    enable_credentials: bool | Unset = UNSET
    enable_questionnaires: bool | Unset = UNSET
    enable_checklists: bool | Unset = UNSET
    enable_endpoint_metadata_import: bool | Unset = UNSET
    enable_user_profile_editable: bool | Unset = UNSET
    enable_product_tracking_files: bool | Unset = UNSET
    enable_finding_groups: bool | Unset = UNSET
    enable_ui_table_based_searching: bool | Unset = UNSET
    enable_calendar: bool | Unset = UNSET
    enable_cvss3_display: bool | Unset = UNSET
    enable_cvss4_display: bool | Unset = UNSET
    default_group_email_pattern: str | Unset = UNSET
    minimum_password_length: int | Unset = UNSET
    maximum_password_length: int | Unset = UNSET
    number_character_required: bool | Unset = UNSET
    special_character_required: bool | Unset = UNSET
    lowercase_character_required: bool | Unset = UNSET
    uppercase_character_required: bool | Unset = UNSET
    non_common_password_required: bool | Unset = UNSET
    api_expose_error_details: bool | Unset = UNSET
    filter_string_matching: bool | Unset = UNSET
    default_group: int | None | Unset = UNSET
    default_group_role: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable_deduplication = self.enable_deduplication

        delete_duplicates = self.delete_duplicates

        max_dupes: int | None | Unset
        if isinstance(self.max_dupes, Unset):
            max_dupes = UNSET
        else:
            max_dupes = self.max_dupes

        email_from = self.email_from

        enable_jira = self.enable_jira

        enable_jira_web_hook = self.enable_jira_web_hook

        disable_jira_webhook_secret = self.disable_jira_webhook_secret

        jira_webhook_secret: None | str | Unset
        if isinstance(self.jira_webhook_secret, Unset):
            jira_webhook_secret = UNSET
        else:
            jira_webhook_secret = self.jira_webhook_secret

        jira_minimum_severity: None | str | Unset
        if isinstance(self.jira_minimum_severity, Unset):
            jira_minimum_severity = UNSET
        elif (
            isinstance(self.jira_minimum_severity, SystemSettingsRequestJiraMinimumSeverityType1)
            or isinstance(
                self.jira_minimum_severity, SystemSettingsRequestJiraMinimumSeverityType2Type1
            )
            or isinstance(
                self.jira_minimum_severity, SystemSettingsRequestJiraMinimumSeverityType3Type1
            )
        ):
            jira_minimum_severity = self.jira_minimum_severity.value
        else:
            jira_minimum_severity = self.jira_minimum_severity

        jira_labels: None | str | Unset
        if isinstance(self.jira_labels, Unset):
            jira_labels = UNSET
        else:
            jira_labels = self.jira_labels

        add_vulnerability_id_to_jira_label = self.add_vulnerability_id_to_jira_label

        enable_github = self.enable_github

        enable_slack_notifications = self.enable_slack_notifications

        slack_channel = self.slack_channel

        slack_token = self.slack_token

        slack_username = self.slack_username

        enable_msteams_notifications = self.enable_msteams_notifications

        msteams_url = self.msteams_url

        enable_mail_notifications = self.enable_mail_notifications

        mail_notifications_to = self.mail_notifications_to

        enable_webhooks_notifications = self.enable_webhooks_notifications

        webhooks_notifications_timeout = self.webhooks_notifications_timeout

        enforce_verified_status = self.enforce_verified_status

        enforce_verified_status_jira = self.enforce_verified_status_jira

        enforce_verified_status_product_grading = self.enforce_verified_status_product_grading

        enforce_verified_status_metrics = self.enforce_verified_status_metrics

        false_positive_history = self.false_positive_history

        retroactive_false_positive_history = self.retroactive_false_positive_history

        url_prefix = self.url_prefix

        team_name = self.team_name

        enable_product_grade = self.enable_product_grade

        product_grade_a = self.product_grade_a

        product_grade_b = self.product_grade_b

        product_grade_c = self.product_grade_c

        product_grade_d = self.product_grade_d

        product_grade_f = self.product_grade_f

        enable_product_tag_inheritance = self.enable_product_tag_inheritance

        enable_benchmark = self.enable_benchmark

        enable_similar_findings = self.enable_similar_findings

        engagement_auto_close = self.engagement_auto_close

        engagement_auto_close_days = self.engagement_auto_close_days

        enable_finding_sla = self.enable_finding_sla

        enable_notify_sla_active = self.enable_notify_sla_active

        enable_notify_sla_active_verified = self.enable_notify_sla_active_verified

        enable_notify_sla_jira_only = self.enable_notify_sla_jira_only

        enable_notify_sla_exponential_backoff = self.enable_notify_sla_exponential_backoff

        allow_anonymous_survey_repsonse = self.allow_anonymous_survey_repsonse

        credentials = self.credentials

        disclaimer_notifications = self.disclaimer_notifications

        disclaimer_reports = self.disclaimer_reports

        disclaimer_reports_forced = self.disclaimer_reports_forced

        disclaimer_notes = self.disclaimer_notes

        risk_acceptance_form_default_days: int | None | Unset
        if isinstance(self.risk_acceptance_form_default_days, Unset):
            risk_acceptance_form_default_days = UNSET
        else:
            risk_acceptance_form_default_days = self.risk_acceptance_form_default_days

        risk_acceptance_notify_before_expiration: int | None | Unset
        if isinstance(self.risk_acceptance_notify_before_expiration, Unset):
            risk_acceptance_notify_before_expiration = UNSET
        else:
            risk_acceptance_notify_before_expiration = self.risk_acceptance_notify_before_expiration

        enable_credentials = self.enable_credentials

        enable_questionnaires = self.enable_questionnaires

        enable_checklists = self.enable_checklists

        enable_endpoint_metadata_import = self.enable_endpoint_metadata_import

        enable_user_profile_editable = self.enable_user_profile_editable

        enable_product_tracking_files = self.enable_product_tracking_files

        enable_finding_groups = self.enable_finding_groups

        enable_ui_table_based_searching = self.enable_ui_table_based_searching

        enable_calendar = self.enable_calendar

        enable_cvss3_display = self.enable_cvss3_display

        enable_cvss4_display = self.enable_cvss4_display

        default_group_email_pattern = self.default_group_email_pattern

        minimum_password_length = self.minimum_password_length

        maximum_password_length = self.maximum_password_length

        number_character_required = self.number_character_required

        special_character_required = self.special_character_required

        lowercase_character_required = self.lowercase_character_required

        uppercase_character_required = self.uppercase_character_required

        non_common_password_required = self.non_common_password_required

        api_expose_error_details = self.api_expose_error_details

        filter_string_matching = self.filter_string_matching

        default_group: int | None | Unset
        if isinstance(self.default_group, Unset):
            default_group = UNSET
        else:
            default_group = self.default_group

        default_group_role: int | None | Unset
        if isinstance(self.default_group_role, Unset):
            default_group_role = UNSET
        else:
            default_group_role = self.default_group_role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_deduplication is not UNSET:
            field_dict["enable_deduplication"] = enable_deduplication
        if delete_duplicates is not UNSET:
            field_dict["delete_duplicates"] = delete_duplicates
        if max_dupes is not UNSET:
            field_dict["max_dupes"] = max_dupes
        if email_from is not UNSET:
            field_dict["email_from"] = email_from
        if enable_jira is not UNSET:
            field_dict["enable_jira"] = enable_jira
        if enable_jira_web_hook is not UNSET:
            field_dict["enable_jira_web_hook"] = enable_jira_web_hook
        if disable_jira_webhook_secret is not UNSET:
            field_dict["disable_jira_webhook_secret"] = disable_jira_webhook_secret
        if jira_webhook_secret is not UNSET:
            field_dict["jira_webhook_secret"] = jira_webhook_secret
        if jira_minimum_severity is not UNSET:
            field_dict["jira_minimum_severity"] = jira_minimum_severity
        if jira_labels is not UNSET:
            field_dict["jira_labels"] = jira_labels
        if add_vulnerability_id_to_jira_label is not UNSET:
            field_dict["add_vulnerability_id_to_jira_label"] = add_vulnerability_id_to_jira_label
        if enable_github is not UNSET:
            field_dict["enable_github"] = enable_github
        if enable_slack_notifications is not UNSET:
            field_dict["enable_slack_notifications"] = enable_slack_notifications
        if slack_channel is not UNSET:
            field_dict["slack_channel"] = slack_channel
        if slack_token is not UNSET:
            field_dict["slack_token"] = slack_token
        if slack_username is not UNSET:
            field_dict["slack_username"] = slack_username
        if enable_msteams_notifications is not UNSET:
            field_dict["enable_msteams_notifications"] = enable_msteams_notifications
        if msteams_url is not UNSET:
            field_dict["msteams_url"] = msteams_url
        if enable_mail_notifications is not UNSET:
            field_dict["enable_mail_notifications"] = enable_mail_notifications
        if mail_notifications_to is not UNSET:
            field_dict["mail_notifications_to"] = mail_notifications_to
        if enable_webhooks_notifications is not UNSET:
            field_dict["enable_webhooks_notifications"] = enable_webhooks_notifications
        if webhooks_notifications_timeout is not UNSET:
            field_dict["webhooks_notifications_timeout"] = webhooks_notifications_timeout
        if enforce_verified_status is not UNSET:
            field_dict["enforce_verified_status"] = enforce_verified_status
        if enforce_verified_status_jira is not UNSET:
            field_dict["enforce_verified_status_jira"] = enforce_verified_status_jira
        if enforce_verified_status_product_grading is not UNSET:
            field_dict["enforce_verified_status_product_grading"] = (
                enforce_verified_status_product_grading
            )
        if enforce_verified_status_metrics is not UNSET:
            field_dict["enforce_verified_status_metrics"] = enforce_verified_status_metrics
        if false_positive_history is not UNSET:
            field_dict["false_positive_history"] = false_positive_history
        if retroactive_false_positive_history is not UNSET:
            field_dict["retroactive_false_positive_history"] = retroactive_false_positive_history
        if url_prefix is not UNSET:
            field_dict["url_prefix"] = url_prefix
        if team_name is not UNSET:
            field_dict["team_name"] = team_name
        if enable_product_grade is not UNSET:
            field_dict["enable_product_grade"] = enable_product_grade
        if product_grade_a is not UNSET:
            field_dict["product_grade_a"] = product_grade_a
        if product_grade_b is not UNSET:
            field_dict["product_grade_b"] = product_grade_b
        if product_grade_c is not UNSET:
            field_dict["product_grade_c"] = product_grade_c
        if product_grade_d is not UNSET:
            field_dict["product_grade_d"] = product_grade_d
        if product_grade_f is not UNSET:
            field_dict["product_grade_f"] = product_grade_f
        if enable_product_tag_inheritance is not UNSET:
            field_dict["enable_product_tag_inheritance"] = enable_product_tag_inheritance
        if enable_benchmark is not UNSET:
            field_dict["enable_benchmark"] = enable_benchmark
        if enable_similar_findings is not UNSET:
            field_dict["enable_similar_findings"] = enable_similar_findings
        if engagement_auto_close is not UNSET:
            field_dict["engagement_auto_close"] = engagement_auto_close
        if engagement_auto_close_days is not UNSET:
            field_dict["engagement_auto_close_days"] = engagement_auto_close_days
        if enable_finding_sla is not UNSET:
            field_dict["enable_finding_sla"] = enable_finding_sla
        if enable_notify_sla_active is not UNSET:
            field_dict["enable_notify_sla_active"] = enable_notify_sla_active
        if enable_notify_sla_active_verified is not UNSET:
            field_dict["enable_notify_sla_active_verified"] = enable_notify_sla_active_verified
        if enable_notify_sla_jira_only is not UNSET:
            field_dict["enable_notify_sla_jira_only"] = enable_notify_sla_jira_only
        if enable_notify_sla_exponential_backoff is not UNSET:
            field_dict["enable_notify_sla_exponential_backoff"] = (
                enable_notify_sla_exponential_backoff
            )
        if allow_anonymous_survey_repsonse is not UNSET:
            field_dict["allow_anonymous_survey_repsonse"] = allow_anonymous_survey_repsonse
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if disclaimer_notifications is not UNSET:
            field_dict["disclaimer_notifications"] = disclaimer_notifications
        if disclaimer_reports is not UNSET:
            field_dict["disclaimer_reports"] = disclaimer_reports
        if disclaimer_reports_forced is not UNSET:
            field_dict["disclaimer_reports_forced"] = disclaimer_reports_forced
        if disclaimer_notes is not UNSET:
            field_dict["disclaimer_notes"] = disclaimer_notes
        if risk_acceptance_form_default_days is not UNSET:
            field_dict["risk_acceptance_form_default_days"] = risk_acceptance_form_default_days
        if risk_acceptance_notify_before_expiration is not UNSET:
            field_dict["risk_acceptance_notify_before_expiration"] = (
                risk_acceptance_notify_before_expiration
            )
        if enable_credentials is not UNSET:
            field_dict["enable_credentials"] = enable_credentials
        if enable_questionnaires is not UNSET:
            field_dict["enable_questionnaires"] = enable_questionnaires
        if enable_checklists is not UNSET:
            field_dict["enable_checklists"] = enable_checklists
        if enable_endpoint_metadata_import is not UNSET:
            field_dict["enable_endpoint_metadata_import"] = enable_endpoint_metadata_import
        if enable_user_profile_editable is not UNSET:
            field_dict["enable_user_profile_editable"] = enable_user_profile_editable
        if enable_product_tracking_files is not UNSET:
            field_dict["enable_product_tracking_files"] = enable_product_tracking_files
        if enable_finding_groups is not UNSET:
            field_dict["enable_finding_groups"] = enable_finding_groups
        if enable_ui_table_based_searching is not UNSET:
            field_dict["enable_ui_table_based_searching"] = enable_ui_table_based_searching
        if enable_calendar is not UNSET:
            field_dict["enable_calendar"] = enable_calendar
        if enable_cvss3_display is not UNSET:
            field_dict["enable_cvss3_display"] = enable_cvss3_display
        if enable_cvss4_display is not UNSET:
            field_dict["enable_cvss4_display"] = enable_cvss4_display
        if default_group_email_pattern is not UNSET:
            field_dict["default_group_email_pattern"] = default_group_email_pattern
        if minimum_password_length is not UNSET:
            field_dict["minimum_password_length"] = minimum_password_length
        if maximum_password_length is not UNSET:
            field_dict["maximum_password_length"] = maximum_password_length
        if number_character_required is not UNSET:
            field_dict["number_character_required"] = number_character_required
        if special_character_required is not UNSET:
            field_dict["special_character_required"] = special_character_required
        if lowercase_character_required is not UNSET:
            field_dict["lowercase_character_required"] = lowercase_character_required
        if uppercase_character_required is not UNSET:
            field_dict["uppercase_character_required"] = uppercase_character_required
        if non_common_password_required is not UNSET:
            field_dict["non_common_password_required"] = non_common_password_required
        if api_expose_error_details is not UNSET:
            field_dict["api_expose_error_details"] = api_expose_error_details
        if filter_string_matching is not UNSET:
            field_dict["filter_string_matching"] = filter_string_matching
        if default_group is not UNSET:
            field_dict["default_group"] = default_group
        if default_group_role is not UNSET:
            field_dict["default_group_role"] = default_group_role

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.enable_deduplication, Unset):
            files.append(
                (
                    "enable_deduplication",
                    (None, str(self.enable_deduplication).encode(), "text/plain"),
                )
            )

        if not isinstance(self.delete_duplicates, Unset):
            files.append(
                ("delete_duplicates", (None, str(self.delete_duplicates).encode(), "text/plain"))
            )

        if not isinstance(self.max_dupes, Unset):
            if isinstance(self.max_dupes, int):
                files.append(("max_dupes", (None, str(self.max_dupes).encode(), "text/plain")))
            else:
                files.append(("max_dupes", (None, str(self.max_dupes).encode(), "text/plain")))

        if not isinstance(self.email_from, Unset):
            files.append(("email_from", (None, str(self.email_from).encode(), "text/plain")))

        if not isinstance(self.enable_jira, Unset):
            files.append(("enable_jira", (None, str(self.enable_jira).encode(), "text/plain")))

        if not isinstance(self.enable_jira_web_hook, Unset):
            files.append(
                (
                    "enable_jira_web_hook",
                    (None, str(self.enable_jira_web_hook).encode(), "text/plain"),
                )
            )

        if not isinstance(self.disable_jira_webhook_secret, Unset):
            files.append(
                (
                    "disable_jira_webhook_secret",
                    (None, str(self.disable_jira_webhook_secret).encode(), "text/plain"),
                )
            )

        if not isinstance(self.jira_webhook_secret, Unset):
            if isinstance(self.jira_webhook_secret, str):
                files.append(
                    (
                        "jira_webhook_secret",
                        (None, str(self.jira_webhook_secret).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "jira_webhook_secret",
                        (None, str(self.jira_webhook_secret).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.jira_minimum_severity, Unset):
            if self.jira_minimum_severity is None:
                files.append(
                    (
                        "jira_minimum_severity",
                        (None, str(self.jira_minimum_severity).encode(), "text/plain"),
                    )
                )
            elif isinstance(
                self.jira_minimum_severity, SystemSettingsRequestJiraMinimumSeverityType1
            ) or isinstance(
                self.jira_minimum_severity, SystemSettingsRequestJiraMinimumSeverityType2Type1
            ):
                files.append(
                    (
                        "jira_minimum_severity",
                        (None, str(self.jira_minimum_severity.value).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "jira_minimum_severity",
                        (None, str(self.jira_minimum_severity.value).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.jira_labels, Unset):
            if isinstance(self.jira_labels, str):
                files.append(("jira_labels", (None, str(self.jira_labels).encode(), "text/plain")))
            else:
                files.append(("jira_labels", (None, str(self.jira_labels).encode(), "text/plain")))

        if not isinstance(self.add_vulnerability_id_to_jira_label, Unset):
            files.append(
                (
                    "add_vulnerability_id_to_jira_label",
                    (None, str(self.add_vulnerability_id_to_jira_label).encode(), "text/plain"),
                )
            )

        if not isinstance(self.enable_github, Unset):
            files.append(("enable_github", (None, str(self.enable_github).encode(), "text/plain")))

        if not isinstance(self.enable_slack_notifications, Unset):
            files.append(
                (
                    "enable_slack_notifications",
                    (None, str(self.enable_slack_notifications).encode(), "text/plain"),
                )
            )

        if not isinstance(self.slack_channel, Unset):
            files.append(("slack_channel", (None, str(self.slack_channel).encode(), "text/plain")))

        if not isinstance(self.slack_token, Unset):
            files.append(("slack_token", (None, str(self.slack_token).encode(), "text/plain")))

        if not isinstance(self.slack_username, Unset):
            files.append(
                ("slack_username", (None, str(self.slack_username).encode(), "text/plain"))
            )

        if not isinstance(self.enable_msteams_notifications, Unset):
            files.append(
                (
                    "enable_msteams_notifications",
                    (None, str(self.enable_msteams_notifications).encode(), "text/plain"),
                )
            )

        if not isinstance(self.msteams_url, Unset):
            files.append(("msteams_url", (None, str(self.msteams_url).encode(), "text/plain")))

        if not isinstance(self.enable_mail_notifications, Unset):
            files.append(
                (
                    "enable_mail_notifications",
                    (None, str(self.enable_mail_notifications).encode(), "text/plain"),
                )
            )

        if not isinstance(self.mail_notifications_to, Unset):
            files.append(
                (
                    "mail_notifications_to",
                    (None, str(self.mail_notifications_to).encode(), "text/plain"),
                )
            )

        if not isinstance(self.enable_webhooks_notifications, Unset):
            files.append(
                (
                    "enable_webhooks_notifications",
                    (None, str(self.enable_webhooks_notifications).encode(), "text/plain"),
                )
            )

        if not isinstance(self.webhooks_notifications_timeout, Unset):
            files.append(
                (
                    "webhooks_notifications_timeout",
                    (None, str(self.webhooks_notifications_timeout).encode(), "text/plain"),
                )
            )

        if not isinstance(self.enforce_verified_status, Unset):
            files.append(
                (
                    "enforce_verified_status",
                    (None, str(self.enforce_verified_status).encode(), "text/plain"),
                )
            )

        if not isinstance(self.enforce_verified_status_jira, Unset):
            files.append(
                (
                    "enforce_verified_status_jira",
                    (None, str(self.enforce_verified_status_jira).encode(), "text/plain"),
                )
            )

        if not isinstance(self.enforce_verified_status_product_grading, Unset):
            files.append(
                (
                    "enforce_verified_status_product_grading",
                    (
                        None,
                        str(self.enforce_verified_status_product_grading).encode(),
                        "text/plain",
                    ),
                )
            )

        if not isinstance(self.enforce_verified_status_metrics, Unset):
            files.append(
                (
                    "enforce_verified_status_metrics",
                    (None, str(self.enforce_verified_status_metrics).encode(), "text/plain"),
                )
            )

        if not isinstance(self.false_positive_history, Unset):
            files.append(
                (
                    "false_positive_history",
                    (None, str(self.false_positive_history).encode(), "text/plain"),
                )
            )

        if not isinstance(self.retroactive_false_positive_history, Unset):
            files.append(
                (
                    "retroactive_false_positive_history",
                    (None, str(self.retroactive_false_positive_history).encode(), "text/plain"),
                )
            )

        if not isinstance(self.url_prefix, Unset):
            files.append(("url_prefix", (None, str(self.url_prefix).encode(), "text/plain")))

        if not isinstance(self.team_name, Unset):
            files.append(("team_name", (None, str(self.team_name).encode(), "text/plain")))

        if not isinstance(self.enable_product_grade, Unset):
            files.append(
                (
                    "enable_product_grade",
                    (None, str(self.enable_product_grade).encode(), "text/plain"),
                )
            )

        if not isinstance(self.product_grade_a, Unset):
            files.append(
                ("product_grade_a", (None, str(self.product_grade_a).encode(), "text/plain"))
            )

        if not isinstance(self.product_grade_b, Unset):
            files.append(
                ("product_grade_b", (None, str(self.product_grade_b).encode(), "text/plain"))
            )

        if not isinstance(self.product_grade_c, Unset):
            files.append(
                ("product_grade_c", (None, str(self.product_grade_c).encode(), "text/plain"))
            )

        if not isinstance(self.product_grade_d, Unset):
            files.append(
                ("product_grade_d", (None, str(self.product_grade_d).encode(), "text/plain"))
            )

        if not isinstance(self.product_grade_f, Unset):
            files.append(
                ("product_grade_f", (None, str(self.product_grade_f).encode(), "text/plain"))
            )

        if not isinstance(self.enable_product_tag_inheritance, Unset):
            files.append(
                (
                    "enable_product_tag_inheritance",
                    (None, str(self.enable_product_tag_inheritance).encode(), "text/plain"),
                )
            )

        if not isinstance(self.enable_benchmark, Unset):
            files.append(
                ("enable_benchmark", (None, str(self.enable_benchmark).encode(), "text/plain"))
            )

        if not isinstance(self.enable_similar_findings, Unset):
            files.append(
                (
                    "enable_similar_findings",
                    (None, str(self.enable_similar_findings).encode(), "text/plain"),
                )
            )

        if not isinstance(self.engagement_auto_close, Unset):
            files.append(
                (
                    "engagement_auto_close",
                    (None, str(self.engagement_auto_close).encode(), "text/plain"),
                )
            )

        if not isinstance(self.engagement_auto_close_days, Unset):
            files.append(
                (
                    "engagement_auto_close_days",
                    (None, str(self.engagement_auto_close_days).encode(), "text/plain"),
                )
            )

        if not isinstance(self.enable_finding_sla, Unset):
            files.append(
                ("enable_finding_sla", (None, str(self.enable_finding_sla).encode(), "text/plain"))
            )

        if not isinstance(self.enable_notify_sla_active, Unset):
            files.append(
                (
                    "enable_notify_sla_active",
                    (None, str(self.enable_notify_sla_active).encode(), "text/plain"),
                )
            )

        if not isinstance(self.enable_notify_sla_active_verified, Unset):
            files.append(
                (
                    "enable_notify_sla_active_verified",
                    (None, str(self.enable_notify_sla_active_verified).encode(), "text/plain"),
                )
            )

        if not isinstance(self.enable_notify_sla_jira_only, Unset):
            files.append(
                (
                    "enable_notify_sla_jira_only",
                    (None, str(self.enable_notify_sla_jira_only).encode(), "text/plain"),
                )
            )

        if not isinstance(self.enable_notify_sla_exponential_backoff, Unset):
            files.append(
                (
                    "enable_notify_sla_exponential_backoff",
                    (None, str(self.enable_notify_sla_exponential_backoff).encode(), "text/plain"),
                )
            )

        if not isinstance(self.allow_anonymous_survey_repsonse, Unset):
            files.append(
                (
                    "allow_anonymous_survey_repsonse",
                    (None, str(self.allow_anonymous_survey_repsonse).encode(), "text/plain"),
                )
            )

        if not isinstance(self.credentials, Unset):
            files.append(("credentials", (None, str(self.credentials).encode(), "text/plain")))

        if not isinstance(self.disclaimer_notifications, Unset):
            files.append(
                (
                    "disclaimer_notifications",
                    (None, str(self.disclaimer_notifications).encode(), "text/plain"),
                )
            )

        if not isinstance(self.disclaimer_reports, Unset):
            files.append(
                ("disclaimer_reports", (None, str(self.disclaimer_reports).encode(), "text/plain"))
            )

        if not isinstance(self.disclaimer_reports_forced, Unset):
            files.append(
                (
                    "disclaimer_reports_forced",
                    (None, str(self.disclaimer_reports_forced).encode(), "text/plain"),
                )
            )

        if not isinstance(self.disclaimer_notes, Unset):
            files.append(
                ("disclaimer_notes", (None, str(self.disclaimer_notes).encode(), "text/plain"))
            )

        if not isinstance(self.risk_acceptance_form_default_days, Unset):
            if isinstance(self.risk_acceptance_form_default_days, int):
                files.append(
                    (
                        "risk_acceptance_form_default_days",
                        (None, str(self.risk_acceptance_form_default_days).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "risk_acceptance_form_default_days",
                        (None, str(self.risk_acceptance_form_default_days).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.risk_acceptance_notify_before_expiration, Unset):
            if isinstance(self.risk_acceptance_notify_before_expiration, int):
                files.append(
                    (
                        "risk_acceptance_notify_before_expiration",
                        (
                            None,
                            str(self.risk_acceptance_notify_before_expiration).encode(),
                            "text/plain",
                        ),
                    )
                )
            else:
                files.append(
                    (
                        "risk_acceptance_notify_before_expiration",
                        (
                            None,
                            str(self.risk_acceptance_notify_before_expiration).encode(),
                            "text/plain",
                        ),
                    )
                )

        if not isinstance(self.enable_credentials, Unset):
            files.append(
                ("enable_credentials", (None, str(self.enable_credentials).encode(), "text/plain"))
            )

        if not isinstance(self.enable_questionnaires, Unset):
            files.append(
                (
                    "enable_questionnaires",
                    (None, str(self.enable_questionnaires).encode(), "text/plain"),
                )
            )

        if not isinstance(self.enable_checklists, Unset):
            files.append(
                ("enable_checklists", (None, str(self.enable_checklists).encode(), "text/plain"))
            )

        if not isinstance(self.enable_endpoint_metadata_import, Unset):
            files.append(
                (
                    "enable_endpoint_metadata_import",
                    (None, str(self.enable_endpoint_metadata_import).encode(), "text/plain"),
                )
            )

        if not isinstance(self.enable_user_profile_editable, Unset):
            files.append(
                (
                    "enable_user_profile_editable",
                    (None, str(self.enable_user_profile_editable).encode(), "text/plain"),
                )
            )

        if not isinstance(self.enable_product_tracking_files, Unset):
            files.append(
                (
                    "enable_product_tracking_files",
                    (None, str(self.enable_product_tracking_files).encode(), "text/plain"),
                )
            )

        if not isinstance(self.enable_finding_groups, Unset):
            files.append(
                (
                    "enable_finding_groups",
                    (None, str(self.enable_finding_groups).encode(), "text/plain"),
                )
            )

        if not isinstance(self.enable_ui_table_based_searching, Unset):
            files.append(
                (
                    "enable_ui_table_based_searching",
                    (None, str(self.enable_ui_table_based_searching).encode(), "text/plain"),
                )
            )

        if not isinstance(self.enable_calendar, Unset):
            files.append(
                ("enable_calendar", (None, str(self.enable_calendar).encode(), "text/plain"))
            )

        if not isinstance(self.enable_cvss3_display, Unset):
            files.append(
                (
                    "enable_cvss3_display",
                    (None, str(self.enable_cvss3_display).encode(), "text/plain"),
                )
            )

        if not isinstance(self.enable_cvss4_display, Unset):
            files.append(
                (
                    "enable_cvss4_display",
                    (None, str(self.enable_cvss4_display).encode(), "text/plain"),
                )
            )

        if not isinstance(self.default_group_email_pattern, Unset):
            files.append(
                (
                    "default_group_email_pattern",
                    (None, str(self.default_group_email_pattern).encode(), "text/plain"),
                )
            )

        if not isinstance(self.minimum_password_length, Unset):
            files.append(
                (
                    "minimum_password_length",
                    (None, str(self.minimum_password_length).encode(), "text/plain"),
                )
            )

        if not isinstance(self.maximum_password_length, Unset):
            files.append(
                (
                    "maximum_password_length",
                    (None, str(self.maximum_password_length).encode(), "text/plain"),
                )
            )

        if not isinstance(self.number_character_required, Unset):
            files.append(
                (
                    "number_character_required",
                    (None, str(self.number_character_required).encode(), "text/plain"),
                )
            )

        if not isinstance(self.special_character_required, Unset):
            files.append(
                (
                    "special_character_required",
                    (None, str(self.special_character_required).encode(), "text/plain"),
                )
            )

        if not isinstance(self.lowercase_character_required, Unset):
            files.append(
                (
                    "lowercase_character_required",
                    (None, str(self.lowercase_character_required).encode(), "text/plain"),
                )
            )

        if not isinstance(self.uppercase_character_required, Unset):
            files.append(
                (
                    "uppercase_character_required",
                    (None, str(self.uppercase_character_required).encode(), "text/plain"),
                )
            )

        if not isinstance(self.non_common_password_required, Unset):
            files.append(
                (
                    "non_common_password_required",
                    (None, str(self.non_common_password_required).encode(), "text/plain"),
                )
            )

        if not isinstance(self.api_expose_error_details, Unset):
            files.append(
                (
                    "api_expose_error_details",
                    (None, str(self.api_expose_error_details).encode(), "text/plain"),
                )
            )

        if not isinstance(self.filter_string_matching, Unset):
            files.append(
                (
                    "filter_string_matching",
                    (None, str(self.filter_string_matching).encode(), "text/plain"),
                )
            )

        if not isinstance(self.default_group, Unset):
            if isinstance(self.default_group, int):
                files.append(
                    ("default_group", (None, str(self.default_group).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("default_group", (None, str(self.default_group).encode(), "text/plain"))
                )

        if not isinstance(self.default_group_role, Unset):
            if isinstance(self.default_group_role, int):
                files.append(
                    (
                        "default_group_role",
                        (None, str(self.default_group_role).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "default_group_role",
                        (None, str(self.default_group_role).encode(), "text/plain"),
                    )
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable_deduplication = d.pop("enable_deduplication", UNSET)

        delete_duplicates = d.pop("delete_duplicates", UNSET)

        def _parse_max_dupes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_dupes = _parse_max_dupes(d.pop("max_dupes", UNSET))

        email_from = d.pop("email_from", UNSET)

        enable_jira = d.pop("enable_jira", UNSET)

        enable_jira_web_hook = d.pop("enable_jira_web_hook", UNSET)

        disable_jira_webhook_secret = d.pop("disable_jira_webhook_secret", UNSET)

        def _parse_jira_webhook_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        jira_webhook_secret = _parse_jira_webhook_secret(d.pop("jira_webhook_secret", UNSET))

        def _parse_jira_minimum_severity(
            data: object,
        ) -> (
            None
            | SystemSettingsRequestJiraMinimumSeverityType1
            | SystemSettingsRequestJiraMinimumSeverityType2Type1
            | SystemSettingsRequestJiraMinimumSeverityType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                jira_minimum_severity_type_1 = SystemSettingsRequestJiraMinimumSeverityType1(data)

                return jira_minimum_severity_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                jira_minimum_severity_type_2_type_1 = (
                    SystemSettingsRequestJiraMinimumSeverityType2Type1(data)
                )

                return jira_minimum_severity_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                jira_minimum_severity_type_3_type_1 = (
                    SystemSettingsRequestJiraMinimumSeverityType3Type1(data)
                )

                return jira_minimum_severity_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | SystemSettingsRequestJiraMinimumSeverityType1
                | SystemSettingsRequestJiraMinimumSeverityType2Type1
                | SystemSettingsRequestJiraMinimumSeverityType3Type1
                | Unset,
                data,
            )

        jira_minimum_severity = _parse_jira_minimum_severity(d.pop("jira_minimum_severity", UNSET))

        def _parse_jira_labels(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        jira_labels = _parse_jira_labels(d.pop("jira_labels", UNSET))

        add_vulnerability_id_to_jira_label = d.pop("add_vulnerability_id_to_jira_label", UNSET)

        enable_github = d.pop("enable_github", UNSET)

        enable_slack_notifications = d.pop("enable_slack_notifications", UNSET)

        slack_channel = d.pop("slack_channel", UNSET)

        slack_token = d.pop("slack_token", UNSET)

        slack_username = d.pop("slack_username", UNSET)

        enable_msteams_notifications = d.pop("enable_msteams_notifications", UNSET)

        msteams_url = d.pop("msteams_url", UNSET)

        enable_mail_notifications = d.pop("enable_mail_notifications", UNSET)

        mail_notifications_to = d.pop("mail_notifications_to", UNSET)

        enable_webhooks_notifications = d.pop("enable_webhooks_notifications", UNSET)

        webhooks_notifications_timeout = d.pop("webhooks_notifications_timeout", UNSET)

        enforce_verified_status = d.pop("enforce_verified_status", UNSET)

        enforce_verified_status_jira = d.pop("enforce_verified_status_jira", UNSET)

        enforce_verified_status_product_grading = d.pop(
            "enforce_verified_status_product_grading", UNSET
        )

        enforce_verified_status_metrics = d.pop("enforce_verified_status_metrics", UNSET)

        false_positive_history = d.pop("false_positive_history", UNSET)

        retroactive_false_positive_history = d.pop("retroactive_false_positive_history", UNSET)

        url_prefix = d.pop("url_prefix", UNSET)

        team_name = d.pop("team_name", UNSET)

        enable_product_grade = d.pop("enable_product_grade", UNSET)

        product_grade_a = d.pop("product_grade_a", UNSET)

        product_grade_b = d.pop("product_grade_b", UNSET)

        product_grade_c = d.pop("product_grade_c", UNSET)

        product_grade_d = d.pop("product_grade_d", UNSET)

        product_grade_f = d.pop("product_grade_f", UNSET)

        enable_product_tag_inheritance = d.pop("enable_product_tag_inheritance", UNSET)

        enable_benchmark = d.pop("enable_benchmark", UNSET)

        enable_similar_findings = d.pop("enable_similar_findings", UNSET)

        engagement_auto_close = d.pop("engagement_auto_close", UNSET)

        engagement_auto_close_days = d.pop("engagement_auto_close_days", UNSET)

        enable_finding_sla = d.pop("enable_finding_sla", UNSET)

        enable_notify_sla_active = d.pop("enable_notify_sla_active", UNSET)

        enable_notify_sla_active_verified = d.pop("enable_notify_sla_active_verified", UNSET)

        enable_notify_sla_jira_only = d.pop("enable_notify_sla_jira_only", UNSET)

        enable_notify_sla_exponential_backoff = d.pop(
            "enable_notify_sla_exponential_backoff", UNSET
        )

        allow_anonymous_survey_repsonse = d.pop("allow_anonymous_survey_repsonse", UNSET)

        credentials = d.pop("credentials", UNSET)

        disclaimer_notifications = d.pop("disclaimer_notifications", UNSET)

        disclaimer_reports = d.pop("disclaimer_reports", UNSET)

        disclaimer_reports_forced = d.pop("disclaimer_reports_forced", UNSET)

        disclaimer_notes = d.pop("disclaimer_notes", UNSET)

        def _parse_risk_acceptance_form_default_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        risk_acceptance_form_default_days = _parse_risk_acceptance_form_default_days(
            d.pop("risk_acceptance_form_default_days", UNSET)
        )

        def _parse_risk_acceptance_notify_before_expiration(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        risk_acceptance_notify_before_expiration = _parse_risk_acceptance_notify_before_expiration(
            d.pop("risk_acceptance_notify_before_expiration", UNSET)
        )

        enable_credentials = d.pop("enable_credentials", UNSET)

        enable_questionnaires = d.pop("enable_questionnaires", UNSET)

        enable_checklists = d.pop("enable_checklists", UNSET)

        enable_endpoint_metadata_import = d.pop("enable_endpoint_metadata_import", UNSET)

        enable_user_profile_editable = d.pop("enable_user_profile_editable", UNSET)

        enable_product_tracking_files = d.pop("enable_product_tracking_files", UNSET)

        enable_finding_groups = d.pop("enable_finding_groups", UNSET)

        enable_ui_table_based_searching = d.pop("enable_ui_table_based_searching", UNSET)

        enable_calendar = d.pop("enable_calendar", UNSET)

        enable_cvss3_display = d.pop("enable_cvss3_display", UNSET)

        enable_cvss4_display = d.pop("enable_cvss4_display", UNSET)

        default_group_email_pattern = d.pop("default_group_email_pattern", UNSET)

        minimum_password_length = d.pop("minimum_password_length", UNSET)

        maximum_password_length = d.pop("maximum_password_length", UNSET)

        number_character_required = d.pop("number_character_required", UNSET)

        special_character_required = d.pop("special_character_required", UNSET)

        lowercase_character_required = d.pop("lowercase_character_required", UNSET)

        uppercase_character_required = d.pop("uppercase_character_required", UNSET)

        non_common_password_required = d.pop("non_common_password_required", UNSET)

        api_expose_error_details = d.pop("api_expose_error_details", UNSET)

        filter_string_matching = d.pop("filter_string_matching", UNSET)

        def _parse_default_group(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        default_group = _parse_default_group(d.pop("default_group", UNSET))

        def _parse_default_group_role(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        default_group_role = _parse_default_group_role(d.pop("default_group_role", UNSET))

        system_settings_request = cls(
            enable_deduplication=enable_deduplication,
            delete_duplicates=delete_duplicates,
            max_dupes=max_dupes,
            email_from=email_from,
            enable_jira=enable_jira,
            enable_jira_web_hook=enable_jira_web_hook,
            disable_jira_webhook_secret=disable_jira_webhook_secret,
            jira_webhook_secret=jira_webhook_secret,
            jira_minimum_severity=jira_minimum_severity,
            jira_labels=jira_labels,
            add_vulnerability_id_to_jira_label=add_vulnerability_id_to_jira_label,
            enable_github=enable_github,
            enable_slack_notifications=enable_slack_notifications,
            slack_channel=slack_channel,
            slack_token=slack_token,
            slack_username=slack_username,
            enable_msteams_notifications=enable_msteams_notifications,
            msteams_url=msteams_url,
            enable_mail_notifications=enable_mail_notifications,
            mail_notifications_to=mail_notifications_to,
            enable_webhooks_notifications=enable_webhooks_notifications,
            webhooks_notifications_timeout=webhooks_notifications_timeout,
            enforce_verified_status=enforce_verified_status,
            enforce_verified_status_jira=enforce_verified_status_jira,
            enforce_verified_status_product_grading=enforce_verified_status_product_grading,
            enforce_verified_status_metrics=enforce_verified_status_metrics,
            false_positive_history=false_positive_history,
            retroactive_false_positive_history=retroactive_false_positive_history,
            url_prefix=url_prefix,
            team_name=team_name,
            enable_product_grade=enable_product_grade,
            product_grade_a=product_grade_a,
            product_grade_b=product_grade_b,
            product_grade_c=product_grade_c,
            product_grade_d=product_grade_d,
            product_grade_f=product_grade_f,
            enable_product_tag_inheritance=enable_product_tag_inheritance,
            enable_benchmark=enable_benchmark,
            enable_similar_findings=enable_similar_findings,
            engagement_auto_close=engagement_auto_close,
            engagement_auto_close_days=engagement_auto_close_days,
            enable_finding_sla=enable_finding_sla,
            enable_notify_sla_active=enable_notify_sla_active,
            enable_notify_sla_active_verified=enable_notify_sla_active_verified,
            enable_notify_sla_jira_only=enable_notify_sla_jira_only,
            enable_notify_sla_exponential_backoff=enable_notify_sla_exponential_backoff,
            allow_anonymous_survey_repsonse=allow_anonymous_survey_repsonse,
            credentials=credentials,
            disclaimer_notifications=disclaimer_notifications,
            disclaimer_reports=disclaimer_reports,
            disclaimer_reports_forced=disclaimer_reports_forced,
            disclaimer_notes=disclaimer_notes,
            risk_acceptance_form_default_days=risk_acceptance_form_default_days,
            risk_acceptance_notify_before_expiration=risk_acceptance_notify_before_expiration,
            enable_credentials=enable_credentials,
            enable_questionnaires=enable_questionnaires,
            enable_checklists=enable_checklists,
            enable_endpoint_metadata_import=enable_endpoint_metadata_import,
            enable_user_profile_editable=enable_user_profile_editable,
            enable_product_tracking_files=enable_product_tracking_files,
            enable_finding_groups=enable_finding_groups,
            enable_ui_table_based_searching=enable_ui_table_based_searching,
            enable_calendar=enable_calendar,
            enable_cvss3_display=enable_cvss3_display,
            enable_cvss4_display=enable_cvss4_display,
            default_group_email_pattern=default_group_email_pattern,
            minimum_password_length=minimum_password_length,
            maximum_password_length=maximum_password_length,
            number_character_required=number_character_required,
            special_character_required=special_character_required,
            lowercase_character_required=lowercase_character_required,
            uppercase_character_required=uppercase_character_required,
            non_common_password_required=non_common_password_required,
            api_expose_error_details=api_expose_error_details,
            filter_string_matching=filter_string_matching,
            default_group=default_group,
            default_group_role=default_group_role,
        )

        system_settings_request.additional_properties = d
        return system_settings_request

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
