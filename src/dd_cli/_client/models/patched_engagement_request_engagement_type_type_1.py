from enum import Enum


class PatchedEngagementRequestEngagementTypeType1(str, Enum):
    CICD = "CI/CD"
    INTERACTIVE = "Interactive"

    def __str__(self) -> str:
        return str(self.value)
