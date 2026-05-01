from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.finding_engagement_engagement_type_type_1 import FindingEngagementEngagementTypeType1
from ..models.finding_engagement_engagement_type_type_2_type_1 import (
    FindingEngagementEngagementTypeType2Type1,
)
from ..models.finding_engagement_engagement_type_type_3_type_1 import (
    FindingEngagementEngagementTypeType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.finding_product import FindingProduct


T = TypeVar("T", bound="FindingEngagement")


@_attrs_define
class FindingEngagement:
    """
    Attributes:
        id (int):
        target_start (datetime.date):
        target_end (datetime.date):
        created (datetime.datetime | None):
        updated (datetime.datetime | None):
        name (None | str | Unset):
        description (None | str | Unset):
        product (FindingProduct | Unset):
        branch_tag (None | str | Unset): Tag or branch of the product the engagement tested.
        engagement_type (FindingEngagementEngagementTypeType1 | FindingEngagementEngagementTypeType2Type1 |
            FindingEngagementEngagementTypeType3Type1 | None | Unset): * `Interactive` - Interactive
            * `CI/CD` - CI/CD
        build_id (None | str | Unset): Build ID of the product the engagement tested.
        commit_hash (None | str | Unset): Commit hash from repo
        version (None | str | Unset): Version of the product the engagement tested.
    """

    id: int
    target_start: datetime.date
    target_end: datetime.date
    created: datetime.datetime | None
    updated: datetime.datetime | None
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    product: FindingProduct | Unset = UNSET
    branch_tag: None | str | Unset = UNSET
    engagement_type: (
        FindingEngagementEngagementTypeType1
        | FindingEngagementEngagementTypeType2Type1
        | FindingEngagementEngagementTypeType3Type1
        | None
        | Unset
    ) = UNSET
    build_id: None | str | Unset = UNSET
    commit_hash: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        target_start = self.target_start.isoformat()

        target_end = self.target_end.isoformat()

        created: None | str
        if isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        updated: None | str
        if isinstance(self.updated, datetime.datetime):
            updated = self.updated.isoformat()
        else:
            updated = self.updated

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        product: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        branch_tag: None | str | Unset
        if isinstance(self.branch_tag, Unset):
            branch_tag = UNSET
        else:
            branch_tag = self.branch_tag

        engagement_type: None | str | Unset
        if isinstance(self.engagement_type, Unset):
            engagement_type = UNSET
        elif (
            isinstance(self.engagement_type, FindingEngagementEngagementTypeType1)
            or isinstance(self.engagement_type, FindingEngagementEngagementTypeType2Type1)
            or isinstance(self.engagement_type, FindingEngagementEngagementTypeType3Type1)
        ):
            engagement_type = self.engagement_type.value
        else:
            engagement_type = self.engagement_type

        build_id: None | str | Unset
        if isinstance(self.build_id, Unset):
            build_id = UNSET
        else:
            build_id = self.build_id

        commit_hash: None | str | Unset
        if isinstance(self.commit_hash, Unset):
            commit_hash = UNSET
        else:
            commit_hash = self.commit_hash

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "target_start": target_start,
                "target_end": target_end,
                "created": created,
                "updated": updated,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if product is not UNSET:
            field_dict["product"] = product
        if branch_tag is not UNSET:
            field_dict["branch_tag"] = branch_tag
        if engagement_type is not UNSET:
            field_dict["engagement_type"] = engagement_type
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if commit_hash is not UNSET:
            field_dict["commit_hash"] = commit_hash
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.finding_product import FindingProduct

        d = dict(src_dict)
        id = d.pop("id")

        target_start = isoparse(d.pop("target_start")).date()

        target_end = isoparse(d.pop("target_end")).date()

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

        def _parse_updated(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_type_0 = isoparse(data)

                return updated_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        updated = _parse_updated(d.pop("updated"))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _product = d.pop("product", UNSET)
        product: FindingProduct | Unset
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = FindingProduct.from_dict(_product)

        def _parse_branch_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_tag = _parse_branch_tag(d.pop("branch_tag", UNSET))

        def _parse_engagement_type(
            data: object,
        ) -> (
            FindingEngagementEngagementTypeType1
            | FindingEngagementEngagementTypeType2Type1
            | FindingEngagementEngagementTypeType3Type1
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
                engagement_type_type_1 = FindingEngagementEngagementTypeType1(data)

                return engagement_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                engagement_type_type_2_type_1 = FindingEngagementEngagementTypeType2Type1(data)

                return engagement_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                engagement_type_type_3_type_1 = FindingEngagementEngagementTypeType3Type1(data)

                return engagement_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                FindingEngagementEngagementTypeType1
                | FindingEngagementEngagementTypeType2Type1
                | FindingEngagementEngagementTypeType3Type1
                | None
                | Unset,
                data,
            )

        engagement_type = _parse_engagement_type(d.pop("engagement_type", UNSET))

        def _parse_build_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        build_id = _parse_build_id(d.pop("build_id", UNSET))

        def _parse_commit_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commit_hash = _parse_commit_hash(d.pop("commit_hash", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        finding_engagement = cls(
            id=id,
            target_start=target_start,
            target_end=target_end,
            created=created,
            updated=updated,
            name=name,
            description=description,
            product=product,
            branch_tag=branch_tag,
            engagement_type=engagement_type,
            build_id=build_id,
            commit_hash=commit_hash,
            version=version,
        )

        finding_engagement.additional_properties = d
        return finding_engagement

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
