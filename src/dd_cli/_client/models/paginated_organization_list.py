from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization import Organization
    from ..models.paginated_organization_list_prefetch import PaginatedOrganizationListPrefetch


T = TypeVar("T", bound="PaginatedOrganizationList")


@_attrs_define
class PaginatedOrganizationList:
    """
    Attributes:
        count (int):  Example: 123.
        results (list[Organization]):
        next_ (None | str | Unset):  Example: http://api.example.org/accounts/?offset=400&limit=100.
        previous (None | str | Unset):  Example: http://api.example.org/accounts/?offset=200&limit=100.
        prefetch (PaginatedOrganizationListPrefetch | Unset):
    """

    count: int
    results: list[Organization]
    next_: None | str | Unset = UNSET
    previous: None | str | Unset = UNSET
    prefetch: PaginatedOrganizationListPrefetch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        next_: None | str | Unset
        if isinstance(self.next_, Unset):
            next_ = UNSET
        else:
            next_ = self.next_

        previous: None | str | Unset
        if isinstance(self.previous, Unset):
            previous = UNSET
        else:
            previous = self.previous

        prefetch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prefetch, Unset):
            prefetch = self.prefetch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "results": results,
            }
        )
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization import Organization
        from ..models.paginated_organization_list_prefetch import PaginatedOrganizationListPrefetch

        d = dict(src_dict)
        count = d.pop("count")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = Organization.from_dict(results_item_data)

            results.append(results_item)

        def _parse_next_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_ = _parse_next_(d.pop("next", UNSET))

        def _parse_previous(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous = _parse_previous(d.pop("previous", UNSET))

        _prefetch = d.pop("prefetch", UNSET)
        prefetch: PaginatedOrganizationListPrefetch | Unset
        if isinstance(_prefetch, Unset):
            prefetch = UNSET
        else:
            prefetch = PaginatedOrganizationListPrefetch.from_dict(_prefetch)

        paginated_organization_list = cls(
            count=count,
            results=results,
            next_=next_,
            previous=previous,
            prefetch=prefetch,
        )

        paginated_organization_list.additional_properties = d
        return paginated_organization_list

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
