from enum import Enum


class TechnologiesRetrievePrefetchItem(str, Enum):
    PRODUCT = "product"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
