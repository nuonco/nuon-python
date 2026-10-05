from enum import StrEnum


class ConfigCustomNestedStackStatus(StrEnum):
    CUSTOM_NESTED_STACK_STATUS_ERROR = "error"
    CUSTOM_NESTED_STACK_STATUS_PENDING = "pending"
    CUSTOM_NESTED_STACK_STATUS_READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
