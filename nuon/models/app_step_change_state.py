from enum import StrEnum


class AppStepChangeState(StrEnum):
    ERROR = "error"
    OK = "ok"
    UNSUPPORTED = "unsupported"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
