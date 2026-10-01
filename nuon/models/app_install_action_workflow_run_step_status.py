from enum import StrEnum


class AppInstallActionWorkflowRunStepStatus(StrEnum):
    INSTALL_ACTION_WORKFLOW_RUN_STEP_STATUS_ERROR = "error"
    INSTALL_ACTION_WORKFLOW_RUN_STEP_STATUS_FINISHED = "finished"
    INSTALL_ACTION_WORKFLOW_RUN_STEP_STATUS_IN_PROGRESS = "in-progress"
    INSTALL_ACTION_WORKFLOW_RUN_STEP_STATUS_PENDING = "pending"
    INSTALL_ACTION_WORKFLOW_RUN_STEP_STATUS_TIMED_OUT = "timed-out"

    def __str__(self) -> str:
        return str(self.value)
