from enum import Enum


class ToolProductSettingsListPrefetchItem(str, Enum):
    NOTES = "notes"
    PRODUCT = "product"
    TOOL_CONFIGURATION = "tool_configuration"

    def __str__(self) -> str:
        return str(self.value)
