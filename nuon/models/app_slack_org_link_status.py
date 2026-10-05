from enum import StrEnum


class AppSlackOrgLinkStatus(StrEnum):
    SLACK_ORG_LINK_STATUS_REVOKED = "revoked"
    SLACK_ORG_LINK_STATUS_VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
