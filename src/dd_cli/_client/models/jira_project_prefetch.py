from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jira_project_prefetch_engagement import JIRAProjectPrefetchEngagement
    from ..models.jira_project_prefetch_jira_instance import JIRAProjectPrefetchJiraInstance
    from ..models.jira_project_prefetch_product import JIRAProjectPrefetchProduct


T = TypeVar("T", bound="JIRAProjectPrefetch")


@_attrs_define
class JIRAProjectPrefetch:
    """
    Attributes:
        engagement (JIRAProjectPrefetchEngagement | Unset):
        jira_instance (JIRAProjectPrefetchJiraInstance | Unset):
        product (JIRAProjectPrefetchProduct | Unset):
    """

    engagement: JIRAProjectPrefetchEngagement | Unset = UNSET
    jira_instance: JIRAProjectPrefetchJiraInstance | Unset = UNSET
    product: JIRAProjectPrefetchProduct | Unset = UNSET
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
        from ..models.jira_project_prefetch_engagement import JIRAProjectPrefetchEngagement
        from ..models.jira_project_prefetch_jira_instance import JIRAProjectPrefetchJiraInstance
        from ..models.jira_project_prefetch_product import JIRAProjectPrefetchProduct

        d = dict(src_dict)
        _engagement = d.pop("engagement", UNSET)
        engagement: JIRAProjectPrefetchEngagement | Unset
        if isinstance(_engagement, Unset):
            engagement = UNSET
        else:
            engagement = JIRAProjectPrefetchEngagement.from_dict(_engagement)

        _jira_instance = d.pop("jira_instance", UNSET)
        jira_instance: JIRAProjectPrefetchJiraInstance | Unset
        if isinstance(_jira_instance, Unset):
            jira_instance = UNSET
        else:
            jira_instance = JIRAProjectPrefetchJiraInstance.from_dict(_jira_instance)

        _product = d.pop("product", UNSET)
        product: JIRAProjectPrefetchProduct | Unset
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = JIRAProjectPrefetchProduct.from_dict(_product)

        jira_project_prefetch = cls(
            engagement=engagement,
            jira_instance=jira_instance,
            product=product,
        )

        jira_project_prefetch.additional_properties = d
        return jira_project_prefetch

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
