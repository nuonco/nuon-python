from enum import StrEnum


class AppQueueEmitterMode(StrEnum):
    QUEUE_EMITTER_MODE_CRON = "cron"
    QUEUE_EMITTER_MODE_FIRE_ONCE = "fire_once"
    QUEUE_EMITTER_MODE_SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
