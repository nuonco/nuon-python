from enum import StrEnum


class AppRunnerProcessType(StrEnum):
    BUILD = "build"
    INSTALL = "install"
    MNG = "mng"
    ORG = "org"
    VALUE_4 = ""

    def __str__(self) -> str:
        return str(self.value)
