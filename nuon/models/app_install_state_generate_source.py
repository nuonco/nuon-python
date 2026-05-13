from enum import Enum


class AppInstallStateGenerateSource(str, Enum):
    LEGACY = "legacy"
    STATE_MANAGER = "state-manager"

    def __str__(self) -> str:
        return str(self.value)
