from enum import StrEnum


class AppAppBranchRunMode(StrEnum):
    MANUAL_ONLY = "manual_only"
    ON_GITHUB_LABEL = "on_github_label"
    ON_TAG = "on_tag"
    PUSH = "push"

    def __str__(self) -> str:
        return str(self.value)
