from enum import Enum


class CredentialAuthentication(str, Enum):
    FORM = "Form"
    SSO = "SSO"

    def __str__(self) -> str:
        return str(self.value)
