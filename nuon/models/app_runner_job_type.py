from enum import Enum


class AppRunnerJobType(str, Enum):
    ACTIONS_WORKFLOW = "actions-workflow"
    CONTAINER_IMAGE_BUILD = "container-image-build"
    DOCKER_BUILD = "docker-build"
    FETCH_IMAGE_METADATA = "fetch-image-metadata"
    HEALTH_CHECK = "health-check"
    HELM_CHART_BUILD = "helm-chart-build"
    HELM_CHART_DEPLOY = "helm-chart-deploy"
    JOB_DEPLOY = "job-deploy"
    KUBERNETES_MANIFEST_BUILD = "kubernetes-manifest-build"
    KUBERNETES_MANIFEST_DEPLOY = "kubernetes-manifest-deploy"
    MNG_FETCH_TOKEN = "mng-fetch-token"
    MNG_RUNNER_RESTART = "mng-runner-restart"
    MNG_RUNNER_UPDATE_VERSION = "mng-runner-update-version"
    MNG_SHUT_DOWN = "mng-shut-down"
    MNG_VM_SHUT_DOWN = "mng-vm-shut-down"
    NOOP = "noop"
    NOOP_BUILD = "noop-build"
    NOOP_DEPLOY = "noop-deploy"
    NOOP_SYNC = "noop-sync"
    OCI_SYNC = "oci-sync"
    RUNNER_HELM = "runner-helm"
    RUNNER_LOCAL = "runner-local"
    RUNNER_TERRAFORM = "runner-terraform"
    SANDBOX_SYNC_SECRETS = "sandbox-sync-secrets"
    SANDBOX_TERRAFORM = "sandbox-terraform"
    SANDBOX_TERRAFORM_PLAN = "sandbox-terraform-plan"
    SHUT_DOWN = "shut-down"
    TERRAFORM_DEPLOY = "terraform-deploy"
    TERRAFORM_MODULE_BUILD = "terraform-module-build"
    UPDATE_VERSION = "update-version"

    def __str__(self) -> str:
        return str(self.value)
