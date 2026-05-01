from enum import Enum


class DojoGroupMembersRetrievePrefetchItem(str, Enum):
    GROUP = "group"
    ROLE = "role"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
