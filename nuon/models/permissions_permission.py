from enum import StrEnum


class PermissionsPermission(StrEnum):
    PERMISSION_ALL = "all"
    PERMISSION_CREATE = "create"
    PERMISSION_DELETE = "delete"
    PERMISSION_READ = "read"
    PERMISSION_UNKNOWN = "unknown"
    PERMISSION_UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
