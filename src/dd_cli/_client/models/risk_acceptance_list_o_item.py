from enum import Enum


class RiskAcceptanceListOItem(str, Enum):
    NAME = "name"
    VALUE_0 = "-name"

    def __str__(self) -> str:
        return str(self.value)
