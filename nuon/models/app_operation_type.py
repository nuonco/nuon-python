from enum import Enum


class AppOperationType(str, Enum):
    DEPLOY = "deploy"
    DEPROVISION = "deprovision"
    PROVISION = "provision"
    REPROVISION = "reprovision"
    TEARDOWN = "teardown"
    TRIGGER = "trigger"

    def __str__(self) -> str:
        return str(self.value)
