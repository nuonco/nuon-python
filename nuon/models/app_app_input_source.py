from enum import Enum


class AppAppInputSource(str, Enum):
    CUSTOMER = "customer"
    VENDOR = "vendor"

    def __str__(self) -> str:
        return str(self.value)
