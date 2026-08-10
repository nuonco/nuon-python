from enum import Enum


class ServiceCreateAppInstallsConfigRequestVcsType(str, Enum):
    CONNECTED = "connected"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
