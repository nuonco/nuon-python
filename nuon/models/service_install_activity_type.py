from enum import StrEnum


class ServiceInstallActivityType(StrEnum):
    INSTALL_ACTIVITY_TYPE_ACTION_RUN = "action_run"
    INSTALL_ACTIVITY_TYPE_POLICY_CHECK = "policy_check"
    INSTALL_ACTIVITY_TYPE_RUNBOOK_RUN = "runbook_run"

    def __str__(self) -> str:
        return str(self.value)
