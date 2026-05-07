from enum import Enum


class EndpointsListOItem(str, Enum):
    ACTIVE_FINDING_COUNT = "active_finding_count"
    HOST = "host"
    ID = "id"
    PRODUCT = "product"
    VALUE_0 = "-active_finding_count"
    VALUE_1 = "-host"
    VALUE_2 = "-id"
    VALUE_3 = "-product"

    def __str__(self) -> str:
        return str(self.value)
