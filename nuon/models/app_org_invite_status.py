from enum import StrEnum


class AppOrgInviteStatus(StrEnum):
    ACCEPTED = "accepted"
    PENDING = "pending"
    REVOKED = "revoked"

    def __str__(self) -> str:
        return str(self.value)
