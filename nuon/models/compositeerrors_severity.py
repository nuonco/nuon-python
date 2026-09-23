from enum import StrEnum


class CompositeerrorsSeverity(StrEnum):
    ERROR = "error"
    FATAL = "fatal"
    INFO = "info"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
