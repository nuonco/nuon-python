from enum import StrEnum


class AppRunnerGroupSettingsAwsAuthMethod(StrEnum):
    IID = "iid"
    STS = "sts"

    def __str__(self) -> str:
        return str(self.value)
