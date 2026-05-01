from enum import Enum


class JiraProductConfigurationsListPrefetchItem(str, Enum):
    ENGAGEMENT = "engagement"
    JIRA_INSTANCE = "jira_instance"
    PRODUCT = "product"

    def __str__(self) -> str:
        return str(self.value)
