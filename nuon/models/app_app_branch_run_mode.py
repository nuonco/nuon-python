from enum import StrEnum


class AppAppBranchRunMode(StrEnum):
    APP_BRANCH_RUN_MODE_GITHUB_LABEL = "on_github_label"
    APP_BRANCH_RUN_MODE_MANUAL_ONLY = "manual_only"
    APP_BRANCH_RUN_MODE_PUSH = "push"
    APP_BRANCH_RUN_MODE_TAG_PREFIX = "on_tag"

    def __str__(self) -> str:
        return str(self.value)
