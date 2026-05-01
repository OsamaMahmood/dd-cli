from enum import Enum


class NotificationsRetrievePrefetchItem(str, Enum):
    PRODUCT = "product"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
