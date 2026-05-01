from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.finding_engagement import FindingEngagement
    from ..models.finding_environment import FindingEnvironment
    from ..models.finding_test_type import FindingTestType


T = TypeVar("T", bound="FindingTest")


@_attrs_define
class FindingTest:
    """
    Attributes:
        id (int):
        title (None | str | Unset):
        test_type (FindingTestType | Unset):
        engagement (FindingEngagement | Unset):
        environment (FindingEnvironment | Unset):
        branch_tag (None | str | Unset): Tag or branch that was tested, a reimport may update this field.
        build_id (None | str | Unset): Build ID that was tested, a reimport may update this field.
        commit_hash (None | str | Unset): Commit hash tested, a reimport may update this field.
        version (None | str | Unset):
    """

    id: int
    title: None | str | Unset = UNSET
    test_type: FindingTestType | Unset = UNSET
    engagement: FindingEngagement | Unset = UNSET
    environment: FindingEnvironment | Unset = UNSET
    branch_tag: None | str | Unset = UNSET
    build_id: None | str | Unset = UNSET
    commit_hash: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        test_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.test_type, Unset):
            test_type = self.test_type.to_dict()

        engagement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.engagement, Unset):
            engagement = self.engagement.to_dict()

        environment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.to_dict()

        branch_tag: None | str | Unset
        if isinstance(self.branch_tag, Unset):
            branch_tag = UNSET
        else:
            branch_tag = self.branch_tag

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
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if test_type is not UNSET:
            field_dict["test_type"] = test_type
        if engagement is not UNSET:
            field_dict["engagement"] = engagement
        if environment is not UNSET:
            field_dict["environment"] = environment
        if branch_tag is not UNSET:
            field_dict["branch_tag"] = branch_tag
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if commit_hash is not UNSET:
            field_dict["commit_hash"] = commit_hash
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.finding_engagement import FindingEngagement
        from ..models.finding_environment import FindingEnvironment
        from ..models.finding_test_type import FindingTestType

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        _test_type = d.pop("test_type", UNSET)
        test_type: FindingTestType | Unset
        if isinstance(_test_type, Unset):
            test_type = UNSET
        else:
            test_type = FindingTestType.from_dict(_test_type)

        _engagement = d.pop("engagement", UNSET)
        engagement: FindingEngagement | Unset
        if isinstance(_engagement, Unset):
            engagement = UNSET
        else:
            engagement = FindingEngagement.from_dict(_engagement)

        _environment = d.pop("environment", UNSET)
        environment: FindingEnvironment | Unset
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = FindingEnvironment.from_dict(_environment)

        def _parse_branch_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_tag = _parse_branch_tag(d.pop("branch_tag", UNSET))

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

        finding_test = cls(
            id=id,
            title=title,
            test_type=test_type,
            engagement=engagement,
            environment=environment,
            branch_tag=branch_tag,
            build_id=build_id,
            commit_hash=commit_hash,
            version=version,
        )

        finding_test.additional_properties = d
        return finding_test

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
