from enum import Enum


class ProductTypeMembersListPrefetchItem(str, Enum):
    PRODUCT_TYPE = "product_type"
    ROLE = "role"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
