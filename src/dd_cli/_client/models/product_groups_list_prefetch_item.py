from enum import Enum


class ProductGroupsListPrefetchItem(str, Enum):
    GROUP = "group"
    PRODUCT = "product"
    ROLE = "role"

    def __str__(self) -> str:
        return str(self.value)
