from enum import Enum


class AppAppConfigVersion(str, Enum):
    V2 = "v2"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
