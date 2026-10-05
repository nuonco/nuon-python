from enum import StrEnum


class AppInstallAppBranchGroupAssignmentSource(StrEnum):
    INSTALL_APP_BRANCH_GROUP_ASSIGNMENT_SOURCE_DEFAULT = "default"
    INSTALL_APP_BRANCH_GROUP_ASSIGNMENT_SOURCE_EXPLICIT = "explicit"
    INSTALL_APP_BRANCH_GROUP_ASSIGNMENT_SOURCE_LABELS = "labels"

    def __str__(self) -> str:
        return str(self.value)
