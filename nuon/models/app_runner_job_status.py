from enum import StrEnum


class AppRunnerJobStatus(StrEnum):
    RUNNER_JOB_STATUS_AVAILABLE = "available"
    RUNNER_JOB_STATUS_CANCELLED = "cancelled"
    RUNNER_JOB_STATUS_FAILED = "failed"
    RUNNER_JOB_STATUS_FINISHED = "finished"
    RUNNER_JOB_STATUS_IN_PROGRESS = "in-progress"
    RUNNER_JOB_STATUS_NOT_ATTEMPTED = "not-attempted"
    RUNNER_JOB_STATUS_QUEUED = "queued"
    RUNNER_JOB_STATUS_TIMED_OUT = "timed-out"
    RUNNER_JOB_STATUS_UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
