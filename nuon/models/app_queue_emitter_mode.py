from enum import Enum


class AppQueueEmitterMode(str, Enum):
    CRON = "cron"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
