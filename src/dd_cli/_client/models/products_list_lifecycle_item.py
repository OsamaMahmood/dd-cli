from enum import Enum


class ProductsListLifecycleItem(str, Enum):
    CONSTRUCTION = "construction"
    PRODUCTION = "production"
    RETIREMENT = "retirement"

    def __str__(self) -> str:
        return str(self.value)
