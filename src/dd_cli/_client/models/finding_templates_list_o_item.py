from enum import Enum


class FindingTemplatesListOItem(str, Enum):
    CWE = "cwe"
    TITLE = "title"
    VALUE_0 = "-cwe"
    VALUE_1 = "-title"

    def __str__(self) -> str:
        return str(self.value)
