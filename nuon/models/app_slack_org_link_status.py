from enum import StrEnum


class AppSlackOrgLinkStatus(StrEnum):
    REVOKED = "revoked"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
