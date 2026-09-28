from enum import StrEnum


class AppStackVersionRunType(StrEnum):
    STACK_VERSION_RUN_TYPE_OUT_OF_BAND = "out-of-band-update"
    STACK_VERSION_RUN_TYPE_WORKFLOW = "workflow-run"

    def __str__(self) -> str:
        return str(self.value)
