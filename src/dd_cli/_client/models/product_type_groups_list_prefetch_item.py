from enum import Enum


class ProductTypeGroupsListPrefetchItem(str, Enum):
    GROUP = "group"
    PRODUCT_TYPE = "product_type"
    ROLE = "role"

    def __str__(self) -> str:
        return str(self.value)
