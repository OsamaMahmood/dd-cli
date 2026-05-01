from enum import Enum


class EngagementPresetsListPrefetchItem(str, Enum):
    NETWORK_LOCATIONS = "network_locations"
    PRODUCT = "product"
    TEST_TYPE = "test_type"

    def __str__(self) -> str:
        return str(self.value)
