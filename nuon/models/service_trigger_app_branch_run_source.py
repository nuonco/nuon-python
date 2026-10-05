from enum import StrEnum


class ServiceTriggerAppBranchRunSource(StrEnum):
    TRIGGER_APP_BRANCH_RUN_SOURCE_COMMIT = "commit"
    TRIGGER_APP_BRANCH_RUN_SOURCE_PR = "pr"
    TRIGGER_APP_BRANCH_RUN_SOURCE_TAG = "tag"

    def __str__(self) -> str:
        return str(self.value)
