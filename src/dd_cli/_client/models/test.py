from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file import File
    from ..models.finding_group import FindingGroup
    from ..models.note import Note


T = TypeVar("T", bound="Test")


@_attrs_define
class Test:
    """
    Attributes:
        id (int):
        test_type_name (str):
        finding_groups (list[FindingGroup]):
        target_start (datetime.datetime):
        target_end (datetime.datetime):
        updated (datetime.datetime | None):
        created (datetime.datetime | None):
        engagement (int):
        test_type (int):
        notes (list[Note]):
        files (list[File]):
        tags (list[str] | Unset):
        scan_type (None | str | Unset):
        title (None | str | Unset):
        description (None | str | Unset):
        percent_complete (int | None | Unset):
        version (None | str | Unset):
        build_id (None | str | Unset): Build ID that was tested, a reimport may update this field.
        commit_hash (None | str | Unset): Commit hash tested, a reimport may update this field.
        branch_tag (None | str | Unset): Tag or branch that was tested, a reimport may update this field.
        lead (int | None | Unset):
        environment (int | None | Unset):
        api_scan_configuration (int | None | Unset):
    """

    id: int
    test_type_name: str
    finding_groups: list[FindingGroup]
    target_start: datetime.datetime
    target_end: datetime.datetime
    updated: datetime.datetime | None
    created: datetime.datetime | None
    engagement: int
    test_type: int
    notes: list[Note]
    files: list[File]
    tags: list[str] | Unset = UNSET
    scan_type: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    percent_complete: int | None | Unset = UNSET
    version: None | str | Unset = UNSET
    build_id: None | str | Unset = UNSET
    commit_hash: None | str | Unset = UNSET
    branch_tag: None | str | Unset = UNSET
    lead: int | None | Unset = UNSET
    environment: int | None | Unset = UNSET
    api_scan_configuration: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        test_type_name = self.test_type_name

        finding_groups = []
        for finding_groups_item_data in self.finding_groups:
            finding_groups_item = finding_groups_item_data.to_dict()
            finding_groups.append(finding_groups_item)

        target_start = self.target_start.isoformat()

        target_end = self.target_end.isoformat()

        updated: None | str
        if isinstance(self.updated, datetime.datetime):
            updated = self.updated.isoformat()
        else:
            updated = self.updated

        created: None | str
        if isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        engagement = self.engagement

        test_type = self.test_type

        notes = []
        for notes_item_data in self.notes:
            notes_item = notes_item_data.to_dict()
            notes.append(notes_item)

        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        scan_type: None | str | Unset
        if isinstance(self.scan_type, Unset):
            scan_type = UNSET
        else:
            scan_type = self.scan_type

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        percent_complete: int | None | Unset
        if isinstance(self.percent_complete, Unset):
            percent_complete = UNSET
        else:
            percent_complete = self.percent_complete

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

        lead: int | None | Unset
        if isinstance(self.lead, Unset):
            lead = UNSET
        else:
            lead = self.lead

        environment: int | None | Unset
        if isinstance(self.environment, Unset):
            environment = UNSET
        else:
            environment = self.environment

        api_scan_configuration: int | None | Unset
        if isinstance(self.api_scan_configuration, Unset):
            api_scan_configuration = UNSET
        else:
            api_scan_configuration = self.api_scan_configuration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "test_type_name": test_type_name,
                "finding_groups": finding_groups,
                "target_start": target_start,
                "target_end": target_end,
                "updated": updated,
                "created": created,
                "engagement": engagement,
                "test_type": test_type,
                "notes": notes,
                "files": files,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if scan_type is not UNSET:
            field_dict["scan_type"] = scan_type
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if percent_complete is not UNSET:
            field_dict["percent_complete"] = percent_complete
        if version is not UNSET:
            field_dict["version"] = version
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if commit_hash is not UNSET:
            field_dict["commit_hash"] = commit_hash
        if branch_tag is not UNSET:
            field_dict["branch_tag"] = branch_tag
        if lead is not UNSET:
            field_dict["lead"] = lead
        if environment is not UNSET:
            field_dict["environment"] = environment
        if api_scan_configuration is not UNSET:
            field_dict["api_scan_configuration"] = api_scan_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file import File
        from ..models.finding_group import FindingGroup
        from ..models.note import Note

        d = dict(src_dict)
        id = d.pop("id")

        test_type_name = d.pop("test_type_name")

        finding_groups = []
        _finding_groups = d.pop("finding_groups")
        for finding_groups_item_data in _finding_groups:
            finding_groups_item = FindingGroup.from_dict(finding_groups_item_data)

            finding_groups.append(finding_groups_item)

        target_start = isoparse(d.pop("target_start"))

        target_end = isoparse(d.pop("target_end"))

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

        engagement = d.pop("engagement")

        test_type = d.pop("test_type")

        notes = []
        _notes = d.pop("notes")
        for notes_item_data in _notes:
            notes_item = Note.from_dict(notes_item_data)

            notes.append(notes_item)

        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = File.from_dict(files_item_data)

            files.append(files_item)

        tags = cast(list[str], d.pop("tags", UNSET))

        def _parse_scan_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scan_type = _parse_scan_type(d.pop("scan_type", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_percent_complete(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        percent_complete = _parse_percent_complete(d.pop("percent_complete", UNSET))

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

        def _parse_lead(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lead = _parse_lead(d.pop("lead", UNSET))

        def _parse_environment(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        environment = _parse_environment(d.pop("environment", UNSET))

        def _parse_api_scan_configuration(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        api_scan_configuration = _parse_api_scan_configuration(
            d.pop("api_scan_configuration", UNSET)
        )

        test = cls(
            id=id,
            test_type_name=test_type_name,
            finding_groups=finding_groups,
            target_start=target_start,
            target_end=target_end,
            updated=updated,
            created=created,
            engagement=engagement,
            test_type=test_type,
            notes=notes,
            files=files,
            tags=tags,
            scan_type=scan_type,
            title=title,
            description=description,
            percent_complete=percent_complete,
            version=version,
            build_id=build_id,
            commit_hash=commit_hash,
            branch_tag=branch_tag,
            lead=lead,
            environment=environment,
            api_scan_configuration=api_scan_configuration,
        )

        test.additional_properties = d
        return test

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
