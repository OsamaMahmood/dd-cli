from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.notifications_request_auto_close_engagement_item import (
    NotificationsRequestAutoCloseEngagementItem,
)
from ..models.notifications_request_close_engagement_item import (
    NotificationsRequestCloseEngagementItem,
)
from ..models.notifications_request_code_review_item import NotificationsRequestCodeReviewItem
from ..models.notifications_request_engagement_added_item import (
    NotificationsRequestEngagementAddedItem,
)
from ..models.notifications_request_jira_update_item import NotificationsRequestJiraUpdateItem
from ..models.notifications_request_other_item import NotificationsRequestOtherItem
from ..models.notifications_request_product_added_item import NotificationsRequestProductAddedItem
from ..models.notifications_request_product_type_added_item import (
    NotificationsRequestProductTypeAddedItem,
)
from ..models.notifications_request_review_requested_item import (
    NotificationsRequestReviewRequestedItem,
)
from ..models.notifications_request_risk_acceptance_expiration_item import (
    NotificationsRequestRiskAcceptanceExpirationItem,
)
from ..models.notifications_request_scan_added_empty import NotificationsRequestScanAddedEmpty
from ..models.notifications_request_scan_added_item import NotificationsRequestScanAddedItem
from ..models.notifications_request_sla_breach_combined_item import (
    NotificationsRequestSlaBreachCombinedItem,
)
from ..models.notifications_request_sla_breach_item import NotificationsRequestSlaBreachItem
from ..models.notifications_request_stale_engagement_item import (
    NotificationsRequestStaleEngagementItem,
)
from ..models.notifications_request_test_added_item import NotificationsRequestTestAddedItem
from ..models.notifications_request_upcoming_engagement_item import (
    NotificationsRequestUpcomingEngagementItem,
)
from ..models.notifications_request_user_mentioned_item import NotificationsRequestUserMentionedItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationsRequest")


