from enum import Enum


class GetAvailableRolesPrincipalType(str, Enum):
    ACTION = "action"
    COMPONENT = "component"
    SANDBOX = "sandbox"

    def __str__(self) -> str:
        return str(self.value)
