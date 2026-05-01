from enum import Enum


class NotificationWebhooksListStatus(str, Enum):
    ACTIVE = "active"
    ACTIVE_TMP = "active_tmp"
    INACTIVE_PERMANENT = "inactive_permanent"
    INACTIVE_TMP = "inactive_tmp"

    def __str__(self) -> str:
        return str(self.value)
