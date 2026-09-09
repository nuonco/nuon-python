from enum import StrEnum


class AppInstallStateGenerateSource(StrEnum):
    LEGACY = "legacy"
    STATE_MANAGER = "state-manager"

    def __str__(self) -> str:
        return str(self.value)
