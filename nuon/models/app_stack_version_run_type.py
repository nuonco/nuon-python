from enum import Enum


class AppStackVersionRunType(str, Enum):
    OUT_OF_BAND_UPDATE = "out-of-band-update"
    WORKFLOW_RUN = "workflow-run"

    def __str__(self) -> str:
        return str(self.value)
