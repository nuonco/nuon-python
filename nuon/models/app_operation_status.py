from enum import StrEnum


class AppOperationStatus(StrEnum):
    FAILED = "failed"
    FINISHED = "finished"
    NOOP = "noop"
    STARTED = "started"

    def __str__(self) -> str:
        return str(self.value)
