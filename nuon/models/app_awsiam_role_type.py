from enum import StrEnum


class AppAWSIAMRoleType(StrEnum):
    AWSIAM_ROLE_TYPE_BREAK_GLASS = "breakglass"
    AWSIAM_ROLE_TYPE_CUSTOM = "custom"
    AWSIAM_ROLE_TYPE_RUNNER_BREAK_GLASS = "runner_breakglass"
    AWSIAM_ROLE_TYPE_RUNNER_DEPROVISION = "runner_deprovision"
    AWSIAM_ROLE_TYPE_RUNNER_MAINTENANCE = "runner_maintenance"
    AWSIAM_ROLE_TYPE_RUNNER_PROVISION = "runner_provision"

    def __str__(self) -> str:
        return str(self.value)
