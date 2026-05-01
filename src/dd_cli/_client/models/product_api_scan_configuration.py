from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_api_scan_configuration_prefetch import ProductAPIScanConfigurationPrefetch


T = TypeVar("T", bound="ProductAPIScanConfiguration")


@_attrs_define
class ProductAPIScanConfiguration:
    """
    Attributes:
        id (int):
        product (int):
        tool_configuration (int):
        service_key_1 (None | str | Unset):
        service_key_2 (None | str | Unset):
        service_key_3 (None | str | Unset):
        prefetch (ProductAPIScanConfigurationPrefetch | Unset):
    """

    id: int
    product: int
    tool_configuration: int
    service_key_1: None | str | Unset = UNSET
    service_key_2: None | str | Unset = UNSET
    service_key_3: None | str | Unset = UNSET
    prefetch: ProductAPIScanConfigurationPrefetch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

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

        prefetch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prefetch, Unset):
            prefetch = self.prefetch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
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
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_api_scan_configuration_prefetch import (
            ProductAPIScanConfigurationPrefetch,
        )

        d = dict(src_dict)
        id = d.pop("id")

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

        _prefetch = d.pop("prefetch", UNSET)
        prefetch: ProductAPIScanConfigurationPrefetch | Unset
        if isinstance(_prefetch, Unset):
            prefetch = UNSET
        else:
            prefetch = ProductAPIScanConfigurationPrefetch.from_dict(_prefetch)

        product_api_scan_configuration = cls(
            id=id,
            product=product,
            tool_configuration=tool_configuration,
            service_key_1=service_key_1,
            service_key_2=service_key_2,
            service_key_3=service_key_3,
            prefetch=prefetch,
        )

        product_api_scan_configuration.additional_properties = d
        return product_api_scan_configuration

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
