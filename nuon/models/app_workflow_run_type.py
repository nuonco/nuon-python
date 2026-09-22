from enum import StrEnum


class AppWorkflowRunType(StrEnum):
    INITIAL = "initial"
    RESUME = "resume"
    RETRY = "retry"
    SKIP = "skip"

    def __str__(self) -> str:
        return str(self.value)
