from enum import Enum


class AssetsListOriginItem(str, Enum):
    CONTRACTOR = "contractor"
    INTERNAL = "internal"
    OPEN_SOURCE = "open source"
    OUTSOURCED = "outsourced"
    PURCHASED = "purchased"
    THIRD_PARTY_LIBRARY = "third party library"

    def __str__(self) -> str:
        return str(self.value)
