from enum import Enum


class QuestionnaireAnsweredQuestionnairesListPrefetchItem(str, Enum):
    ASSIGNEE = "assignee"
    ENGAGEMENT = "engagement"
    RESPONDER = "responder"
    SURVEY = "survey"

    def __str__(self) -> str:
        return str(self.value)
