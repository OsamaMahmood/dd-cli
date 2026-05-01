from enum import Enum


class EngagementsListOItem(str, Enum):
    CREATED = "created"
    LEAD = "lead"
    NAME = "name"
    STATUS = "status"
    TARGET_END = "target_end"
    TARGET_START = "target_start"
    UPDATED = "updated"
    VALUE_0 = "-created"
    VALUE_1 = "-lead"
    VALUE_2 = "-name"
    VALUE_3 = "-status"
    VALUE_4 = "-target_end"
    VALUE_5 = "-target_start"
    VALUE_6 = "-updated"
    VALUE_7 = "-version"
    VERSION = "version"

    def __str__(self) -> str:
        return str(self.value)
