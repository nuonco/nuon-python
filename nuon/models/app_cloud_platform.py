from enum import Enum


class AppCloudPlatform(str, Enum):
    AWS = "aws"
    AZURE = "azure"
    GCP = "gcp"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
