from enum import Enum


class AppRunnerGroupType(str, Enum):
    INSTALL = "install"
    ORG = "org"

    def __str__(self) -> str:
        return str(self.value)
