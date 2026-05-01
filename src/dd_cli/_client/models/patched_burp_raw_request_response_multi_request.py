from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedBurpRawRequestResponseMultiRequest")


@_attrs_define
class PatchedBurpRawRequestResponseMultiRequest:
    """
    Attributes:
        burp_request_base_64 (str | Unset):
        burp_response_base_64 (str | Unset):
        finding (int | None | Unset):
    """

    burp_request_base_64: str | Unset = UNSET
    burp_response_base_64: str | Unset = UNSET
    finding: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        burp_request_base_64 = self.burp_request_base_64

        burp_response_base_64 = self.burp_response_base_64

        finding: int | None | Unset
        if isinstance(self.finding, Unset):
            finding = UNSET
        else:
            finding = self.finding

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if burp_request_base_64 is not UNSET:
            field_dict["burpRequestBase64"] = burp_request_base_64
        if burp_response_base_64 is not UNSET:
            field_dict["burpResponseBase64"] = burp_response_base_64
        if finding is not UNSET:
            field_dict["finding"] = finding

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.burp_request_base_64, Unset):
            files.append(
                ("burpRequestBase64", (None, str(self.burp_request_base_64).encode(), "text/plain"))
            )

        if not isinstance(self.burp_response_base_64, Unset):
            files.append(
                (
                    "burpResponseBase64",
                    (None, str(self.burp_response_base_64).encode(), "text/plain"),
                )
            )

        if not isinstance(self.finding, Unset):
            if isinstance(self.finding, int):
                files.append(("finding", (None, str(self.finding).encode(), "text/plain")))
            else:
                files.append(("finding", (None, str(self.finding).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        burp_request_base_64 = d.pop("burpRequestBase64", UNSET)

        burp_response_base_64 = d.pop("burpResponseBase64", UNSET)

        def _parse_finding(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        finding = _parse_finding(d.pop("finding", UNSET))

        patched_burp_raw_request_response_multi_request = cls(
            burp_request_base_64=burp_request_base_64,
            burp_response_base_64=burp_response_base_64,
            finding=finding,
        )

        patched_burp_raw_request_response_multi_request.additional_properties = d
        return patched_burp_raw_request_response_multi_request

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
