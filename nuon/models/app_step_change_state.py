from enum import StrEnum


class AppStepChangeState(StrEnum):
    STEP_CHANGE_STATE_ERROR = "error"
    STEP_CHANGE_STATE_OK = "ok"
    STEP_CHANGE_STATE_UNKNOWN = ""
    STEP_CHANGE_STATE_UNSUPPORTED = "unsupported"

    def __str__(self) -> str:
        return str(self.value)
