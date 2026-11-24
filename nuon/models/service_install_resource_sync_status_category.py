from enum import StrEnum


class ServiceInstallResourceSyncStatusCategory(StrEnum):
    INSTALL_RESOURCE_SYNC_STATUS_CATEGORY_CHANGES_NOT_APPLIED = "changes-not-applied"
    INSTALL_RESOURCE_SYNC_STATUS_CATEGORY_DISABLED = "disabled"
    INSTALL_RESOURCE_SYNC_STATUS_CATEGORY_IN_SYNC = "in-sync"
    INSTALL_RESOURCE_SYNC_STATUS_CATEGORY_STATE_DRIFT_DETECTED = "state-drift-detected"
    INSTALL_RESOURCE_SYNC_STATUS_CATEGORY_TORN_DOWN = "torn-down"
    INSTALL_RESOURCE_SYNC_STATUS_CATEGORY_UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
