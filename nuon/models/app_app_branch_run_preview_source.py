from enum import StrEnum


class AppAppBranchRunPreviewSource(StrEnum):
    BRANCH = "branch"
    COMMIT = "commit"
    LOCAL = "local"
    PR = "pr"

    def __str__(self) -> str:
        return str(self.value)
