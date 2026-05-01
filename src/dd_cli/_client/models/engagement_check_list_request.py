from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="EngagementCheckListRequest")


@_attrs_define
class EngagementCheckListRequest:
    """
    Attributes:
        session_management (str | Unset):
        encryption_crypto (str | Unset):
        configuration_management (str | Unset):
        authentication (str | Unset):
        authorization_and_access_control (str | Unset):
        data_input_sanitization_validation (str | Unset):
        sensitive_data (str | Unset):
        other (str | Unset):
        session_issues (list[int] | Unset):
        crypto_issues (list[int] | Unset):
        config_issues (list[int] | Unset):
        auth_issues (list[int] | Unset):
        author_issues (list[int] | Unset):
        data_issues (list[int] | Unset):
        sensitive_issues (list[int] | Unset):
        other_issues (list[int] | Unset):
    """

    session_management: str | Unset = UNSET
    encryption_crypto: str | Unset = UNSET
    configuration_management: str | Unset = UNSET
    authentication: str | Unset = UNSET
    authorization_and_access_control: str | Unset = UNSET
    data_input_sanitization_validation: str | Unset = UNSET
    sensitive_data: str | Unset = UNSET
    other: str | Unset = UNSET
    session_issues: list[int] | Unset = UNSET
    crypto_issues: list[int] | Unset = UNSET
    config_issues: list[int] | Unset = UNSET
    auth_issues: list[int] | Unset = UNSET
    author_issues: list[int] | Unset = UNSET
    data_issues: list[int] | Unset = UNSET
    sensitive_issues: list[int] | Unset = UNSET
    other_issues: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_management = self.session_management

        encryption_crypto = self.encryption_crypto

        configuration_management = self.configuration_management

        authentication = self.authentication

        authorization_and_access_control = self.authorization_and_access_control

        data_input_sanitization_validation = self.data_input_sanitization_validation

        sensitive_data = self.sensitive_data

        other = self.other

        session_issues: list[int] | Unset = UNSET
        if not isinstance(self.session_issues, Unset):
            session_issues = self.session_issues

        crypto_issues: list[int] | Unset = UNSET
        if not isinstance(self.crypto_issues, Unset):
            crypto_issues = self.crypto_issues

        config_issues: list[int] | Unset = UNSET
        if not isinstance(self.config_issues, Unset):
            config_issues = self.config_issues

        auth_issues: list[int] | Unset = UNSET
        if not isinstance(self.auth_issues, Unset):
            auth_issues = self.auth_issues

        author_issues: list[int] | Unset = UNSET
        if not isinstance(self.author_issues, Unset):
            author_issues = self.author_issues

        data_issues: list[int] | Unset = UNSET
        if not isinstance(self.data_issues, Unset):
            data_issues = self.data_issues

        sensitive_issues: list[int] | Unset = UNSET
        if not isinstance(self.sensitive_issues, Unset):
            sensitive_issues = self.sensitive_issues

        other_issues: list[int] | Unset = UNSET
        if not isinstance(self.other_issues, Unset):
            other_issues = self.other_issues

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if session_management is not UNSET:
            field_dict["session_management"] = session_management
        if encryption_crypto is not UNSET:
            field_dict["encryption_crypto"] = encryption_crypto
        if configuration_management is not UNSET:
            field_dict["configuration_management"] = configuration_management
        if authentication is not UNSET:
            field_dict["authentication"] = authentication
        if authorization_and_access_control is not UNSET:
            field_dict["authorization_and_access_control"] = authorization_and_access_control
        if data_input_sanitization_validation is not UNSET:
            field_dict["data_input_sanitization_validation"] = data_input_sanitization_validation
        if sensitive_data is not UNSET:
            field_dict["sensitive_data"] = sensitive_data
        if other is not UNSET:
            field_dict["other"] = other
        if session_issues is not UNSET:
            field_dict["session_issues"] = session_issues
        if crypto_issues is not UNSET:
            field_dict["crypto_issues"] = crypto_issues
        if config_issues is not UNSET:
            field_dict["config_issues"] = config_issues
        if auth_issues is not UNSET:
            field_dict["auth_issues"] = auth_issues
        if author_issues is not UNSET:
            field_dict["author_issues"] = author_issues
        if data_issues is not UNSET:
            field_dict["data_issues"] = data_issues
        if sensitive_issues is not UNSET:
            field_dict["sensitive_issues"] = sensitive_issues
        if other_issues is not UNSET:
            field_dict["other_issues"] = other_issues

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.session_management, Unset):
            files.append(
                ("session_management", (None, str(self.session_management).encode(), "text/plain"))
            )

        if not isinstance(self.encryption_crypto, Unset):
            files.append(
                ("encryption_crypto", (None, str(self.encryption_crypto).encode(), "text/plain"))
            )

        if not isinstance(self.configuration_management, Unset):
            files.append(
                (
                    "configuration_management",
                    (None, str(self.configuration_management).encode(), "text/plain"),
                )
            )

        if not isinstance(self.authentication, Unset):
            files.append(
                ("authentication", (None, str(self.authentication).encode(), "text/plain"))
            )

        if not isinstance(self.authorization_and_access_control, Unset):
            files.append(
                (
                    "authorization_and_access_control",
                    (None, str(self.authorization_and_access_control).encode(), "text/plain"),
                )
            )

        if not isinstance(self.data_input_sanitization_validation, Unset):
            files.append(
                (
                    "data_input_sanitization_validation",
                    (None, str(self.data_input_sanitization_validation).encode(), "text/plain"),
                )
            )

        if not isinstance(self.sensitive_data, Unset):
            files.append(
                ("sensitive_data", (None, str(self.sensitive_data).encode(), "text/plain"))
            )

        if not isinstance(self.other, Unset):
            files.append(("other", (None, str(self.other).encode(), "text/plain")))

        if not isinstance(self.session_issues, Unset):
            for session_issues_item_element in self.session_issues:
                files.append(
                    (
                        "session_issues",
                        (None, str(session_issues_item_element).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.crypto_issues, Unset):
            for crypto_issues_item_element in self.crypto_issues:
                files.append(
                    (
                        "crypto_issues",
                        (None, str(crypto_issues_item_element).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.config_issues, Unset):
            for config_issues_item_element in self.config_issues:
                files.append(
                    (
                        "config_issues",
                        (None, str(config_issues_item_element).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.auth_issues, Unset):
            for auth_issues_item_element in self.auth_issues:
                files.append(
                    ("auth_issues", (None, str(auth_issues_item_element).encode(), "text/plain"))
                )

        if not isinstance(self.author_issues, Unset):
            for author_issues_item_element in self.author_issues:
                files.append(
                    (
                        "author_issues",
                        (None, str(author_issues_item_element).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.data_issues, Unset):
            for data_issues_item_element in self.data_issues:
                files.append(
                    ("data_issues", (None, str(data_issues_item_element).encode(), "text/plain"))
                )

        if not isinstance(self.sensitive_issues, Unset):
            for sensitive_issues_item_element in self.sensitive_issues:
                files.append(
                    (
                        "sensitive_issues",
                        (None, str(sensitive_issues_item_element).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.other_issues, Unset):
            for other_issues_item_element in self.other_issues:
                files.append(
                    ("other_issues", (None, str(other_issues_item_element).encode(), "text/plain"))
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_management = d.pop("session_management", UNSET)

        encryption_crypto = d.pop("encryption_crypto", UNSET)

        configuration_management = d.pop("configuration_management", UNSET)

        authentication = d.pop("authentication", UNSET)

        authorization_and_access_control = d.pop("authorization_and_access_control", UNSET)

        data_input_sanitization_validation = d.pop("data_input_sanitization_validation", UNSET)

        sensitive_data = d.pop("sensitive_data", UNSET)

        other = d.pop("other", UNSET)

        session_issues = cast(list[int], d.pop("session_issues", UNSET))

        crypto_issues = cast(list[int], d.pop("crypto_issues", UNSET))

        config_issues = cast(list[int], d.pop("config_issues", UNSET))

        auth_issues = cast(list[int], d.pop("auth_issues", UNSET))

        author_issues = cast(list[int], d.pop("author_issues", UNSET))

        data_issues = cast(list[int], d.pop("data_issues", UNSET))

        sensitive_issues = cast(list[int], d.pop("sensitive_issues", UNSET))

        other_issues = cast(list[int], d.pop("other_issues", UNSET))

        engagement_check_list_request = cls(
            session_management=session_management,
            encryption_crypto=encryption_crypto,
            configuration_management=configuration_management,
            authentication=authentication,
            authorization_and_access_control=authorization_and_access_control,
            data_input_sanitization_validation=data_input_sanitization_validation,
            sensitive_data=sensitive_data,
            other=other,
            session_issues=session_issues,
            crypto_issues=crypto_issues,
            config_issues=config_issues,
            auth_issues=auth_issues,
            author_issues=author_issues,
            data_issues=data_issues,
            sensitive_issues=sensitive_issues,
            other_issues=other_issues,
        )

        engagement_check_list_request.additional_properties = d
        return engagement_check_list_request

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
