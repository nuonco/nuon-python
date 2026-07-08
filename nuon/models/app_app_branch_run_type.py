from enum import Enum


class AppAppBranchRunType(str, Enum):
    GIT_PREVIEW_RUN = "git-preview-run"
    GIT_RUN = "git-run"
    MANUAL_RUN = "manual-run"

    def __str__(self) -> str:
        return str(self.value)
