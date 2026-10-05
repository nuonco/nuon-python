from enum import StrEnum


class AppRunnerGroupType(StrEnum):
    RUNNER_GROUP_TYPE_INSTALL = "install"
    RUNNER_GROUP_TYPE_ORG = "org"

    def __str__(self) -> str:
        return str(self.value)
