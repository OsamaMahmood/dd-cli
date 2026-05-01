from enum import Enum


class ProductRequestOriginType2Type1(str, Enum):
    CONTRACTOR = "contractor"
    INTERNAL = "internal"
    OPEN_SOURCE = "open source"
    OUTSOURCED = "outsourced"
    PURCHASED = "purchased"
    THIRD_PARTY_LIBRARY = "third party library"
    VALUE_6 = ""

    def __str__(self) -> str:
        return str(self.value)
