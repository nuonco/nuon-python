from enum import Enum


class AppRunnerJobOperationType(str, Enum):
    APPLY_PLAN = "apply-plan"
    BUILD = "build"
    CREATE_APPLY_PLAN = "create-apply-plan"
    CREATE_TEARDOWN_PLAN = "create-teardown-plan"
    EXEC = "exec"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
