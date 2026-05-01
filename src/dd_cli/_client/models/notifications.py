from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notifications_auto_close_engagement_item import NotificationsAutoCloseEngagementItem
from ..models.notifications_close_engagement_item import NotificationsCloseEngagementItem
from ..models.notifications_code_review_item import NotificationsCodeReviewItem
from ..models.notifications_engagement_added_item import NotificationsEngagementAddedItem
from ..models.notifications_jira_update_item import NotificationsJiraUpdateItem
from ..models.notifications_other_item import NotificationsOtherItem
from ..models.notifications_product_added_item import NotificationsProductAddedItem
from ..models.notifications_product_type_added_item import NotificationsProductTypeAddedItem
from ..models.notifications_review_requested_item import NotificationsReviewRequestedItem
from ..models.notifications_risk_acceptance_expiration_item import (
    NotificationsRiskAcceptanceExpirationItem,
)
from ..models.notifications_scan_added_empty import NotificationsScanAddedEmpty
from ..models.notifications_scan_added_item import NotificationsScanAddedItem
from ..models.notifications_sla_breach_combined_item import NotificationsSlaBreachCombinedItem
from ..models.notifications_sla_breach_item import NotificationsSlaBreachItem
from ..models.notifications_stale_engagement_item import NotificationsStaleEngagementItem
from ..models.notifications_test_added_item import NotificationsTestAddedItem
from ..models.notifications_upcoming_engagement_item import NotificationsUpcomingEngagementItem
from ..models.notifications_user_mentioned_item import NotificationsUserMentionedItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notifications_prefetch import NotificationsPrefetch


T = TypeVar("T", bound="Notifications")


