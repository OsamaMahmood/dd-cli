from enum import Enum


class TestImportFindingActionActionType3Type1(str, Enum):
    C = "C"
    N = "N"
    R = "R"
    U = "U"
    VALUE_4 = ""

    def __str__(self) -> str:
        return str(self.value)
