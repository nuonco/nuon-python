from enum import Enum


class ConfigCustomNestedStackStatus(str, Enum):
    ERROR = "error"
    PENDING = "pending"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
