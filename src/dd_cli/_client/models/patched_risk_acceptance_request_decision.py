from enum import Enum


class PatchedRiskAcceptanceRequestDecision(str, Enum):
    A = "A"
    F = "F"
    M = "M"
    T = "T"
    V = "V"

    def __str__(self) -> str:
        return str(self.value)
