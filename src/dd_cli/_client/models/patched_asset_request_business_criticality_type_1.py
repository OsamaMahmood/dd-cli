from enum import Enum


class PatchedAssetRequestBusinessCriticalityType1(str, Enum):
    HIGH = "high"
    LOW = "low"
    MEDIUM = "medium"
    NONE = "none"
    VALUE_6 = ""
    VERY_HIGH = "very high"
    VERY_LOW = "very low"

    def __str__(self) -> str:
        return str(self.value)
