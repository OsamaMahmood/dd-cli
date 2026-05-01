from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_product_member_list_prefetch_product import (
        PaginatedProductMemberListPrefetchProduct,
    )
    from ..models.paginated_product_member_list_prefetch_role import (
        PaginatedProductMemberListPrefetchRole,
    )
    from ..models.paginated_product_member_list_prefetch_user import (
        PaginatedProductMemberListPrefetchUser,
    )


T = TypeVar("T", bound="PaginatedProductMemberListPrefetch")


@_attrs_define
class PaginatedProductMemberListPrefetch:
    """
    Attributes:
        product (PaginatedProductMemberListPrefetchProduct | Unset):
        role (PaginatedProductMemberListPrefetchRole | Unset):
        user (PaginatedProductMemberListPrefetchUser | Unset):
    """

    product: PaginatedProductMemberListPrefetchProduct | Unset = UNSET
    role: PaginatedProductMemberListPrefetchRole | Unset = UNSET
    user: PaginatedProductMemberListPrefetchUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product is not UNSET:
            field_dict["product"] = product
        if role is not UNSET:
            field_dict["role"] = role
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_product_member_list_prefetch_product import (
            PaginatedProductMemberListPrefetchProduct,
        )
        from ..models.paginated_product_member_list_prefetch_role import (
            PaginatedProductMemberListPrefetchRole,
        )
        from ..models.paginated_product_member_list_prefetch_user import (
            PaginatedProductMemberListPrefetchUser,
        )

        d = dict(src_dict)
        _product = d.pop("product", UNSET)
        product: PaginatedProductMemberListPrefetchProduct | Unset
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = PaginatedProductMemberListPrefetchProduct.from_dict(_product)

        _role = d.pop("role", UNSET)
        role: PaginatedProductMemberListPrefetchRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = PaginatedProductMemberListPrefetchRole.from_dict(_role)

        _user = d.pop("user", UNSET)
        user: PaginatedProductMemberListPrefetchUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = PaginatedProductMemberListPrefetchUser.from_dict(_user)

        paginated_product_member_list_prefetch = cls(
            product=product,
            role=role,
            user=user,
        )

        paginated_product_member_list_prefetch.additional_properties = d
        return paginated_product_member_list_prefetch

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
