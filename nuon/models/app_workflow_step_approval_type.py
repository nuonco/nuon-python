from enum import StrEnum


class AppWorkflowStepApprovalType(StrEnum):
    APPROVE_ALL_APPROVAL_TYPE = "approve-all"
    APP_BRANCH_PLAN_APPROVAL_TYPE = "app_branch_plan"
    HELM_APPROVAL_APPROVAL_TYPE = "helm_approval"
    INSTALL_CREATION_APPROVAL_TYPE = "install_creation"
    KUBERNETES_MANIFEST_APPROVAL_TYPE = "kubernetes_manifest_approval"
    NOOP_APPROVAL_TYPE = "noop"
    PULUMI_APPROVAL_TYPE = "pulumi_plan"
    TERRAFORM_PLAN_APPROVAL_TYPE = "terraform_plan"

    def __str__(self) -> str:
        return str(self.value)
