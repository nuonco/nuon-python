from enum import StrEnum


class ServiceInstallDeploymentType(StrEnum):
    INSTALL_DEPLOYMENT_TYPE_APP_BRANCH_UPDATE = "app_branch_update"
    INSTALL_DEPLOYMENT_TYPE_COMPONENT_DEPLOY = "component_deploy"
    INSTALL_DEPLOYMENT_TYPE_IMAGE_UPDATE = "image_update"
    INSTALL_DEPLOYMENT_TYPE_INSTALL_CONFIG_UPDATE = "install_config_update"
    INSTALL_DEPLOYMENT_TYPE_PROVISION = "provision"
    INSTALL_DEPLOYMENT_TYPE_REPROVISION = "reprovision"
    INSTALL_DEPLOYMENT_TYPE_SANDBOX_REPROVISION = "sandbox_reprovision"
    INSTALL_DEPLOYMENT_TYPE_STACK_UPDATE = "stack_update"

    def __str__(self) -> str:
        return str(self.value)
