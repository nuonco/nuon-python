from enum import StrEnum


class ServiceCompleteInstallStepRequestInstallMode(StrEnum):
    CLOUD = "cloud"
    SANDBOX = "sandbox"

    def __str__(self) -> str:
        return str(self.value)
