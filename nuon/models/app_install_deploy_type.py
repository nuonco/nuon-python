from enum import StrEnum


class AppInstallDeployType(StrEnum):
    APPLY = "apply"
    RECOVER = "recover"
    SYNC_IMAGE = "sync-image"
    TEARDOWN = "teardown"

    def __str__(self) -> str:
        return str(self.value)
