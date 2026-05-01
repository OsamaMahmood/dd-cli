from enum import Enum


class DojoGroupsRetrievePrefetchItem(str, Enum):
    PRODUCT_GROUPS = "product_groups"
    PRODUCT_TYPE_GROUPS = "product_type_groups"
    USERS = "users"

    def __str__(self) -> str:
        return str(self.value)
