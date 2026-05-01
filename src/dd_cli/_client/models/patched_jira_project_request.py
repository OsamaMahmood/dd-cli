from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedJIRAProjectRequest")


@_attrs_define
class PatchedJIRAProjectRequest:
    """
    Attributes:
        project_key (str | Unset):
        issue_template_dir (None | str | Unset): Choose the folder containing the Django templates used to render the
            JIRA issue description. These are stored in dojo/templates/issue-trackers. Leave empty to use the default
            jira_full templates.
        component (str | Unset):
        custom_fields (Any | Unset): JIRA custom field JSON mapping of Id to value, e.g. {"customfield_10122": [{"name":
            "8.0.1"}]}
        default_assignee (None | str | Unset): JIRA default assignee (name). If left blank then it defaults to whatever
            is configured in JIRA.
        jira_labels (None | str | Unset): JIRA issue labels space seperated
        add_vulnerability_id_to_jira_label (bool | Unset):
        push_all_issues (bool | Unset): Automatically create JIRA tickets for verified findings, assuming
            enforce_verified_status is True, or for all findings otherwise. Once linked, the JIRA ticket will continue to
            sync, regardless of status in DefectDojo.
        enable_engagement_epic_mapping (bool | Unset):
        epic_issue_type_name (str | Unset): The name of the of structure that represents an Epic
        push_notes (bool | Unset):
        product_jira_sla_notification (bool | Unset):
        risk_acceptance_expiration_notification (bool | Unset):
        enabled (bool | Unset): When disabled, Findings will no longer be pushed to Jira, even if they have already been
            pushed previously.
        jira_instance (int | None | Unset):
        product (int | None | Unset):
        engagement (int | None | Unset):
    """

    project_key: str | Unset = UNSET
    issue_template_dir: None | str | Unset = UNSET
    component: str | Unset = UNSET
    custom_fields: Any | Unset = UNSET
    default_assignee: None | str | Unset = UNSET
    jira_labels: None | str | Unset = UNSET
    add_vulnerability_id_to_jira_label: bool | Unset = UNSET
    push_all_issues: bool | Unset = UNSET
    enable_engagement_epic_mapping: bool | Unset = UNSET
    epic_issue_type_name: str | Unset = UNSET
    push_notes: bool | Unset = UNSET
    product_jira_sla_notification: bool | Unset = UNSET
    risk_acceptance_expiration_notification: bool | Unset = UNSET
    enabled: bool | Unset = UNSET
    jira_instance: int | None | Unset = UNSET
    product: int | None | Unset = UNSET
    engagement: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_key = self.project_key

        issue_template_dir: None | str | Unset
        if isinstance(self.issue_template_dir, Unset):
            issue_template_dir = UNSET
        else:
            issue_template_dir = self.issue_template_dir

        component = self.component

        custom_fields = self.custom_fields

        default_assignee: None | str | Unset
        if isinstance(self.default_assignee, Unset):
            default_assignee = UNSET
        else:
            default_assignee = self.default_assignee

        jira_labels: None | str | Unset
        if isinstance(self.jira_labels, Unset):
            jira_labels = UNSET
        else:
            jira_labels = self.jira_labels

        add_vulnerability_id_to_jira_label = self.add_vulnerability_id_to_jira_label

        push_all_issues = self.push_all_issues

        enable_engagement_epic_mapping = self.enable_engagement_epic_mapping

        epic_issue_type_name = self.epic_issue_type_name

        push_notes = self.push_notes

        product_jira_sla_notification = self.product_jira_sla_notification

        risk_acceptance_expiration_notification = self.risk_acceptance_expiration_notification

        enabled = self.enabled

        jira_instance: int | None | Unset
        if isinstance(self.jira_instance, Unset):
            jira_instance = UNSET
        else:
            jira_instance = self.jira_instance

        product: int | None | Unset
        if isinstance(self.product, Unset):
            product = UNSET
        else:
            product = self.product

        engagement: int | None | Unset
        if isinstance(self.engagement, Unset):
            engagement = UNSET
        else:
            engagement = self.engagement

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_key is not UNSET:
            field_dict["project_key"] = project_key
        if issue_template_dir is not UNSET:
            field_dict["issue_template_dir"] = issue_template_dir
        if component is not UNSET:
            field_dict["component"] = component
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if default_assignee is not UNSET:
            field_dict["default_assignee"] = default_assignee
        if jira_labels is not UNSET:
            field_dict["jira_labels"] = jira_labels
        if add_vulnerability_id_to_jira_label is not UNSET:
            field_dict["add_vulnerability_id_to_jira_label"] = add_vulnerability_id_to_jira_label
        if push_all_issues is not UNSET:
            field_dict["push_all_issues"] = push_all_issues
        if enable_engagement_epic_mapping is not UNSET:
            field_dict["enable_engagement_epic_mapping"] = enable_engagement_epic_mapping
        if epic_issue_type_name is not UNSET:
            field_dict["epic_issue_type_name"] = epic_issue_type_name
        if push_notes is not UNSET:
            field_dict["push_notes"] = push_notes
        if product_jira_sla_notification is not UNSET:
            field_dict["product_jira_sla_notification"] = product_jira_sla_notification
        if risk_acceptance_expiration_notification is not UNSET:
            field_dict["risk_acceptance_expiration_notification"] = (
                risk_acceptance_expiration_notification
            )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if jira_instance is not UNSET:
            field_dict["jira_instance"] = jira_instance
        if product is not UNSET:
            field_dict["product"] = product
        if engagement is not UNSET:
            field_dict["engagement"] = engagement

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.project_key, Unset):
            files.append(("project_key", (None, str(self.project_key).encode(), "text/plain")))

        if not isinstance(self.issue_template_dir, Unset):
            if isinstance(self.issue_template_dir, str):
                files.append(
                    (
                        "issue_template_dir",
                        (None, str(self.issue_template_dir).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "issue_template_dir",
                        (None, str(self.issue_template_dir).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.component, Unset):
            files.append(("component", (None, str(self.component).encode(), "text/plain")))

        if not isinstance(self.custom_fields, Unset):
            files.append(("custom_fields", (None, str(self.custom_fields).encode(), "text/plain")))

        if not isinstance(self.default_assignee, Unset):
            if isinstance(self.default_assignee, str):
                files.append(
                    ("default_assignee", (None, str(self.default_assignee).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("default_assignee", (None, str(self.default_assignee).encode(), "text/plain"))
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

        if not isinstance(self.push_all_issues, Unset):
            files.append(
                ("push_all_issues", (None, str(self.push_all_issues).encode(), "text/plain"))
            )

        if not isinstance(self.enable_engagement_epic_mapping, Unset):
            files.append(
                (
                    "enable_engagement_epic_mapping",
                    (None, str(self.enable_engagement_epic_mapping).encode(), "text/plain"),
                )
            )

        if not isinstance(self.epic_issue_type_name, Unset):
            files.append(
                (
                    "epic_issue_type_name",
                    (None, str(self.epic_issue_type_name).encode(), "text/plain"),
                )
            )

        if not isinstance(self.push_notes, Unset):
            files.append(("push_notes", (None, str(self.push_notes).encode(), "text/plain")))

        if not isinstance(self.product_jira_sla_notification, Unset):
            files.append(
                (
                    "product_jira_sla_notification",
                    (None, str(self.product_jira_sla_notification).encode(), "text/plain"),
                )
            )

        if not isinstance(self.risk_acceptance_expiration_notification, Unset):
            files.append(
                (
                    "risk_acceptance_expiration_notification",
                    (
                        None,
                        str(self.risk_acceptance_expiration_notification).encode(),
                        "text/plain",
                    ),
                )
            )

        if not isinstance(self.enabled, Unset):
            files.append(("enabled", (None, str(self.enabled).encode(), "text/plain")))

        if not isinstance(self.jira_instance, Unset):
            if isinstance(self.jira_instance, int):
                files.append(
                    ("jira_instance", (None, str(self.jira_instance).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("jira_instance", (None, str(self.jira_instance).encode(), "text/plain"))
                )

        if not isinstance(self.product, Unset):
            if isinstance(self.product, int):
                files.append(("product", (None, str(self.product).encode(), "text/plain")))
            else:
                files.append(("product", (None, str(self.product).encode(), "text/plain")))

        if not isinstance(self.engagement, Unset):
            if isinstance(self.engagement, int):
                files.append(("engagement", (None, str(self.engagement).encode(), "text/plain")))
            else:
                files.append(("engagement", (None, str(self.engagement).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_key = d.pop("project_key", UNSET)

        def _parse_issue_template_dir(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issue_template_dir = _parse_issue_template_dir(d.pop("issue_template_dir", UNSET))

        component = d.pop("component", UNSET)

        custom_fields = d.pop("custom_fields", UNSET)

        def _parse_default_assignee(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_assignee = _parse_default_assignee(d.pop("default_assignee", UNSET))

        def _parse_jira_labels(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        jira_labels = _parse_jira_labels(d.pop("jira_labels", UNSET))

        add_vulnerability_id_to_jira_label = d.pop("add_vulnerability_id_to_jira_label", UNSET)

        push_all_issues = d.pop("push_all_issues", UNSET)

        enable_engagement_epic_mapping = d.pop("enable_engagement_epic_mapping", UNSET)

        epic_issue_type_name = d.pop("epic_issue_type_name", UNSET)

        push_notes = d.pop("push_notes", UNSET)

        product_jira_sla_notification = d.pop("product_jira_sla_notification", UNSET)

        risk_acceptance_expiration_notification = d.pop(
            "risk_acceptance_expiration_notification", UNSET
        )

        enabled = d.pop("enabled", UNSET)

        def _parse_jira_instance(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        jira_instance = _parse_jira_instance(d.pop("jira_instance", UNSET))

        def _parse_product(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        product = _parse_product(d.pop("product", UNSET))

        def _parse_engagement(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        engagement = _parse_engagement(d.pop("engagement", UNSET))

        patched_jira_project_request = cls(
            project_key=project_key,
            issue_template_dir=issue_template_dir,
            component=component,
            custom_fields=custom_fields,
            default_assignee=default_assignee,
            jira_labels=jira_labels,
            add_vulnerability_id_to_jira_label=add_vulnerability_id_to_jira_label,
            push_all_issues=push_all_issues,
            enable_engagement_epic_mapping=enable_engagement_epic_mapping,
            epic_issue_type_name=epic_issue_type_name,
            push_notes=push_notes,
            product_jira_sla_notification=product_jira_sla_notification,
            risk_acceptance_expiration_notification=risk_acceptance_expiration_notification,
            enabled=enabled,
            jira_instance=jira_instance,
            product=product,
            engagement=engagement,
        )

        patched_jira_project_request.additional_properties = d
        return patched_jira_project_request

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
