from enum import Enum


class ProductMembersRetrievePrefetchItem(str, Enum):
    PRODUCT = "product"
    ROLE = "role"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
