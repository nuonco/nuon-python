from enum import StrEnum


class AppInstallConfigImpact(StrEnum):
    BREAK_GLASS = "break_glass"
    PERMISSIONS = "permissions"
    RUNNER_CONFIG = "runner_config"
    SECRETS = "secrets"
    STACK_CONFIG = "stack_config"

    def __str__(self) -> str:
        return str(self.value)
