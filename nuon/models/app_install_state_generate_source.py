from enum import StrEnum


class AppInstallStateGenerateSource(StrEnum):
    INSTALL_STATE_GENERATE_SOURCE_LEGACY = "legacy"
    INSTALL_STATE_GENERATE_SOURCE_STATE_MANAGER = "state-manager"

    def __str__(self) -> str:
        return str(self.value)
