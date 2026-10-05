from enum import StrEnum


class AppCloudConnectionStatus(StrEnum):
    CLOUD_CONNECTION_STATUS_ERROR = "error"
    CLOUD_CONNECTION_STATUS_PENDING = "pending"
    CLOUD_CONNECTION_STATUS_VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
