from enum import Enum


class AppOperationStatus(str, Enum):
    FAILED = "failed"
    FINISHED = "finished"
    NOOP = "noop"
    STARTED = "started"

    def __str__(self) -> str:
        return str(self.value)
