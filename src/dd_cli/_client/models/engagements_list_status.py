from enum import Enum


class EngagementsListStatus(str, Enum):
    BLOCKED = "Blocked"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"
    IN_PROGRESS = "In Progress"
    NOT_STARTED = "Not Started"
    ON_HOLD = "On Hold"
    WAITING_FOR_RESOURCE = "Waiting for Resource"

    def __str__(self) -> str:
        return str(self.value)
