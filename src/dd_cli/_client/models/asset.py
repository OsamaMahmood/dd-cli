from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.asset_business_criticality_type_1 import AssetBusinessCriticalityType1
from ..models.asset_business_criticality_type_2_type_1 import AssetBusinessCriticalityType2Type1
from ..models.asset_business_criticality_type_3_type_1 import AssetBusinessCriticalityType3Type1
from ..models.asset_lifecycle_type_1 import AssetLifecycleType1
from ..models.asset_lifecycle_type_2_type_1 import AssetLifecycleType2Type1
from ..models.asset_lifecycle_type_3_type_1 import AssetLifecycleType3Type1
from ..models.asset_origin_type_1 import AssetOriginType1
from ..models.asset_origin_type_2_type_1 import AssetOriginType2Type1
from ..models.asset_origin_type_3_type_1 import AssetOriginType3Type1
from ..models.asset_platform_type_1 import AssetPlatformType1
from ..models.asset_platform_type_2_type_1 import AssetPlatformType2Type1
from ..models.asset_platform_type_3_type_1 import AssetPlatformType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_prefetch import AssetPrefetch
    from ..models.product_meta import ProductMeta


T = TypeVar("T", bound="Asset")


@_attrs_define
class Asset:
    """
    Attributes:
        id (int):
        findings_count (int):
        findings_list (list[int]):
        asset_meta (list[ProductMeta]):
        organization (int):
        name (str):
        description (str):
        created (datetime.datetime | None):
        members (list[int]):
        authorization_groups (list[int]):
        tags (list[str] | Unset):
        asset_numeric_grade (int | None | Unset):
        enable_asset_tag_inheritance (bool | Unset):  Default: False.
        asset_managers (int | None | Unset):
        business_criticality (AssetBusinessCriticalityType1 | AssetBusinessCriticalityType2Type1 |
            AssetBusinessCriticalityType3Type1 | None | Unset): * `very high` - Very High
            * `high` - High
            * `medium` - Medium
            * `low` - Low
            * `very low` - Very Low
            * `none` - None
        platform (AssetPlatformType1 | AssetPlatformType2Type1 | AssetPlatformType3Type1 | None | Unset): * `web
            service` - API
            * `desktop` - Desktop
            * `iot` - Internet of Things
            * `mobile` - Mobile
            * `web` - Web
        lifecycle (AssetLifecycleType1 | AssetLifecycleType2Type1 | AssetLifecycleType3Type1 | None | Unset): *
            `construction` - Construction
            * `production` - Production
            * `retirement` - Retirement
        origin (AssetOriginType1 | AssetOriginType2Type1 | AssetOriginType3Type1 | None | Unset): * `third party
            library` - Third Party Library
            * `purchased` - Purchased
            * `contractor` - Contractor Developed
            * `internal` - Internally Developed
            * `open source` - Open Source
            * `outsourced` - Outsourced
        user_records (int | None | Unset): Estimate the number of user records within the application.
        revenue (None | str | Unset): Estimate the application's revenue.
        external_audience (bool | Unset): Specify if the application is used by people outside the organization.
        internet_accessible (bool | Unset): Specify if the application is accessible from the public internet.
        enable_simple_risk_acceptance (bool | Unset): Allows simple risk acceptance by checking/unchecking a checkbox.
        enable_full_risk_acceptance (bool | Unset): Allows full risk acceptance using a risk acceptance form, expiration
            date, uploaded proof, etc.
        disable_sla_breach_notifications (bool | Unset): Disable SLA breach notifications if configured in the global
            settings
        technical_contact (int | None | Unset):
        team_manager (int | None | Unset):
        sla_configuration (int | Unset):
        regulations (list[int] | Unset):
        prefetch (AssetPrefetch | Unset):
    """

    id: int
    findings_count: int
    findings_list: list[int]
    asset_meta: list[ProductMeta]
    organization: int
    name: str
    description: str
    created: datetime.datetime | None
    members: list[int]
    authorization_groups: list[int]
    tags: list[str] | Unset = UNSET
    asset_numeric_grade: int | None | Unset = UNSET
    enable_asset_tag_inheritance: bool | Unset = False
    asset_managers: int | None | Unset = UNSET
    business_criticality: (
        AssetBusinessCriticalityType1
        | AssetBusinessCriticalityType2Type1
        | AssetBusinessCriticalityType3Type1
        | None
        | Unset
    ) = UNSET
    platform: (
        AssetPlatformType1 | AssetPlatformType2Type1 | AssetPlatformType3Type1 | None | Unset
    ) = UNSET
    lifecycle: (
        AssetLifecycleType1 | AssetLifecycleType2Type1 | AssetLifecycleType3Type1 | None | Unset
    ) = UNSET
    origin: AssetOriginType1 | AssetOriginType2Type1 | AssetOriginType3Type1 | None | Unset = UNSET
    user_records: int | None | Unset = UNSET
    revenue: None | str | Unset = UNSET
    external_audience: bool | Unset = UNSET
    internet_accessible: bool | Unset = UNSET
    enable_simple_risk_acceptance: bool | Unset = UNSET
    enable_full_risk_acceptance: bool | Unset = UNSET
    disable_sla_breach_notifications: bool | Unset = UNSET
    technical_contact: int | None | Unset = UNSET
    team_manager: int | None | Unset = UNSET
    sla_configuration: int | Unset = UNSET
    regulations: list[int] | Unset = UNSET
    prefetch: AssetPrefetch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        findings_count = self.findings_count

        findings_list = self.findings_list

        asset_meta = []
        for asset_meta_item_data in self.asset_meta:
            asset_meta_item = asset_meta_item_data.to_dict()
            asset_meta.append(asset_meta_item)

        organization = self.organization

        name = self.name

        description = self.description

        created: None | str
        if isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        members = self.members

        authorization_groups = self.authorization_groups

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        asset_numeric_grade: int | None | Unset
        if isinstance(self.asset_numeric_grade, Unset):
            asset_numeric_grade = UNSET
        else:
            asset_numeric_grade = self.asset_numeric_grade

        enable_asset_tag_inheritance = self.enable_asset_tag_inheritance

        asset_managers: int | None | Unset
        if isinstance(self.asset_managers, Unset):
            asset_managers = UNSET
        else:
            asset_managers = self.asset_managers

        business_criticality: None | str | Unset
        if isinstance(self.business_criticality, Unset):
            business_criticality = UNSET
        elif (
            isinstance(self.business_criticality, AssetBusinessCriticalityType1)
            or isinstance(self.business_criticality, AssetBusinessCriticalityType2Type1)
            or isinstance(self.business_criticality, AssetBusinessCriticalityType3Type1)
        ):
            business_criticality = self.business_criticality.value
        else:
            business_criticality = self.business_criticality

        platform: None | str | Unset
        if isinstance(self.platform, Unset):
            platform = UNSET
        elif (
            isinstance(self.platform, AssetPlatformType1)
            or isinstance(self.platform, AssetPlatformType2Type1)
            or isinstance(self.platform, AssetPlatformType3Type1)
        ):
            platform = self.platform.value
        else:
            platform = self.platform

        lifecycle: None | str | Unset
        if isinstance(self.lifecycle, Unset):
            lifecycle = UNSET
        elif (
            isinstance(self.lifecycle, AssetLifecycleType1)
            or isinstance(self.lifecycle, AssetLifecycleType2Type1)
            or isinstance(self.lifecycle, AssetLifecycleType3Type1)
        ):
            lifecycle = self.lifecycle.value
        else:
            lifecycle = self.lifecycle

        origin: None | str | Unset
        if isinstance(self.origin, Unset):
            origin = UNSET
        elif (
            isinstance(self.origin, AssetOriginType1)
            or isinstance(self.origin, AssetOriginType2Type1)
            or isinstance(self.origin, AssetOriginType3Type1)
        ):
            origin = self.origin.value
        else:
            origin = self.origin

        user_records: int | None | Unset
        if isinstance(self.user_records, Unset):
            user_records = UNSET
        else:
            user_records = self.user_records

        revenue: None | str | Unset
        if isinstance(self.revenue, Unset):
            revenue = UNSET
        else:
            revenue = self.revenue

        external_audience = self.external_audience

        internet_accessible = self.internet_accessible

        enable_simple_risk_acceptance = self.enable_simple_risk_acceptance

        enable_full_risk_acceptance = self.enable_full_risk_acceptance

        disable_sla_breach_notifications = self.disable_sla_breach_notifications

        technical_contact: int | None | Unset
        if isinstance(self.technical_contact, Unset):
            technical_contact = UNSET
        else:
            technical_contact = self.technical_contact

        team_manager: int | None | Unset
        if isinstance(self.team_manager, Unset):
            team_manager = UNSET
        else:
            team_manager = self.team_manager

        sla_configuration = self.sla_configuration

        regulations: list[int] | Unset = UNSET
        if not isinstance(self.regulations, Unset):
            regulations = self.regulations

        prefetch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prefetch, Unset):
            prefetch = self.prefetch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "findings_count": findings_count,
                "findings_list": findings_list,
                "asset_meta": asset_meta,
                "organization": organization,
                "name": name,
                "description": description,
                "created": created,
                "members": members,
                "authorization_groups": authorization_groups,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if asset_numeric_grade is not UNSET:
            field_dict["asset_numeric_grade"] = asset_numeric_grade
        if enable_asset_tag_inheritance is not UNSET:
            field_dict["enable_asset_tag_inheritance"] = enable_asset_tag_inheritance
        if asset_managers is not UNSET:
            field_dict["asset_managers"] = asset_managers
        if business_criticality is not UNSET:
            field_dict["business_criticality"] = business_criticality
        if platform is not UNSET:
            field_dict["platform"] = platform
        if lifecycle is not UNSET:
            field_dict["lifecycle"] = lifecycle
        if origin is not UNSET:
            field_dict["origin"] = origin
        if user_records is not UNSET:
            field_dict["user_records"] = user_records
        if revenue is not UNSET:
            field_dict["revenue"] = revenue
        if external_audience is not UNSET:
            field_dict["external_audience"] = external_audience
        if internet_accessible is not UNSET:
            field_dict["internet_accessible"] = internet_accessible
        if enable_simple_risk_acceptance is not UNSET:
            field_dict["enable_simple_risk_acceptance"] = enable_simple_risk_acceptance
        if enable_full_risk_acceptance is not UNSET:
            field_dict["enable_full_risk_acceptance"] = enable_full_risk_acceptance
        if disable_sla_breach_notifications is not UNSET:
            field_dict["disable_sla_breach_notifications"] = disable_sla_breach_notifications
        if technical_contact is not UNSET:
            field_dict["technical_contact"] = technical_contact
        if team_manager is not UNSET:
            field_dict["team_manager"] = team_manager
        if sla_configuration is not UNSET:
            field_dict["sla_configuration"] = sla_configuration
        if regulations is not UNSET:
            field_dict["regulations"] = regulations
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_prefetch import AssetPrefetch
        from ..models.product_meta import ProductMeta

        d = dict(src_dict)
        id = d.pop("id")

        findings_count = d.pop("findings_count")

        findings_list = cast(list[int], d.pop("findings_list"))

        asset_meta = []
        _asset_meta = d.pop("asset_meta")
        for asset_meta_item_data in _asset_meta:
            asset_meta_item = ProductMeta.from_dict(asset_meta_item_data)

            asset_meta.append(asset_meta_item)

        organization = d.pop("organization")

        name = d.pop("name")

        description = d.pop("description")

        def _parse_created(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_type_0 = isoparse(data)

                return created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        created = _parse_created(d.pop("created"))

        members = cast(list[int], d.pop("members"))

        authorization_groups = cast(list[int], d.pop("authorization_groups"))

        tags = cast(list[str], d.pop("tags", UNSET))

        def _parse_asset_numeric_grade(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        asset_numeric_grade = _parse_asset_numeric_grade(d.pop("asset_numeric_grade", UNSET))

        enable_asset_tag_inheritance = d.pop("enable_asset_tag_inheritance", UNSET)

        def _parse_asset_managers(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        asset_managers = _parse_asset_managers(d.pop("asset_managers", UNSET))

        def _parse_business_criticality(
            data: object,
        ) -> (
            AssetBusinessCriticalityType1
            | AssetBusinessCriticalityType2Type1
            | AssetBusinessCriticalityType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                business_criticality_type_1 = AssetBusinessCriticalityType1(data)

                return business_criticality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                business_criticality_type_2_type_1 = AssetBusinessCriticalityType2Type1(data)

                return business_criticality_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                business_criticality_type_3_type_1 = AssetBusinessCriticalityType3Type1(data)

                return business_criticality_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AssetBusinessCriticalityType1
                | AssetBusinessCriticalityType2Type1
                | AssetBusinessCriticalityType3Type1
                | None
                | Unset,
                data,
            )

        business_criticality = _parse_business_criticality(d.pop("business_criticality", UNSET))

        def _parse_platform(
            data: object,
        ) -> AssetPlatformType1 | AssetPlatformType2Type1 | AssetPlatformType3Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                platform_type_1 = AssetPlatformType1(data)

                return platform_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                platform_type_2_type_1 = AssetPlatformType2Type1(data)

                return platform_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                platform_type_3_type_1 = AssetPlatformType3Type1(data)

                return platform_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AssetPlatformType1
                | AssetPlatformType2Type1
                | AssetPlatformType3Type1
                | None
                | Unset,
                data,
            )

        platform = _parse_platform(d.pop("platform", UNSET))

        def _parse_lifecycle(
            data: object,
        ) -> (
            AssetLifecycleType1 | AssetLifecycleType2Type1 | AssetLifecycleType3Type1 | None | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lifecycle_type_1 = AssetLifecycleType1(data)

                return lifecycle_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lifecycle_type_2_type_1 = AssetLifecycleType2Type1(data)

                return lifecycle_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lifecycle_type_3_type_1 = AssetLifecycleType3Type1(data)

                return lifecycle_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AssetLifecycleType1
                | AssetLifecycleType2Type1
                | AssetLifecycleType3Type1
                | None
                | Unset,
                data,
            )

        lifecycle = _parse_lifecycle(d.pop("lifecycle", UNSET))

        def _parse_origin(
            data: object,
        ) -> AssetOriginType1 | AssetOriginType2Type1 | AssetOriginType3Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_type_1 = AssetOriginType1(data)

                return origin_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_type_2_type_1 = AssetOriginType2Type1(data)

                return origin_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_type_3_type_1 = AssetOriginType3Type1(data)

                return origin_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AssetOriginType1 | AssetOriginType2Type1 | AssetOriginType3Type1 | None | Unset,
                data,
            )

        origin = _parse_origin(d.pop("origin", UNSET))

        def _parse_user_records(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_records = _parse_user_records(d.pop("user_records", UNSET))

        def _parse_revenue(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        revenue = _parse_revenue(d.pop("revenue", UNSET))

        external_audience = d.pop("external_audience", UNSET)

        internet_accessible = d.pop("internet_accessible", UNSET)

        enable_simple_risk_acceptance = d.pop("enable_simple_risk_acceptance", UNSET)

        enable_full_risk_acceptance = d.pop("enable_full_risk_acceptance", UNSET)

        disable_sla_breach_notifications = d.pop("disable_sla_breach_notifications", UNSET)

        def _parse_technical_contact(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        technical_contact = _parse_technical_contact(d.pop("technical_contact", UNSET))

        def _parse_team_manager(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        team_manager = _parse_team_manager(d.pop("team_manager", UNSET))

        sla_configuration = d.pop("sla_configuration", UNSET)

        regulations = cast(list[int], d.pop("regulations", UNSET))

        _prefetch = d.pop("prefetch", UNSET)
        prefetch: AssetPrefetch | Unset
        if isinstance(_prefetch, Unset):
            prefetch = UNSET
        else:
            prefetch = AssetPrefetch.from_dict(_prefetch)

        asset = cls(
            id=id,
            findings_count=findings_count,
            findings_list=findings_list,
            asset_meta=asset_meta,
            organization=organization,
            name=name,
            description=description,
            created=created,
            members=members,
            authorization_groups=authorization_groups,
            tags=tags,
            asset_numeric_grade=asset_numeric_grade,
            enable_asset_tag_inheritance=enable_asset_tag_inheritance,
            asset_managers=asset_managers,
            business_criticality=business_criticality,
            platform=platform,
            lifecycle=lifecycle,
            origin=origin,
            user_records=user_records,
            revenue=revenue,
            external_audience=external_audience,
            internet_accessible=internet_accessible,
            enable_simple_risk_acceptance=enable_simple_risk_acceptance,
            enable_full_risk_acceptance=enable_full_risk_acceptance,
            disable_sla_breach_notifications=disable_sla_breach_notifications,
            technical_contact=technical_contact,
            team_manager=team_manager,
            sla_configuration=sla_configuration,
            regulations=regulations,
            prefetch=prefetch,
        )

        asset.additional_properties = d
        return asset

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
