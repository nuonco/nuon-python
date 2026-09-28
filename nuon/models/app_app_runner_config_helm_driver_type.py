from enum import StrEnum


class AppAppRunnerConfigHelmDriverType(StrEnum):
    APP_RUNNER_HELM_DRIVER_CONFIG_MAP = "configmap"
    APP_RUNNER_HELM_DRIVER_EMPTY = ""
    APP_RUNNER_HELM_DRIVER_SECRET = "secret"

    def __str__(self) -> str:
        return str(self.value)
