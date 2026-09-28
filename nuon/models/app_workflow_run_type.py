from enum import StrEnum


class AppWorkflowRunType(StrEnum):
    WORKFLOW_RUN_TYPE_INITIAL = "initial"
    WORKFLOW_RUN_TYPE_RESUME = "resume"
    WORKFLOW_RUN_TYPE_RETRY = "retry"
    WORKFLOW_RUN_TYPE_SKIP = "skip"

    def __str__(self) -> str:
        return str(self.value)
