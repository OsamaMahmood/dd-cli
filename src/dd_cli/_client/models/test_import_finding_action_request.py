from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.test_import_finding_action_request_action_type_1 import (
    TestImportFindingActionRequestActionType1,
)
from ..models.test_import_finding_action_request_action_type_2_type_1 import (
    TestImportFindingActionRequestActionType2Type1,
)
from ..models.test_import_finding_action_request_action_type_3_type_1 import (
    TestImportFindingActionRequestActionType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TestImportFindingActionRequest")


@_attrs_define
class TestImportFindingActionRequest:
    """
    Attributes:
        action (None | TestImportFindingActionRequestActionType1 | TestImportFindingActionRequestActionType2Type1 |
            TestImportFindingActionRequestActionType3Type1 | Unset): * `N` - created
            * `C` - closed
            * `R` - reactivated
            * `U` - untouched
    """

    action: (
        None
        | TestImportFindingActionRequestActionType1
        | TestImportFindingActionRequestActionType2Type1
        | TestImportFindingActionRequestActionType3Type1
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: None | str | Unset
        if isinstance(self.action, Unset):
            action = UNSET
        elif (
            isinstance(self.action, TestImportFindingActionRequestActionType1)
            or isinstance(self.action, TestImportFindingActionRequestActionType2Type1)
            or isinstance(self.action, TestImportFindingActionRequestActionType3Type1)
        ):
            action = self.action.value
        else:
            action = self.action

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_action(
            data: object,
        ) -> (
            None
            | TestImportFindingActionRequestActionType1
            | TestImportFindingActionRequestActionType2Type1
            | TestImportFindingActionRequestActionType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                action_type_1 = TestImportFindingActionRequestActionType1(data)

                return action_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                action_type_2_type_1 = TestImportFindingActionRequestActionType2Type1(data)

                return action_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                action_type_3_type_1 = TestImportFindingActionRequestActionType3Type1(data)

                return action_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TestImportFindingActionRequestActionType1
                | TestImportFindingActionRequestActionType2Type1
                | TestImportFindingActionRequestActionType3Type1
                | Unset,
                data,
            )

        action = _parse_action(d.pop("action", UNSET))

        test_import_finding_action_request = cls(
            action=action,
        )

        test_import_finding_action_request.additional_properties = d
        return test_import_finding_action_request

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
