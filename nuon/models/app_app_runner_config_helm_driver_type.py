from enum import StrEnum


class AppAppRunnerConfigHelmDriverType(StrEnum):
    CONFIGMAP = "configmap"
    SECRET = "secret"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
