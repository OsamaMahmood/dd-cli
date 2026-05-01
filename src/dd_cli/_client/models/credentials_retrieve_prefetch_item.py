from enum import Enum


class CredentialsRetrievePrefetchItem(str, Enum):
    ENVIRONMENT = "environment"
    NOTES = "notes"

    def __str__(self) -> str:
        return str(self.value)
