from enum import StrEnum


class ListServiceAccountsManagement(StrEnum):
    ALL = "all"
    SYSTEM = "system"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
