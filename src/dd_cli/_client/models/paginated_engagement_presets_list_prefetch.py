from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_engagement_presets_list_prefetch_network_locations import (
        PaginatedEngagementPresetsListPrefetchNetworkLocations,
    )
    from ..models.paginated_engagement_presets_list_prefetch_product import (
        PaginatedEngagementPresetsListPrefetchProduct,
    )
    from ..models.paginated_engagement_presets_list_prefetch_test_type import (
        PaginatedEngagementPresetsListPrefetchTestType,
    )


T = TypeVar("T", bound="PaginatedEngagementPresetsListPrefetch")


@_attrs_define
class PaginatedEngagementPresetsListPrefetch:
    """
    Attributes:
        network_locations (PaginatedEngagementPresetsListPrefetchNetworkLocations | Unset):
        product (PaginatedEngagementPresetsListPrefetchProduct | Unset):
        test_type (PaginatedEngagementPresetsListPrefetchTestType | Unset):
    """

    network_locations: PaginatedEngagementPresetsListPrefetchNetworkLocations | Unset = UNSET
    product: PaginatedEngagementPresetsListPrefetchProduct | Unset = UNSET
    test_type: PaginatedEngagementPresetsListPrefetchTestType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_locations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.network_locations, Unset):
            network_locations = self.network_locations.to_dict()

        product: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        test_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.test_type, Unset):
            test_type = self.test_type.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network_locations is not UNSET:
            field_dict["network_locations"] = network_locations
        if product is not UNSET:
            field_dict["product"] = product
        if test_type is not UNSET:
            field_dict["test_type"] = test_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_engagement_presets_list_prefetch_network_locations import (
            PaginatedEngagementPresetsListPrefetchNetworkLocations,
        )
        from ..models.paginated_engagement_presets_list_prefetch_product import (
            PaginatedEngagementPresetsListPrefetchProduct,
        )
        from ..models.paginated_engagement_presets_list_prefetch_test_type import (
            PaginatedEngagementPresetsListPrefetchTestType,
        )

        d = dict(src_dict)
        _network_locations = d.pop("network_locations", UNSET)
        network_locations: PaginatedEngagementPresetsListPrefetchNetworkLocations | Unset
        if isinstance(_network_locations, Unset):
            network_locations = UNSET
        else:
            network_locations = PaginatedEngagementPresetsListPrefetchNetworkLocations.from_dict(
                _network_locations
            )

        _product = d.pop("product", UNSET)
        product: PaginatedEngagementPresetsListPrefetchProduct | Unset
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = PaginatedEngagementPresetsListPrefetchProduct.from_dict(_product)

        _test_type = d.pop("test_type", UNSET)
        test_type: PaginatedEngagementPresetsListPrefetchTestType | Unset
        if isinstance(_test_type, Unset):
            test_type = UNSET
        else:
            test_type = PaginatedEngagementPresetsListPrefetchTestType.from_dict(_test_type)

        paginated_engagement_presets_list_prefetch = cls(
            network_locations=network_locations,
            product=product,
            test_type=test_type,
        )

        paginated_engagement_presets_list_prefetch.additional_properties = d
        return paginated_engagement_presets_list_prefetch

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
