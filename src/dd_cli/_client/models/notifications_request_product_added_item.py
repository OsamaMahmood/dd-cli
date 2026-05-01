from enum import Enum


class NotificationsRequestProductAddedItem(str, Enum):
    ALERT = "alert"
    MAIL = "mail"
    MSTEAMS = "msteams"
    SLACK = "slack"
    WEBHOOKS = "webhooks"

    def __str__(self) -> str:
        return str(self.value)
