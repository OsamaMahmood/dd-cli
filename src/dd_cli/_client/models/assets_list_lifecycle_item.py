from enum import Enum


class AssetsListLifecycleItem(str, Enum):
    CONSTRUCTION = "construction"
    PRODUCTION = "production"
    RETIREMENT = "retirement"

    def __str__(self) -> str:
        return str(self.value)
