from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedLanguageRequest")


@_attrs_define
class PatchedLanguageRequest:
    """
    Attributes:
        files (int | None | Unset):
        blank (int | None | Unset):
        comment (int | None | Unset):
        code (int | None | Unset):
        language (int | Unset):
        product (int | Unset):
        user (int | None | Unset):
    """

    files: int | None | Unset = UNSET
    blank: int | None | Unset = UNSET
    comment: int | None | Unset = UNSET
    code: int | None | Unset = UNSET
    language: int | Unset = UNSET
    product: int | Unset = UNSET
    user: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        language = self.language

        product = self.product

        user: int | None | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files
        if blank is not UNSET:
            field_dict["blank"] = blank
        if comment is not UNSET:
            field_dict["comment"] = comment
        if code is not UNSET:
            field_dict["code"] = code
        if language is not UNSET:
            field_dict["language"] = language
        if product is not UNSET:
            field_dict["product"] = product
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.files, Unset):
            if isinstance(self.files, int):
                files.append(("files", (None, str(self.files).encode(), "text/plain")))
            else:
                files.append(("files", (None, str(self.files).encode(), "text/plain")))

        if not isinstance(self.blank, Unset):
            if isinstance(self.blank, int):
                files.append(("blank", (None, str(self.blank).encode(), "text/plain")))
            else:
                files.append(("blank", (None, str(self.blank).encode(), "text/plain")))

        if not isinstance(self.comment, Unset):
            if isinstance(self.comment, int):
                files.append(("comment", (None, str(self.comment).encode(), "text/plain")))
            else:
                files.append(("comment", (None, str(self.comment).encode(), "text/plain")))

        if not isinstance(self.code, Unset):
            if isinstance(self.code, int):
                files.append(("code", (None, str(self.code).encode(), "text/plain")))
            else:
                files.append(("code", (None, str(self.code).encode(), "text/plain")))

        if not isinstance(self.language, Unset):
            files.append(("language", (None, str(self.language).encode(), "text/plain")))

        if not isinstance(self.product, Unset):
            files.append(("product", (None, str(self.product).encode(), "text/plain")))

        if not isinstance(self.user, Unset):
            if isinstance(self.user, int):
                files.append(("user", (None, str(self.user).encode(), "text/plain")))
            else:
                files.append(("user", (None, str(self.user).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        language = d.pop("language", UNSET)

        product = d.pop("product", UNSET)

        def _parse_user(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user = _parse_user(d.pop("user", UNSET))

        patched_language_request = cls(
            files=files,
            blank=blank,
            comment=comment,
            code=code,
            language=language,
            product=product,
            user=user,
        )

        patched_language_request.additional_properties = d
        return patched_language_request

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
