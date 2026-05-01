from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedUserContactInfoRequest")


@_attrs_define
class PatchedUserContactInfoRequest:
    """
    Attributes:
        title (None | str | Unset):
        phone_number (str | Unset): Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.
        cell_number (str | Unset): Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.
        twitter_username (None | str | Unset):
        github_username (None | str | Unset):
        slack_username (None | str | Unset): Email address associated with your slack account
        slack_user_id (None | str | Unset):
        block_execution (bool | Unset): Instead of async deduping a finding the findings will be deduped synchronously
            and will 'block' the user until completion.
        force_password_reset (bool | Unset): Forces this user to reset their password on next login.
        token_last_reset (datetime.datetime | None | Unset): Timestamp of the most recent API token reset for this user.
        password_last_reset (datetime.datetime | None | Unset): Timestamp of the most recent password reset for this
            user.
        user (int | Unset):
    """

    title: None | str | Unset = UNSET
    phone_number: str | Unset = UNSET
    cell_number: str | Unset = UNSET
    twitter_username: None | str | Unset = UNSET
    github_username: None | str | Unset = UNSET
    slack_username: None | str | Unset = UNSET
    slack_user_id: None | str | Unset = UNSET
    block_execution: bool | Unset = UNSET
    force_password_reset: bool | Unset = UNSET
    token_last_reset: datetime.datetime | None | Unset = UNSET
    password_last_reset: datetime.datetime | None | Unset = UNSET
    user: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        phone_number = self.phone_number

        cell_number = self.cell_number

        twitter_username: None | str | Unset
        if isinstance(self.twitter_username, Unset):
            twitter_username = UNSET
        else:
            twitter_username = self.twitter_username

        github_username: None | str | Unset
        if isinstance(self.github_username, Unset):
            github_username = UNSET
        else:
            github_username = self.github_username

        slack_username: None | str | Unset
        if isinstance(self.slack_username, Unset):
            slack_username = UNSET
        else:
            slack_username = self.slack_username

        slack_user_id: None | str | Unset
        if isinstance(self.slack_user_id, Unset):
            slack_user_id = UNSET
        else:
            slack_user_id = self.slack_user_id

        block_execution = self.block_execution

        force_password_reset = self.force_password_reset

        token_last_reset: None | str | Unset
        if isinstance(self.token_last_reset, Unset):
            token_last_reset = UNSET
        elif isinstance(self.token_last_reset, datetime.datetime):
            token_last_reset = self.token_last_reset.isoformat()
        else:
            token_last_reset = self.token_last_reset

        password_last_reset: None | str | Unset
        if isinstance(self.password_last_reset, Unset):
            password_last_reset = UNSET
        elif isinstance(self.password_last_reset, datetime.datetime):
            password_last_reset = self.password_last_reset.isoformat()
        else:
            password_last_reset = self.password_last_reset

        user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if cell_number is not UNSET:
            field_dict["cell_number"] = cell_number
        if twitter_username is not UNSET:
            field_dict["twitter_username"] = twitter_username
        if github_username is not UNSET:
            field_dict["github_username"] = github_username
        if slack_username is not UNSET:
            field_dict["slack_username"] = slack_username
        if slack_user_id is not UNSET:
            field_dict["slack_user_id"] = slack_user_id
        if block_execution is not UNSET:
            field_dict["block_execution"] = block_execution
        if force_password_reset is not UNSET:
            field_dict["force_password_reset"] = force_password_reset
        if token_last_reset is not UNSET:
            field_dict["token_last_reset"] = token_last_reset
        if password_last_reset is not UNSET:
            field_dict["password_last_reset"] = password_last_reset
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.title, Unset):
            if isinstance(self.title, str):
                files.append(("title", (None, str(self.title).encode(), "text/plain")))
            else:
                files.append(("title", (None, str(self.title).encode(), "text/plain")))

        if not isinstance(self.phone_number, Unset):
            files.append(("phone_number", (None, str(self.phone_number).encode(), "text/plain")))

        if not isinstance(self.cell_number, Unset):
            files.append(("cell_number", (None, str(self.cell_number).encode(), "text/plain")))

        if not isinstance(self.twitter_username, Unset):
            if isinstance(self.twitter_username, str):
                files.append(
                    ("twitter_username", (None, str(self.twitter_username).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("twitter_username", (None, str(self.twitter_username).encode(), "text/plain"))
                )

        if not isinstance(self.github_username, Unset):
            if isinstance(self.github_username, str):
                files.append(
                    ("github_username", (None, str(self.github_username).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("github_username", (None, str(self.github_username).encode(), "text/plain"))
                )

        if not isinstance(self.slack_username, Unset):
            if isinstance(self.slack_username, str):
                files.append(
                    ("slack_username", (None, str(self.slack_username).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("slack_username", (None, str(self.slack_username).encode(), "text/plain"))
                )

        if not isinstance(self.slack_user_id, Unset):
            if isinstance(self.slack_user_id, str):
                files.append(
                    ("slack_user_id", (None, str(self.slack_user_id).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("slack_user_id", (None, str(self.slack_user_id).encode(), "text/plain"))
                )

        if not isinstance(self.block_execution, Unset):
            files.append(
                ("block_execution", (None, str(self.block_execution).encode(), "text/plain"))
            )

        if not isinstance(self.force_password_reset, Unset):
            files.append(
                (
                    "force_password_reset",
                    (None, str(self.force_password_reset).encode(), "text/plain"),
                )
            )

        if not isinstance(self.token_last_reset, Unset):
            if isinstance(self.token_last_reset, datetime.datetime):
                files.append(
                    (
                        "token_last_reset",
                        (None, self.token_last_reset.isoformat().encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    ("token_last_reset", (None, str(self.token_last_reset).encode(), "text/plain"))
                )

        if not isinstance(self.password_last_reset, Unset):
            if isinstance(self.password_last_reset, datetime.datetime):
                files.append(
                    (
                        "password_last_reset",
                        (None, self.password_last_reset.isoformat().encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "password_last_reset",
                        (None, str(self.password_last_reset).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.user, Unset):
            files.append(("user", (None, str(self.user).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        phone_number = d.pop("phone_number", UNSET)

        cell_number = d.pop("cell_number", UNSET)

        def _parse_twitter_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        twitter_username = _parse_twitter_username(d.pop("twitter_username", UNSET))

        def _parse_github_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        github_username = _parse_github_username(d.pop("github_username", UNSET))

        def _parse_slack_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slack_username = _parse_slack_username(d.pop("slack_username", UNSET))

        def _parse_slack_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slack_user_id = _parse_slack_user_id(d.pop("slack_user_id", UNSET))

        block_execution = d.pop("block_execution", UNSET)

        force_password_reset = d.pop("force_password_reset", UNSET)

        def _parse_token_last_reset(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                token_last_reset_type_0 = isoparse(data)

                return token_last_reset_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        token_last_reset = _parse_token_last_reset(d.pop("token_last_reset", UNSET))

        def _parse_password_last_reset(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                password_last_reset_type_0 = isoparse(data)

                return password_last_reset_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        password_last_reset = _parse_password_last_reset(d.pop("password_last_reset", UNSET))

        user = d.pop("user", UNSET)

        patched_user_contact_info_request = cls(
            title=title,
            phone_number=phone_number,
            cell_number=cell_number,
            twitter_username=twitter_username,
            github_username=github_username,
            slack_username=slack_username,
            slack_user_id=slack_user_id,
            block_execution=block_execution,
            force_password_reset=force_password_reset,
            token_last_reset=token_last_reset,
            password_last_reset=password_last_reset,
            user=user,
        )

        patched_user_contact_info_request.additional_properties = d
        return patched_user_contact_info_request

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
