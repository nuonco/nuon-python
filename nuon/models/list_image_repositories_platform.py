from enum import StrEnum


class ListImageRepositoriesPlatform(StrEnum):
    AWS = "aws"
    AZURE = "azure"
    GCP = "gcp"

    def __str__(self) -> str:
        return str(self.value)
