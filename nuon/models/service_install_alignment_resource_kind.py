from enum import StrEnum


class ServiceInstallAlignmentResourceKind(StrEnum):
    INSTALL_ALIGNMENT_RESOURCE_KIND_COMPONENT = "component"
    INSTALL_ALIGNMENT_RESOURCE_KIND_IMAGE = "image"
    INSTALL_ALIGNMENT_RESOURCE_KIND_SANDBOX = "sandbox"
    INSTALL_ALIGNMENT_RESOURCE_KIND_STACK = "stack"

    def __str__(self) -> str:
        return str(self.value)
