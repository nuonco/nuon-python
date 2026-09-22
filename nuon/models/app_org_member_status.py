from enum import StrEnum


class AppOrgMemberStatus(StrEnum):
    ACTIVE = "active"
    INVITED = "invited"

    def __str__(self) -> str:
        return str(self.value)
