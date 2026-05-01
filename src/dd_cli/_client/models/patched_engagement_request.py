from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from .. import types
from ..models.patched_engagement_request_engagement_type_type_1 import (
    PatchedEngagementRequestEngagementTypeType1,
)
from ..models.patched_engagement_request_engagement_type_type_2_type_1 import (
    PatchedEngagementRequestEngagementTypeType2Type1,
)
from ..models.patched_engagement_request_engagement_type_type_3_type_1 import (
    PatchedEngagementRequestEngagementTypeType3Type1,
)
from ..models.patched_engagement_request_status_type_1 import PatchedEngagementRequestStatusType1
from ..models.patched_engagement_request_status_type_2_type_1 import (
    PatchedEngagementRequestStatusType2Type1,
)
from ..models.patched_engagement_request_status_type_3_type_1 import (
    PatchedEngagementRequestStatusType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedEngagementRequest")


@_attrs_define
class PatchedEngagementRequest:
    """
    Attributes:
        tags (list[str] | Unset):
        name (None | str | Unset):
        description (None | str | Unset):
        version (None | str | Unset): Version of the product the engagement tested.
        first_contacted (datetime.date | None | Unset):
        target_start (datetime.date | Unset):
        target_end (datetime.date | Unset):
        reason (None | str | Unset):
        tracker (None | str | Unset): Link to epic or ticket system with changes to version.
        test_strategy (None | str | Unset):
        threat_model (bool | Unset):
        api_test (bool | Unset):
        pen_test (bool | Unset):
        check_list (bool | Unset):
        status (None | PatchedEngagementRequestStatusType1 | PatchedEngagementRequestStatusType2Type1 |
            PatchedEngagementRequestStatusType3Type1 | Unset): * `Not Started` - Not Started
            * `Blocked` - Blocked
            * `Cancelled` - Cancelled
            * `Completed` - Completed
            * `In Progress` - In Progress
            * `On Hold` - On Hold
            * `Waiting for Resource` - Waiting for Resource
        engagement_type (None | PatchedEngagementRequestEngagementTypeType1 |
            PatchedEngagementRequestEngagementTypeType2Type1 | PatchedEngagementRequestEngagementTypeType3Type1 | Unset): *
            `Interactive` - Interactive
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
        product (int | Unset):
        build_server (int | None | Unset): Build server responsible for CI/CD test
        source_code_management_server (int | None | Unset): Source code server for CI/CD test
        orchestration_engine (int | None | Unset): Orchestration service responsible for CI/CD test
    """

    tags: list[str] | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    first_contacted: datetime.date | None | Unset = UNSET
    target_start: datetime.date | Unset = UNSET
    target_end: datetime.date | Unset = UNSET
    reason: None | str | Unset = UNSET
    tracker: None | str | Unset = UNSET
    test_strategy: None | str | Unset = UNSET
    threat_model: bool | Unset = UNSET
    api_test: bool | Unset = UNSET
    pen_test: bool | Unset = UNSET
    check_list: bool | Unset = UNSET
    status: (
        None
        | PatchedEngagementRequestStatusType1
        | PatchedEngagementRequestStatusType2Type1
        | PatchedEngagementRequestStatusType3Type1
        | Unset
    ) = UNSET
    engagement_type: (
        None
        | PatchedEngagementRequestEngagementTypeType1
        | PatchedEngagementRequestEngagementTypeType2Type1
        | PatchedEngagementRequestEngagementTypeType3Type1
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
    product: int | Unset = UNSET
    build_server: int | None | Unset = UNSET
    source_code_management_server: int | None | Unset = UNSET
    orchestration_engine: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        target_start: str | Unset = UNSET
        if not isinstance(self.target_start, Unset):
            target_start = self.target_start.isoformat()

        target_end: str | Unset = UNSET
        if not isinstance(self.target_end, Unset):
            target_end = self.target_end.isoformat()

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
            isinstance(self.status, PatchedEngagementRequestStatusType1)
            or isinstance(self.status, PatchedEngagementRequestStatusType2Type1)
            or isinstance(self.status, PatchedEngagementRequestStatusType3Type1)
        ):
            status = self.status.value
        else:
            status = self.status

        engagement_type: None | str | Unset
        if isinstance(self.engagement_type, Unset):
            engagement_type = UNSET
        elif (
            isinstance(self.engagement_type, PatchedEngagementRequestEngagementTypeType1)
            or isinstance(self.engagement_type, PatchedEngagementRequestEngagementTypeType2Type1)
            or isinstance(self.engagement_type, PatchedEngagementRequestEngagementTypeType3Type1)
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

        product = self.product

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
        field_dict.update({})
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
        if target_start is not UNSET:
            field_dict["target_start"] = target_start
        if target_end is not UNSET:
            field_dict["target_end"] = target_end
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
        if product is not UNSET:
            field_dict["product"] = product
        if build_server is not UNSET:
            field_dict["build_server"] = build_server
        if source_code_management_server is not UNSET:
            field_dict["source_code_management_server"] = source_code_management_server
        if orchestration_engine is not UNSET:
            field_dict["orchestration_engine"] = orchestration_engine

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.tags, Unset):
            for tags_item_element in self.tags:
                files.append(("tags", (None, str(tags_item_element).encode(), "text/plain")))

        if not isinstance(self.name, Unset):
            if isinstance(self.name, str):
                files.append(("name", (None, str(self.name).encode(), "text/plain")))
            else:
                files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            if isinstance(self.description, str):
                files.append(("description", (None, str(self.description).encode(), "text/plain")))
            else:
                files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.version, Unset):
            if isinstance(self.version, str):
                files.append(("version", (None, str(self.version).encode(), "text/plain")))
            else:
                files.append(("version", (None, str(self.version).encode(), "text/plain")))

        if not isinstance(self.first_contacted, Unset):
            if isinstance(self.first_contacted, datetime.date):
                files.append(
                    (
                        "first_contacted",
                        (None, self.first_contacted.isoformat().encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    ("first_contacted", (None, str(self.first_contacted).encode(), "text/plain"))
                )

        if not isinstance(self.target_start, Unset):
            files.append(
                ("target_start", (None, self.target_start.isoformat().encode(), "text/plain"))
            )

        if not isinstance(self.target_end, Unset):
            files.append(("target_end", (None, self.target_end.isoformat().encode(), "text/plain")))

        if not isinstance(self.reason, Unset):
            if isinstance(self.reason, str):
                files.append(("reason", (None, str(self.reason).encode(), "text/plain")))
            else:
                files.append(("reason", (None, str(self.reason).encode(), "text/plain")))

        if not isinstance(self.tracker, Unset):
            if isinstance(self.tracker, str):
                files.append(("tracker", (None, str(self.tracker).encode(), "text/plain")))
            else:
                files.append(("tracker", (None, str(self.tracker).encode(), "text/plain")))

        if not isinstance(self.test_strategy, Unset):
            if isinstance(self.test_strategy, str):
                files.append(
                    ("test_strategy", (None, str(self.test_strategy).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("test_strategy", (None, str(self.test_strategy).encode(), "text/plain"))
                )

        if not isinstance(self.threat_model, Unset):
            files.append(("threat_model", (None, str(self.threat_model).encode(), "text/plain")))

        if not isinstance(self.api_test, Unset):
            files.append(("api_test", (None, str(self.api_test).encode(), "text/plain")))

        if not isinstance(self.pen_test, Unset):
            files.append(("pen_test", (None, str(self.pen_test).encode(), "text/plain")))

        if not isinstance(self.check_list, Unset):
            files.append(("check_list", (None, str(self.check_list).encode(), "text/plain")))

        if not isinstance(self.status, Unset):
            if self.status is None:
                files.append(("status", (None, str(self.status).encode(), "text/plain")))
            elif isinstance(self.status, PatchedEngagementRequestStatusType1) or isinstance(
                self.status, PatchedEngagementRequestStatusType2Type1
            ):
                files.append(("status", (None, str(self.status.value).encode(), "text/plain")))
            else:
                files.append(("status", (None, str(self.status.value).encode(), "text/plain")))

        if not isinstance(self.engagement_type, Unset):
            if self.engagement_type is None:
                files.append(
                    ("engagement_type", (None, str(self.engagement_type).encode(), "text/plain"))
                )
            elif isinstance(
                self.engagement_type, PatchedEngagementRequestEngagementTypeType1
            ) or isinstance(self.engagement_type, PatchedEngagementRequestEngagementTypeType2Type1):
                files.append(
                    (
                        "engagement_type",
                        (None, str(self.engagement_type.value).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "engagement_type",
                        (None, str(self.engagement_type.value).encode(), "text/plain"),
                    )
                )

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

        if not isinstance(self.source_code_management_uri, Unset):
            if isinstance(self.source_code_management_uri, str):
                files.append(
                    (
                        "source_code_management_uri",
                        (None, str(self.source_code_management_uri).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "source_code_management_uri",
                        (None, str(self.source_code_management_uri).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.deduplication_on_engagement, Unset):
            files.append(
                (
                    "deduplication_on_engagement",
                    (None, str(self.deduplication_on_engagement).encode(), "text/plain"),
                )
            )

        if not isinstance(self.lead, Unset):
            if isinstance(self.lead, int):
                files.append(("lead", (None, str(self.lead).encode(), "text/plain")))
            else:
                files.append(("lead", (None, str(self.lead).encode(), "text/plain")))

        if not isinstance(self.requester, Unset):
            if isinstance(self.requester, int):
                files.append(("requester", (None, str(self.requester).encode(), "text/plain")))
            else:
                files.append(("requester", (None, str(self.requester).encode(), "text/plain")))

        if not isinstance(self.preset, Unset):
            if isinstance(self.preset, int):
                files.append(("preset", (None, str(self.preset).encode(), "text/plain")))
            else:
                files.append(("preset", (None, str(self.preset).encode(), "text/plain")))

        if not isinstance(self.report_type, Unset):
            if isinstance(self.report_type, int):
                files.append(("report_type", (None, str(self.report_type).encode(), "text/plain")))
            else:
                files.append(("report_type", (None, str(self.report_type).encode(), "text/plain")))

        if not isinstance(self.product, Unset):
            files.append(("product", (None, str(self.product).encode(), "text/plain")))

        if not isinstance(self.build_server, Unset):
            if isinstance(self.build_server, int):
                files.append(
                    ("build_server", (None, str(self.build_server).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("build_server", (None, str(self.build_server).encode(), "text/plain"))
                )

        if not isinstance(self.source_code_management_server, Unset):
            if isinstance(self.source_code_management_server, int):
                files.append(
                    (
                        "source_code_management_server",
                        (None, str(self.source_code_management_server).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "source_code_management_server",
                        (None, str(self.source_code_management_server).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.orchestration_engine, Unset):
            if isinstance(self.orchestration_engine, int):
                files.append(
                    (
                        "orchestration_engine",
                        (None, str(self.orchestration_engine).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "orchestration_engine",
                        (None, str(self.orchestration_engine).encode(), "text/plain"),
                    )
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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

        _target_start = d.pop("target_start", UNSET)
        target_start: datetime.date | Unset
        if isinstance(_target_start, Unset):
            target_start = UNSET
        else:
            target_start = isoparse(_target_start).date()

        _target_end = d.pop("target_end", UNSET)
        target_end: datetime.date | Unset
        if isinstance(_target_end, Unset):
            target_end = UNSET
        else:
            target_end = isoparse(_target_end).date()

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
            None
            | PatchedEngagementRequestStatusType1
            | PatchedEngagementRequestStatusType2Type1
            | PatchedEngagementRequestStatusType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = PatchedEngagementRequestStatusType1(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_2_type_1 = PatchedEngagementRequestStatusType2Type1(data)

                return status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_3_type_1 = PatchedEngagementRequestStatusType3Type1(data)

                return status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PatchedEngagementRequestStatusType1
                | PatchedEngagementRequestStatusType2Type1
                | PatchedEngagementRequestStatusType3Type1
                | Unset,
                data,
            )

        status = _parse_status(d.pop("status", UNSET))

        def _parse_engagement_type(
            data: object,
        ) -> (
            None
            | PatchedEngagementRequestEngagementTypeType1
            | PatchedEngagementRequestEngagementTypeType2Type1
            | PatchedEngagementRequestEngagementTypeType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                engagement_type_type_1 = PatchedEngagementRequestEngagementTypeType1(data)

                return engagement_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                engagement_type_type_2_type_1 = PatchedEngagementRequestEngagementTypeType2Type1(
                    data
                )

                return engagement_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                engagement_type_type_3_type_1 = PatchedEngagementRequestEngagementTypeType3Type1(
                    data
                )

                return engagement_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PatchedEngagementRequestEngagementTypeType1
                | PatchedEngagementRequestEngagementTypeType2Type1
                | PatchedEngagementRequestEngagementTypeType3Type1
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

        product = d.pop("product", UNSET)

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

        patched_engagement_request = cls(
            tags=tags,
            name=name,
            description=description,
            version=version,
            first_contacted=first_contacted,
            target_start=target_start,
            target_end=target_end,
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
            product=product,
            build_server=build_server,
            source_code_management_server=source_code_management_server,
            orchestration_engine=orchestration_engine,
        )

        patched_engagement_request.additional_properties = d
        return patched_engagement_request

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
