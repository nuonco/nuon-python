from enum import StrEnum


class ConfigAppPolicyType(StrEnum):
    APP_POLICY_TYPE_CONTAINER_IMAGE = "container_image"
    APP_POLICY_TYPE_DOCKER_BUILD = "docker_build"
    APP_POLICY_TYPE_HELM_CHART = "helm_chart"
    APP_POLICY_TYPE_KUBERNETES_CLUSTER = "kubernetes_cluster"
    APP_POLICY_TYPE_KUBERNETES_MANIFEST = "kubernetes_manifest"
    APP_POLICY_TYPE_PULUMI = "pulumi"
    APP_POLICY_TYPE_SANDBOX = "sandbox"
    APP_POLICY_TYPE_TERRAFORM_MODULE = "terraform_module"

    def __str__(self) -> str:
        return str(self.value)
