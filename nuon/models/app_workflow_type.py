from enum import StrEnum


class AppWorkflowType(StrEnum):
    WORKFLOW_TYPE_ACTION_WORKFLOW_RUN = "action_workflow_run"
    WORKFLOW_TYPE_APP_BRANCHES_COMPONENT_REPO_UPDATE = "app_branches_component_repo_update"
    WORKFLOW_TYPE_APP_BRANCHES_CONFIG_REPO_UPDATE = "app_branches_config_repo_update"
    WORKFLOW_TYPE_APP_BRANCHES_RUN = "app_branches_manual_update"
    WORKFLOW_TYPE_APP_BRANCH_CONFIG_UPDATE = "app_branch_config_update"
    WORKFLOW_TYPE_APP_CONFIG_BUILD = "app_config_build"
    WORKFLOW_TYPE_APP_INSTALL_SYNC = "app_install_sync"
    WORKFLOW_TYPE_COMPONENT_DISABLED = "component_disabled"
    WORKFLOW_TYPE_COMPONENT_ENABLED = "component_enabled"
    WORKFLOW_TYPE_DEPLOY_COMPONENTS = "deploy_components"
    WORKFLOW_TYPE_DEPROVISION = "deprovision"
    WORKFLOW_TYPE_DEPROVISION_SANDBOX = "deprovision_sandbox"
    WORKFLOW_TYPE_DRIFT_RUN = "drift_run"
    WORKFLOW_TYPE_DRIFT_RUN_REPROVISION_SANDBOX = "drift_run_reprovision_sandbox"
    WORKFLOW_TYPE_INPUT_UPDATE = "input_update"
    WORKFLOW_TYPE_MANUAL_DEPLOY = "manual_deploy"
    WORKFLOW_TYPE_PROVISION = "provision"
    WORKFLOW_TYPE_RECOVER_HELM_RELEASE = "recover_helm_release"
    WORKFLOW_TYPE_REPROVISION = "reprovision"
    WORKFLOW_TYPE_REPROVISION_SANDBOX = "reprovision_sandbox"
    WORKFLOW_TYPE_REPROVISION_STACK = "reprovision_stack"
    WORKFLOW_TYPE_RUNBOOK_RUN = "runbook_run"
    WORKFLOW_TYPE_SYNC_SECRETS = "sync_secrets"
    WORKFLOW_TYPE_TEARDOWN_COMPONENT = "teardown_component"
    WORKFLOW_TYPE_TEARDOWN_COMPONENTS = "teardown_components"

    def __str__(self) -> str:
        return str(self.value)
