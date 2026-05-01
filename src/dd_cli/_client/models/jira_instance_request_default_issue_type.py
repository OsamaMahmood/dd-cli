from enum import Enum


class JIRAInstanceRequestDefaultIssueType(str, Enum):
    BUG = "Bug"
    EPIC = "Epic"
    SECURITY = "Security"
    SPIKE = "Spike"
    STORY = "Story"
    TASK = "Task"

    def __str__(self) -> str:
        return str(self.value)
