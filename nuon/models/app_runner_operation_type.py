from enum import StrEnum


class AppRunnerOperationType(StrEnum):
    DEPROVISION = "deprovision"
    PROVISION = "provision"
    PROVISION_SERVICE_ACCOUNT = "provision_service_account"
    REPROVISION = "reprovision"

    def __str__(self) -> str:
        return str(self.value)
