from enum import Enum


class PatchedProductRequestLifecycleType1(str, Enum):
    CONSTRUCTION = "construction"
    PRODUCTION = "production"
    RETIREMENT = "retirement"
    VALUE_3 = ""

    def __str__(self) -> str:
        return str(self.value)
