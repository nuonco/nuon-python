from enum import StrEnum


class AppAppBranchRunType(StrEnum):
    APP_BRANCH_RUN_TYPE_GIT = "git-run"
    APP_BRANCH_RUN_TYPE_GIT_PREVIEW = "git-preview-run"
    APP_BRANCH_RUN_TYPE_MANUAL = "manual-run"

    def __str__(self) -> str:
        return str(self.value)
