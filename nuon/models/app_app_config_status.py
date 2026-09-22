from enum import StrEnum


class AppAppConfigStatus(StrEnum):
    ACTIVE = "active"
    ERROR = "error"
    OUTDATED = "outdated"
    PENDING = "pending"
    SYNCING = "syncing"

    def __str__(self) -> str:
        return str(self.value)
