from enum import Enum


class AppInstallActionWorkflowRunStatus(str, Enum):
    CANCELLED = "cancelled"
    ERROR = "error"
    FINISHED = "finished"
    IN_PROGRESS = "in-progress"
    QUEUED = "queued"
    TIMED_OUT = "timed-out"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
