from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BurpRawRequestResponseMulti")


@_attrs_define
class BurpRawRequestResponseMulti:
    """
    Attributes:
        id (int):
        burp_request_base_64 (str):
        burp_response_base_64 (str):
        finding (int | None | Unset):
    """

    id: int
    burp_request_base_64: str
    burp_response_base_64: str
    finding: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        burp_request_base_64 = self.burp_request_base_64

        burp_response_base_64 = self.burp_response_base_64

        finding: int | None | Unset
        if isinstance(self.finding, Unset):
            finding = UNSET
        else:
            finding = self.finding

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "burpRequestBase64": burp_request_base_64,
                "burpResponseBase64": burp_response_base_64,
            }
        )
        if finding is not UNSET:
            field_dict["finding"] = finding

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        burp_request_base_64 = d.pop("burpRequestBase64")

        burp_response_base_64 = d.pop("burpResponseBase64")

        def _parse_finding(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        finding = _parse_finding(d.pop("finding", UNSET))

        burp_raw_request_response_multi = cls(
            id=id,
            burp_request_base_64=burp_request_base_64,
            burp_response_base_64=burp_response_base_64,
            finding=finding,
        )

        burp_raw_request_response_multi.additional_properties = d
        return burp_raw_request_response_multi

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
