from enum import StrEnum


class AppRunnerJobExecutionStatus(StrEnum):
    RUNNER_JOB_EXECUTION_STATUS_CANCELLED = "cancelled"
    RUNNER_JOB_EXECUTION_STATUS_CLEANING_UP = "cleaning-up"
    RUNNER_JOB_EXECUTION_STATUS_FAILED = "failed"
    RUNNER_JOB_EXECUTION_STATUS_FINISHED = "finished"
    RUNNER_JOB_EXECUTION_STATUS_INITIALIZING = "initializing"
    RUNNER_JOB_EXECUTION_STATUS_IN_PROGRESS = "in-progress"
    RUNNER_JOB_EXECUTION_STATUS_NOT_ATTEMPTED = "not-attempted"
    RUNNER_JOB_EXECUTION_STATUS_PENDING = "pending"
    RUNNER_JOB_EXECUTION_STATUS_TIMED_OUT = "timed-out"
    RUNNER_JOB_EXECUTION_STATUS_UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
