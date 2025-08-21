from enum import Enum


class AppWorkflowStepResponseType(str, Enum):
    APPROVE = "approve"
    AUTO_APPROVE = "auto-approve"
    DENY = "deny"
    RETRY = "retry"
    SKIP = "skip"

    def __str__(self) -> str:
        return str(self.value)
