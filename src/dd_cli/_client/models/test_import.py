from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_import_finding_action import TestImportFindingAction


T = TypeVar("T", bound="TestImport")


@_attrs_define
class TestImport:
    """
    Attributes:
        id (int):
        test_import_finding_action_set (list[TestImportFindingAction]):
        created (datetime.datetime):
        modified (datetime.datetime):
        test (int):
        findings_affected (list[int]):
        import_settings (Any | Unset):
        type_ (str | Unset):
        version (None | str | Unset):
        build_id (None | str | Unset): Build ID that was tested, a reimport may update this field.
        commit_hash (None | str | Unset): Commit hash tested, a reimport may update this field.
        branch_tag (None | str | Unset): Tag or branch that was tested, a reimport may update this field.
    """

    id: int
    test_import_finding_action_set: list[TestImportFindingAction]
    created: datetime.datetime
    modified: datetime.datetime
    test: int
    findings_affected: list[int]
    import_settings: Any | Unset = UNSET
    type_: str | Unset = UNSET
    version: None | str | Unset = UNSET
    build_id: None | str | Unset = UNSET
    commit_hash: None | str | Unset = UNSET
    branch_tag: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        test_import_finding_action_set = []
        for test_import_finding_action_set_item_data in self.test_import_finding_action_set:
            test_import_finding_action_set_item = test_import_finding_action_set_item_data.to_dict()
            test_import_finding_action_set.append(test_import_finding_action_set_item)

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        test = self.test

        findings_affected = self.findings_affected

        import_settings = self.import_settings

        type_ = self.type_

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

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

        branch_tag: None | str | Unset
        if isinstance(self.branch_tag, Unset):
            branch_tag = UNSET
        else:
            branch_tag = self.branch_tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "test_import_finding_action_set": test_import_finding_action_set,
                "created": created,
                "modified": modified,
                "test": test,
                "findings_affected": findings_affected,
            }
        )
        if import_settings is not UNSET:
            field_dict["import_settings"] = import_settings
        if type_ is not UNSET:
            field_dict["type"] = type_
        if version is not UNSET:
            field_dict["version"] = version
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if commit_hash is not UNSET:
            field_dict["commit_hash"] = commit_hash
        if branch_tag is not UNSET:
            field_dict["branch_tag"] = branch_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_import_finding_action import TestImportFindingAction

        d = dict(src_dict)
        id = d.pop("id")

        test_import_finding_action_set = []
        _test_import_finding_action_set = d.pop("test_import_finding_action_set")
        for test_import_finding_action_set_item_data in _test_import_finding_action_set:
            test_import_finding_action_set_item = TestImportFindingAction.from_dict(
                test_import_finding_action_set_item_data
            )

            test_import_finding_action_set.append(test_import_finding_action_set_item)

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        test = d.pop("test")

        findings_affected = cast(list[int], d.pop("findings_affected"))

        import_settings = d.pop("import_settings", UNSET)

        type_ = d.pop("type", UNSET)

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

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

        def _parse_branch_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_tag = _parse_branch_tag(d.pop("branch_tag", UNSET))

        test_import = cls(
            id=id,
            test_import_finding_action_set=test_import_finding_action_set,
            created=created,
            modified=modified,
            test=test,
            findings_affected=findings_affected,
            import_settings=import_settings,
            type_=type_,
            version=version,
            build_id=build_id,
            commit_hash=commit_hash,
            branch_tag=branch_tag,
        )

        test_import.additional_properties = d
        return test_import

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
