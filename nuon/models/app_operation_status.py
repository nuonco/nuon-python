from enum import StrEnum


class AppOperationStatus(StrEnum):
    OPERATION_STATUS_FAILED = "failed"
    OPERATION_STATUS_FINISHED = "finished"
    OPERATION_STATUS_NOOP = "noop"
    OPERATION_STATUS_STARTED = "started"

    def __str__(self) -> str:
        return str(self.value)
