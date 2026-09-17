from enum import StrEnum


class AppAppBranchRunMode(StrEnum):
    MANUAL_ONLY = "manual_only"
    ON_GITHUB_LABEL = "on_github_label"
    ON_TAG_PREFIX = "on_tag_prefix"
    PUSH = "push"

    def __str__(self) -> str:
        return str(self.value)
