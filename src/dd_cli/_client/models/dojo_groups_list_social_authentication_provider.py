from enum import Enum


class DojoGroupsListSocialAuthenticationProvider(str, Enum):
    AZUREAD = "AzureAD"
    REMOTE = "Remote"

    def __str__(self) -> str:
        return str(self.value)
