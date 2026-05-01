from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CredentialMapping")


@_attrs_define
class CredentialMapping:
    """
    Attributes:
        id (int):
        cred_id (int):
        is_authn_provider (bool | Unset):
        url (None | str | Unset):
        product (int | None | Unset):
        finding (int | None | Unset):
        engagement (int | None | Unset):
        test (int | None | Unset):
    """

    id: int
    cred_id: int
    is_authn_provider: bool | Unset = UNSET
    url: None | str | Unset = UNSET
    product: int | None | Unset = UNSET
    finding: int | None | Unset = UNSET
    engagement: int | None | Unset = UNSET
    test: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        cred_id = self.cred_id

        is_authn_provider = self.is_authn_provider

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        product: int | None | Unset
        if isinstance(self.product, Unset):
            product = UNSET
        else:
            product = self.product

        finding: int | None | Unset
        if isinstance(self.finding, Unset):
            finding = UNSET
        else:
            finding = self.finding

        engagement: int | None | Unset
        if isinstance(self.engagement, Unset):
            engagement = UNSET
        else:
            engagement = self.engagement

        test: int | None | Unset
        if isinstance(self.test, Unset):
            test = UNSET
        else:
            test = self.test

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "cred_id": cred_id,
            }
        )
        if is_authn_provider is not UNSET:
            field_dict["is_authn_provider"] = is_authn_provider
        if url is not UNSET:
            field_dict["url"] = url
        if product is not UNSET:
            field_dict["product"] = product
        if finding is not UNSET:
            field_dict["finding"] = finding
        if engagement is not UNSET:
            field_dict["engagement"] = engagement
        if test is not UNSET:
            field_dict["test"] = test

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        cred_id = d.pop("cred_id")

        is_authn_provider = d.pop("is_authn_provider", UNSET)

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_product(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        product = _parse_product(d.pop("product", UNSET))

        def _parse_finding(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        finding = _parse_finding(d.pop("finding", UNSET))

        def _parse_engagement(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        engagement = _parse_engagement(d.pop("engagement", UNSET))

        def _parse_test(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        test = _parse_test(d.pop("test", UNSET))

        credential_mapping = cls(
            id=id,
            cred_id=cred_id,
            is_authn_provider=is_authn_provider,
            url=url,
            product=product,
            finding=finding,
            engagement=engagement,
            test=test,
        )

        credential_mapping.additional_properties = d
        return credential_mapping

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
