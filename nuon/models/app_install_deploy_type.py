from enum import Enum


class AppInstallDeployType(str, Enum):
    APPLY = "apply"
    RECOVER = "recover"
    SYNC_IMAGE = "sync-image"
    TEARDOWN = "teardown"

    def __str__(self) -> str:
        return str(self.value)
