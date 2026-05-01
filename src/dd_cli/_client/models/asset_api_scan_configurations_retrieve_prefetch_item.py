from enum import Enum


class AssetApiScanConfigurationsRetrievePrefetchItem(str, Enum):
    PRODUCT = "product"
    TOOL_CONFIGURATION = "tool_configuration"

    def __str__(self) -> str:
        return str(self.value)
