from enum import Enum


class AppAppConfigStatus(str, Enum):
    ACTIVE = "active"
    ERROR = "error"
    OUTDATED = "outdated"
    PENDING = "pending"
    SYNCING = "syncing"

    def __str__(self) -> str:
        return str(self.value)
