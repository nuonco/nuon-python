from enum import Enum


class AppRunnerProcessType(str, Enum):
    BUILD = "build"
    INSTALL = "install"
    MNG = "mng"
    ORG = "org"
    VALUE_4 = ""

    def __str__(self) -> str:
        return str(self.value)
