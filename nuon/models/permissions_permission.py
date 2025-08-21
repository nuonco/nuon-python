from enum import Enum


class PermissionsPermission(str, Enum):
    ALL = "all"
    CREATE = "create"
    DELETE = "delete"
    READ = "read"
    UNKNOWN = "unknown"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
