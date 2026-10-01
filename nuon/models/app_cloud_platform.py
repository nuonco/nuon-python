from enum import StrEnum


class AppCloudPlatform(StrEnum):
    CLOUD_PLATFORM_AWS = "aws"
    CLOUD_PLATFORM_AZURE = "azure"
    CLOUD_PLATFORM_GCP = "gcp"
    CLOUD_PLATFORM_UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
