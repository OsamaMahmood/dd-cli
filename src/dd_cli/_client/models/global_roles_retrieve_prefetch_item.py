from enum import Enum


class GlobalRolesRetrievePrefetchItem(str, Enum):
    GROUP = "group"
    ROLE = "role"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
