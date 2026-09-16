from enum import StrEnum


class AppAWSIAMRoleType(StrEnum):
    BREAKGLASS = "breakglass"
    CUSTOM = "custom"
    RUNNER_BREAKGLASS = "runner_breakglass"
    RUNNER_DEPROVISION = "runner_deprovision"
    RUNNER_MAINTENANCE = "runner_maintenance"
    RUNNER_PROVISION = "runner_provision"

    def __str__(self) -> str:
        return str(self.value)
