from enum import StrEnum


class AppRunnerJobExecutionStatus(StrEnum):
    CANCELLED = "cancelled"
    CLEANING_UP = "cleaning-up"
    FAILED = "failed"
    FINISHED = "finished"
    INITIALIZING = "initializing"
    IN_PROGRESS = "in-progress"
    NOT_ATTEMPTED = "not-attempted"
    PENDING = "pending"
    TIMED_OUT = "timed-out"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
