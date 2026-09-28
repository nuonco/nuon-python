from enum import StrEnum


class ServiceInstallUpdateType(StrEnum):
    INSTALL_UPDATE_TYPE_APP_CONFIG = "app_config"
    INSTALL_UPDATE_TYPE_INPUTS = "inputs"
    INSTALL_UPDATE_TYPE_INSTALL_CONFIG = "install_config"
    INSTALL_UPDATE_TYPE_STACK = "stack"

    def __str__(self) -> str:
        return str(self.value)
