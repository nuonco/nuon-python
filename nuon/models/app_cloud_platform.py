from enum import StrEnum


class AppCloudPlatform(StrEnum):
    AWS = "aws"
    AZURE = "azure"
    GCP = "gcp"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
