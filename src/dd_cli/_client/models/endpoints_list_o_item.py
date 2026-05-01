from enum import Enum


class EndpointsListOItem(str, Enum):
    HOST = "host"
    ID = "id"
    PRODUCT = "product"
    VALUE_0 = "-host"
    VALUE_1 = "-id"
    VALUE_2 = "-product"

    def __str__(self) -> str:
        return str(self.value)
