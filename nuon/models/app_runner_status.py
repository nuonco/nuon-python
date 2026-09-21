from enum import StrEnum


class AppRunnerStatus(StrEnum):
    ACTIVE = "active"
    AWAITING_HEARTBEAT = "awaiting-heartbeat"
    AWAITING_INSTALL_STACK_RUN = "awaiting-install-stack-run"
    DEPROVISIONED = "deprovisioned"
    DEPROVISIONING = "deprovisioning"
    DISABLED = "disabled"
    ERROR = "error"
    OFFLINE = "offline"
    PENDING = "pending"
    PROVISIONING = "provisioning"
    REPROVISIONING = "reprovisioning"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
