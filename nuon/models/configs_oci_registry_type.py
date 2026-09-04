from enum import StrEnum


class ConfigsOCIRegistryType(StrEnum):
    ACR = "acr"
    ECR = "ecr"
    GAR = "gar"
    PRIVATE_OCI = "private_oci"
    PUBLIC_OCI = "public_oci"

    def __str__(self) -> str:
        return str(self.value)
