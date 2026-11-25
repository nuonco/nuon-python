from enum import StrEnum


class ServiceInstallResourceSyncStatusResourceKind(StrEnum):
    INSTALL_RESOURCE_SYNC_STATUS_RESOURCE_KIND_COMPONENT = "component"
    INSTALL_RESOURCE_SYNC_STATUS_RESOURCE_KIND_IMAGE = "image"
    INSTALL_RESOURCE_SYNC_STATUS_RESOURCE_KIND_SANDBOX = "sandbox"
    INSTALL_RESOURCE_SYNC_STATUS_RESOURCE_KIND_STACK = "stack"

    def __str__(self) -> str:
        return str(self.value)
