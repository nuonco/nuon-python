from enum import StrEnum


class ServiceRespondInstallCreationApprovalRequestResponseType(StrEnum):
    APPROVE = "approve"
    DENY = "deny"

    def __str__(self) -> str:
        return str(self.value)
