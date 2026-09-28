from enum import StrEnum


class AppRunnerJobOperationType(StrEnum):
    RUNNER_JOB_OPERATION_TYPE_APPLY_PLAN = "apply-plan"
    RUNNER_JOB_OPERATION_TYPE_BUILD = "build"
    RUNNER_JOB_OPERATION_TYPE_CREATE_APPLY_PLAN = "create-apply-plan"
    RUNNER_JOB_OPERATION_TYPE_CREATE_TEARDOWN_PLAN = "create-teardown-plan"
    RUNNER_JOB_OPERATION_TYPE_EXEC = "exec"
    RUNNER_JOB_OPERATION_TYPE_UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
