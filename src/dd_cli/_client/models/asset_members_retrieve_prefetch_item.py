from enum import Enum


class AssetMembersRetrievePrefetchItem(str, Enum):
    PRODUCT = "product"
    ROLE = "role"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
