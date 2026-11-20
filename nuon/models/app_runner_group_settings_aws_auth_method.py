from enum import StrEnum


class AppRunnerGroupSettingsAwsAuthMethod(StrEnum):
    IID = "iid"
    STS = "sts"
    STS_BOUND = "sts-bound"
    STS_VENDOR = "sts-vendor"

    def __str__(self) -> str:
        return str(self.value)
