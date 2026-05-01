from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.patched_asset_request_business_criticality_type_1 import (
    PatchedAssetRequestBusinessCriticalityType1,
)
from ..models.patched_asset_request_business_criticality_type_2_type_1 import (
    PatchedAssetRequestBusinessCriticalityType2Type1,
)
from ..models.patched_asset_request_business_criticality_type_3_type_1 import (
    PatchedAssetRequestBusinessCriticalityType3Type1,
)
from ..models.patched_asset_request_lifecycle_type_1 import PatchedAssetRequestLifecycleType1
from ..models.patched_asset_request_lifecycle_type_2_type_1 import (
    PatchedAssetRequestLifecycleType2Type1,
)
from ..models.patched_asset_request_lifecycle_type_3_type_1 import (
    PatchedAssetRequestLifecycleType3Type1,
)
from ..models.patched_asset_request_origin_type_1 import PatchedAssetRequestOriginType1
from ..models.patched_asset_request_origin_type_2_type_1 import PatchedAssetRequestOriginType2Type1
from ..models.patched_asset_request_origin_type_3_type_1 import PatchedAssetRequestOriginType3Type1
from ..models.patched_asset_request_platform_type_1 import PatchedAssetRequestPlatformType1
from ..models.patched_asset_request_platform_type_2_type_1 import (
    PatchedAssetRequestPlatformType2Type1,
)
from ..models.patched_asset_request_platform_type_3_type_1 import (
    PatchedAssetRequestPlatformType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedAssetRequest")


@_attrs_define
class PatchedAssetRequest:
    """
    Attributes:
        tags (list[str] | Unset):
        organization (int | Unset):
        asset_numeric_grade (int | None | Unset):
        enable_asset_tag_inheritance (bool | Unset):  Default: False.
        asset_managers (int | None | Unset):
        business_criticality (None | PatchedAssetRequestBusinessCriticalityType1 |
            PatchedAssetRequestBusinessCriticalityType2Type1 | PatchedAssetRequestBusinessCriticalityType3Type1 | Unset): *
            `very high` - Very High
            * `high` - High
            * `medium` - Medium
            * `low` - Low
            * `very low` - Very Low
            * `none` - None
        platform (None | PatchedAssetRequestPlatformType1 | PatchedAssetRequestPlatformType2Type1 |
            PatchedAssetRequestPlatformType3Type1 | Unset): * `web service` - API
            * `desktop` - Desktop
            * `iot` - Internet of Things
            * `mobile` - Mobile
            * `web` - Web
        lifecycle (None | PatchedAssetRequestLifecycleType1 | PatchedAssetRequestLifecycleType2Type1 |
            PatchedAssetRequestLifecycleType3Type1 | Unset): * `construction` - Construction
            * `production` - Production
            * `retirement` - Retirement
        origin (None | PatchedAssetRequestOriginType1 | PatchedAssetRequestOriginType2Type1 |
            PatchedAssetRequestOriginType3Type1 | Unset): * `third party library` - Third Party Library
            * `purchased` - Purchased
            * `contractor` - Contractor Developed
            * `internal` - Internally Developed
            * `open source` - Open Source
            * `outsourced` - Outsourced
        name (str | Unset):
        description (str | Unset):
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
    """

    tags: list[str] | Unset = UNSET
    organization: int | Unset = UNSET
    asset_numeric_grade: int | None | Unset = UNSET
    enable_asset_tag_inheritance: bool | Unset = False
    asset_managers: int | None | Unset = UNSET
    business_criticality: (
        None
        | PatchedAssetRequestBusinessCriticalityType1
        | PatchedAssetRequestBusinessCriticalityType2Type1
        | PatchedAssetRequestBusinessCriticalityType3Type1
        | Unset
    ) = UNSET
    platform: (
        None
        | PatchedAssetRequestPlatformType1
        | PatchedAssetRequestPlatformType2Type1
        | PatchedAssetRequestPlatformType3Type1
        | Unset
    ) = UNSET
    lifecycle: (
        None
        | PatchedAssetRequestLifecycleType1
        | PatchedAssetRequestLifecycleType2Type1
        | PatchedAssetRequestLifecycleType3Type1
        | Unset
    ) = UNSET
    origin: (
        None
        | PatchedAssetRequestOriginType1
        | PatchedAssetRequestOriginType2Type1
        | PatchedAssetRequestOriginType3Type1
        | Unset
    ) = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        organization = self.organization

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
            isinstance(self.business_criticality, PatchedAssetRequestBusinessCriticalityType1)
            or isinstance(
                self.business_criticality, PatchedAssetRequestBusinessCriticalityType2Type1
            )
            or isinstance(
                self.business_criticality, PatchedAssetRequestBusinessCriticalityType3Type1
            )
        ):
            business_criticality = self.business_criticality.value
        else:
            business_criticality = self.business_criticality

        platform: None | str | Unset
        if isinstance(self.platform, Unset):
            platform = UNSET
        elif (
            isinstance(self.platform, PatchedAssetRequestPlatformType1)
            or isinstance(self.platform, PatchedAssetRequestPlatformType2Type1)
            or isinstance(self.platform, PatchedAssetRequestPlatformType3Type1)
        ):
            platform = self.platform.value
        else:
            platform = self.platform

        lifecycle: None | str | Unset
        if isinstance(self.lifecycle, Unset):
            lifecycle = UNSET
        elif (
            isinstance(self.lifecycle, PatchedAssetRequestLifecycleType1)
            or isinstance(self.lifecycle, PatchedAssetRequestLifecycleType2Type1)
            or isinstance(self.lifecycle, PatchedAssetRequestLifecycleType3Type1)
        ):
            lifecycle = self.lifecycle.value
        else:
            lifecycle = self.lifecycle

        origin: None | str | Unset
        if isinstance(self.origin, Unset):
            origin = UNSET
        elif (
            isinstance(self.origin, PatchedAssetRequestOriginType1)
            or isinstance(self.origin, PatchedAssetRequestOriginType2Type1)
            or isinstance(self.origin, PatchedAssetRequestOriginType3Type1)
        ):
            origin = self.origin.value
        else:
            origin = self.origin

        name = self.name

        description = self.description

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tags is not UNSET:
            field_dict["tags"] = tags
        if organization is not UNSET:
            field_dict["organization"] = organization
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
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
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

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.tags, Unset):
            for tags_item_element in self.tags:
                files.append(("tags", (None, str(tags_item_element).encode(), "text/plain")))

        if not isinstance(self.organization, Unset):
            files.append(("organization", (None, str(self.organization).encode(), "text/plain")))

        if not isinstance(self.asset_numeric_grade, Unset):
            if isinstance(self.asset_numeric_grade, int):
                files.append(
                    (
                        "asset_numeric_grade",
                        (None, str(self.asset_numeric_grade).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "asset_numeric_grade",
                        (None, str(self.asset_numeric_grade).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.enable_asset_tag_inheritance, Unset):
            files.append(
                (
                    "enable_asset_tag_inheritance",
                    (None, str(self.enable_asset_tag_inheritance).encode(), "text/plain"),
                )
            )

        if not isinstance(self.asset_managers, Unset):
            if isinstance(self.asset_managers, int):
                files.append(
                    ("asset_managers", (None, str(self.asset_managers).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("asset_managers", (None, str(self.asset_managers).encode(), "text/plain"))
                )

        if not isinstance(self.business_criticality, Unset):
            if self.business_criticality is None:
                files.append(
                    (
                        "business_criticality",
                        (None, str(self.business_criticality).encode(), "text/plain"),
                    )
                )
            elif isinstance(
                self.business_criticality, PatchedAssetRequestBusinessCriticalityType1
            ) or isinstance(
                self.business_criticality, PatchedAssetRequestBusinessCriticalityType2Type1
            ):
                files.append(
                    (
                        "business_criticality",
                        (None, str(self.business_criticality.value).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "business_criticality",
                        (None, str(self.business_criticality.value).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.platform, Unset):
            if self.platform is None:
                files.append(("platform", (None, str(self.platform).encode(), "text/plain")))
            elif isinstance(self.platform, PatchedAssetRequestPlatformType1) or isinstance(
                self.platform, PatchedAssetRequestPlatformType2Type1
            ):
                files.append(("platform", (None, str(self.platform.value).encode(), "text/plain")))
            else:
                files.append(("platform", (None, str(self.platform.value).encode(), "text/plain")))

        if not isinstance(self.lifecycle, Unset):
            if self.lifecycle is None:
                files.append(("lifecycle", (None, str(self.lifecycle).encode(), "text/plain")))
            elif isinstance(self.lifecycle, PatchedAssetRequestLifecycleType1) or isinstance(
                self.lifecycle, PatchedAssetRequestLifecycleType2Type1
            ):
                files.append(
                    ("lifecycle", (None, str(self.lifecycle.value).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("lifecycle", (None, str(self.lifecycle.value).encode(), "text/plain"))
                )

        if not isinstance(self.origin, Unset):
            if self.origin is None:
                files.append(("origin", (None, str(self.origin).encode(), "text/plain")))
            elif isinstance(self.origin, PatchedAssetRequestOriginType1) or isinstance(
                self.origin, PatchedAssetRequestOriginType2Type1
            ):
                files.append(("origin", (None, str(self.origin.value).encode(), "text/plain")))
            else:
                files.append(("origin", (None, str(self.origin.value).encode(), "text/plain")))

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.user_records, Unset):
            if isinstance(self.user_records, int):
                files.append(
                    ("user_records", (None, str(self.user_records).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("user_records", (None, str(self.user_records).encode(), "text/plain"))
                )

        if not isinstance(self.revenue, Unset):
            if isinstance(self.revenue, str):
                files.append(("revenue", (None, str(self.revenue).encode(), "text/plain")))
            else:
                files.append(("revenue", (None, str(self.revenue).encode(), "text/plain")))

        if not isinstance(self.external_audience, Unset):
            files.append(
                ("external_audience", (None, str(self.external_audience).encode(), "text/plain"))
            )

        if not isinstance(self.internet_accessible, Unset):
            files.append(
                (
                    "internet_accessible",
                    (None, str(self.internet_accessible).encode(), "text/plain"),
                )
            )

        if not isinstance(self.enable_simple_risk_acceptance, Unset):
            files.append(
                (
                    "enable_simple_risk_acceptance",
                    (None, str(self.enable_simple_risk_acceptance).encode(), "text/plain"),
                )
            )

        if not isinstance(self.enable_full_risk_acceptance, Unset):
            files.append(
                (
                    "enable_full_risk_acceptance",
                    (None, str(self.enable_full_risk_acceptance).encode(), "text/plain"),
                )
            )

        if not isinstance(self.disable_sla_breach_notifications, Unset):
            files.append(
                (
                    "disable_sla_breach_notifications",
                    (None, str(self.disable_sla_breach_notifications).encode(), "text/plain"),
                )
            )

        if not isinstance(self.technical_contact, Unset):
            if isinstance(self.technical_contact, int):
                files.append(
                    (
                        "technical_contact",
                        (None, str(self.technical_contact).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "technical_contact",
                        (None, str(self.technical_contact).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.team_manager, Unset):
            if isinstance(self.team_manager, int):
                files.append(
                    ("team_manager", (None, str(self.team_manager).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("team_manager", (None, str(self.team_manager).encode(), "text/plain"))
                )

        if not isinstance(self.sla_configuration, Unset):
            files.append(
                ("sla_configuration", (None, str(self.sla_configuration).encode(), "text/plain"))
            )

        if not isinstance(self.regulations, Unset):
            for regulations_item_element in self.regulations:
                files.append(
                    ("regulations", (None, str(regulations_item_element).encode(), "text/plain"))
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tags = cast(list[str], d.pop("tags", UNSET))

        organization = d.pop("organization", UNSET)

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
            None
            | PatchedAssetRequestBusinessCriticalityType1
            | PatchedAssetRequestBusinessCriticalityType2Type1
            | PatchedAssetRequestBusinessCriticalityType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                business_criticality_type_1 = PatchedAssetRequestBusinessCriticalityType1(data)

                return business_criticality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                business_criticality_type_2_type_1 = (
                    PatchedAssetRequestBusinessCriticalityType2Type1(data)
                )

                return business_criticality_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                business_criticality_type_3_type_1 = (
                    PatchedAssetRequestBusinessCriticalityType3Type1(data)
                )

                return business_criticality_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PatchedAssetRequestBusinessCriticalityType1
                | PatchedAssetRequestBusinessCriticalityType2Type1
                | PatchedAssetRequestBusinessCriticalityType3Type1
                | Unset,
                data,
            )

        business_criticality = _parse_business_criticality(d.pop("business_criticality", UNSET))

        def _parse_platform(
            data: object,
        ) -> (
            None
            | PatchedAssetRequestPlatformType1
            | PatchedAssetRequestPlatformType2Type1
            | PatchedAssetRequestPlatformType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                platform_type_1 = PatchedAssetRequestPlatformType1(data)

                return platform_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                platform_type_2_type_1 = PatchedAssetRequestPlatformType2Type1(data)

                return platform_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                platform_type_3_type_1 = PatchedAssetRequestPlatformType3Type1(data)

                return platform_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PatchedAssetRequestPlatformType1
                | PatchedAssetRequestPlatformType2Type1
                | PatchedAssetRequestPlatformType3Type1
                | Unset,
                data,
            )

        platform = _parse_platform(d.pop("platform", UNSET))

        def _parse_lifecycle(
            data: object,
        ) -> (
            None
            | PatchedAssetRequestLifecycleType1
            | PatchedAssetRequestLifecycleType2Type1
            | PatchedAssetRequestLifecycleType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lifecycle_type_1 = PatchedAssetRequestLifecycleType1(data)

                return lifecycle_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lifecycle_type_2_type_1 = PatchedAssetRequestLifecycleType2Type1(data)

                return lifecycle_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lifecycle_type_3_type_1 = PatchedAssetRequestLifecycleType3Type1(data)

                return lifecycle_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PatchedAssetRequestLifecycleType1
                | PatchedAssetRequestLifecycleType2Type1
                | PatchedAssetRequestLifecycleType3Type1
                | Unset,
                data,
            )

        lifecycle = _parse_lifecycle(d.pop("lifecycle", UNSET))

        def _parse_origin(
            data: object,
        ) -> (
            None
            | PatchedAssetRequestOriginType1
            | PatchedAssetRequestOriginType2Type1
            | PatchedAssetRequestOriginType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_type_1 = PatchedAssetRequestOriginType1(data)

                return origin_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_type_2_type_1 = PatchedAssetRequestOriginType2Type1(data)

                return origin_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_type_3_type_1 = PatchedAssetRequestOriginType3Type1(data)

                return origin_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PatchedAssetRequestOriginType1
                | PatchedAssetRequestOriginType2Type1
                | PatchedAssetRequestOriginType3Type1
                | Unset,
                data,
            )

        origin = _parse_origin(d.pop("origin", UNSET))

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

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

        patched_asset_request = cls(
            tags=tags,
            organization=organization,
            asset_numeric_grade=asset_numeric_grade,
            enable_asset_tag_inheritance=enable_asset_tag_inheritance,
            asset_managers=asset_managers,
            business_criticality=business_criticality,
            platform=platform,
            lifecycle=lifecycle,
            origin=origin,
            name=name,
            description=description,
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
        )

        patched_asset_request.additional_properties = d
        return patched_asset_request

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
