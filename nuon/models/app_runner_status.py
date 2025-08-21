from enum import Enum


class AppRunnerStatus(str, Enum):
    ACTIVE = "active"
    AWAITING_INSTALL_STACK_RUN = "awaiting-install-stack-run"
    DEPROVISIONED = "deprovisioned"
    DEPROVISIONING = "deprovisioning"
    ERROR = "error"
    OFFLINE = "offline"
    PENDING = "pending"
    PROVISIONING = "provisioning"
    REPROVISIONING = "reprovisioning"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
