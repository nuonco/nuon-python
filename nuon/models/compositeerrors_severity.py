from enum import StrEnum


class CompositeerrorsSeverity(StrEnum):
    SEVERITY_ERROR = "error"
    SEVERITY_FATAL = "fatal"
    SEVERITY_INFO = "info"
    SEVERITY_WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
