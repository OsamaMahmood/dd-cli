from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_tool_product_settings_list_prefetch_notes import (
        PaginatedToolProductSettingsListPrefetchNotes,
    )
    from ..models.paginated_tool_product_settings_list_prefetch_product import (
        PaginatedToolProductSettingsListPrefetchProduct,
    )
    from ..models.paginated_tool_product_settings_list_prefetch_tool_configuration import (
        PaginatedToolProductSettingsListPrefetchToolConfiguration,
    )


T = TypeVar("T", bound="PaginatedToolProductSettingsListPrefetch")


@_attrs_define
class PaginatedToolProductSettingsListPrefetch:
    """
    Attributes:
        notes (PaginatedToolProductSettingsListPrefetchNotes | Unset):
        product (PaginatedToolProductSettingsListPrefetchProduct | Unset):
        tool_configuration (PaginatedToolProductSettingsListPrefetchToolConfiguration | Unset):
    """

    notes: PaginatedToolProductSettingsListPrefetchNotes | Unset = UNSET
    product: PaginatedToolProductSettingsListPrefetchProduct | Unset = UNSET
    tool_configuration: PaginatedToolProductSettingsListPrefetchToolConfiguration | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notes, Unset):
            notes = self.notes.to_dict()

        product: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        tool_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tool_configuration, Unset):
            tool_configuration = self.tool_configuration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if notes is not UNSET:
            field_dict["notes"] = notes
        if product is not UNSET:
            field_dict["product"] = product
        if tool_configuration is not UNSET:
            field_dict["tool_configuration"] = tool_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_tool_product_settings_list_prefetch_notes import (
            PaginatedToolProductSettingsListPrefetchNotes,
        )
        from ..models.paginated_tool_product_settings_list_prefetch_product import (
            PaginatedToolProductSettingsListPrefetchProduct,
        )
        from ..models.paginated_tool_product_settings_list_prefetch_tool_configuration import (
            PaginatedToolProductSettingsListPrefetchToolConfiguration,
        )

        d = dict(src_dict)
        _notes = d.pop("notes", UNSET)
        notes: PaginatedToolProductSettingsListPrefetchNotes | Unset
        if isinstance(_notes, Unset):
            notes = UNSET
        else:
            notes = PaginatedToolProductSettingsListPrefetchNotes.from_dict(_notes)

        _product = d.pop("product", UNSET)
        product: PaginatedToolProductSettingsListPrefetchProduct | Unset
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = PaginatedToolProductSettingsListPrefetchProduct.from_dict(_product)

        _tool_configuration = d.pop("tool_configuration", UNSET)
        tool_configuration: PaginatedToolProductSettingsListPrefetchToolConfiguration | Unset
        if isinstance(_tool_configuration, Unset):
            tool_configuration = UNSET
        else:
            tool_configuration = (
                PaginatedToolProductSettingsListPrefetchToolConfiguration.from_dict(
                    _tool_configuration
                )
            )

        paginated_tool_product_settings_list_prefetch = cls(
            notes=notes,
            product=product,
            tool_configuration=tool_configuration,
        )

        paginated_tool_product_settings_list_prefetch.additional_properties = d
        return paginated_tool_product_settings_list_prefetch

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
