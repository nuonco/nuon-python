from enum import StrEnum


class GetInstallDeploymentSummariesState(StrEnum):
    ACTIVE = "active"
    FINISHED = "finished"

    def __str__(self) -> str:
        return str(self.value)
