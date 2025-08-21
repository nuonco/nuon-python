from enum import Enum


class AppStepErrorBehavior(str, Enum):
    ABORT = "abort"
    CONTINUE = "continue"

    def __str__(self) -> str:
        return str(self.value)
