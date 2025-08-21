from enum import Enum


class AppInstallerType(str, Enum):
    SELF_HOSTED = "self_hosted"

    def __str__(self) -> str:
        return str(self.value)
