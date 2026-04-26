from enum import Enum


class AppWorkflowRunType(str, Enum):
    INITIAL = "initial"
    RESUME = "resume"
    RETRY = "retry"
    SKIP = "skip"

    def __str__(self) -> str:
        return str(self.value)
