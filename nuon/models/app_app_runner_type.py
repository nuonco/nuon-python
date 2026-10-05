from enum import StrEnum


class AppAppRunnerType(StrEnum):
    APP_RUNNER_TYPE_AWS = "aws"
    APP_RUNNER_TYPE_AWSECS = "aws-ecs"
    APP_RUNNER_TYPE_AWSEKS = "aws-eks"
    APP_RUNNER_TYPE_AZURE = "azure"
    APP_RUNNER_TYPE_AZURE_ACS = "azure-acs"
    APP_RUNNER_TYPE_AZURE_AKS = "azure-aks"
    APP_RUNNER_TYPE_GCP = "gcp"
    APP_RUNNER_TYPE_GCPGKE = "gcp-gke"
    APP_RUNNER_TYPE_LOCAL = "local"
    APP_RUNNER_TYPE_UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
