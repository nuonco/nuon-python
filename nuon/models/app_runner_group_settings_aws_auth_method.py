from enum import Enum


class AppRunnerGroupSettingsAwsAuthMethod(str, Enum):
    IID = "iid"
    STS = "sts"

    def __str__(self) -> str:
        return str(self.value)
