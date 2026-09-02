from enum import StrEnum


class ServiceCreateAppInstallsConfigRequestVcsType(StrEnum):
    CONNECTED = "connected"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
