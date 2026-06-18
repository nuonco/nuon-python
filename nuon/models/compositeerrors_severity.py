from enum import Enum


class CompositeerrorsSeverity(str, Enum):
    ERROR = "error"
    FATAL = "fatal"
    INFO = "info"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
