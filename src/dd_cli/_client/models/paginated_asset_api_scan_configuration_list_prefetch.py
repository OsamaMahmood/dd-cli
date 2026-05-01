from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_asset_api_scan_configuration_list_prefetch_product import (
        PaginatedAssetAPIScanConfigurationListPrefetchProduct,
    )
    from ..models.paginated_asset_api_scan_configuration_list_prefetch_tool_configuration import (
        PaginatedAssetAPIScanConfigurationListPrefetchToolConfiguration,
    )


T = TypeVar("T", bound="PaginatedAssetAPIScanConfigurationListPrefetch")


@_attrs_define
class PaginatedAssetAPIScanConfigurationListPrefetch:
    """
    Attributes:
        product (PaginatedAssetAPIScanConfigurationListPrefetchProduct | Unset):
        tool_configuration (PaginatedAssetAPIScanConfigurationListPrefetchToolConfiguration | Unset):
    """

    product: PaginatedAssetAPIScanConfigurationListPrefetchProduct | Unset = UNSET
    tool_configuration: PaginatedAssetAPIScanConfigurationListPrefetchToolConfiguration | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        tool_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tool_configuration, Unset):
            tool_configuration = self.tool_configuration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product is not UNSET:
            field_dict["product"] = product
        if tool_configuration is not UNSET:
            field_dict["tool_configuration"] = tool_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_asset_api_scan_configuration_list_prefetch_product import (
            PaginatedAssetAPIScanConfigurationListPrefetchProduct,
        )
        from ..models.paginated_asset_api_scan_configuration_list_prefetch_tool_configuration import (
            PaginatedAssetAPIScanConfigurationListPrefetchToolConfiguration,
        )

        d = dict(src_dict)
        _product = d.pop("product", UNSET)
        product: PaginatedAssetAPIScanConfigurationListPrefetchProduct | Unset
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = PaginatedAssetAPIScanConfigurationListPrefetchProduct.from_dict(_product)

        _tool_configuration = d.pop("tool_configuration", UNSET)
        tool_configuration: PaginatedAssetAPIScanConfigurationListPrefetchToolConfiguration | Unset
        if isinstance(_tool_configuration, Unset):
            tool_configuration = UNSET
        else:
            tool_configuration = (
                PaginatedAssetAPIScanConfigurationListPrefetchToolConfiguration.from_dict(
                    _tool_configuration
                )
            )

        paginated_asset_api_scan_configuration_list_prefetch = cls(
            product=product,
            tool_configuration=tool_configuration,
        )

        paginated_asset_api_scan_configuration_list_prefetch.additional_properties = d
        return paginated_asset_api_scan_configuration_list_prefetch

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
