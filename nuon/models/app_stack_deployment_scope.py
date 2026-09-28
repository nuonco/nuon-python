from enum import StrEnum


class AppStackDeploymentScope(StrEnum):
    STACK_DEPLOYMENT_SCOPE_RESOURCE_GROUP = "resource_group"
    STACK_DEPLOYMENT_SCOPE_SUBSCRIPTION = "subscription"

    def __str__(self) -> str:
        return str(self.value)
