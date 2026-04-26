from enum import Enum


class AppRunnerProcessShutdownType(str, Enum):
    FORCE = "force"
    GRACEFUL = "graceful"
    RESTART = "restart"

    def __str__(self) -> str:
        return str(self.value)
