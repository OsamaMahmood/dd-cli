from enum import Enum


class ToolProductSettingsRetrievePrefetchItem(str, Enum):
    NOTES = "notes"
    PRODUCT = "product"
    TOOL_CONFIGURATION = "tool_configuration"

    def __str__(self) -> str:
        return str(self.value)
