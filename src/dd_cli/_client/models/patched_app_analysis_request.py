from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedAppAnalysisRequest")


@_attrs_define
class PatchedAppAnalysisRequest:
    """
    Attributes:
        tags (list[str] | Unset):
        name (str | Unset):
        confidence (int | None | Unset):
        version (None | str | Unset):
        icon (None | str | Unset):
        website (None | str | Unset):
        website_found (None | str | Unset):
        product (int | Unset):
        user (int | Unset):
    """

    tags: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    confidence: int | None | Unset = UNSET
    version: None | str | Unset = UNSET
    icon: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    website_found: None | str | Unset = UNSET
    product: int | Unset = UNSET
    user: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        name = self.name

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

        product = self.product

        user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tags is not UNSET:
            field_dict["tags"] = tags
        if name is not UNSET:
            field_dict["name"] = name
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
        if product is not UNSET:
            field_dict["product"] = product
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.tags, Unset):
            for tags_item_element in self.tags:
                files.append(("tags", (None, str(tags_item_element).encode(), "text/plain")))

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.confidence, Unset):
            if isinstance(self.confidence, int):
                files.append(("confidence", (None, str(self.confidence).encode(), "text/plain")))
            else:
                files.append(("confidence", (None, str(self.confidence).encode(), "text/plain")))

        if not isinstance(self.version, Unset):
            if isinstance(self.version, str):
                files.append(("version", (None, str(self.version).encode(), "text/plain")))
            else:
                files.append(("version", (None, str(self.version).encode(), "text/plain")))

        if not isinstance(self.icon, Unset):
            if isinstance(self.icon, str):
                files.append(("icon", (None, str(self.icon).encode(), "text/plain")))
            else:
                files.append(("icon", (None, str(self.icon).encode(), "text/plain")))

        if not isinstance(self.website, Unset):
            if isinstance(self.website, str):
                files.append(("website", (None, str(self.website).encode(), "text/plain")))
            else:
                files.append(("website", (None, str(self.website).encode(), "text/plain")))

        if not isinstance(self.website_found, Unset):
            if isinstance(self.website_found, str):
                files.append(
                    ("website_found", (None, str(self.website_found).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("website_found", (None, str(self.website_found).encode(), "text/plain"))
                )

        if not isinstance(self.product, Unset):
            files.append(("product", (None, str(self.product).encode(), "text/plain")))

        if not isinstance(self.user, Unset):
            files.append(("user", (None, str(self.user).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tags = cast(list[str], d.pop("tags", UNSET))

        name = d.pop("name", UNSET)

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

        product = d.pop("product", UNSET)

        user = d.pop("user", UNSET)

        patched_app_analysis_request = cls(
            tags=tags,
            name=name,
            confidence=confidence,
            version=version,
            icon=icon,
            website=website,
            website_found=website_found,
            product=product,
            user=user,
        )

        patched_app_analysis_request.additional_properties = d
        return patched_app_analysis_request

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
