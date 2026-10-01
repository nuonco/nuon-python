from enum import StrEnum


class AppOrgMemberStatus(StrEnum):
    ORG_MEMBER_STATUS_ACTIVE = "active"
    ORG_MEMBER_STATUS_INVITED = "invited"

    def __str__(self) -> str:
        return str(self.value)
