from enum import StrEnum


class AppTriggerTargetType(StrEnum):
    TRIGGER_TARGET_TYPE_APP_BRANCH_RUN = "app_branch_run"
    TRIGGER_TARGET_TYPE_RUNBOOK = "runbook"

    def __str__(self) -> str:
        return str(self.value)
