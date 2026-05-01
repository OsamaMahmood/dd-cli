from enum import Enum


class PatchedToolConfigurationRequestAuthenticationTypeType3Type1(str, Enum):
    API = "API"
    PASSWORD = "Password"
    SSH = "SSH"
    VALUE_3 = ""

    def __str__(self) -> str:
        return str(self.value)
