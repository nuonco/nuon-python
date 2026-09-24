from enum import StrEnum


class AppAppBranchRunPreviewMode(StrEnum):
    APP_BRANCH_RUN_PREVIEW_MODE_APPLY = "apply"
    APP_BRANCH_RUN_PREVIEW_MODE_BUILD_ONLY = "build-only"
    APP_BRANCH_RUN_PREVIEW_MODE_NONE = "none"
    APP_BRANCH_RUN_PREVIEW_MODE_PLAN_ONLY = "plan-only"

    def __str__(self) -> str:
        return str(self.value)
