from enum import StrEnum


class AppInstallConfigImpact(StrEnum):
    INSTALL_CONFIG_IMPACT_BREAK_GLASS = "break_glass"
    INSTALL_CONFIG_IMPACT_PERMISSIONS = "permissions"
    INSTALL_CONFIG_IMPACT_RUNNER_CONFIG = "runner_config"
    INSTALL_CONFIG_IMPACT_SECRETS = "secrets"
    INSTALL_CONFIG_IMPACT_STACK_CONFIG = "stack_config"

    def __str__(self) -> str:
        return str(self.value)
