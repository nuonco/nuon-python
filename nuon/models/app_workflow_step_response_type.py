from enum import Enum


class AppWorkflowStepResponseType(str, Enum):
    APPROVE = "approve"
    AUTO_APPROVE = "auto-approve"
    DENY = "deny"
    DENY_SKIP_CURRENT = "deny-skip-current"
    DENY_SKIP_CURRENT_AND_DEPENDENTS = "deny-skip-current-and-dependents"
    RETRY = "retry"

    def __str__(self) -> str:
        return str(self.value)