@_attrs_define
class Notifications:
    """
    Attributes:
        id (int):
        product (int | None | Unset):
        user (int | None | Unset):
        product_type_added (list[NotificationsProductTypeAddedItem] | Unset):
        product_added (list[NotificationsProductAddedItem] | Unset):
        engagement_added (list[NotificationsEngagementAddedItem] | Unset):
        test_added (list[NotificationsTestAddedItem] | Unset):
        scan_added (list[NotificationsScanAddedItem] | Unset):
        jira_update (list[NotificationsJiraUpdateItem] | Unset):
        upcoming_engagement (list[NotificationsUpcomingEngagementItem] | Unset):
        stale_engagement (list[NotificationsStaleEngagementItem] | Unset):
        auto_close_engagement (list[NotificationsAutoCloseEngagementItem] | Unset):
        close_engagement (list[NotificationsCloseEngagementItem] | Unset):
        user_mentioned (list[NotificationsUserMentionedItem] | Unset):
        code_review (list[NotificationsCodeReviewItem] | Unset):
        review_requested (list[NotificationsReviewRequestedItem] | Unset):
        other (list[NotificationsOtherItem] | Unset):
        sla_breach (list[NotificationsSlaBreachItem] | Unset):
        sla_breach_combined (list[NotificationsSlaBreachCombinedItem] | Unset):
        risk_acceptance_expiration (list[NotificationsRiskAcceptanceExpirationItem] | Unset):
        template (bool | Unset):  Default: False.
        scan_added_empty (NotificationsScanAddedEmpty | Unset): Triggered whenever an (re-)import has been done (even if
            that created/updated/closed no findings).

            * `slack` - slack
            * `msteams` - msteams
            * `mail` - mail
            * `webhooks` - webhooks
            * `alert` - alert
        prefetch (NotificationsPrefetch | Unset):
    """

    id: int
    product: int | None | Unset = UNSET
    user: int | None | Unset = UNSET
    product_type_added: list[NotificationsProductTypeAddedItem] | Unset = UNSET
    product_added: list[NotificationsProductAddedItem] | Unset = UNSET
    engagement_added: list[NotificationsEngagementAddedItem] | Unset = UNSET
    test_added: list[NotificationsTestAddedItem] | Unset = UNSET
    scan_added: list[NotificationsScanAddedItem] | Unset = UNSET
    jira_update: list[NotificationsJiraUpdateItem] | Unset = UNSET
    upcoming_engagement: list[NotificationsUpcomingEngagementItem] | Unset = UNSET
    stale_engagement: list[NotificationsStaleEngagementItem] | Unset = UNSET
    auto_close_engagement: list[NotificationsAutoCloseEngagementItem] | Unset = UNSET
    close_engagement: list[NotificationsCloseEngagementItem] | Unset = UNSET
    user_mentioned: list[NotificationsUserMentionedItem] | Unset = UNSET
    code_review: list[NotificationsCodeReviewItem] | Unset = UNSET
    review_requested: list[NotificationsReviewRequestedItem] | Unset = UNSET
    other: list[NotificationsOtherItem] | Unset = UNSET
    sla_breach: list[NotificationsSlaBreachItem] | Unset = UNSET
    sla_breach_combined: list[NotificationsSlaBreachCombinedItem] | Unset = UNSET
    risk_acceptance_expiration: list[NotificationsRiskAcceptanceExpirationItem] | Unset = UNSET
    template: bool | Unset = False
    scan_added_empty: NotificationsScanAddedEmpty | Unset = UNSET
    prefetch: NotificationsPrefetch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

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

        prefetch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prefetch, Unset):
            prefetch = self.prefetch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
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
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notifications_prefetch import NotificationsPrefetch

        d = dict(src_dict)
        id = d.pop("id")

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
        product_type_added: list[NotificationsProductTypeAddedItem] | Unset = UNSET
        if _product_type_added is not UNSET:
            product_type_added = []
            for product_type_added_item_data in _product_type_added:
                product_type_added_item = NotificationsProductTypeAddedItem(
                    product_type_added_item_data
                )

                product_type_added.append(product_type_added_item)

        _product_added = d.pop("product_added", UNSET)
        product_added: list[NotificationsProductAddedItem] | Unset = UNSET
        if _product_added is not UNSET:
            product_added = []
            for product_added_item_data in _product_added:
                product_added_item = NotificationsProductAddedItem(product_added_item_data)

                product_added.append(product_added_item)

        _engagement_added = d.pop("engagement_added", UNSET)
        engagement_added: list[NotificationsEngagementAddedItem] | Unset = UNSET
        if _engagement_added is not UNSET:
            engagement_added = []
            for engagement_added_item_data in _engagement_added:
                engagement_added_item = NotificationsEngagementAddedItem(engagement_added_item_data)

                engagement_added.append(engagement_added_item)

        _test_added = d.pop("test_added", UNSET)
        test_added: list[NotificationsTestAddedItem] | Unset = UNSET
        if _test_added is not UNSET:
            test_added = []
            for test_added_item_data in _test_added:
                test_added_item = NotificationsTestAddedItem(test_added_item_data)

                test_added.append(test_added_item)

        _scan_added = d.pop("scan_added", UNSET)
        scan_added: list[NotificationsScanAddedItem] | Unset = UNSET
        if _scan_added is not UNSET:
            scan_added = []
            for scan_added_item_data in _scan_added:
                scan_added_item = NotificationsScanAddedItem(scan_added_item_data)

                scan_added.append(scan_added_item)

        _jira_update = d.pop("jira_update", UNSET)
        jira_update: list[NotificationsJiraUpdateItem] | Unset = UNSET
        if _jira_update is not UNSET:
            jira_update = []
            for jira_update_item_data in _jira_update:
                jira_update_item = NotificationsJiraUpdateItem(jira_update_item_data)

                jira_update.append(jira_update_item)

        _upcoming_engagement = d.pop("upcoming_engagement", UNSET)
        upcoming_engagement: list[NotificationsUpcomingEngagementItem] | Unset = UNSET
        if _upcoming_engagement is not UNSET:
            upcoming_engagement = []
            for upcoming_engagement_item_data in _upcoming_engagement:
                upcoming_engagement_item = NotificationsUpcomingEngagementItem(
                    upcoming_engagement_item_data
                )

                upcoming_engagement.append(upcoming_engagement_item)

        _stale_engagement = d.pop("stale_engagement", UNSET)
        stale_engagement: list[NotificationsStaleEngagementItem] | Unset = UNSET
        if _stale_engagement is not UNSET:
            stale_engagement = []
            for stale_engagement_item_data in _stale_engagement:
                stale_engagement_item = NotificationsStaleEngagementItem(stale_engagement_item_data)

                stale_engagement.append(stale_engagement_item)

        _auto_close_engagement = d.pop("auto_close_engagement", UNSET)
        auto_close_engagement: list[NotificationsAutoCloseEngagementItem] | Unset = UNSET
        if _auto_close_engagement is not UNSET:
            auto_close_engagement = []
            for auto_close_engagement_item_data in _auto_close_engagement:
                auto_close_engagement_item = NotificationsAutoCloseEngagementItem(
                    auto_close_engagement_item_data
                )

                auto_close_engagement.append(auto_close_engagement_item)

        _close_engagement = d.pop("close_engagement", UNSET)
        close_engagement: list[NotificationsCloseEngagementItem] | Unset = UNSET
        if _close_engagement is not UNSET:
            close_engagement = []
            for close_engagement_item_data in _close_engagement:
                close_engagement_item = NotificationsCloseEngagementItem(close_engagement_item_data)

                close_engagement.append(close_engagement_item)

        _user_mentioned = d.pop("user_mentioned", UNSET)
        user_mentioned: list[NotificationsUserMentionedItem] | Unset = UNSET
        if _user_mentioned is not UNSET:
            user_mentioned = []
            for user_mentioned_item_data in _user_mentioned:
                user_mentioned_item = NotificationsUserMentionedItem(user_mentioned_item_data)

                user_mentioned.append(user_mentioned_item)

        _code_review = d.pop("code_review", UNSET)
        code_review: list[NotificationsCodeReviewItem] | Unset = UNSET
        if _code_review is not UNSET:
            code_review = []
            for code_review_item_data in _code_review:
                code_review_item = NotificationsCodeReviewItem(code_review_item_data)

                code_review.append(code_review_item)

        _review_requested = d.pop("review_requested", UNSET)
        review_requested: list[NotificationsReviewRequestedItem] | Unset = UNSET
        if _review_requested is not UNSET:
            review_requested = []
            for review_requested_item_data in _review_requested:
                review_requested_item = NotificationsReviewRequestedItem(review_requested_item_data)

                review_requested.append(review_requested_item)

        _other = d.pop("other", UNSET)
        other: list[NotificationsOtherItem] | Unset = UNSET
        if _other is not UNSET:
            other = []
            for other_item_data in _other:
                other_item = NotificationsOtherItem(other_item_data)

                other.append(other_item)

        _sla_breach = d.pop("sla_breach", UNSET)
        sla_breach: list[NotificationsSlaBreachItem] | Unset = UNSET
        if _sla_breach is not UNSET:
            sla_breach = []
            for sla_breach_item_data in _sla_breach:
                sla_breach_item = NotificationsSlaBreachItem(sla_breach_item_data)

                sla_breach.append(sla_breach_item)

        _sla_breach_combined = d.pop("sla_breach_combined", UNSET)
        sla_breach_combined: list[NotificationsSlaBreachCombinedItem] | Unset = UNSET
        if _sla_breach_combined is not UNSET:
            sla_breach_combined = []
            for sla_breach_combined_item_data in _sla_breach_combined:
                sla_breach_combined_item = NotificationsSlaBreachCombinedItem(
                    sla_breach_combined_item_data
                )

                sla_breach_combined.append(sla_breach_combined_item)

        _risk_acceptance_expiration = d.pop("risk_acceptance_expiration", UNSET)
        risk_acceptance_expiration: list[NotificationsRiskAcceptanceExpirationItem] | Unset = UNSET
        if _risk_acceptance_expiration is not UNSET:
            risk_acceptance_expiration = []
            for risk_acceptance_expiration_item_data in _risk_acceptance_expiration:
                risk_acceptance_expiration_item = NotificationsRiskAcceptanceExpirationItem(
                    risk_acceptance_expiration_item_data
                )

                risk_acceptance_expiration.append(risk_acceptance_expiration_item)

        template = d.pop("template", UNSET)

        _scan_added_empty = d.pop("scan_added_empty", UNSET)
        scan_added_empty: NotificationsScanAddedEmpty | Unset
        if isinstance(_scan_added_empty, Unset):
            scan_added_empty = UNSET
        else:
            scan_added_empty = NotificationsScanAddedEmpty(_scan_added_empty)

        _prefetch = d.pop("prefetch", UNSET)
        prefetch: NotificationsPrefetch | Unset
        if isinstance(_prefetch, Unset):
            prefetch = UNSET
        else:
            prefetch = NotificationsPrefetch.from_dict(_prefetch)

        notifications = cls(
            id=id,
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
            prefetch=prefetch,
        )

        notifications.additional_properties = d
        return notifications

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
