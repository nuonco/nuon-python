from enum import StrEnum


class GetAppBundlesStatus(StrEnum):
    ACTIVE = "active"
    ERROR = "error"
    PUBLISHING = "publishing"
    QUEUED = "queued"

    def __str__(self) -> str:
        return str(self.value)
