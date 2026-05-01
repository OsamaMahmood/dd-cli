from enum import Enum


class ImportScanMinimumSeverity(str, Enum):
    CRITICAL = "Critical"
    HIGH = "High"
    INFO = "Info"
    LOW = "Low"
    MEDIUM = "Medium"

    def __str__(self) -> str:
        return str(self.value)
