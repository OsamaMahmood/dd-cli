from enum import Enum


class TestsListOItem(str, Enum):
    API_SCAN_CONFIGURATION = "api_scan_configuration"
    BRANCH_TAG = "branch_tag"
    BUILD_ID = "build_id"
    COMMIT_HASH = "commit_hash"
    CREATED = "created"
    ENGAGEMENT = "engagement"
    LEAD = "lead"
    TARGET_END = "target_end"
    TARGET_START = "target_start"
    TEST_TYPE = "test_type"
    TITLE = "title"
    UPDATED = "updated"
    VALUE_0 = "-api_scan_configuration"
    VALUE_1 = "-branch_tag"
    VALUE_10 = "-title"
    VALUE_11 = "-updated"
    VALUE_12 = "-version"
    VALUE_2 = "-build_id"
    VALUE_3 = "-commit_hash"
    VALUE_4 = "-created"
    VALUE_5 = "-engagement"
    VALUE_6 = "-lead"
    VALUE_7 = "-target_end"
    VALUE_8 = "-target_start"
    VALUE_9 = "-test_type"
    VERSION = "version"

    def __str__(self) -> str:
        return str(self.value)
