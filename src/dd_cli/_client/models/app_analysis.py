from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_analysis_prefetch import AppAnalysisPrefetch


T = TypeVar("T", bound="AppAnalysis")


@_attrs_define
class AppAnalysis:
    """
    Attributes:
        id (int):
        name (str):
        created (datetime.datetime):
        product (int):
        user (int):
        tags (list[str] | Unset):
        confidence (int | None | Unset):
        version (None | str | Unset):
        icon (None | str | Unset):
        website (None | str | Unset):
        website_found (None | str | Unset):
        prefetch (AppAnalysisPrefetch | Unset):
    """

    id: int
    name: str
    created: datetime.datetime
    product: int
    user: int
    tags: list[str] | Unset = UNSET
    confidence: int | None | Unset = UNSET
    version: None | str | Unset = UNSET
    icon: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    website_found: None | str | Unset = UNSET
    prefetch: AppAnalysisPrefetch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        created = self.created.isoformat()

        product = self.product

        user = self.user

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        confidence: int | None | Unset
        if isinstance(self.confidence, Unset):
            confidence = UNSET
        else:
            confidence = self.confidence

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        icon: None | str | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        website_found: None | str | Unset
        if isinstance(self.website_found, Unset):
            website_found = UNSET
        else:
            website_found = self.website_found

        prefetch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prefetch, Unset):
            prefetch = self.prefetch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "created": created,
                "product": product,
                "user": user,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if version is not UNSET:
            field_dict["version"] = version
        if icon is not UNSET:
            field_dict["icon"] = icon
        if website is not UNSET:
            field_dict["website"] = website
        if website_found is not UNSET:
            field_dict["website_found"] = website_found
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_analysis_prefetch import AppAnalysisPrefetch

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        created = isoparse(d.pop("created"))

        product = d.pop("product")

        user = d.pop("user")

        tags = cast(list[str], d.pop("tags", UNSET))

        def _parse_confidence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        confidence = _parse_confidence(d.pop("confidence", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        def _parse_website_found(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_found = _parse_website_found(d.pop("website_found", UNSET))

        _prefetch = d.pop("prefetch", UNSET)
        prefetch: AppAnalysisPrefetch | Unset
        if isinstance(_prefetch, Unset):
            prefetch = UNSET
        else:
            prefetch = AppAnalysisPrefetch.from_dict(_prefetch)

        app_analysis = cls(
            id=id,
            name=name,
            created=created,
            product=product,
            user=user,
            tags=tags,
            confidence=confidence,
            version=version,
            icon=icon,
            website=website,
            website_found=website_found,
            prefetch=prefetch,
        )

        app_analysis.additional_properties = d
        return app_analysis

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
