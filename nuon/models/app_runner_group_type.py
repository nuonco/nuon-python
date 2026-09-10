from enum import StrEnum


class AppRunnerGroupType(StrEnum):
    INSTALL = "install"
    ORG = "org"

    def __str__(self) -> str:
        return str(self.value)
