from enum import Enum


class AppComponentType(str, Enum):
    DOCKER_BUILD = "docker_build"
    EXTERNAL_IMAGE = "external_image"
    HELM_CHART = "helm_chart"
    JOB = "job"
    KUBERNETES_MANIFEST = "kubernetes_manifest"
    TERRAFORM_MODULE = "terraform_module"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
