from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.language_prefetch_language import LanguagePrefetchLanguage
    from ..models.language_prefetch_product import LanguagePrefetchProduct
    from ..models.language_prefetch_user import LanguagePrefetchUser


T = TypeVar("T", bound="LanguagePrefetch")


@_attrs_define
class LanguagePrefetch:
    """
    Attributes:
        language (LanguagePrefetchLanguage | Unset):
        product (LanguagePrefetchProduct | Unset):
        user (LanguagePrefetchUser | Unset):
    """

    language: LanguagePrefetchLanguage | Unset = UNSET
    product: LanguagePrefetchProduct | Unset = UNSET
    user: LanguagePrefetchUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        product: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if language is not UNSET:
            field_dict["language"] = language
        if product is not UNSET:
            field_dict["product"] = product
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.language_prefetch_language import LanguagePrefetchLanguage
        from ..models.language_prefetch_product import LanguagePrefetchProduct
        from ..models.language_prefetch_user import LanguagePrefetchUser

        d = dict(src_dict)
        _language = d.pop("language", UNSET)
        language: LanguagePrefetchLanguage | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = LanguagePrefetchLanguage.from_dict(_language)

        _product = d.pop("product", UNSET)
        product: LanguagePrefetchProduct | Unset
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = LanguagePrefetchProduct.from_dict(_product)

        _user = d.pop("user", UNSET)
        user: LanguagePrefetchUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = LanguagePrefetchUser.from_dict(_user)

        language_prefetch = cls(
            language=language,
            product=product,
            user=user,
        )

        language_prefetch.additional_properties = d
        return language_prefetch

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
