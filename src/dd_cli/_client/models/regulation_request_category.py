from enum import Enum


class RegulationRequestCategory(str, Enum):
    CORPORATE = "corporate"
    EDUCATION = "education"
    FINANCE = "finance"
    GOVERNMENT = "government"
    MEDICAL = "medical"
    OTHER = "other"
    PRIVACY = "privacy"
    SECURITY = "security"

    def __str__(self) -> str:
        return str(self.value)
