from enum import Enum


class ToolConfigurationsListPrefetchItem(str, Enum):
    TOOL_TYPE = "tool_type"

    def __str__(self) -> str:
        return str(self.value)
