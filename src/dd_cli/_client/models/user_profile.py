from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dojo_group_member import DojoGroupMember
    from ..models.global_role import GlobalRole
    from ..models.product_member import ProductMember
    from ..models.product_type_member import ProductTypeMember
    from ..models.user import User
    from ..models.user_contact_info import UserContactInfo


T = TypeVar("T", bound="UserProfile")


@_attrs_define
class UserProfile:
    """
    Attributes:
        user (User):
        dojo_group_member (list[DojoGroupMember]):
        product_type_member (list[ProductTypeMember]):
        product_member (list[ProductMember]):
        user_contact_info (UserContactInfo | Unset):
        global_role (GlobalRole | Unset):
    """

    user: User
    dojo_group_member: list[DojoGroupMember]
    product_type_member: list[ProductTypeMember]
    product_member: list[ProductMember]
    user_contact_info: UserContactInfo | Unset = UNSET
    global_role: GlobalRole | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user.to_dict()

        dojo_group_member = []
        for dojo_group_member_item_data in self.dojo_group_member:
            dojo_group_member_item = dojo_group_member_item_data.to_dict()
            dojo_group_member.append(dojo_group_member_item)

        product_type_member = []
        for product_type_member_item_data in self.product_type_member:
            product_type_member_item = product_type_member_item_data.to_dict()
            product_type_member.append(product_type_member_item)

        product_member = []
        for product_member_item_data in self.product_member:
            product_member_item = product_member_item_data.to_dict()
            product_member.append(product_member_item)

        user_contact_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_contact_info, Unset):
            user_contact_info = self.user_contact_info.to_dict()

        global_role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.global_role, Unset):
            global_role = self.global_role.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "dojo_group_member": dojo_group_member,
                "product_type_member": product_type_member,
                "product_member": product_member,
            }
        )
        if user_contact_info is not UNSET:
            field_dict["user_contact_info"] = user_contact_info
        if global_role is not UNSET:
            field_dict["global_role"] = global_role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dojo_group_member import DojoGroupMember
        from ..models.global_role import GlobalRole
        from ..models.product_member import ProductMember
        from ..models.product_type_member import ProductTypeMember
        from ..models.user import User
        from ..models.user_contact_info import UserContactInfo

        d = dict(src_dict)
        user = User.from_dict(d.pop("user"))

        dojo_group_member = []
        _dojo_group_member = d.pop("dojo_group_member")
        for dojo_group_member_item_data in _dojo_group_member:
            dojo_group_member_item = DojoGroupMember.from_dict(dojo_group_member_item_data)

            dojo_group_member.append(dojo_group_member_item)

        product_type_member = []
        _product_type_member = d.pop("product_type_member")
        for product_type_member_item_data in _product_type_member:
            product_type_member_item = ProductTypeMember.from_dict(product_type_member_item_data)

            product_type_member.append(product_type_member_item)

        product_member = []
        _product_member = d.pop("product_member")
        for product_member_item_data in _product_member:
            product_member_item = ProductMember.from_dict(product_member_item_data)

            product_member.append(product_member_item)

        _user_contact_info = d.pop("user_contact_info", UNSET)
        user_contact_info: UserContactInfo | Unset
        if isinstance(_user_contact_info, Unset):
            user_contact_info = UNSET
        else:
            user_contact_info = UserContactInfo.from_dict(_user_contact_info)

        _global_role = d.pop("global_role", UNSET)
        global_role: GlobalRole | Unset
        if isinstance(_global_role, Unset):
            global_role = UNSET
        else:
            global_role = GlobalRole.from_dict(_global_role)

        user_profile = cls(
            user=user,
            dojo_group_member=dojo_group_member,
            product_type_member=product_type_member,
            product_member=product_member,
            user_contact_info=user_contact_info,
            global_role=global_role,
        )

        user_profile.additional_properties = d
        return user_profile

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
