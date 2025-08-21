from enum import Enum


class AppAppRunnerType(str, Enum):
    AWS = "aws"
    AWS_ECS = "aws-ecs"
    AWS_EKS = "aws-eks"
    AZURE = "azure"
    AZURE_ACS = "azure-acs"
    AZURE_AKS = "azure-aks"
    LOCAL = "local"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
