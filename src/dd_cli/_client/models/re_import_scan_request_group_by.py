from enum import Enum


class ReImportScanRequestGroupBy(str, Enum):
    COMPONENT_NAME = "component_name"
    COMPONENT_NAMECOMPONENT_VERSION = "component_name+component_version"
    COMPONENT_NAMECOMPONENT_VERSIONFILE_PATH = "component_name+component_version+file_path"
    FILE_PATH = "file_path"
    FINDING_TITLE = "finding_title"
    VULN_ID_FROM_TOOL = "vuln_id_from_tool"

    def __str__(self) -> str:
        return str(self.value)
