from enum import StrEnum


class AppRunnerStatus(StrEnum):
    RUNNER_STATUS_ACTIVE = "active"
    RUNNER_STATUS_AWAITING_HEARTBEAT = "awaiting-heartbeat"
    RUNNER_STATUS_AWAITING_INSTALL_STACK_RUN = "awaiting-install-stack-run"
    RUNNER_STATUS_DEPROVISIONED = "deprovisioned"
    RUNNER_STATUS_DEPROVISIONING = "deprovisioning"
    RUNNER_STATUS_DISABLED = "disabled"
    RUNNER_STATUS_ERROR = "error"
    RUNNER_STATUS_OFFLINE = "offline"
    RUNNER_STATUS_PENDING = "pending"
    RUNNER_STATUS_PROVISIONING = "provisioning"
    RUNNER_STATUS_REPROVISIONING = "reprovisioning"
    RUNNER_STATUS_UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
