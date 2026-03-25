from enum import Enum


class ServiceCompleteInstallStepRequestInstallMode(str, Enum):
    CLOUD = "cloud"
    SANDBOX = "sandbox"

    def __str__(self) -> str:
        return str(self.value)
