from enum import Enum


class AppAWSIAMRoleType(str, Enum):
    BREAKGLASS = "breakglass"
    RUNNER_BREAKGLASS = "runner_breakglass"
    RUNNER_DEPROVISION = "runner_deprovision"
    RUNNER_MAINTENANCE = "runner_maintenance"
    RUNNER_PROVISION = "runner_provision"

    def __str__(self) -> str:
        return str(self.value)
