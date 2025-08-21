from enum import Enum


class AppWorkflowStepExecutionType(str, Enum):
    APPROVAL = "approval"
    HIDDEN = "hidden"
    SKIPPED = "skipped"
    SYSTEM = "system"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
