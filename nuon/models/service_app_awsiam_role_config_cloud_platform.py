from enum import Enum


class ServiceAppAWSIAMRoleConfigCloudPlatform(str, Enum):
    AWS = "aws"
    GCP = "gcp"

    def __str__(self) -> str:
        return str(self.value)
