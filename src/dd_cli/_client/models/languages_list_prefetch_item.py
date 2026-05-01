from enum import Enum


class LanguagesListPrefetchItem(str, Enum):
    LANGUAGE = "language"
    PRODUCT = "product"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
