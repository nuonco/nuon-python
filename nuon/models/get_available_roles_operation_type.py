from enum import StrEnum


class GetAvailableRolesOperationType(StrEnum):
    DEPLOY = "deploy"
    DEPROVISION = "deprovision"
    PROVISION = "provision"
    REPROVISION = "reprovision"
    TEARDOWN = "teardown"
    TRIGGER = "trigger"

    def __str__(self) -> str:
        return str(self.value)
