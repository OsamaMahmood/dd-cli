from enum import Enum


class AssetRequestPlatformType3Type1(str, Enum):
    DESKTOP = "desktop"
    IOT = "iot"
    MOBILE = "mobile"
    VALUE_5 = ""
    WEB = "web"
    WEB_SERVICE = "web service"

    def __str__(self) -> str:
        return str(self.value)
