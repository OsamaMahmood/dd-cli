from enum import Enum


class RiskAcceptanceListOItem(str, Enum):
    CREATED = "created"
    NAME = "name"
    UPDATED = "updated"
    VALUE_0 = "-created"
    VALUE_1 = "-name"
    VALUE_2 = "-updated"

    def __str__(self) -> str:
        return str(self.value)
