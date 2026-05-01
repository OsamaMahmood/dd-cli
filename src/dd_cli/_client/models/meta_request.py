from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="MetaRequest")


@_attrs_define
class MetaRequest:
    """
    Attributes:
        name (str):
        value (str):
        product (int | None | Unset):
        endpoint (int | None | Unset):
        finding (int | None | Unset):
    """

    name: str
    value: str
    product: int | None | Unset = UNSET
    endpoint: int | None | Unset = UNSET
    finding: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value = self.value

        product: int | None | Unset
        if isinstance(self.product, Unset):
            product = UNSET
        else:
            product = self.product

        endpoint: int | None | Unset
        if isinstance(self.endpoint, Unset):
            endpoint = UNSET
        else:
            endpoint = self.endpoint

        finding: int | None | Unset
        if isinstance(self.finding, Unset):
            finding = UNSET
        else:
            finding = self.finding

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )
        if product is not UNSET:
            field_dict["product"] = product
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if finding is not UNSET:
            field_dict["finding"] = finding

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("value", (None, str(self.value).encode(), "text/plain")))

        if not isinstance(self.product, Unset):
            if isinstance(self.product, int):
                files.append(("product", (None, str(self.product).encode(), "text/plain")))
            else:
                files.append(("product", (None, str(self.product).encode(), "text/plain")))

        if not isinstance(self.endpoint, Unset):
            if isinstance(self.endpoint, int):
                files.append(("endpoint", (None, str(self.endpoint).encode(), "text/plain")))
            else:
                files.append(("endpoint", (None, str(self.endpoint).encode(), "text/plain")))

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
        name = d.pop("name")

        value = d.pop("value")

        def _parse_product(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        product = _parse_product(d.pop("product", UNSET))

        def _parse_endpoint(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        endpoint = _parse_endpoint(d.pop("endpoint", UNSET))

        def _parse_finding(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        finding = _parse_finding(d.pop("finding", UNSET))

        meta_request = cls(
            name=name,
            value=value,
            product=product,
            endpoint=endpoint,
            finding=finding,
        )

        meta_request.additional_properties = d
        return meta_request

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
