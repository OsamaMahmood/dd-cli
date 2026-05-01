from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.engagement_engagement_type_type_1 import EngagementEngagementTypeType1
from ..models.engagement_engagement_type_type_2_type_1 import EngagementEngagementTypeType2Type1
from ..models.engagement_engagement_type_type_3_type_1 import EngagementEngagementTypeType3Type1
from ..models.engagement_status_type_1 import EngagementStatusType1
from ..models.engagement_status_type_2_type_1 import EngagementStatusType2Type1
from ..models.engagement_status_type_3_type_1 import EngagementStatusType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file import File
    from ..models.note import Note


T = TypeVar("T", bound="Engagement")


@_attrs_define
class Engagement:
    """
    Attributes:
        id (int):
        target_start (datetime.date):
        target_end (datetime.date):
        updated (datetime.datetime | None):
        created (datetime.datetime | None):
        active (bool):
        progress (str):
        tmodel_path (None | str):
        done_testing (bool):
        product (int):
        notes (list[Note]):
        files (list[File]):
        risk_acceptance (list[int]):
        tags (list[str] | Unset):
        name (None | str | Unset):
        description (None | str | Unset):
        version (None | str | Unset): Version of the product the engagement tested.
        first_contacted (datetime.date | None | Unset):
        reason (None | str | Unset):
        tracker (None | str | Unset): Link to epic or ticket system with changes to version.
        test_strategy (None | str | Unset):
        threat_model (bool | Unset):
        api_test (bool | Unset):
        pen_test (bool | Unset):
        check_list (bool | Unset):
        status (EngagementStatusType1 | EngagementStatusType2Type1 | EngagementStatusType3Type1 | None | Unset): * `Not
            Started` - Not Started
            * `Blocked` - Blocked
            * `Cancelled` - Cancelled
            * `Completed` - Completed
            * `In Progress` - In Progress
            * `On Hold` - On Hold
            * `Waiting for Resource` - Waiting for Resource
        engagement_type (EngagementEngagementTypeType1 | EngagementEngagementTypeType2Type1 |
            EngagementEngagementTypeType3Type1 | None | Unset): * `Interactive` - Interactive
            * `CI/CD` - CI/CD
        build_id (None | str | Unset): Build ID of the product the engagement tested.
        commit_hash (None | str | Unset): Commit hash from repo
        branch_tag (None | str | Unset): Tag or branch of the product the engagement tested.
        source_code_management_uri (None | str | Unset): Resource link to source code
        deduplication_on_engagement (bool | Unset): If enabled deduplication will only mark a finding in this engagement
            as duplicate of another finding if both findings are in this engagement. If disabled, deduplication is on the
            product level.
        lead (int | None | Unset):
        requester (int | None | Unset):
        preset (int | None | Unset): Settings and notes for performing this engagement.
        report_type (int | None | Unset):
        build_server (int | None | Unset): Build server responsible for CI/CD test
        source_code_management_server (int | None | Unset): Source code server for CI/CD test
        orchestration_engine (int | None | Unset): Orchestration service responsible for CI/CD test
    """

    id: int
    target_start: datetime.date
    target_end: datetime.date
    updated: datetime.datetime | None
    created: datetime.datetime | None
    active: bool
    progress: str
    tmodel_path: None | str
    done_testing: bool
    product: int
    notes: list[Note]
    files: list[File]
    risk_acceptance: list[int]
    tags: list[str] | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    first_contacted: datetime.date | None | Unset = UNSET
    reason: None | str | Unset = UNSET
    tracker: None | str | Unset = UNSET
    test_strategy: None | str | Unset = UNSET
    threat_model: bool | Unset = UNSET
    api_test: bool | Unset = UNSET
    pen_test: bool | Unset = UNSET
    check_list: bool | Unset = UNSET
    status: (
        EngagementStatusType1
        | EngagementStatusType2Type1
        | EngagementStatusType3Type1
        | None
        | Unset
    ) = UNSET
    engagement_type: (
        EngagementEngagementTypeType1
        | EngagementEngagementTypeType2Type1
        | EngagementEngagementTypeType3Type1
        | None
        | Unset
    ) = UNSET
    build_id: None | str | Unset = UNSET
    commit_hash: None | str | Unset = UNSET
    branch_tag: None | str | Unset = UNSET
    source_code_management_uri: None | str | Unset = UNSET
    deduplication_on_engagement: bool | Unset = UNSET
    lead: int | None | Unset = UNSET
    requester: int | None | Unset = UNSET
    preset: int | None | Unset = UNSET
    report_type: int | None | Unset = UNSET
    build_server: int | None | Unset = UNSET
    source_code_management_server: int | None | Unset = UNSET
    orchestration_engine: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

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

        active = self.active

        progress = self.progress

        tmodel_path: None | str
        tmodel_path = self.tmodel_path

        done_testing = self.done_testing

        product = self.product

        notes = []
        for notes_item_data in self.notes:
            notes_item = notes_item_data.to_dict()
            notes.append(notes_item)

        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        risk_acceptance = self.risk_acceptance

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

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

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        first_contacted: None | str | Unset
        if isinstance(self.first_contacted, Unset):
            first_contacted = UNSET
        elif isinstance(self.first_contacted, datetime.date):
            first_contacted = self.first_contacted.isoformat()
        else:
            first_contacted = self.first_contacted

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        tracker: None | str | Unset
        if isinstance(self.tracker, Unset):
            tracker = UNSET
        else:
            tracker = self.tracker

        test_strategy: None | str | Unset
        if isinstance(self.test_strategy, Unset):
            test_strategy = UNSET
        else:
            test_strategy = self.test_strategy

        threat_model = self.threat_model

        api_test = self.api_test

        pen_test = self.pen_test

        check_list = self.check_list

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif (
            isinstance(self.status, EngagementStatusType1)
            or isinstance(self.status, EngagementStatusType2Type1)
            or isinstance(self.status, EngagementStatusType3Type1)
        ):
            status = self.status.value
        else:
            status = self.status

        engagement_type: None | str | Unset
        if isinstance(self.engagement_type, Unset):
            engagement_type = UNSET
        elif (
            isinstance(self.engagement_type, EngagementEngagementTypeType1)
            or isinstance(self.engagement_type, EngagementEngagementTypeType2Type1)
            or isinstance(self.engagement_type, EngagementEngagementTypeType3Type1)
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

        branch_tag: None | str | Unset
        if isinstance(self.branch_tag, Unset):
            branch_tag = UNSET
        else:
            branch_tag = self.branch_tag

        source_code_management_uri: None | str | Unset
        if isinstance(self.source_code_management_uri, Unset):
            source_code_management_uri = UNSET
        else:
            source_code_management_uri = self.source_code_management_uri

        deduplication_on_engagement = self.deduplication_on_engagement

        lead: int | None | Unset
        if isinstance(self.lead, Unset):
            lead = UNSET
        else:
            lead = self.lead

        requester: int | None | Unset
        if isinstance(self.requester, Unset):
            requester = UNSET
        else:
            requester = self.requester

        preset: int | None | Unset
        if isinstance(self.preset, Unset):
            preset = UNSET
        else:
            preset = self.preset

        report_type: int | None | Unset
        if isinstance(self.report_type, Unset):
            report_type = UNSET
        else:
            report_type = self.report_type

        build_server: int | None | Unset
        if isinstance(self.build_server, Unset):
            build_server = UNSET
        else:
            build_server = self.build_server

        source_code_management_server: int | None | Unset
        if isinstance(self.source_code_management_server, Unset):
            source_code_management_server = UNSET
        else:
            source_code_management_server = self.source_code_management_server

        orchestration_engine: int | None | Unset
        if isinstance(self.orchestration_engine, Unset):
            orchestration_engine = UNSET
        else:
            orchestration_engine = self.orchestration_engine

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "target_start": target_start,
                "target_end": target_end,
                "updated": updated,
                "created": created,
                "active": active,
                "progress": progress,
                "tmodel_path": tmodel_path,
                "done_testing": done_testing,
                "product": product,
                "notes": notes,
                "files": files,
                "risk_acceptance": risk_acceptance,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if version is not UNSET:
            field_dict["version"] = version
        if first_contacted is not UNSET:
            field_dict["first_contacted"] = first_contacted
        if reason is not UNSET:
            field_dict["reason"] = reason
        if tracker is not UNSET:
            field_dict["tracker"] = tracker
        if test_strategy is not UNSET:
            field_dict["test_strategy"] = test_strategy
        if threat_model is not UNSET:
            field_dict["threat_model"] = threat_model
        if api_test is not UNSET:
            field_dict["api_test"] = api_test
        if pen_test is not UNSET:
            field_dict["pen_test"] = pen_test
        if check_list is not UNSET:
            field_dict["check_list"] = check_list
        if status is not UNSET:
            field_dict["status"] = status
        if engagement_type is not UNSET:
            field_dict["engagement_type"] = engagement_type
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if commit_hash is not UNSET:
            field_dict["commit_hash"] = commit_hash
        if branch_tag is not UNSET:
            field_dict["branch_tag"] = branch_tag
        if source_code_management_uri is not UNSET:
            field_dict["source_code_management_uri"] = source_code_management_uri
        if deduplication_on_engagement is not UNSET:
            field_dict["deduplication_on_engagement"] = deduplication_on_engagement
        if lead is not UNSET:
            field_dict["lead"] = lead
        if requester is not UNSET:
            field_dict["requester"] = requester
        if preset is not UNSET:
            field_dict["preset"] = preset
        if report_type is not UNSET:
            field_dict["report_type"] = report_type
        if build_server is not UNSET:
            field_dict["build_server"] = build_server
        if source_code_management_server is not UNSET:
            field_dict["source_code_management_server"] = source_code_management_server
        if orchestration_engine is not UNSET:
            field_dict["orchestration_engine"] = orchestration_engine

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file import File
        from ..models.note import Note

        d = dict(src_dict)
        id = d.pop("id")

        target_start = isoparse(d.pop("target_start")).date()

        target_end = isoparse(d.pop("target_end")).date()

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

        active = d.pop("active")

        progress = d.pop("progress")

        def _parse_tmodel_path(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tmodel_path = _parse_tmodel_path(d.pop("tmodel_path"))

        done_testing = d.pop("done_testing")

        product = d.pop("product")

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

        risk_acceptance = cast(list[int], d.pop("risk_acceptance"))

        tags = cast(list[str], d.pop("tags", UNSET))

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

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_first_contacted(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_contacted_type_0 = isoparse(data).date()

                return first_contacted_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        first_contacted = _parse_first_contacted(d.pop("first_contacted", UNSET))

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_tracker(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tracker = _parse_tracker(d.pop("tracker", UNSET))

        def _parse_test_strategy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        test_strategy = _parse_test_strategy(d.pop("test_strategy", UNSET))

        threat_model = d.pop("threat_model", UNSET)

        api_test = d.pop("api_test", UNSET)

        pen_test = d.pop("pen_test", UNSET)

        check_list = d.pop("check_list", UNSET)

        def _parse_status(
            data: object,
        ) -> (
            EngagementStatusType1
            | EngagementStatusType2Type1
            | EngagementStatusType3Type1
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
                status_type_1 = EngagementStatusType1(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_2_type_1 = EngagementStatusType2Type1(data)

                return status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_3_type_1 = EngagementStatusType3Type1(data)

                return status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                EngagementStatusType1
                | EngagementStatusType2Type1
                | EngagementStatusType3Type1
                | None
                | Unset,
                data,
            )

        status = _parse_status(d.pop("status", UNSET))

        def _parse_engagement_type(
            data: object,
        ) -> (
            EngagementEngagementTypeType1
            | EngagementEngagementTypeType2Type1
            | EngagementEngagementTypeType3Type1
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
                engagement_type_type_1 = EngagementEngagementTypeType1(data)

                return engagement_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                engagement_type_type_2_type_1 = EngagementEngagementTypeType2Type1(data)

                return engagement_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                engagement_type_type_3_type_1 = EngagementEngagementTypeType3Type1(data)

                return engagement_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                EngagementEngagementTypeType1
                | EngagementEngagementTypeType2Type1
                | EngagementEngagementTypeType3Type1
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

        def _parse_branch_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_tag = _parse_branch_tag(d.pop("branch_tag", UNSET))

        def _parse_source_code_management_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_code_management_uri = _parse_source_code_management_uri(
            d.pop("source_code_management_uri", UNSET)
        )

        deduplication_on_engagement = d.pop("deduplication_on_engagement", UNSET)

        def _parse_lead(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lead = _parse_lead(d.pop("lead", UNSET))

        def _parse_requester(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        requester = _parse_requester(d.pop("requester", UNSET))

        def _parse_preset(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        preset = _parse_preset(d.pop("preset", UNSET))

        def _parse_report_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        report_type = _parse_report_type(d.pop("report_type", UNSET))

        def _parse_build_server(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        build_server = _parse_build_server(d.pop("build_server", UNSET))

        def _parse_source_code_management_server(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        source_code_management_server = _parse_source_code_management_server(
            d.pop("source_code_management_server", UNSET)
        )

        def _parse_orchestration_engine(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        orchestration_engine = _parse_orchestration_engine(d.pop("orchestration_engine", UNSET))

        engagement = cls(
            id=id,
            target_start=target_start,
            target_end=target_end,
            updated=updated,
            created=created,
            active=active,
            progress=progress,
            tmodel_path=tmodel_path,
            done_testing=done_testing,
            product=product,
            notes=notes,
            files=files,
            risk_acceptance=risk_acceptance,
            tags=tags,
            name=name,
            description=description,
            version=version,
            first_contacted=first_contacted,
            reason=reason,
            tracker=tracker,
            test_strategy=test_strategy,
            threat_model=threat_model,
            api_test=api_test,
            pen_test=pen_test,
            check_list=check_list,
            status=status,
            engagement_type=engagement_type,
            build_id=build_id,
            commit_hash=commit_hash,
            branch_tag=branch_tag,
            source_code_management_uri=source_code_management_uri,
            deduplication_on_engagement=deduplication_on_engagement,
            lead=lead,
            requester=requester,
            preset=preset,
            report_type=report_type,
            build_server=build_server,
            source_code_management_server=source_code_management_server,
            orchestration_engine=orchestration_engine,
        )

        engagement.additional_properties = d
        return engagement

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
