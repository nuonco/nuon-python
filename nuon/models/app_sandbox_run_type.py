from enum import StrEnum


class AppSandboxRunType(StrEnum):
    SANDBOX_RUN_TYPE_DEPROVISION = "deprovision"
    SANDBOX_RUN_TYPE_PROVISION = "provision"
    SANDBOX_RUN_TYPE_REPROVISION = "reprovision"

    def __str__(self) -> str:
        return str(self.value)
