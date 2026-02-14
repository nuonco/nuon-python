from enum import Enum


class AppActionWorkflowTriggerType(str, Enum):
    ADHOC = "adhoc"
    CRON = "cron"
    MANUAL = "manual"
    POST_DEPLOY_ALL_COMPONENTS = "post-deploy-all-components"
    POST_DEPLOY_COMPONENT = "post-deploy-component"
    POST_DEPROVISION = "post-deprovision"
    POST_DEPROVISION_SANDBOX = "post-deprovision-sandbox"
    POST_PROVISION = "post-provision"
    POST_REPROVISION = "post-reprovision"
    POST_REPROVISION_SANDBOX = "post-reprovision-sandbox"
    POST_SECRETS_SYNC = "post-secrets-sync"
    POST_TEARDOWN_ALL_COMPONENTS = "post-teardown-all-components"
    POST_TEARDOWN_COMPONENT = "post-teardown-component"
    POST_UPDATE_INPUTS = "post-update-inputs"
    PRE_DEPLOY_ALL_COMPONENTS = "pre-deploy-all-components"
    PRE_DEPLOY_COMPONENT = "pre-deploy-component"
    PRE_DEPROVISION = "pre-deprovision"
    PRE_DEPROVISION_SANDBOX = "pre-deprovision-sandbox"
    PRE_PROVISION = "pre-provision"
    PRE_REPROVISION = "pre-reprovision"
    PRE_REPROVISION_SANDBOX = "pre-reprovision-sandbox"
    PRE_SECRETS_SYNC = "pre-secrets-sync"
    PRE_TEARDOWN_ALL_COMPONENTS = "pre-teardown-all-components"
    PRE_TEARDOWN_COMPONENT = "pre-teardown-component"
    PRE_UPDATE_INPUTS = "pre-update-inputs"

    def __str__(self) -> str:
        return str(self.value)
