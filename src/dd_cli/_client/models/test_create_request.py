from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="TestCreateRequest")


@_attrs_define
class TestCreateRequest:
    """
    Attributes:
        engagement (int):
        target_start (datetime.datetime):
        target_end (datetime.datetime):
        test_type (int):
        notes (list[int | None] | Unset):
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

    engagement: int
    target_start: datetime.datetime
    target_end: datetime.datetime
    test_type: int
    notes: list[int | None] | Unset = UNSET
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
        engagement = self.engagement

        target_start = self.target_start.isoformat()

        target_end = self.target_end.isoformat()

        test_type = self.test_type

        notes: list[int | None] | Unset = UNSET
        if not isinstance(self.notes, Unset):
            notes = []
            for notes_item_data in self.notes:
                notes_item: int | None
                notes_item = notes_item_data
                notes.append(notes_item)

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
                "engagement": engagement,
                "target_start": target_start,
                "target_end": target_end,
                "test_type": test_type,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes
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

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("engagement", (None, str(self.engagement).encode(), "text/plain")))

        files.append(("target_start", (None, self.target_start.isoformat().encode(), "text/plain")))

        files.append(("target_end", (None, self.target_end.isoformat().encode(), "text/plain")))

        files.append(("test_type", (None, str(self.test_type).encode(), "text/plain")))

        if not isinstance(self.notes, Unset):
            for notes_item_element in self.notes:
                if isinstance(notes_item_element, int):
                    files.append(("notes", (None, str(notes_item_element).encode(), "text/plain")))
                else:
                    files.append(("notes", (None, str(notes_item_element).encode(), "text/plain")))

        if not isinstance(self.tags, Unset):
            for tags_item_element in self.tags:
                files.append(("tags", (None, str(tags_item_element).encode(), "text/plain")))

        if not isinstance(self.scan_type, Unset):
            if isinstance(self.scan_type, str):
                files.append(("scan_type", (None, str(self.scan_type).encode(), "text/plain")))
            else:
                files.append(("scan_type", (None, str(self.scan_type).encode(), "text/plain")))

        if not isinstance(self.title, Unset):
            if isinstance(self.title, str):
                files.append(("title", (None, str(self.title).encode(), "text/plain")))
            else:
                files.append(("title", (None, str(self.title).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            if isinstance(self.description, str):
                files.append(("description", (None, str(self.description).encode(), "text/plain")))
            else:
                files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.percent_complete, Unset):
            if isinstance(self.percent_complete, int):
                files.append(
                    ("percent_complete", (None, str(self.percent_complete).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("percent_complete", (None, str(self.percent_complete).encode(), "text/plain"))
                )

        if not isinstance(self.version, Unset):
            if isinstance(self.version, str):
                files.append(("version", (None, str(self.version).encode(), "text/plain")))
            else:
                files.append(("version", (None, str(self.version).encode(), "text/plain")))

        if not isinstance(self.build_id, Unset):
            if isinstance(self.build_id, str):
                files.append(("build_id", (None, str(self.build_id).encode(), "text/plain")))
            else:
                files.append(("build_id", (None, str(self.build_id).encode(), "text/plain")))

        if not isinstance(self.commit_hash, Unset):
            if isinstance(self.commit_hash, str):
                files.append(("commit_hash", (None, str(self.commit_hash).encode(), "text/plain")))
            else:
                files.append(("commit_hash", (None, str(self.commit_hash).encode(), "text/plain")))

        if not isinstance(self.branch_tag, Unset):
            if isinstance(self.branch_tag, str):
                files.append(("branch_tag", (None, str(self.branch_tag).encode(), "text/plain")))
            else:
                files.append(("branch_tag", (None, str(self.branch_tag).encode(), "text/plain")))

        if not isinstance(self.lead, Unset):
            if isinstance(self.lead, int):
                files.append(("lead", (None, str(self.lead).encode(), "text/plain")))
            else:
                files.append(("lead", (None, str(self.lead).encode(), "text/plain")))

        if not isinstance(self.environment, Unset):
            if isinstance(self.environment, int):
                files.append(("environment", (None, str(self.environment).encode(), "text/plain")))
            else:
                files.append(("environment", (None, str(self.environment).encode(), "text/plain")))

        if not isinstance(self.api_scan_configuration, Unset):
            if isinstance(self.api_scan_configuration, int):
                files.append(
                    (
                        "api_scan_configuration",
                        (None, str(self.api_scan_configuration).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "api_scan_configuration",
                        (None, str(self.api_scan_configuration).encode(), "text/plain"),
                    )
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        engagement = d.pop("engagement")

        target_start = isoparse(d.pop("target_start"))

        target_end = isoparse(d.pop("target_end"))

        test_type = d.pop("test_type")

        _notes = d.pop("notes", UNSET)
        notes: list[int | None] | Unset = UNSET
        if _notes is not UNSET:
            notes = []
            for notes_item_data in _notes:

                def _parse_notes_item(data: object) -> int | None:
                    if data is None:
                        return data
                    return cast(int | None, data)

                notes_item = _parse_notes_item(notes_item_data)

                notes.append(notes_item)

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

        test_create_request = cls(
            engagement=engagement,
            target_start=target_start,
            target_end=target_end,
            test_type=test_type,
            notes=notes,
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

        test_create_request.additional_properties = d
        return test_create_request

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
