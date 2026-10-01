from enum import StrEnum


class AppRunnerOperationType(StrEnum):
    RUNNER_OPERATION_TYPE_DEPROVISION = "deprovision"
    RUNNER_OPERATION_TYPE_PROVISION = "provision"
    RUNNER_OPERATION_TYPE_PROVISION_SERVICE_ACCOUNT = "provision_service_account"
    RUNNER_OPERATION_TYPE_REPROVISION = "reprovision"

    def __str__(self) -> str:
        return str(self.value)
