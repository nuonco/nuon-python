from enum import StrEnum


class AppInstallDeployType(StrEnum):
    INSTALL_DEPLOY_TYPE_APPLY = "apply"
    INSTALL_DEPLOY_TYPE_RECOVER = "recover"
    INSTALL_DEPLOY_TYPE_SYNC = "sync-image"
    INSTALL_DEPLOY_TYPE_TEARDOWN = "teardown"

    def __str__(self) -> str:
        return str(self.value)
