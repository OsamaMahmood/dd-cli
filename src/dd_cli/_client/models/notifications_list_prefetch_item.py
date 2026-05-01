from enum import Enum


class NotificationsListPrefetchItem(str, Enum):
    PRODUCT = "product"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
