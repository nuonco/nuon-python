from enum import StrEnum


class ServiceConnectionResponsePlatform(StrEnum):
    AWS = "aws"

    def __str__(self) -> str:
        return str(self.value)
