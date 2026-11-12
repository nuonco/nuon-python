from enum import StrEnum


class ServiceInstallDeploymentSourceDiffStatus(StrEnum):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"
    UNSUPPORTED = "unsupported"

    def __str__(self) -> str:
        return str(self.value)
