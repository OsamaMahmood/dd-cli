from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.patched_regulation_request_category import PatchedRegulationRequestCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedRegulationRequest")


@_attrs_define
class PatchedRegulationRequest:
    """
    Attributes:
        name (str | Unset): The name of the regulation.
        acronym (str | Unset): A shortened representation of the name.
        category (PatchedRegulationRequestCategory | Unset): The subject of the regulation.

            * `privacy` - Privacy
            * `finance` - Finance
            * `education` - Education
            * `medical` - Medical
            * `corporate` - Corporate
            * `security` - Security
            * `government` - Government
            * `other` - Other
        jurisdiction (str | Unset): The territory over which the regulation applies.
        description (str | Unset): Information about the regulation's purpose.
        reference (str | Unset): An external URL for more information.
    """

    name: str | Unset = UNSET
    acronym: str | Unset = UNSET
    category: PatchedRegulationRequestCategory | Unset = UNSET
    jurisdiction: str | Unset = UNSET
    description: str | Unset = UNSET
    reference: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        acronym = self.acronym

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        jurisdiction = self.jurisdiction

        description = self.description

        reference = self.reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if acronym is not UNSET:
            field_dict["acronym"] = acronym
        if category is not UNSET:
            field_dict["category"] = category
        if jurisdiction is not UNSET:
            field_dict["jurisdiction"] = jurisdiction
        if description is not UNSET:
            field_dict["description"] = description
        if reference is not UNSET:
            field_dict["reference"] = reference

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.acronym, Unset):
            files.append(("acronym", (None, str(self.acronym).encode(), "text/plain")))

        if not isinstance(self.category, Unset):
            files.append(("category", (None, str(self.category.value).encode(), "text/plain")))

        if not isinstance(self.jurisdiction, Unset):
            files.append(("jurisdiction", (None, str(self.jurisdiction).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.reference, Unset):
            files.append(("reference", (None, str(self.reference).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        acronym = d.pop("acronym", UNSET)

        _category = d.pop("category", UNSET)
        category: PatchedRegulationRequestCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = PatchedRegulationRequestCategory(_category)

        jurisdiction = d.pop("jurisdiction", UNSET)

        description = d.pop("description", UNSET)

        reference = d.pop("reference", UNSET)

        patched_regulation_request = cls(
            name=name,
            acronym=acronym,
            category=category,
            jurisdiction=jurisdiction,
            description=description,
            reference=reference,
        )

        patched_regulation_request.additional_properties = d
        return patched_regulation_request

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
