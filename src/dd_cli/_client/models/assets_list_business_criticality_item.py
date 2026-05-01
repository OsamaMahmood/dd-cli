from enum import Enum


class AssetsListBusinessCriticalityItem(str, Enum):
    HIGH = "high"
    LOW = "low"
    MEDIUM = "medium"
    NONE = "none"
    VERY_HIGH = "very high"
    VERY_LOW = "very low"

    def __str__(self) -> str:
        return str(self.value)
