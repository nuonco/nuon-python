from enum import StrEnum


class AppWorkflowStepExecutionType(StrEnum):
    APPROVAL = "approval"
    HIDDEN = "hidden"
    SKIPPED = "skipped"
    SYSTEM = "system"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
