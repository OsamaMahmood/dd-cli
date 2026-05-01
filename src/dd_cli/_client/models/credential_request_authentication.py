from enum import Enum


class CredentialRequestAuthentication(str, Enum):
    FORM = "Form"
    SSO = "SSO"

    def __str__(self) -> str:
        return str(self.value)
