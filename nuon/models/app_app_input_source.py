from enum import StrEnum


class AppAppInputSource(StrEnum):
    APP_INPUT_SOURCE_CUSTOMER = "customer"
    APP_INPUT_SOURCE_VENDOR = "vendor"

    def __str__(self) -> str:
        return str(self.value)
