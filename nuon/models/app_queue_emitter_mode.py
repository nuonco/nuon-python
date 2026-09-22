from enum import StrEnum


class AppQueueEmitterMode(StrEnum):
    CRON = "cron"
    FIRE_ONCE = "fire_once"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
