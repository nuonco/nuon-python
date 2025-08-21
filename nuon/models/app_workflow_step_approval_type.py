from enum import Enum


class AppWorkflowStepApprovalType(str, Enum):
    APPROVE_ALL = "approve-all"
    HELM_APPROVAL = "helm_approval"
    KUBERNETES_MANIFEST_APPROVAL = "kubernetes_manifest_approval"
    NOOP = "noop"
    TERRAFORM_PLAN = "terraform_plan"

    def __str__(self) -> str:
        return str(self.value)
