from enum import Enum


class ServiceUpdateRunnerSettingsRequestAwsAuthMethod(str, Enum):
    IID = "iid"
    STS = "sts"

    def __str__(self) -> str:
        return str(self.value)
