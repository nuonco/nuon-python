from enum import StrEnum


class AppAppInputSource(StrEnum):
    CUSTOMER = "customer"
    VENDOR = "vendor"

    def __str__(self) -> str:
        return str(self.value)
