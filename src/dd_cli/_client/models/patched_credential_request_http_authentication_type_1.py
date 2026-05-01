from enum import Enum


class PatchedCredentialRequestHttpAuthenticationType1(str, Enum):
    BASIC = "Basic"
    NTLM = "NTLM"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
