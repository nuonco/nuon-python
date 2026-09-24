from enum import StrEnum


class AppStackType(StrEnum):
    STACK_TYPE_AWS = "aws-cloudformation"
    STACK_TYPE_AZURE = "azure-bicep"
    STACK_TYPE_GCP = "gcp-terraform"

    def __str__(self) -> str:
        return str(self.value)
