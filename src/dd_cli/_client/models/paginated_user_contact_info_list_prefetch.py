from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_user_contact_info_list_prefetch_user import (
        PaginatedUserContactInfoListPrefetchUser,
    )


T = TypeVar("T", bound="PaginatedUserContactInfoListPrefetch")


@_attrs_define
class PaginatedUserContactInfoListPrefetch:
    """
    Attributes:
        user (PaginatedUserContactInfoListPrefetchUser | Unset):
    """

    user: PaginatedUserContactInfoListPrefetchUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_user_contact_info_list_prefetch_user import (
            PaginatedUserContactInfoListPrefetchUser,
        )

        d = dict(src_dict)
        _user = d.pop("user", UNSET)
        user: PaginatedUserContactInfoListPrefetchUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = PaginatedUserContactInfoListPrefetchUser.from_dict(_user)

        paginated_user_contact_info_list_prefetch = cls(
            user=user,
        )

        paginated_user_contact_info_list_prefetch.additional_properties = d
        return paginated_user_contact_info_list_prefetch

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
