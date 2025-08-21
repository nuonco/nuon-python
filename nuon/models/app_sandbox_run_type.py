from enum import Enum


class AppSandboxRunType(str, Enum):
    DEPROVISION = "deprovision"
    PROVISION = "provision"
    REPROVISION = "reprovision"

    def __str__(self) -> str:
        return str(self.value)
