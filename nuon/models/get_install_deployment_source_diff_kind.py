from enum import StrEnum


class GetInstallDeploymentSourceDiffKind(StrEnum):
    COMPONENT = "component"
    SANDBOX = "sandbox"

    def __str__(self) -> str:
        return str(self.value)
