from enum import StrEnum


class ServiceConnectionListResponsePlatform(StrEnum):
    AWS = "aws"

    def __str__(self) -> str:
        return str(self.value)
