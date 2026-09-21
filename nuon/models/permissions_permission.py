from enum import StrEnum


class PermissionsPermission(StrEnum):
    ALL = "all"
    CREATE = "create"
    DELETE = "delete"
    READ = "read"
    UNKNOWN = "unknown"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
