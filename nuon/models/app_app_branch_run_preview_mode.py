from enum import StrEnum


class AppAppBranchRunPreviewMode(StrEnum):
    APPLY = "apply"
    BUILD_ONLY = "build-only"
    PLAN_ONLY = "plan-only"

    def __str__(self) -> str:
        return str(self.value)