@_attrs_define
class NotificationsRequest:
    """
    Attributes:
        product (int | None | Unset):
        user (int | None | Unset):
        product_type_added (list[NotificationsRequestProductTypeAddedItem] | Unset):
        product_added (list[NotificationsRequestProductAddedItem] | Unset):
        engagement_added (list[NotificationsRequestEngagementAddedItem] | Unset):
        test_added (list[NotificationsRequestTestAddedItem] | Unset):
        scan_added (list[NotificationsRequestScanAddedItem] | Unset):
        jira_update (list[NotificationsRequestJiraUpdateItem] | Unset):
        upcoming_engagement (list[NotificationsRequestUpcomingEngagementItem] | Unset):
        stale_engagement (list[NotificationsRequestStaleEngagementItem] | Unset):
        auto_close_engagement (list[NotificationsRequestAutoCloseEngagementItem] | Unset):
        close_engagement (list[NotificationsRequestCloseEngagementItem] | Unset):
        user_mentioned (list[NotificationsRequestUserMentionedItem] | Unset):
        code_review (list[NotificationsRequestCodeReviewItem] | Unset):
        review_requested (list[NotificationsRequestReviewRequestedItem] | Unset):
        other (list[NotificationsRequestOtherItem] | Unset):
        sla_breach (list[NotificationsRequestSlaBreachItem] | Unset):
        sla_breach_combined (list[NotificationsRequestSlaBreachCombinedItem] | Unset):
        risk_acceptance_expiration (list[NotificationsRequestRiskAcceptanceExpirationItem] | Unset):
        template (bool | Unset):  Default: False.
        scan_added_empty (NotificationsRequestScanAddedEmpty | Unset): Triggered whenever an (re-)import has been done
            (even if that created/updated/closed no findings).

            * `slack` - slack
            * `msteams` - msteams
            * `mail` - mail
            * `webhooks` - webhooks
            * `alert` - alert
    """

    product: int | None | Unset = UNSET
    user: int | None | Unset = UNSET
    product_type_added: list[NotificationsRequestProductTypeAddedItem] | Unset = UNSET
    product_added: list[NotificationsRequestProductAddedItem] | Unset = UNSET
    engagement_added: list[NotificationsRequestEngagementAddedItem] | Unset = UNSET
    test_added: list[NotificationsRequestTestAddedItem] | Unset = UNSET
    scan_added: list[NotificationsRequestScanAddedItem] | Unset = UNSET
    jira_update: list[NotificationsRequestJiraUpdateItem] | Unset = UNSET
    upcoming_engagement: list[NotificationsRequestUpcomingEngagementItem] | Unset = UNSET
    stale_engagement: list[NotificationsRequestStaleEngagementItem] | Unset = UNSET
    auto_close_engagement: list[NotificationsRequestAutoCloseEngagementItem] | Unset = UNSET
    close_engagement: list[NotificationsRequestCloseEngagementItem] | Unset = UNSET
    user_mentioned: list[NotificationsRequestUserMentionedItem] | Unset = UNSET
    code_review: list[NotificationsRequestCodeReviewItem] | Unset = UNSET
    review_requested: list[NotificationsRequestReviewRequestedItem] | Unset = UNSET
    other: list[NotificationsRequestOtherItem] | Unset = UNSET
    sla_breach: list[NotificationsRequestSlaBreachItem] | Unset = UNSET
    sla_breach_combined: list[NotificationsRequestSlaBreachCombinedItem] | Unset = UNSET
    risk_acceptance_expiration: list[NotificationsRequestRiskAcceptanceExpirationItem] | Unset = (
        UNSET
    )
    template: bool | Unset = False
    scan_added_empty: NotificationsRequestScanAddedEmpty | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product: int | None | Unset
        if isinstance(self.product, Unset):
            product = UNSET
        else:
            product = self.product

        user: int | None | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        product_type_added: list[str] | Unset = UNSET
        if not isinstance(self.product_type_added, Unset):
            product_type_added = []
            for product_type_added_item_data in self.product_type_added:
                product_type_added_item = product_type_added_item_data.value
                product_type_added.append(product_type_added_item)

        product_added: list[str] | Unset = UNSET
        if not isinstance(self.product_added, Unset):
            product_added = []
            for product_added_item_data in self.product_added:
                product_added_item = product_added_item_data.value
                product_added.append(product_added_item)

        engagement_added: list[str] | Unset = UNSET
        if not isinstance(self.engagement_added, Unset):
            engagement_added = []
            for engagement_added_item_data in self.engagement_added:
                engagement_added_item = engagement_added_item_data.value
                engagement_added.append(engagement_added_item)

        test_added: list[str] | Unset = UNSET
        if not isinstance(self.test_added, Unset):
            test_added = []
            for test_added_item_data in self.test_added:
                test_added_item = test_added_item_data.value
                test_added.append(test_added_item)

        scan_added: list[str] | Unset = UNSET
        if not isinstance(self.scan_added, Unset):
            scan_added = []
            for scan_added_item_data in self.scan_added:
                scan_added_item = scan_added_item_data.value
                scan_added.append(scan_added_item)

        jira_update: list[str] | Unset = UNSET
        if not isinstance(self.jira_update, Unset):
            jira_update = []
            for jira_update_item_data in self.jira_update:
                jira_update_item = jira_update_item_data.value
                jira_update.append(jira_update_item)

        upcoming_engagement: list[str] | Unset = UNSET
        if not isinstance(self.upcoming_engagement, Unset):
            upcoming_engagement = []
            for upcoming_engagement_item_data in self.upcoming_engagement:
                upcoming_engagement_item = upcoming_engagement_item_data.value
                upcoming_engagement.append(upcoming_engagement_item)

        stale_engagement: list[str] | Unset = UNSET
        if not isinstance(self.stale_engagement, Unset):
            stale_engagement = []
            for stale_engagement_item_data in self.stale_engagement:
                stale_engagement_item = stale_engagement_item_data.value
                stale_engagement.append(stale_engagement_item)

        auto_close_engagement: list[str] | Unset = UNSET
        if not isinstance(self.auto_close_engagement, Unset):
            auto_close_engagement = []
            for auto_close_engagement_item_data in self.auto_close_engagement:
                auto_close_engagement_item = auto_close_engagement_item_data.value
                auto_close_engagement.append(auto_close_engagement_item)

        close_engagement: list[str] | Unset = UNSET
        if not isinstance(self.close_engagement, Unset):
            close_engagement = []
            for close_engagement_item_data in self.close_engagement:
                close_engagement_item = close_engagement_item_data.value
                close_engagement.append(close_engagement_item)

        user_mentioned: list[str] | Unset = UNSET
        if not isinstance(self.user_mentioned, Unset):
            user_mentioned = []
            for user_mentioned_item_data in self.user_mentioned:
                user_mentioned_item = user_mentioned_item_data.value
                user_mentioned.append(user_mentioned_item)

        code_review: list[str] | Unset = UNSET
        if not isinstance(self.code_review, Unset):
            code_review = []
            for code_review_item_data in self.code_review:
                code_review_item = code_review_item_data.value
                code_review.append(code_review_item)

        review_requested: list[str] | Unset = UNSET
        if not isinstance(self.review_requested, Unset):
            review_requested = []
            for review_requested_item_data in self.review_requested:
                review_requested_item = review_requested_item_data.value
                review_requested.append(review_requested_item)

        other: list[str] | Unset = UNSET
        if not isinstance(self.other, Unset):
            other = []
            for other_item_data in self.other:
                other_item = other_item_data.value
                other.append(other_item)

        sla_breach: list[str] | Unset = UNSET
        if not isinstance(self.sla_breach, Unset):
            sla_breach = []
            for sla_breach_item_data in self.sla_breach:
                sla_breach_item = sla_breach_item_data.value
                sla_breach.append(sla_breach_item)

        sla_breach_combined: list[str] | Unset = UNSET
        if not isinstance(self.sla_breach_combined, Unset):
            sla_breach_combined = []
            for sla_breach_combined_item_data in self.sla_breach_combined:
                sla_breach_combined_item = sla_breach_combined_item_data.value
                sla_breach_combined.append(sla_breach_combined_item)

        risk_acceptance_expiration: list[str] | Unset = UNSET
        if not isinstance(self.risk_acceptance_expiration, Unset):
            risk_acceptance_expiration = []
            for risk_acceptance_expiration_item_data in self.risk_acceptance_expiration:
                risk_acceptance_expiration_item = risk_acceptance_expiration_item_data.value
                risk_acceptance_expiration.append(risk_acceptance_expiration_item)

        template = self.template

        scan_added_empty: str | Unset = UNSET
        if not isinstance(self.scan_added_empty, Unset):
            scan_added_empty = self.scan_added_empty.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product is not UNSET:
            field_dict["product"] = product
        if user is not UNSET:
            field_dict["user"] = user
        if product_type_added is not UNSET:
            field_dict["product_type_added"] = product_type_added
        if product_added is not UNSET:
            field_dict["product_added"] = product_added
        if engagement_added is not UNSET:
            field_dict["engagement_added"] = engagement_added
        if test_added is not UNSET:
            field_dict["test_added"] = test_added
        if scan_added is not UNSET:
            field_dict["scan_added"] = scan_added
        if jira_update is not UNSET:
            field_dict["jira_update"] = jira_update
        if upcoming_engagement is not UNSET:
            field_dict["upcoming_engagement"] = upcoming_engagement
        if stale_engagement is not UNSET:
            field_dict["stale_engagement"] = stale_engagement
        if auto_close_engagement is not UNSET:
            field_dict["auto_close_engagement"] = auto_close_engagement
        if close_engagement is not UNSET:
            field_dict["close_engagement"] = close_engagement
        if user_mentioned is not UNSET:
            field_dict["user_mentioned"] = user_mentioned
        if code_review is not UNSET:
            field_dict["code_review"] = code_review
        if review_requested is not UNSET:
            field_dict["review_requested"] = review_requested
        if other is not UNSET:
            field_dict["other"] = other
        if sla_breach is not UNSET:
            field_dict["sla_breach"] = sla_breach
        if sla_breach_combined is not UNSET:
            field_dict["sla_breach_combined"] = sla_breach_combined
        if risk_acceptance_expiration is not UNSET:
            field_dict["risk_acceptance_expiration"] = risk_acceptance_expiration
        if template is not UNSET:
            field_dict["template"] = template
        if scan_added_empty is not UNSET:
            field_dict["scan_added_empty"] = scan_added_empty

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.product, Unset):
            if isinstance(self.product, int):
                files.append(("product", (None, str(self.product).encode(), "text/plain")))
            else:
                files.append(("product", (None, str(self.product).encode(), "text/plain")))

        if not isinstance(self.user, Unset):
            if isinstance(self.user, int):
                files.append(("user", (None, str(self.user).encode(), "text/plain")))
            else:
                files.append(("user", (None, str(self.user).encode(), "text/plain")))

        if not isinstance(self.product_type_added, Unset):
            for product_type_added_item_element in self.product_type_added:
                files.append(
                    (
                        "product_type_added",
                        (None, str(product_type_added_item_element.value).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.product_added, Unset):
            for product_added_item_element in self.product_added:
                files.append(
                    (
                        "product_added",
                        (None, str(product_added_item_element.value).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.engagement_added, Unset):
            for engagement_added_item_element in self.engagement_added:
                files.append(
                    (
                        "engagement_added",
                        (None, str(engagement_added_item_element.value).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.test_added, Unset):
            for test_added_item_element in self.test_added:
                files.append(
                    (
                        "test_added",
                        (None, str(test_added_item_element.value).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.scan_added, Unset):
            for scan_added_item_element in self.scan_added:
                files.append(
                    (
                        "scan_added",
                        (None, str(scan_added_item_element.value).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.jira_update, Unset):
            for jira_update_item_element in self.jira_update:
                files.append(
                    (
                        "jira_update",
                        (None, str(jira_update_item_element.value).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.upcoming_engagement, Unset):
            for upcoming_engagement_item_element in self.upcoming_engagement:
                files.append(
                    (
                        "upcoming_engagement",
                        (None, str(upcoming_engagement_item_element.value).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.stale_engagement, Unset):
            for stale_engagement_item_element in self.stale_engagement:
                files.append(
                    (
                        "stale_engagement",
                        (None, str(stale_engagement_item_element.value).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.auto_close_engagement, Unset):
            for auto_close_engagement_item_element in self.auto_close_engagement:
                files.append(
                    (
                        "auto_close_engagement",
                        (
                            None,
                            str(auto_close_engagement_item_element.value).encode(),
                            "text/plain",
                        ),
                    )
                )

        if not isinstance(self.close_engagement, Unset):
            for close_engagement_item_element in self.close_engagement:
                files.append(
                    (
                        "close_engagement",
                        (None, str(close_engagement_item_element.value).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.user_mentioned, Unset):
            for user_mentioned_item_element in self.user_mentioned:
                files.append(
                    (
                        "user_mentioned",
                        (None, str(user_mentioned_item_element.value).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.code_review, Unset):
            for code_review_item_element in self.code_review:
                files.append(
                    (
                        "code_review",
                        (None, str(code_review_item_element.value).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.review_requested, Unset):
            for review_requested_item_element in self.review_requested:
                files.append(
                    (
                        "review_requested",
                        (None, str(review_requested_item_element.value).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.other, Unset):
            for other_item_element in self.other:
                files.append(
                    ("other", (None, str(other_item_element.value).encode(), "text/plain"))
                )

        if not isinstance(self.sla_breach, Unset):
            for sla_breach_item_element in self.sla_breach:
                files.append(
                    (
                        "sla_breach",
                        (None, str(sla_breach_item_element.value).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.sla_breach_combined, Unset):
            for sla_breach_combined_item_element in self.sla_breach_combined:
                files.append(
                    (
                        "sla_breach_combined",
                        (None, str(sla_breach_combined_item_element.value).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.risk_acceptance_expiration, Unset):
            for risk_acceptance_expiration_item_element in self.risk_acceptance_expiration:
                files.append(
                    (
                        "risk_acceptance_expiration",
                        (
                            None,
                            str(risk_acceptance_expiration_item_element.value).encode(),
                            "text/plain",
                        ),
                    )
                )

        if not isinstance(self.template, Unset):
            files.append(("template", (None, str(self.template).encode(), "text/plain")))

        if not isinstance(self.scan_added_empty, Unset):
            files.append(
                (
                    "scan_added_empty",
                    (None, str(self.scan_added_empty.value).encode(), "text/plain"),
                )
            )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_product(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        product = _parse_product(d.pop("product", UNSET))

        def _parse_user(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user = _parse_user(d.pop("user", UNSET))

        _product_type_added = d.pop("product_type_added", UNSET)
        product_type_added: list[NotificationsRequestProductTypeAddedItem] | Unset = UNSET
        if _product_type_added is not UNSET:
            product_type_added = []
            for product_type_added_item_data in _product_type_added:
                product_type_added_item = NotificationsRequestProductTypeAddedItem(
                    product_type_added_item_data
                )

                product_type_added.append(product_type_added_item)

        _product_added = d.pop("product_added", UNSET)
        product_added: list[NotificationsRequestProductAddedItem] | Unset = UNSET
        if _product_added is not UNSET:
            product_added = []
            for product_added_item_data in _product_added:
                product_added_item = NotificationsRequestProductAddedItem(product_added_item_data)

                product_added.append(product_added_item)

        _engagement_added = d.pop("engagement_added", UNSET)
        engagement_added: list[NotificationsRequestEngagementAddedItem] | Unset = UNSET
        if _engagement_added is not UNSET:
            engagement_added = []
            for engagement_added_item_data in _engagement_added:
                engagement_added_item = NotificationsRequestEngagementAddedItem(
                    engagement_added_item_data
                )

                engagement_added.append(engagement_added_item)

        _test_added = d.pop("test_added", UNSET)
        test_added: list[NotificationsRequestTestAddedItem] | Unset = UNSET
        if _test_added is not UNSET:
            test_added = []
            for test_added_item_data in _test_added:
                test_added_item = NotificationsRequestTestAddedItem(test_added_item_data)

                test_added.append(test_added_item)

        _scan_added = d.pop("scan_added", UNSET)
        scan_added: list[NotificationsRequestScanAddedItem] | Unset = UNSET
        if _scan_added is not UNSET:
            scan_added = []
            for scan_added_item_data in _scan_added:
                scan_added_item = NotificationsRequestScanAddedItem(scan_added_item_data)

                scan_added.append(scan_added_item)

        _jira_update = d.pop("jira_update", UNSET)
        jira_update: list[NotificationsRequestJiraUpdateItem] | Unset = UNSET
        if _jira_update is not UNSET:
            jira_update = []
            for jira_update_item_data in _jira_update:
                jira_update_item = NotificationsRequestJiraUpdateItem(jira_update_item_data)

                jira_update.append(jira_update_item)

        _upcoming_engagement = d.pop("upcoming_engagement", UNSET)
        upcoming_engagement: list[NotificationsRequestUpcomingEngagementItem] | Unset = UNSET
        if _upcoming_engagement is not UNSET:
            upcoming_engagement = []
            for upcoming_engagement_item_data in _upcoming_engagement:
                upcoming_engagement_item = NotificationsRequestUpcomingEngagementItem(
                    upcoming_engagement_item_data
                )

                upcoming_engagement.append(upcoming_engagement_item)

        _stale_engagement = d.pop("stale_engagement", UNSET)
        stale_engagement: list[NotificationsRequestStaleEngagementItem] | Unset = UNSET
        if _stale_engagement is not UNSET:
            stale_engagement = []
            for stale_engagement_item_data in _stale_engagement:
                stale_engagement_item = NotificationsRequestStaleEngagementItem(
                    stale_engagement_item_data
                )

                stale_engagement.append(stale_engagement_item)

        _auto_close_engagement = d.pop("auto_close_engagement", UNSET)
        auto_close_engagement: list[NotificationsRequestAutoCloseEngagementItem] | Unset = UNSET
        if _auto_close_engagement is not UNSET:
            auto_close_engagement = []
            for auto_close_engagement_item_data in _auto_close_engagement:
                auto_close_engagement_item = NotificationsRequestAutoCloseEngagementItem(
                    auto_close_engagement_item_data
                )

                auto_close_engagement.append(auto_close_engagement_item)

        _close_engagement = d.pop("close_engagement", UNSET)
        close_engagement: list[NotificationsRequestCloseEngagementItem] | Unset = UNSET
        if _close_engagement is not UNSET:
            close_engagement = []
            for close_engagement_item_data in _close_engagement:
                close_engagement_item = NotificationsRequestCloseEngagementItem(
                    close_engagement_item_data
                )

                close_engagement.append(close_engagement_item)

        _user_mentioned = d.pop("user_mentioned", UNSET)
        user_mentioned: list[NotificationsRequestUserMentionedItem] | Unset = UNSET
        if _user_mentioned is not UNSET:
            user_mentioned = []
            for user_mentioned_item_data in _user_mentioned:
                user_mentioned_item = NotificationsRequestUserMentionedItem(
                    user_mentioned_item_data
                )

                user_mentioned.append(user_mentioned_item)

        _code_review = d.pop("code_review", UNSET)
        code_review: list[NotificationsRequestCodeReviewItem] | Unset = UNSET
        if _code_review is not UNSET:
            code_review = []
            for code_review_item_data in _code_review:
                code_review_item = NotificationsRequestCodeReviewItem(code_review_item_data)

                code_review.append(code_review_item)

        _review_requested = d.pop("review_requested", UNSET)
        review_requested: list[NotificationsRequestReviewRequestedItem] | Unset = UNSET
        if _review_requested is not UNSET:
            review_requested = []
            for review_requested_item_data in _review_requested:
                review_requested_item = NotificationsRequestReviewRequestedItem(
                    review_requested_item_data
                )

                review_requested.append(review_requested_item)

        _other = d.pop("other", UNSET)
        other: list[NotificationsRequestOtherItem] | Unset = UNSET
        if _other is not UNSET:
            other = []
            for other_item_data in _other:
                other_item = NotificationsRequestOtherItem(other_item_data)

                other.append(other_item)

        _sla_breach = d.pop("sla_breach", UNSET)
        sla_breach: list[NotificationsRequestSlaBreachItem] | Unset = UNSET
        if _sla_breach is not UNSET:
            sla_breach = []
            for sla_breach_item_data in _sla_breach:
                sla_breach_item = NotificationsRequestSlaBreachItem(sla_breach_item_data)

                sla_breach.append(sla_breach_item)

        _sla_breach_combined = d.pop("sla_breach_combined", UNSET)
        sla_breach_combined: list[NotificationsRequestSlaBreachCombinedItem] | Unset = UNSET
        if _sla_breach_combined is not UNSET:
            sla_breach_combined = []
            for sla_breach_combined_item_data in _sla_breach_combined:
                sla_breach_combined_item = NotificationsRequestSlaBreachCombinedItem(
                    sla_breach_combined_item_data
                )

                sla_breach_combined.append(sla_breach_combined_item)

        _risk_acceptance_expiration = d.pop("risk_acceptance_expiration", UNSET)
        risk_acceptance_expiration: (
            list[NotificationsRequestRiskAcceptanceExpirationItem] | Unset
        ) = UNSET
        if _risk_acceptance_expiration is not UNSET:
            risk_acceptance_expiration = []
            for risk_acceptance_expiration_item_data in _risk_acceptance_expiration:
                risk_acceptance_expiration_item = NotificationsRequestRiskAcceptanceExpirationItem(
                    risk_acceptance_expiration_item_data
                )

                risk_acceptance_expiration.append(risk_acceptance_expiration_item)

        template = d.pop("template", UNSET)

        _scan_added_empty = d.pop("scan_added_empty", UNSET)
        scan_added_empty: NotificationsRequestScanAddedEmpty | Unset
        if isinstance(_scan_added_empty, Unset):
            scan_added_empty = UNSET
        else:
            scan_added_empty = NotificationsRequestScanAddedEmpty(_scan_added_empty)

        notifications_request = cls(
            product=product,
            user=user,
            product_type_added=product_type_added,
            product_added=product_added,
            engagement_added=engagement_added,
            test_added=test_added,
            scan_added=scan_added,
            jira_update=jira_update,
            upcoming_engagement=upcoming_engagement,
            stale_engagement=stale_engagement,
            auto_close_engagement=auto_close_engagement,
            close_engagement=close_engagement,
            user_mentioned=user_mentioned,
            code_review=code_review,
            review_requested=review_requested,
            other=other,
            sla_breach=sla_breach,
            sla_breach_combined=sla_breach_combined,
            risk_acceptance_expiration=risk_acceptance_expiration,
            template=template,
            scan_added_empty=scan_added_empty,
        )

        notifications_request.additional_properties = d
        return notifications_request

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
