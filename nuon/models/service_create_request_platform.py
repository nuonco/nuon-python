from enum import StrEnum


class ServiceCreateRequestPlatform(StrEnum):
    AWS = "aws"

    def __str__(self) -> str:
        return str(self.value)
