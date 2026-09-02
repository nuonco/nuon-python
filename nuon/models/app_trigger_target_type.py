from enum import StrEnum


class AppTriggerTargetType(StrEnum):
    APP_BRANCH_RUN = "app_branch_run"
    RUNBOOK = "runbook"

    def __str__(self) -> str:
        return str(self.value)
