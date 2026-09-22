from enum import StrEnum


class AppInstallActionWorkflowRunStepStatus(StrEnum):
    ERROR = "error"
    FINISHED = "finished"
    IN_PROGRESS = "in-progress"
    PENDING = "pending"
    TIMED_OUT = "timed-out"

    def __str__(self) -> str:
        return str(self.value)
