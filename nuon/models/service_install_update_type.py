from enum import StrEnum


class ServiceInstallUpdateType(StrEnum):
    APP_CONFIG = "app_config"
    INPUTS = "inputs"
    INSTALL_CONFIG = "install_config"
    STACK = "stack"

    def __str__(self) -> str:
        return str(self.value)
