from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedEngagementPresetsRequest")


@_attrs_define
class PatchedEngagementPresetsRequest:
    """
    Attributes:
        title (str | Unset): Brief description of preset.
        notes (None | str | Unset): Description of what needs to be tested or setting up environment for testing
        scope (str | Unset): Scope of Engagement testing, IP's/Resources/URL's)
        product (int | Unset):
        test_type (list[int] | Unset):
        network_locations (list[int] | Unset):
    """

    title: str | Unset = UNSET
    notes: None | str | Unset = UNSET
    scope: str | Unset = UNSET
    product: int | Unset = UNSET
    test_type: list[int] | Unset = UNSET
    network_locations: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        scope = self.scope

        product = self.product

        test_type: list[int] | Unset = UNSET
        if not isinstance(self.test_type, Unset):
            test_type = self.test_type

        network_locations: list[int] | Unset = UNSET
        if not isinstance(self.network_locations, Unset):
            network_locations = self.network_locations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if notes is not UNSET:
            field_dict["notes"] = notes
        if scope is not UNSET:
            field_dict["scope"] = scope
        if product is not UNSET:
            field_dict["product"] = product
        if test_type is not UNSET:
            field_dict["test_type"] = test_type
        if network_locations is not UNSET:
            field_dict["network_locations"] = network_locations

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.title, Unset):
            files.append(("title", (None, str(self.title).encode(), "text/plain")))

        if not isinstance(self.notes, Unset):
            if isinstance(self.notes, str):
                files.append(("notes", (None, str(self.notes).encode(), "text/plain")))
            else:
                files.append(("notes", (None, str(self.notes).encode(), "text/plain")))

        if not isinstance(self.scope, Unset):
            files.append(("scope", (None, str(self.scope).encode(), "text/plain")))

        if not isinstance(self.product, Unset):
            files.append(("product", (None, str(self.product).encode(), "text/plain")))

        if not isinstance(self.test_type, Unset):
            for test_type_item_element in self.test_type:
                files.append(
                    ("test_type", (None, str(test_type_item_element).encode(), "text/plain"))
                )

        if not isinstance(self.network_locations, Unset):
            for network_locations_item_element in self.network_locations:
                files.append(
                    (
                        "network_locations",
                        (None, str(network_locations_item_element).encode(), "text/plain"),
                    )
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        scope = d.pop("scope", UNSET)

        product = d.pop("product", UNSET)

        test_type = cast(list[int], d.pop("test_type", UNSET))

        network_locations = cast(list[int], d.pop("network_locations", UNSET))

        patched_engagement_presets_request = cls(
            title=title,
            notes=notes,
            scope=scope,
            product=product,
            test_type=test_type,
            network_locations=network_locations,
        )

        patched_engagement_presets_request.additional_properties = d
        return patched_engagement_presets_request

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
