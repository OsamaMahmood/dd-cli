from enum import Enum


class TestImportsListOItem(str, Enum):
    BRANCH_TAG = "branch_tag"
    BUILD_ID = "build_id"
    COMMIT_HASH = "commit_hash"
    CREATED = "created"
    ID = "id"
    MODIFIED = "modified"
    VALUE_0 = "-branch_tag"
    VALUE_1 = "-build_id"
    VALUE_2 = "-commit_hash"
    VALUE_3 = "-created"
    VALUE_4 = "-id"
    VALUE_5 = "-modified"
    VALUE_6 = "-version"
    VERSION = "version"

    def __str__(self) -> str:
        return str(self.value)
