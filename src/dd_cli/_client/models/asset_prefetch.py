from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_prefetch_authorization_groups import AssetPrefetchAuthorizationGroups
    from ..models.asset_prefetch_members import AssetPrefetchMembers
    from ..models.asset_prefetch_prod_type import AssetPrefetchProdType
    from ..models.asset_prefetch_product_manager import AssetPrefetchProductManager
    from ..models.asset_prefetch_regulations import AssetPrefetchRegulations
    from ..models.asset_prefetch_sla_configuration import AssetPrefetchSlaConfiguration
    from ..models.asset_prefetch_team_manager import AssetPrefetchTeamManager
    from ..models.asset_prefetch_technical_contact import AssetPrefetchTechnicalContact


T = TypeVar("T", bound="AssetPrefetch")


@_attrs_define
class AssetPrefetch:
    """
    Attributes:
        authorization_groups (AssetPrefetchAuthorizationGroups | Unset):
        members (AssetPrefetchMembers | Unset):
        prod_type (AssetPrefetchProdType | Unset):
        product_manager (AssetPrefetchProductManager | Unset):
        regulations (AssetPrefetchRegulations | Unset):
        sla_configuration (AssetPrefetchSlaConfiguration | Unset):
        team_manager (AssetPrefetchTeamManager | Unset):
        technical_contact (AssetPrefetchTechnicalContact | Unset):
    """

    authorization_groups: AssetPrefetchAuthorizationGroups | Unset = UNSET
    members: AssetPrefetchMembers | Unset = UNSET
    prod_type: AssetPrefetchProdType | Unset = UNSET
    product_manager: AssetPrefetchProductManager | Unset = UNSET
    regulations: AssetPrefetchRegulations | Unset = UNSET
    sla_configuration: AssetPrefetchSlaConfiguration | Unset = UNSET
    team_manager: AssetPrefetchTeamManager | Unset = UNSET
    technical_contact: AssetPrefetchTechnicalContact | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authorization_groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authorization_groups, Unset):
            authorization_groups = self.authorization_groups.to_dict()

        members: dict[str, Any] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = self.members.to_dict()

        prod_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prod_type, Unset):
            prod_type = self.prod_type.to_dict()

        product_manager: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_manager, Unset):
            product_manager = self.product_manager.to_dict()

        regulations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.regulations, Unset):
            regulations = self.regulations.to_dict()

        sla_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sla_configuration, Unset):
            sla_configuration = self.sla_configuration.to_dict()

        team_manager: dict[str, Any] | Unset = UNSET
        if not isinstance(self.team_manager, Unset):
            team_manager = self.team_manager.to_dict()

        technical_contact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.technical_contact, Unset):
            technical_contact = self.technical_contact.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authorization_groups is not UNSET:
            field_dict["authorization_groups"] = authorization_groups
        if members is not UNSET:
            field_dict["members"] = members
        if prod_type is not UNSET:
            field_dict["prod_type"] = prod_type
        if product_manager is not UNSET:
            field_dict["product_manager"] = product_manager
        if regulations is not UNSET:
            field_dict["regulations"] = regulations
        if sla_configuration is not UNSET:
            field_dict["sla_configuration"] = sla_configuration
        if team_manager is not UNSET:
            field_dict["team_manager"] = team_manager
        if technical_contact is not UNSET:
            field_dict["technical_contact"] = technical_contact

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_prefetch_authorization_groups import AssetPrefetchAuthorizationGroups
        from ..models.asset_prefetch_members import AssetPrefetchMembers
        from ..models.asset_prefetch_prod_type import AssetPrefetchProdType
        from ..models.asset_prefetch_product_manager import AssetPrefetchProductManager
        from ..models.asset_prefetch_regulations import AssetPrefetchRegulations
        from ..models.asset_prefetch_sla_configuration import AssetPrefetchSlaConfiguration
        from ..models.asset_prefetch_team_manager import AssetPrefetchTeamManager
        from ..models.asset_prefetch_technical_contact import AssetPrefetchTechnicalContact

        d = dict(src_dict)
        _authorization_groups = d.pop("authorization_groups", UNSET)
        authorization_groups: AssetPrefetchAuthorizationGroups | Unset
        if isinstance(_authorization_groups, Unset):
            authorization_groups = UNSET
        else:
            authorization_groups = AssetPrefetchAuthorizationGroups.from_dict(_authorization_groups)

        _members = d.pop("members", UNSET)
        members: AssetPrefetchMembers | Unset
        if isinstance(_members, Unset):
            members = UNSET
        else:
            members = AssetPrefetchMembers.from_dict(_members)

        _prod_type = d.pop("prod_type", UNSET)
        prod_type: AssetPrefetchProdType | Unset
        if isinstance(_prod_type, Unset):
            prod_type = UNSET
        else:
            prod_type = AssetPrefetchProdType.from_dict(_prod_type)

        _product_manager = d.pop("product_manager", UNSET)
        product_manager: AssetPrefetchProductManager | Unset
        if isinstance(_product_manager, Unset):
            product_manager = UNSET
        else:
            product_manager = AssetPrefetchProductManager.from_dict(_product_manager)

        _regulations = d.pop("regulations", UNSET)
        regulations: AssetPrefetchRegulations | Unset
        if isinstance(_regulations, Unset):
            regulations = UNSET
        else:
            regulations = AssetPrefetchRegulations.from_dict(_regulations)

        _sla_configuration = d.pop("sla_configuration", UNSET)
        sla_configuration: AssetPrefetchSlaConfiguration | Unset
        if isinstance(_sla_configuration, Unset):
            sla_configuration = UNSET
        else:
            sla_configuration = AssetPrefetchSlaConfiguration.from_dict(_sla_configuration)

        _team_manager = d.pop("team_manager", UNSET)
        team_manager: AssetPrefetchTeamManager | Unset
        if isinstance(_team_manager, Unset):
            team_manager = UNSET
        else:
            team_manager = AssetPrefetchTeamManager.from_dict(_team_manager)

        _technical_contact = d.pop("technical_contact", UNSET)
        technical_contact: AssetPrefetchTechnicalContact | Unset
        if isinstance(_technical_contact, Unset):
            technical_contact = UNSET
        else:
            technical_contact = AssetPrefetchTechnicalContact.from_dict(_technical_contact)

        asset_prefetch = cls(
            authorization_groups=authorization_groups,
            members=members,
            prod_type=prod_type,
            product_manager=product_manager,
            regulations=regulations,
            sla_configuration=sla_configuration,
            team_manager=team_manager,
            technical_contact=technical_contact,
        )

        asset_prefetch.additional_properties = d
        return asset_prefetch

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
