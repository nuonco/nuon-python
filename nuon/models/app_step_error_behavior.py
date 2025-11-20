from enum import Enum


class AppStepErrorBehavior(str, Enum):
    ABORT = "abort"

    def __str__(self) -> str:
        return str(self.value)
