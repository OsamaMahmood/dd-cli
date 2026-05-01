from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedSLAConfigurationRequest")


@_attrs_define
class PatchedSLAConfigurationRequest:
    """
    Attributes:
        name (str | Unset): A unique name for the set of SLAs.
        description (None | str | Unset):
        critical (int | Unset): The number of days to remediate a critical finding.
        enforce_critical (bool | Unset): When enabled, critical findings will be assigned an SLA expiration date based
            on the critical finding SLA days within this SLA configuration.
        high (int | Unset): The number of days to remediate a high finding.
        enforce_high (bool | Unset): When enabled, high findings will be assigned an SLA expiration date based on the
            high finding SLA days within this SLA configuration.
        medium (int | Unset): The number of days to remediate a medium finding.
        enforce_medium (bool | Unset): When enabled, medium findings will be assigned an SLA expiration date based on
            the medium finding SLA days within this SLA configuration.
        low (int | Unset): The number of days to remediate a low finding.
        enforce_low (bool | Unset): When enabled, low findings will be assigned an SLA expiration date based on the low
            finding SLA days within this SLA configuration.
        restart_sla_on_reactivation (bool | Unset): When enabled, findings that were previously mitigated but are
            reactivated durign reimport will have their SLA period restarted.
    """

    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    critical: int | Unset = UNSET
    enforce_critical: bool | Unset = UNSET
    high: int | Unset = UNSET
    enforce_high: bool | Unset = UNSET
    medium: int | Unset = UNSET
    enforce_medium: bool | Unset = UNSET
    low: int | Unset = UNSET
    enforce_low: bool | Unset = UNSET
    restart_sla_on_reactivation: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        critical = self.critical

        enforce_critical = self.enforce_critical

        high = self.high

        enforce_high = self.enforce_high

        medium = self.medium

        enforce_medium = self.enforce_medium

        low = self.low

        enforce_low = self.enforce_low

        restart_sla_on_reactivation = self.restart_sla_on_reactivation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if critical is not UNSET:
            field_dict["critical"] = critical
        if enforce_critical is not UNSET:
            field_dict["enforce_critical"] = enforce_critical
        if high is not UNSET:
            field_dict["high"] = high
        if enforce_high is not UNSET:
            field_dict["enforce_high"] = enforce_high
        if medium is not UNSET:
            field_dict["medium"] = medium
        if enforce_medium is not UNSET:
            field_dict["enforce_medium"] = enforce_medium
        if low is not UNSET:
            field_dict["low"] = low
        if enforce_low is not UNSET:
            field_dict["enforce_low"] = enforce_low
        if restart_sla_on_reactivation is not UNSET:
            field_dict["restart_sla_on_reactivation"] = restart_sla_on_reactivation

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            if isinstance(self.description, str):
                files.append(("description", (None, str(self.description).encode(), "text/plain")))
            else:
                files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.critical, Unset):
            files.append(("critical", (None, str(self.critical).encode(), "text/plain")))

        if not isinstance(self.enforce_critical, Unset):
            files.append(
                ("enforce_critical", (None, str(self.enforce_critical).encode(), "text/plain"))
            )

        if not isinstance(self.high, Unset):
            files.append(("high", (None, str(self.high).encode(), "text/plain")))

        if not isinstance(self.enforce_high, Unset):
            files.append(("enforce_high", (None, str(self.enforce_high).encode(), "text/plain")))

        if not isinstance(self.medium, Unset):
            files.append(("medium", (None, str(self.medium).encode(), "text/plain")))

        if not isinstance(self.enforce_medium, Unset):
            files.append(
                ("enforce_medium", (None, str(self.enforce_medium).encode(), "text/plain"))
            )

        if not isinstance(self.low, Unset):
            files.append(("low", (None, str(self.low).encode(), "text/plain")))

        if not isinstance(self.enforce_low, Unset):
            files.append(("enforce_low", (None, str(self.enforce_low).encode(), "text/plain")))

        if not isinstance(self.restart_sla_on_reactivation, Unset):
            files.append(
                (
                    "restart_sla_on_reactivation",
                    (None, str(self.restart_sla_on_reactivation).encode(), "text/plain"),
                )
            )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        critical = d.pop("critical", UNSET)

        enforce_critical = d.pop("enforce_critical", UNSET)

        high = d.pop("high", UNSET)

        enforce_high = d.pop("enforce_high", UNSET)

        medium = d.pop("medium", UNSET)

        enforce_medium = d.pop("enforce_medium", UNSET)

        low = d.pop("low", UNSET)

        enforce_low = d.pop("enforce_low", UNSET)

        restart_sla_on_reactivation = d.pop("restart_sla_on_reactivation", UNSET)

        patched_sla_configuration_request = cls(
            name=name,
            description=description,
            critical=critical,
            enforce_critical=enforce_critical,
            high=high,
            enforce_high=enforce_high,
            medium=medium,
            enforce_medium=enforce_medium,
            low=low,
            enforce_low=enforce_low,
            restart_sla_on_reactivation=restart_sla_on_reactivation,
        )

        patched_sla_configuration_request.additional_properties = d
        return patched_sla_configuration_request

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
