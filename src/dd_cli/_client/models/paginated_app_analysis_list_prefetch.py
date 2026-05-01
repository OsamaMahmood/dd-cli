from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_app_analysis_list_prefetch_product import (
        PaginatedAppAnalysisListPrefetchProduct,
    )
    from ..models.paginated_app_analysis_list_prefetch_user import (
        PaginatedAppAnalysisListPrefetchUser,
    )


T = TypeVar("T", bound="PaginatedAppAnalysisListPrefetch")


@_attrs_define
class PaginatedAppAnalysisListPrefetch:
    """
    Attributes:
        product (PaginatedAppAnalysisListPrefetchProduct | Unset):
        user (PaginatedAppAnalysisListPrefetchUser | Unset):
    """

    product: PaginatedAppAnalysisListPrefetchProduct | Unset = UNSET
    user: PaginatedAppAnalysisListPrefetchUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product is not UNSET:
            field_dict["product"] = product
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_app_analysis_list_prefetch_product import (
            PaginatedAppAnalysisListPrefetchProduct,
        )
        from ..models.paginated_app_analysis_list_prefetch_user import (
            PaginatedAppAnalysisListPrefetchUser,
        )

        d = dict(src_dict)
        _product = d.pop("product", UNSET)
        product: PaginatedAppAnalysisListPrefetchProduct | Unset
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = PaginatedAppAnalysisListPrefetchProduct.from_dict(_product)

        _user = d.pop("user", UNSET)
        user: PaginatedAppAnalysisListPrefetchUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = PaginatedAppAnalysisListPrefetchUser.from_dict(_user)

        paginated_app_analysis_list_prefetch = cls(
            product=product,
            user=user,
        )

        paginated_app_analysis_list_prefetch.additional_properties = d
        return paginated_app_analysis_list_prefetch

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
