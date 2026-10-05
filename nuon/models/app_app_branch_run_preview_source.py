from enum import StrEnum


class AppAppBranchRunPreviewSource(StrEnum):
    APP_BRANCH_RUN_PREVIEW_SOURCE_BRANCH = "branch"
    APP_BRANCH_RUN_PREVIEW_SOURCE_COMMIT = "commit"
    APP_BRANCH_RUN_PREVIEW_SOURCE_LOCAL = "local"
    APP_BRANCH_RUN_PREVIEW_SOURCE_PR = "pr"

    def __str__(self) -> str:
        return str(self.value)
