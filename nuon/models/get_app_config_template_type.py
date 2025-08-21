from enum import Enum


class GetAppConfigTemplateType(str, Enum):
    AWS_ECS = "aws-ecs"
    AWS_ECS_BYOVPC = "aws-ecs-byovpc"
    AWS_EKS = "aws-eks"
    AWS_EKS_BYOVPC = "aws-eks-byovpc"
    AZURE_AKS = "azure-aks"
    CONTAINER_IMAGE = "container-image"
    DOCKER_BUILD = "docker-build"
    ECR_CONTAINER_IMAGE = "ecr-container-image"
    FLAT = "flat"
    HELM = "helm"
    INPUTS = "inputs"
    INSTALLER = "installer"
    JOB = "job"
    RUNNER = "runner"
    SANDBOX = "sandbox"
    TERRAFORM = "terraform"
    TERRAFORMINFRA = "terraformInfra"
    TOP_LEVEL = "top-level"

    def __str__(self) -> str:
        return str(self.value)
