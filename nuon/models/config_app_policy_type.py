from enum import Enum


class ConfigAppPolicyType(str, Enum):
    CONTAINER_IMAGE = "container_image"
    DOCKER_BUILD = "docker_build"
    HELM_CHART = "helm_chart"
    KUBERNETES_CLUSTER = "kubernetes_cluster"
    KUBERNETES_MANIFEST = "kubernetes_manifest"
    SANDBOX = "sandbox"
    TERRAFORM_MODULE = "terraform_module"

    def __str__(self) -> str:
        return str(self.value)
