from enum import StrEnum


class ServiceAppConfigTemplateType(StrEnum):
    APP_CONFIG_TEMPLATE_TYPE_AWS_ECS = "aws-ecs"
    APP_CONFIG_TEMPLATE_TYPE_AWS_ECSBYOVPC = "aws-ecs-byovpc"
    APP_CONFIG_TEMPLATE_TYPE_AWS_EKS = "aws-eks"
    APP_CONFIG_TEMPLATE_TYPE_AWS_EKSBYOVPC = "aws-eks-byovpc"
    APP_CONFIG_TEMPLATE_TYPE_AZURE_AKS = "azure-aks"
    APP_CONFIG_TEMPLATE_TYPE_CONTAINER_IMAGE = "container-image"
    APP_CONFIG_TEMPLATE_TYPE_DOCKER_BUILD = "docker-build"
    APP_CONFIG_TEMPLATE_TYPE_ECR_CONTAINER_IMAGE = "ecr-container-image"
    APP_CONFIG_TEMPLATE_TYPE_FLAT = "flat"
    APP_CONFIG_TEMPLATE_TYPE_HELM = "helm"
    APP_CONFIG_TEMPLATE_TYPE_INPUTS = "inputs"
    APP_CONFIG_TEMPLATE_TYPE_INSTALLER = "installer"
    APP_CONFIG_TEMPLATE_TYPE_JOB = "job"
    APP_CONFIG_TEMPLATE_TYPE_RUNNER = "runner"
    APP_CONFIG_TEMPLATE_TYPE_SANDBOX = "sandbox"
    APP_CONFIG_TEMPLATE_TYPE_TERRAFORM = "terraform"
    APP_CONFIG_TEMPLATE_TYPE_TERRAFORM_INFRA = "terraformInfra"
    APP_CONFIG_TEMPLATE_TYPE_TOP_LEVEL = "top-level"

    def __str__(self) -> str:
        return str(self.value)
