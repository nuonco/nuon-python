from enum import StrEnum


class GetAvailableRolesPrincipalType(StrEnum):
    ACTION = "action"
    COMPONENT = "component"
    SANDBOX = "sandbox"

    def __str__(self) -> str:
        return str(self.value)
