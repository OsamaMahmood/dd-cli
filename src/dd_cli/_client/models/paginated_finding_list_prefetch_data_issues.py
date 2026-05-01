from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.engagement_check_list import EngagementCheckList


T = TypeVar("T", bound="PaginatedFindingListPrefetchDataIssues")


@_attrs_define
class PaginatedFindingListPrefetchDataIssues:
    """ """

    additional_properties: dict[str, EngagementCheckList] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.engagement_check_list import EngagementCheckList

        d = dict(src_dict)
        paginated_finding_list_prefetch_data_issues = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = EngagementCheckList.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        paginated_finding_list_prefetch_data_issues.additional_properties = additional_properties
        return paginated_finding_list_prefetch_data_issues

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> EngagementCheckList:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: EngagementCheckList) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
