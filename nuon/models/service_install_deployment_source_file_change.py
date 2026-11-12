from enum import StrEnum


class ServiceInstallDeploymentSourceFileChange(StrEnum):
    ADDED = "added"
    MODIFIED = "modified"
    REMOVED = "removed"

    def __str__(self) -> str:
        return str(self.value)
