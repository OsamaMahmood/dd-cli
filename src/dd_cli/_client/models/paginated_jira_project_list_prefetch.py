from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_jira_project_list_prefetch_engagement import (
        PaginatedJIRAProjectListPrefetchEngagement,
    )
    from ..models.paginated_jira_project_list_prefetch_jira_instance import (
        PaginatedJIRAProjectListPrefetchJiraInstance,
    )
    from ..models.paginated_jira_project_list_prefetch_product import (
        PaginatedJIRAProjectListPrefetchProduct,
    )


T = TypeVar("T", bound="PaginatedJIRAProjectListPrefetch")


@_attrs_define
class PaginatedJIRAProjectListPrefetch:
    """
    Attributes:
        engagement (PaginatedJIRAProjectListPrefetchEngagement | Unset):
        jira_instance (PaginatedJIRAProjectListPrefetchJiraInstance | Unset):
        product (PaginatedJIRAProjectListPrefetchProduct | Unset):
    """

    engagement: PaginatedJIRAProjectListPrefetchEngagement | Unset = UNSET
    jira_instance: PaginatedJIRAProjectListPrefetchJiraInstance | Unset = UNSET
    product: PaginatedJIRAProjectListPrefetchProduct | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        engagement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.engagement, Unset):
            engagement = self.engagement.to_dict()

        jira_instance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.jira_instance, Unset):
            jira_instance = self.jira_instance.to_dict()

        product: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if engagement is not UNSET:
            field_dict["engagement"] = engagement
        if jira_instance is not UNSET:
            field_dict["jira_instance"] = jira_instance
        if product is not UNSET:
            field_dict["product"] = product

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_jira_project_list_prefetch_engagement import (
            PaginatedJIRAProjectListPrefetchEngagement,
        )
        from ..models.paginated_jira_project_list_prefetch_jira_instance import (
            PaginatedJIRAProjectListPrefetchJiraInstance,
        )
        from ..models.paginated_jira_project_list_prefetch_product import (
            PaginatedJIRAProjectListPrefetchProduct,
        )

        d = dict(src_dict)
        _engagement = d.pop("engagement", UNSET)
        engagement: PaginatedJIRAProjectListPrefetchEngagement | Unset
        if isinstance(_engagement, Unset):
            engagement = UNSET
        else:
            engagement = PaginatedJIRAProjectListPrefetchEngagement.from_dict(_engagement)

        _jira_instance = d.pop("jira_instance", UNSET)
        jira_instance: PaginatedJIRAProjectListPrefetchJiraInstance | Unset
        if isinstance(_jira_instance, Unset):
            jira_instance = UNSET
        else:
            jira_instance = PaginatedJIRAProjectListPrefetchJiraInstance.from_dict(_jira_instance)

        _product = d.pop("product", UNSET)
        product: PaginatedJIRAProjectListPrefetchProduct | Unset
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = PaginatedJIRAProjectListPrefetchProduct.from_dict(_product)

        paginated_jira_project_list_prefetch = cls(
            engagement=engagement,
            jira_instance=jira_instance,
            product=product,
        )

        paginated_jira_project_list_prefetch.additional_properties = d
        return paginated_jira_project_list_prefetch

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
