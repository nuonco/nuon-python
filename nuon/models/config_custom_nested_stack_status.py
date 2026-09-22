from enum import StrEnum


class ConfigCustomNestedStackStatus(StrEnum):
    ERROR = "error"
    PENDING = "pending"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
