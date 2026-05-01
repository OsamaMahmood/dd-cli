from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.language_prefetch import LanguagePrefetch


T = TypeVar("T", bound="Language")


@_attrs_define
class Language:
    """
    Attributes:
        id (int):
        created (datetime.datetime):
        language (int):
        product (int):
        files (int | None | Unset):
        blank (int | None | Unset):
        comment (int | None | Unset):
        code (int | None | Unset):
        user (int | None | Unset):
        prefetch (LanguagePrefetch | Unset):
    """

    id: int
    created: datetime.datetime
    language: int
    product: int
    files: int | None | Unset = UNSET
    blank: int | None | Unset = UNSET
    comment: int | None | Unset = UNSET
    code: int | None | Unset = UNSET
    user: int | None | Unset = UNSET
    prefetch: LanguagePrefetch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created = self.created.isoformat()

        language = self.language

        product = self.product

        files: int | None | Unset
        if isinstance(self.files, Unset):
            files = UNSET
        else:
            files = self.files

        blank: int | None | Unset
        if isinstance(self.blank, Unset):
            blank = UNSET
        else:
            blank = self.blank

        comment: int | None | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        code: int | None | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        user: int | None | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        prefetch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prefetch, Unset):
            prefetch = self.prefetch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created": created,
                "language": language,
                "product": product,
            }
        )
        if files is not UNSET:
            field_dict["files"] = files
        if blank is not UNSET:
            field_dict["blank"] = blank
        if comment is not UNSET:
            field_dict["comment"] = comment
        if code is not UNSET:
            field_dict["code"] = code
        if user is not UNSET:
            field_dict["user"] = user
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.language_prefetch import LanguagePrefetch

        d = dict(src_dict)
        id = d.pop("id")

        created = isoparse(d.pop("created"))

        language = d.pop("language")

        product = d.pop("product")

        def _parse_files(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        files = _parse_files(d.pop("files", UNSET))

        def _parse_blank(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        blank = _parse_blank(d.pop("blank", UNSET))

        def _parse_comment(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

        def _parse_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_user(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user = _parse_user(d.pop("user", UNSET))

        _prefetch = d.pop("prefetch", UNSET)
        prefetch: LanguagePrefetch | Unset
        if isinstance(_prefetch, Unset):
            prefetch = UNSET
        else:
            prefetch = LanguagePrefetch.from_dict(_prefetch)

        language = cls(
            id=id,
            created=created,
            language=language,
            product=product,
            files=files,
            blank=blank,
            comment=comment,
            code=code,
            user=user,
            prefetch=prefetch,
        )

        language.additional_properties = d
        return language

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
