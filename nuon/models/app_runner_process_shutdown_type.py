from enum import StrEnum


class AppRunnerProcessShutdownType(StrEnum):
    RUNNER_PROCESS_SHUTDOWN_TYPE_FORCE = "force"
    RUNNER_PROCESS_SHUTDOWN_TYPE_GRACEFUL = "graceful"
    RUNNER_PROCESS_SHUTDOWN_TYPE_RESTART = "restart"

    def __str__(self) -> str:
        return str(self.value)
