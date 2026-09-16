from enum import StrEnum


class AppRunnerProcessShutdownType(StrEnum):
    FORCE = "force"
    GRACEFUL = "graceful"
    RESTART = "restart"

    def __str__(self) -> str:
        return str(self.value)
