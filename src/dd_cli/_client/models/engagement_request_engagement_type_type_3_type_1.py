from enum import Enum


class EngagementRequestEngagementTypeType3Type1(str, Enum):
    CICD = "CI/CD"
    INTERACTIVE = "Interactive"

    def __str__(self) -> str:
        return str(self.value)
