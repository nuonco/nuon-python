from enum import StrEnum


class ConfigsOCIRegistryType(StrEnum):
    OCI_REGISTRY_TYPE_ACR = "acr"
    OCI_REGISTRY_TYPE_ECR = "ecr"
    OCI_REGISTRY_TYPE_GAR = "gar"
    OCI_REGISTRY_TYPE_PRIVATE_OCI = "private_oci"
    OCI_REGISTRY_TYPE_PUBLIC_OCI = "public_oci"

    def __str__(self) -> str:
        return str(self.value)
