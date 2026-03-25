from enum import Enum


class AppStackType(str, Enum):
    AWS_CLOUDFORMATION = "aws-cloudformation"
    GCP_TERRAFORM = "gcp-terraform"

    def __str__(self) -> str:
        return str(self.value)
