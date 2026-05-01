from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_credential_list_prefetch_environment import (
        PaginatedCredentialListPrefetchEnvironment,
    )
    from ..models.paginated_credential_list_prefetch_notes import (
        PaginatedCredentialListPrefetchNotes,
    )


T = TypeVar("T", bound="PaginatedCredentialListPrefetch")


@_attrs_define
class PaginatedCredentialListPrefetch:
    """
    Attributes:
        environment (PaginatedCredentialListPrefetchEnvironment | Unset):
        notes (PaginatedCredentialListPrefetchNotes | Unset):
    """

    environment: PaginatedCredentialListPrefetchEnvironment | Unset = UNSET
    notes: PaginatedCredentialListPrefetchNotes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.to_dict()

        notes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notes, Unset):
            notes = self.notes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if environment is not UNSET:
            field_dict["environment"] = environment
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_credential_list_prefetch_environment import (
            PaginatedCredentialListPrefetchEnvironment,
        )
        from ..models.paginated_credential_list_prefetch_notes import (
            PaginatedCredentialListPrefetchNotes,
        )

        d = dict(src_dict)
        _environment = d.pop("environment", UNSET)
        environment: PaginatedCredentialListPrefetchEnvironment | Unset
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = PaginatedCredentialListPrefetchEnvironment.from_dict(_environment)

        _notes = d.pop("notes", UNSET)
        notes: PaginatedCredentialListPrefetchNotes | Unset
        if isinstance(_notes, Unset):
            notes = UNSET
        else:
            notes = PaginatedCredentialListPrefetchNotes.from_dict(_notes)

        paginated_credential_list_prefetch = cls(
            environment=environment,
            notes=notes,
        )

        paginated_credential_list_prefetch.additional_properties = d
        return paginated_credential_list_prefetch

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
