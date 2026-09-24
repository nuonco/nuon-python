from enum import StrEnum


class AppAppConfigVersion(StrEnum):
    APP_CONFIG_VERSION_DEFAULT = ""
    APP_CONFIG_VERSION_V2 = "v2"

    def __str__(self) -> str:
        return str(self.value)
