from enum import StrEnum


class AppOperationType(StrEnum):
    OPERATION_DEPLOY = "deploy"
    OPERATION_DEPROVISION = "deprovision"
    OPERATION_PROVISION = "provision"
    OPERATION_REPROVISION = "reprovision"
    OPERATION_TEARDOWN = "teardown"
    OPERATION_TRIGGER = "trigger"

    def __str__(self) -> str:
        return str(self.value)
