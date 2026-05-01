from enum import Enum


class AssetGroupsRetrievePrefetchItem(str, Enum):
    GROUP = "group"
    PRODUCT = "product"
    ROLE = "role"

    def __str__(self) -> str:
        return str(self.value)
