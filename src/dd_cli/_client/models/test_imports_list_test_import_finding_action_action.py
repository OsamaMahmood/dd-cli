from enum import Enum


class TestImportsListTestImportFindingActionAction(str, Enum):
    C = "C"
    N = "N"
    R = "R"
    U = "U"

    def __str__(self) -> str:
        return str(self.value)
