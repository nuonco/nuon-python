from enum import StrEnum


class AppAppConfigStatus(StrEnum):
    APP_CONFIG_STATUS_ACTIVE = "active"
    APP_CONFIG_STATUS_ERROR = "error"
    APP_CONFIG_STATUS_OUTDATED = "outdated"
    APP_CONFIG_STATUS_PENDING = "pending"
    APP_CONFIG_STATUS_SYNCING = "syncing"

    def __str__(self) -> str:
        return str(self.value)
