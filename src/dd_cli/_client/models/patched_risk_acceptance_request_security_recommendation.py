from enum import Enum


class PatchedRiskAcceptanceRequestSecurityRecommendation(str, Enum):
    A = "A"
    F = "F"
    M = "M"
    T = "T"
    V = "V"

    def __str__(self) -> str:
        return str(self.value)
