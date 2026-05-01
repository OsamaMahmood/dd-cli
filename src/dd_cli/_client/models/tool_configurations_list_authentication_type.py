from enum import Enum


class ToolConfigurationsListAuthenticationType(str, Enum):
    API = "API"
    PASSWORD = "Password"
    SSH = "SSH"

    def __str__(self) -> str:
        return str(self.value)
