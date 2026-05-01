from enum import Enum


class OrganizationsListPrefetchItem(str, Enum):
    AUTHORIZATION_GROUPS = "authorization_groups"
    MEMBERS = "members"

    def __str__(self) -> str:
        return str(self.value)
