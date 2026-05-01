from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductAPIScanConfigurationRequest")


@_attrs_define
class ProductAPIScanConfigurationRequest:
    """
    Attributes:
        product (int):
        tool_configuration (int):
        service_key_1 (None | str | Unset):
        service_key_2 (None | str | Unset):
        service_key_3 (None | str | Unset):
    """

    product: int
    tool_configuration: int
    service_key_1: None | str | Unset = UNSET
    service_key_2: None | str | Unset = UNSET
    service_key_3: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product = self.product

        tool_configuration = self.tool_configuration

        service_key_1: None | str | Unset
        if isinstance(self.service_key_1, Unset):
            service_key_1 = UNSET
        else:
            service_key_1 = self.service_key_1

        service_key_2: None | str | Unset
        if isinstance(self.service_key_2, Unset):
            service_key_2 = UNSET
        else:
            service_key_2 = self.service_key_2

        service_key_3: None | str | Unset
        if isinstance(self.service_key_3, Unset):
            service_key_3 = UNSET
        else:
            service_key_3 = self.service_key_3

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product": product,
                "tool_configuration": tool_configuration,
            }
        )
        if service_key_1 is not UNSET:
            field_dict["service_key_1"] = service_key_1
        if service_key_2 is not UNSET:
            field_dict["service_key_2"] = service_key_2
        if service_key_3 is not UNSET:
            field_dict["service_key_3"] = service_key_3

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("product", (None, str(self.product).encode(), "text/plain")))

        files.append(
            ("tool_configuration", (None, str(self.tool_configuration).encode(), "text/plain"))
        )

        if not isinstance(self.service_key_1, Unset):
            if isinstance(self.service_key_1, str):
                files.append(
                    ("service_key_1", (None, str(self.service_key_1).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("service_key_1", (None, str(self.service_key_1).encode(), "text/plain"))
                )

        if not isinstance(self.service_key_2, Unset):
            if isinstance(self.service_key_2, str):
                files.append(
                    ("service_key_2", (None, str(self.service_key_2).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("service_key_2", (None, str(self.service_key_2).encode(), "text/plain"))
                )

        if not isinstance(self.service_key_3, Unset):
            if isinstance(self.service_key_3, str):
                files.append(
                    ("service_key_3", (None, str(self.service_key_3).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("service_key_3", (None, str(self.service_key_3).encode(), "text/plain"))
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product = d.pop("product")

        tool_configuration = d.pop("tool_configuration")

        def _parse_service_key_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_key_1 = _parse_service_key_1(d.pop("service_key_1", UNSET))

        def _parse_service_key_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_key_2 = _parse_service_key_2(d.pop("service_key_2", UNSET))

        def _parse_service_key_3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_key_3 = _parse_service_key_3(d.pop("service_key_3", UNSET))

        product_api_scan_configuration_request = cls(
            product=product,
            tool_configuration=tool_configuration,
            service_key_1=service_key_1,
            service_key_2=service_key_2,
            service_key_3=service_key_3,
        )

        product_api_scan_configuration_request.additional_properties = d
        return product_api_scan_configuration_request

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
