from enum import StrEnum


class AppOrgInviteStatus(StrEnum):
    ORG_INVITE_STATUS_ACCEPTED = "accepted"
    ORG_INVITE_STATUS_PENDING = "pending"
    ORG_INVITE_STATUS_REVOKED = "revoked"

    def __str__(self) -> str:
        return str(self.value)
