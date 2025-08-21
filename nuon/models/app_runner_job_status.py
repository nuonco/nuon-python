from enum import Enum


class AppRunnerJobStatus(str, Enum):
    AVAILABLE = "available"
    CANCELLED = "cancelled"
    FAILED = "failed"
    FINISHED = "finished"
    IN_PROGRESS = "in-progress"
    NOT_ATTEMPTED = "not-attempted"
    QUEUED = "queued"
    TIMED_OUT = "timed-out"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
