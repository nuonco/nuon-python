from enum import StrEnum


class AppAppBranchRunTrigger(StrEnum):
    GITHUB_LABEL = "github_label"
    MANUAL = "manual"
    ONBOARDING = "onboarding"
    PULL_REQUEST = "pull_request"
    PUSH = "push"
    TAG = "tag"

    def __str__(self) -> str:
        return str(self.value)
