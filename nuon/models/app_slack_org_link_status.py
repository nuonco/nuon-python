from enum import Enum


class AppSlackOrgLinkStatus(str, Enum):
    REVOKED = "revoked"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
