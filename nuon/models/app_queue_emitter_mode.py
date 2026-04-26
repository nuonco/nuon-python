from enum import Enum


class AppQueueEmitterMode(str, Enum):
    CRON = "cron"
    FIRE_ONCE = "fire_once"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
