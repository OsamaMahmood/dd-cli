from enum import Enum


class SystemSettingsRequestJiraMinimumSeverityType3Type1(str, Enum):
    CRITICAL = "Critical"
    HIGH = "High"
    INFO = "Info"
    LOW = "Low"
    MEDIUM = "Medium"
    VALUE_5 = ""

    def __str__(self) -> str:
        return str(self.value)
