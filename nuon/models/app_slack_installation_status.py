from enum import StrEnum


class AppSlackInstallationStatus(StrEnum):
    ACTIVE = "active"
    DISABLED = "disabled"
    UNINSTALLED = "uninstalled"

    def __str__(self) -> str:
        return str(self.value)
