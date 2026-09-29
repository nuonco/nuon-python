from enum import StrEnum


class AppInstallCreationApprovalStatus(StrEnum):
    INSTALL_CREATION_APPROVAL_STATUS_APPROVED = "approved"
    INSTALL_CREATION_APPROVAL_STATUS_DENIED = "denied"
    INSTALL_CREATION_APPROVAL_STATUS_PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
