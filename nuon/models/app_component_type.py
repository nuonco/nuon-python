from enum import StrEnum


class AppComponentType(StrEnum):
    COMPONENT_TYPE_DOCKER_BUILD = "docker_build"
    COMPONENT_TYPE_EXTERNAL_IMAGE = "external_image"
    COMPONENT_TYPE_HELM_CHART = "helm_chart"
    COMPONENT_TYPE_JOB = "job"
    COMPONENT_TYPE_KUBERNETES_MANIFEST = "kubernetes_manifest"
    COMPONENT_TYPE_PULUMI = "pulumi"
    COMPONENT_TYPE_TERRAFORM_MODULE = "terraform_module"
    COMPONENT_TYPE_UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
