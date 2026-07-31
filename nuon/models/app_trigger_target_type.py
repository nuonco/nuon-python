from enum import Enum


class AppTriggerTargetType(str, Enum):
    APP_BRANCH_RUN = "app_branch_run"
    RUNBOOK = "runbook"

    def __str__(self) -> str:
        return str(self.value)
