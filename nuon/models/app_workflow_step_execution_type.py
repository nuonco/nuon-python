from enum import StrEnum


class AppWorkflowStepExecutionType(StrEnum):
    WORKFLOW_STEP_EXECUTION_TYPE_APPROVAL = "approval"
    WORKFLOW_STEP_EXECUTION_TYPE_HIDDEN = "hidden"
    WORKFLOW_STEP_EXECUTION_TYPE_SKIPPED = "skipped"
    WORKFLOW_STEP_EXECUTION_TYPE_SYSTEM = "system"
    WORKFLOW_STEP_EXECUTION_TYPE_USER = "user"

    def __str__(self) -> str:
        return str(self.value)
