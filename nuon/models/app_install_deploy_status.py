from enum import Enum


class AppInstallDeployStatus(str, Enum):
    ACTIVE = "active"
    APPROVAL_DENIED = "approval-denied"
    CANCELLED = "cancelled"
    ERROR = "error"
    EXECUTING = "executing"
    INACTIVE = "inactive"
    NOOP = "noop"
    PENDING = "pending"
    PENDING_APPROVAL = "pending-approval"
    PLANNING = "planning"
    QUEUED = "queued"
    SYNCING = "syncing"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
