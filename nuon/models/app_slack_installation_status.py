from enum import Enum


class AppSlackInstallationStatus(str, Enum):
    ACTIVE = "active"
    DISABLED = "disabled"
    UNINSTALLED = "uninstalled"

    def __str__(self) -> str:
        return str(self.value)
