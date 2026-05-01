from enum import Enum


class CredentialsListPrefetchItem(str, Enum):
    ENVIRONMENT = "environment"
    NOTES = "notes"

    def __str__(self) -> str:
        return str(self.value)
