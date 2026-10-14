from enum import StrEnum


class AppRunbookTriggerType(StrEnum):
    RUNBOOK_TRIGGER_TYPE_CRON = "cron"
    RUNBOOK_TRIGGER_TYPE_MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
