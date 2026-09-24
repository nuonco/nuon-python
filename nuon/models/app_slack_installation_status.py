from enum import StrEnum


class AppSlackInstallationStatus(StrEnum):
    SLACK_INSTALLATION_STATUS_ACTIVE = "active"
    SLACK_INSTALLATION_STATUS_DISABLED = "disabled"
    SLACK_INSTALLATION_STATUS_UNINSTALLED = "uninstalled"

    def __str__(self) -> str:
        return str(self.value)
