from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.jira_instance_default_issue_type import JIRAInstanceDefaultIssueType
from ..types import UNSET, Unset

T = TypeVar("T", bound="JIRAInstance")


@_attrs_define
class JIRAInstance:
    """
    Attributes:
        id (int):
        url (str): For more information how to configure Jira, read the DefectDojo documentation.
        username (str): Username or Email Address, see DefectDojo documentation for more information.
        epic_name_id (int): To obtain the 'Epic name id' visit https://<YOUR JIRA URL>/rest/api/2/field and search for
            Epic Name. Copy the number out of cf[number] and paste it here.
        open_status_key (int): Transition ID to Re-Open JIRA issues, visit https://<YOUR JIRA
            URL>/rest/api/latest/issue/<ANY VALID ISSUE KEY>/transitions?expand=transitions.fields to find the ID for your
            JIRA instance
        close_status_key (int): Transition ID to Close JIRA issues, visit https://<YOUR JIRA
            URL>/rest/api/latest/issue/<ANY VALID ISSUE KEY>/transitions?expand=transitions.fields to find the ID for your
            JIRA instance
        info_mapping_severity (str): Maps to the 'Priority' field in Jira. For example: Info
        low_mapping_severity (str): Maps to the 'Priority' field in Jira. For example: Low
        medium_mapping_severity (str): Maps to the 'Priority' field in Jira. For example: Medium
        high_mapping_severity (str): Maps to the 'Priority' field in Jira. For example: High
        critical_mapping_severity (str): Maps to the 'Priority' field in Jira. For example: Critical
        configuration_name (str | Unset): Enter a name to give to this configuration
        default_issue_type (JIRAInstanceDefaultIssueType | Unset): You can define extra issue types in settings.py

            * `Task` - Task
            * `Story` - Story
            * `Epic` - Epic
            * `Spike` - Spike
            * `Bug` - Bug
            * `Security` - Security
        issue_template_dir (None | str | Unset): Choose the folder containing the Django templates used to render the
            JIRA issue description. These are stored in dojo/templates/issue-trackers. Leave empty to use the default
            jira_full templates.
        finding_text (None | str | Unset): Additional text that will be added to the finding in Jira. For example
            including how the finding was created or who to contact for more information.
        accepted_mapping_resolution (None | str | Unset): JIRA issues that are closed in JIRA with one of these
            resolutions will result in the Finding becoming Risk Accepted in Defect Dojo. JIRA issues that are closed in
            JIRA with one of these resolutions will result in the Finding becoming Risk Accepted in Defect Dojo. The
            expiration time for this Risk Acceptance will be determined by the "Risk acceptance form default days" in
            "System Settings". This mapping is not used when Findings are pushed to JIRA. In that case the Risk Accepted
            Findings are closed in JIRA and JIRA sets the default resolution.
        false_positive_mapping_resolution (None | str | Unset): JIRA issues that are closed in JIRA with one of these
            resolutions will result in the Finding being marked as False Positive Defect Dojo. This mapping is not used when
            Findings are pushed to JIRA. In that case the Finding is closed in JIRA and JIRA sets the default resolution.
        global_jira_sla_notification (bool | Unset): This setting can be overidden at the Product level
        finding_jira_sync (bool | Unset): If enabled, this will sync changes to a Finding automatically to JIRA
    """

    id: int
    url: str
    username: str
    epic_name_id: int
    open_status_key: int
    close_status_key: int
    info_mapping_severity: str
    low_mapping_severity: str
    medium_mapping_severity: str
    high_mapping_severity: str
    critical_mapping_severity: str
    configuration_name: str | Unset = UNSET
    default_issue_type: JIRAInstanceDefaultIssueType | Unset = UNSET
    issue_template_dir: None | str | Unset = UNSET
    finding_text: None | str | Unset = UNSET
    accepted_mapping_resolution: None | str | Unset = UNSET
    false_positive_mapping_resolution: None | str | Unset = UNSET
    global_jira_sla_notification: bool | Unset = UNSET
    finding_jira_sync: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        username = self.username

        epic_name_id = self.epic_name_id

        open_status_key = self.open_status_key

        close_status_key = self.close_status_key

        info_mapping_severity = self.info_mapping_severity

        low_mapping_severity = self.low_mapping_severity

        medium_mapping_severity = self.medium_mapping_severity

        high_mapping_severity = self.high_mapping_severity

        critical_mapping_severity = self.critical_mapping_severity

        configuration_name = self.configuration_name

        default_issue_type: str | Unset = UNSET
        if not isinstance(self.default_issue_type, Unset):
            default_issue_type = self.default_issue_type.value

        issue_template_dir: None | str | Unset
        if isinstance(self.issue_template_dir, Unset):
            issue_template_dir = UNSET
        else:
            issue_template_dir = self.issue_template_dir

        finding_text: None | str | Unset
        if isinstance(self.finding_text, Unset):
            finding_text = UNSET
        else:
            finding_text = self.finding_text

        accepted_mapping_resolution: None | str | Unset
        if isinstance(self.accepted_mapping_resolution, Unset):
            accepted_mapping_resolution = UNSET
        else:
            accepted_mapping_resolution = self.accepted_mapping_resolution

        false_positive_mapping_resolution: None | str | Unset
        if isinstance(self.false_positive_mapping_resolution, Unset):
            false_positive_mapping_resolution = UNSET
        else:
            false_positive_mapping_resolution = self.false_positive_mapping_resolution

        global_jira_sla_notification = self.global_jira_sla_notification

        finding_jira_sync = self.finding_jira_sync

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "username": username,
                "epic_name_id": epic_name_id,
                "open_status_key": open_status_key,
                "close_status_key": close_status_key,
                "info_mapping_severity": info_mapping_severity,
                "low_mapping_severity": low_mapping_severity,
                "medium_mapping_severity": medium_mapping_severity,
                "high_mapping_severity": high_mapping_severity,
                "critical_mapping_severity": critical_mapping_severity,
            }
        )
        if configuration_name is not UNSET:
            field_dict["configuration_name"] = configuration_name
        if default_issue_type is not UNSET:
            field_dict["default_issue_type"] = default_issue_type
        if issue_template_dir is not UNSET:
            field_dict["issue_template_dir"] = issue_template_dir
        if finding_text is not UNSET:
            field_dict["finding_text"] = finding_text
        if accepted_mapping_resolution is not UNSET:
            field_dict["accepted_mapping_resolution"] = accepted_mapping_resolution
        if false_positive_mapping_resolution is not UNSET:
            field_dict["false_positive_mapping_resolution"] = false_positive_mapping_resolution
        if global_jira_sla_notification is not UNSET:
            field_dict["global_jira_sla_notification"] = global_jira_sla_notification
        if finding_jira_sync is not UNSET:
            field_dict["finding_jira_sync"] = finding_jira_sync

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        username = d.pop("username")

        epic_name_id = d.pop("epic_name_id")

        open_status_key = d.pop("open_status_key")

        close_status_key = d.pop("close_status_key")

        info_mapping_severity = d.pop("info_mapping_severity")

        low_mapping_severity = d.pop("low_mapping_severity")

        medium_mapping_severity = d.pop("medium_mapping_severity")

        high_mapping_severity = d.pop("high_mapping_severity")

        critical_mapping_severity = d.pop("critical_mapping_severity")

        configuration_name = d.pop("configuration_name", UNSET)

        _default_issue_type = d.pop("default_issue_type", UNSET)
        default_issue_type: JIRAInstanceDefaultIssueType | Unset
        if isinstance(_default_issue_type, Unset):
            default_issue_type = UNSET
        else:
            default_issue_type = JIRAInstanceDefaultIssueType(_default_issue_type)

        def _parse_issue_template_dir(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issue_template_dir = _parse_issue_template_dir(d.pop("issue_template_dir", UNSET))

        def _parse_finding_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        finding_text = _parse_finding_text(d.pop("finding_text", UNSET))

        def _parse_accepted_mapping_resolution(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accepted_mapping_resolution = _parse_accepted_mapping_resolution(
            d.pop("accepted_mapping_resolution", UNSET)
        )

        def _parse_false_positive_mapping_resolution(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        false_positive_mapping_resolution = _parse_false_positive_mapping_resolution(
            d.pop("false_positive_mapping_resolution", UNSET)
        )

        global_jira_sla_notification = d.pop("global_jira_sla_notification", UNSET)

        finding_jira_sync = d.pop("finding_jira_sync", UNSET)

        jira_instance = cls(
            id=id,
            url=url,
            username=username,
            epic_name_id=epic_name_id,
            open_status_key=open_status_key,
            close_status_key=close_status_key,
            info_mapping_severity=info_mapping_severity,
            low_mapping_severity=low_mapping_severity,
            medium_mapping_severity=medium_mapping_severity,
            high_mapping_severity=high_mapping_severity,
            critical_mapping_severity=critical_mapping_severity,
            configuration_name=configuration_name,
            default_issue_type=default_issue_type,
            issue_template_dir=issue_template_dir,
            finding_text=finding_text,
            accepted_mapping_resolution=accepted_mapping_resolution,
            false_positive_mapping_resolution=false_positive_mapping_resolution,
            global_jira_sla_notification=global_jira_sla_notification,
            finding_jira_sync=finding_jira_sync,
        )

        jira_instance.additional_properties = d
        return jira_instance

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
