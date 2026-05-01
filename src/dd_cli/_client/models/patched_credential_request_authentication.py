from enum import Enum


class PatchedCredentialRequestAuthentication(str, Enum):
    FORM = "Form"
    SSO = "SSO"

    def __str__(self) -> str:
        return str(self.value)
