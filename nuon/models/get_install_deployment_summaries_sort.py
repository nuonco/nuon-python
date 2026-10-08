from enum import StrEnum


class GetInstallDeploymentSummariesSort(StrEnum):
    ATTENTION = "attention"

    def __str__(self) -> str:
        return str(self.value)
