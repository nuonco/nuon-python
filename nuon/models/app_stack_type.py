from enum import StrEnum


class AppStackType(StrEnum):
    AWS_CLOUDFORMATION = "aws-cloudformation"
    AZURE_BICEP = "azure-bicep"
    GCP_TERRAFORM = "gcp-terraform"

    def __str__(self) -> str:
        return str(self.value)
