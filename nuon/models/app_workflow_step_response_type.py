from enum import StrEnum


class AppWorkflowStepResponseType(StrEnum):
    WORKFLOW_STEP_APPROVAL_RESPONSE_TYPE_APPROVE = "approve"
    WORKFLOW_STEP_APPROVAL_RESPONSE_TYPE_AUTO_APPROVE = "auto-approve"
    WORKFLOW_STEP_APPROVAL_RESPONSE_TYPE_DENY = "deny"
    WORKFLOW_STEP_APPROVAL_RESPONSE_TYPE_RETRY_PLAN = "retry"
    WORKFLOW_STEP_APPROVAL_RESPONSE_TYPE_SKIP_CURRENT = "deny-skip-current"
    WORKFLOW_STEP_APPROVAL_RESPONSE_TYPE_SKIP_CURRENT_AND_DEPENDENTS = "deny-skip-current-and-dependents"

    def __str__(self) -> str:
        return str(self.value)
