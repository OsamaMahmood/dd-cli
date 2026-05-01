from enum import Enum


class ProductsListPlatformItem(str, Enum):
    DESKTOP = "desktop"
    IOT = "iot"
    MOBILE = "mobile"
    WEB = "web"
    WEB_SERVICE = "web service"

    def __str__(self) -> str:
        return str(self.value)
