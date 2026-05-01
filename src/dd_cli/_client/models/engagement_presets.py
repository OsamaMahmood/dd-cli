from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engagement_presets_prefetch import EngagementPresetsPrefetch


T = TypeVar("T", bound="EngagementPresets")


@_attrs_define
class EngagementPresets:
    """
    Attributes:
        id (int):
        created (datetime.datetime):
        product (int):
        title (str | Unset): Brief description of preset.
        notes (None | str | Unset): Description of what needs to be tested or setting up environment for testing
        scope (str | Unset): Scope of Engagement testing, IP's/Resources/URL's)
        test_type (list[int] | Unset):
        network_locations (list[int] | Unset):
        prefetch (EngagementPresetsPrefetch | Unset):
    """

    id: int
    created: datetime.datetime
    product: int
    title: str | Unset = UNSET
    notes: None | str | Unset = UNSET
    scope: str | Unset = UNSET
    test_type: list[int] | Unset = UNSET
    network_locations: list[int] | Unset = UNSET
    prefetch: EngagementPresetsPrefetch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created = self.created.isoformat()

        product = self.product

        title = self.title

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        scope = self.scope

        test_type: list[int] | Unset = UNSET
        if not isinstance(self.test_type, Unset):
            test_type = self.test_type

        network_locations: list[int] | Unset = UNSET
        if not isinstance(self.network_locations, Unset):
            network_locations = self.network_locations

        prefetch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prefetch, Unset):
            prefetch = self.prefetch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created": created,
                "product": product,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if notes is not UNSET:
            field_dict["notes"] = notes
        if scope is not UNSET:
            field_dict["scope"] = scope
        if test_type is not UNSET:
            field_dict["test_type"] = test_type
        if network_locations is not UNSET:
            field_dict["network_locations"] = network_locations
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.engagement_presets_prefetch import EngagementPresetsPrefetch

        d = dict(src_dict)
        id = d.pop("id")

        created = isoparse(d.pop("created"))

        product = d.pop("product")

        title = d.pop("title", UNSET)

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        scope = d.pop("scope", UNSET)

        test_type = cast(list[int], d.pop("test_type", UNSET))

        network_locations = cast(list[int], d.pop("network_locations", UNSET))

        _prefetch = d.pop("prefetch", UNSET)
        prefetch: EngagementPresetsPrefetch | Unset
        if isinstance(_prefetch, Unset):
            prefetch = UNSET
        else:
            prefetch = EngagementPresetsPrefetch.from_dict(_prefetch)

        engagement_presets = cls(
            id=id,
            created=created,
            product=product,
            title=title,
            notes=notes,
            scope=scope,
            test_type=test_type,
            network_locations=network_locations,
            prefetch=prefetch,
        )

        engagement_presets.additional_properties = d
        return engagement_presets

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
