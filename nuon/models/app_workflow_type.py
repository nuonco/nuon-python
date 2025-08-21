from enum import Enum


class AppWorkflowType(str, Enum):
    ACTION_WORKFLOW_RUN = "action_workflow_run"
    APP_BRANCHES_COMPONENT_REPO_UPDATE = "app_branches_component_repo_update"
    APP_BRANCHES_CONFIG_REPO_UPDATE = "app_branches_config_repo_update"
    APP_BRANCHES_MANUAL_UPDATE = "app_branches_manual_update"
    DEPLOY_COMPONENTS = "deploy_components"
    DEPROVISION = "deprovision"
    DEPROVISION_SANDBOX = "deprovision_sandbox"
    INPUT_UPDATE = "input_update"
    MANUAL_DEPLOY = "manual_deploy"
    PROVISION = "provision"
    REPROVISION = "reprovision"
    REPROVISION_SANDBOX = "reprovision_sandbox"
    SYNC_SECRETS = "sync_secrets"
    TEARDOWN_COMPONENT = "teardown_component"
    TEARDOWN_COMPONENTS = "teardown_components"

    def __str__(self) -> str:
        return str(self.value)
