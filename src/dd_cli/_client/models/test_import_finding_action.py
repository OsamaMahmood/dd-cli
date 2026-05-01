from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.test_import_finding_action_action_type_1 import TestImportFindingActionActionType1
from ..models.test_import_finding_action_action_type_2_type_1 import (
    TestImportFindingActionActionType2Type1,
)
from ..models.test_import_finding_action_action_type_3_type_1 import (
    TestImportFindingActionActionType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TestImportFindingAction")


@_attrs_define
class TestImportFindingAction:
    """
    Attributes:
        id (int):
        created (datetime.datetime):
        modified (datetime.datetime):
        test_import (int):
        finding (int):
        action (None | TestImportFindingActionActionType1 | TestImportFindingActionActionType2Type1 |
            TestImportFindingActionActionType3Type1 | Unset): * `N` - created
            * `C` - closed
            * `R` - reactivated
            * `U` - untouched
    """

    id: int
    created: datetime.datetime
    modified: datetime.datetime
    test_import: int
    finding: int
    action: (
        None
        | TestImportFindingActionActionType1
        | TestImportFindingActionActionType2Type1
        | TestImportFindingActionActionType3Type1
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        test_import = self.test_import

        finding = self.finding

        action: None | str | Unset
        if isinstance(self.action, Unset):
            action = UNSET
        elif (
            isinstance(self.action, TestImportFindingActionActionType1)
            or isinstance(self.action, TestImportFindingActionActionType2Type1)
            or isinstance(self.action, TestImportFindingActionActionType3Type1)
        ):
            action = self.action.value
        else:
            action = self.action

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created": created,
                "modified": modified,
                "test_import": test_import,
                "finding": finding,
            }
        )
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        test_import = d.pop("test_import")

        finding = d.pop("finding")

        def _parse_action(
            data: object,
        ) -> (
            None
            | TestImportFindingActionActionType1
            | TestImportFindingActionActionType2Type1
            | TestImportFindingActionActionType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                action_type_1 = TestImportFindingActionActionType1(data)

                return action_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                action_type_2_type_1 = TestImportFindingActionActionType2Type1(data)

                return action_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                action_type_3_type_1 = TestImportFindingActionActionType3Type1(data)

                return action_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TestImportFindingActionActionType1
                | TestImportFindingActionActionType2Type1
                | TestImportFindingActionActionType3Type1
                | Unset,
                data,
            )

        action = _parse_action(d.pop("action", UNSET))

        test_import_finding_action = cls(
            id=id,
            created=created,
            modified=modified,
            test_import=test_import,
            finding=finding,
            action=action,
        )

        test_import_finding_action.additional_properties = d
        return test_import_finding_action

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
