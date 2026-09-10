from enum import StrEnum


class AppSandboxRunType(StrEnum):
    DEPROVISION = "deprovision"
    PROVISION = "provision"
    REPROVISION = "reprovision"

    def __str__(self) -> str:
        return str(self.value)
