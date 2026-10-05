from enum import StrEnum


class AppCloudConnectionPlatform(StrEnum):
    AWS = "aws"

    def __str__(self) -> str:
        return str(self.value)
