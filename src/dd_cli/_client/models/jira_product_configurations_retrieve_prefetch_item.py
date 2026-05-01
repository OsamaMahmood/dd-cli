from enum import Enum


class JiraProductConfigurationsRetrievePrefetchItem(str, Enum):
    ENGAGEMENT = "engagement"
    JIRA_INSTANCE = "jira_instance"
    PRODUCT = "product"

    def __str__(self) -> str:
        return str(self.value)
