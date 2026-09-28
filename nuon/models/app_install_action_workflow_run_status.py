from enum import StrEnum


class AppInstallActionWorkflowRunStatus(StrEnum):
    INSTALL_ACTION_RUN_STATUS_CANCELLED = "cancelled"
    INSTALL_ACTION_RUN_STATUS_ERROR = "error"
    INSTALL_ACTION_RUN_STATUS_FINISHED = "finished"
    INSTALL_ACTION_RUN_STATUS_IN_PROGRESS = "in-progress"
    INSTALL_ACTION_RUN_STATUS_QUEUED = "queued"
    INSTALL_ACTION_RUN_STATUS_RETRIED = "retried"
    INSTALL_ACTION_RUN_STATUS_TIMED_OUT = "timed-out"
    INSTALL_ACTION_RUN_STATUS_UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
