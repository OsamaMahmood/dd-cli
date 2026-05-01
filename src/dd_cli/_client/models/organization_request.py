from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationRequest")


@_attrs_define
class OrganizationRequest:
    """
    Attributes:
        name (str):
        critical_asset (bool | Unset):  Default: False.
        key_asset (bool | Unset):  Default: False.
        description (None | str | Unset):
    """

    name: str
    critical_asset: bool | Unset = False
    key_asset: bool | Unset = False
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        critical_asset = self.critical_asset

        key_asset = self.key_asset

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if critical_asset is not UNSET:
            field_dict["critical_asset"] = critical_asset
        if key_asset is not UNSET:
            field_dict["key_asset"] = key_asset
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.critical_asset, Unset):
            files.append(
                ("critical_asset", (None, str(self.critical_asset).encode(), "text/plain"))
            )

        if not isinstance(self.key_asset, Unset):
            files.append(("key_asset", (None, str(self.key_asset).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            if isinstance(self.description, str):
                files.append(("description", (None, str(self.description).encode(), "text/plain")))
            else:
                files.append(("description", (None, str(self.description).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        critical_asset = d.pop("critical_asset", UNSET)

        key_asset = d.pop("key_asset", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        organization_request = cls(
            name=name,
            critical_asset=critical_asset,
            key_asset=key_asset,
            description=description,
        )

        organization_request.additional_properties = d
        return organization_request

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
