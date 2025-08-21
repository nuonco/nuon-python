from enum import Enum


class ConfigAppPolicyType(str, Enum):
    KUBERNETES_CLUSTER = "kubernetes_cluster"
    RUNNER_JOB_ACTION_WORKFLOW = "runner_job_action_workflow"
    RUNNER_JOB_HELM_DEPLOY = "runner_job_helm_deploy"
    RUNNER_JOB_TERRAFORM_DEPLOY = "runner_job_terraform_deploy"

    def __str__(self) -> str:
        return str(self.value)
