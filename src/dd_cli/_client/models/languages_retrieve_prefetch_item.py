from enum import Enum


class LanguagesRetrievePrefetchItem(str, Enum):
    LANGUAGE = "language"
    PRODUCT = "product"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
