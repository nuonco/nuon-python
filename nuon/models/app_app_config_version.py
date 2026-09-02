from enum import StrEnum


class AppAppConfigVersion(StrEnum):
    V2 = "v2"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
