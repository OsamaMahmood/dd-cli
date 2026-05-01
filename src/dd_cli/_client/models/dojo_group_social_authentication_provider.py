from enum import Enum


class DojoGroupSocialAuthenticationProvider(str, Enum):
    AZUREAD = "AzureAD"
    REMOTE = "Remote"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
