from enum import Enum


class NotificationsScanAddedEmpty(str, Enum):
    ALERT = "alert"
    MAIL = "mail"
    MSTEAMS = "msteams"
    SLACK = "slack"
    VALUE_5 = ""
    WEBHOOKS = "webhooks"

    def __str__(self) -> str:
        return str(self.value)
