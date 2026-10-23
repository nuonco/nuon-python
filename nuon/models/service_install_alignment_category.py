from enum import StrEnum


class ServiceInstallAlignmentCategory(StrEnum):
    INSTALL_ALIGNMENT_CATEGORY_CHANGES_NOT_APPLIED = "changes-not-applied"
    INSTALL_ALIGNMENT_CATEGORY_DISABLED = "disabled"
    INSTALL_ALIGNMENT_CATEGORY_IN_SYNC = "in-sync"
    INSTALL_ALIGNMENT_CATEGORY_STATE_DRIFT_DETECTED = "state-drift-detected"
    INSTALL_ALIGNMENT_CATEGORY_TORN_DOWN = "torn-down"
    INSTALL_ALIGNMENT_CATEGORY_UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
