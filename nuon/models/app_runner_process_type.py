from enum import StrEnum


class AppRunnerProcessType(StrEnum):
    RUNNER_PROCESS_TYPE_BUILD = "build"
    RUNNER_PROCESS_TYPE_INSTALL = "install"
    RUNNER_PROCESS_TYPE_MNG = "mng"
    RUNNER_PROCESS_TYPE_ORG = "org"
    RUNNER_PROCESS_TYPE_UNKNOWN = ""

    def __str__(self) -> str:
        return str(self.value)
