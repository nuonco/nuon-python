from enum import StrEnum


class AppAppBranchRunTrigger(StrEnum):
    APP_BRANCH_RUN_TRIGGER_GITHUB_LABEL = "github_label"
    APP_BRANCH_RUN_TRIGGER_MANUAL = "manual"
    APP_BRANCH_RUN_TRIGGER_ONBOARDING = "onboarding"
    APP_BRANCH_RUN_TRIGGER_PULL_REQUEST = "pull_request"
    APP_BRANCH_RUN_TRIGGER_PUSH = "push"
    APP_BRANCH_RUN_TRIGGER_TAG = "tag"

    def __str__(self) -> str:
        return str(self.value)
