from enum import Enum


class AppAppRunnerConfigHelmDriverType(str, Enum):
    CONFIGMAP = "configmap"
    SECRET = "secret"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
