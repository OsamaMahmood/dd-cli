from enum import Enum


class EngagementRequestEngagementTypeType1(str, Enum):
    CICD = "CI/CD"
    INTERACTIVE = "Interactive"

    def __str__(self) -> str:
        return str(self.value)
