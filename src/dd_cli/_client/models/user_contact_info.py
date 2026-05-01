from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user import User
    from ..models.user_contact_info_prefetch import UserContactInfoPrefetch


T = TypeVar("T", bound="UserContactInfo")


@_attrs_define
class UserContactInfo:
    """
    Attributes:
        id (int):
        user_profile (User):
        user (int):
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
        prefetch (UserContactInfoPrefetch | Unset):
    """

    id: int
    user_profile: User
    user: int
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
    prefetch: UserContactInfoPrefetch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_profile = self.user_profile.to_dict()

        user = self.user

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

        prefetch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prefetch, Unset):
            prefetch = self.prefetch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_profile": user_profile,
                "user": user,
            }
        )
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
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user import User
        from ..models.user_contact_info_prefetch import UserContactInfoPrefetch

        d = dict(src_dict)
        id = d.pop("id")

        user_profile = User.from_dict(d.pop("user_profile"))

        user = d.pop("user")

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

        _prefetch = d.pop("prefetch", UNSET)
        prefetch: UserContactInfoPrefetch | Unset
        if isinstance(_prefetch, Unset):
            prefetch = UNSET
        else:
            prefetch = UserContactInfoPrefetch.from_dict(_prefetch)

        user_contact_info = cls(
            id=id,
            user_profile=user_profile,
            user=user,
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
            prefetch=prefetch,
        )

        user_contact_info.additional_properties = d
        return user_contact_info

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
