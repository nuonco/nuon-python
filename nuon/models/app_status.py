from enum import Enum


class AppStatus(str, Enum):
    ACTIVE = "active"
    APPLYING = "applying"
    APPROVAL_AWAITING = "approval-awaiting"
    APPROVAL_DENIED = "approval-denied"
    APPROVAL_EXPIRED = "approval-expired"
    APPROVAL_RETRY = "approval-retry"
    APPROVED = "approved"
    AUTO_SKIPPED = "auto-skipped"
    AWAITING_USER_RUN = "awaiting-user-run"
    BUILDING = "building"
    CANCELLED = "cancelled"
    CHECKING_PLAN = "checking-plan"
    DELETING = "deleting"
    DISCARDED = "discarded"
    ERROR = "error"
    EXPIRED = "expired"
    GENERATING = "generating"
    IN_PROGRESS = "in-progress"
    NOOP = "noop"
    NOT_ATTEMPTED = "not-attempted"
    OUTDATED = "outdated"
    PENDING = "pending"
    PLANNING = "planning"
    PROVISIONING = "provisioning"
    RETRYING = "retrying"
    SUCCESS = "success"
    USER_SKIPPED = "user-skipped"

    def __str__(self) -> str:
        return str(self.value)
